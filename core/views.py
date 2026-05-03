"""
Landing Atelier IA — capture de leads.
Comportement :
  GET  → render avec timestamp pour le time-trap.
  POST → anti-bot (honeypot + time-trap) → save Lead → email PDF au lead +
         notification email à Vincent.
"""
import logging
import time

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

from .forms import LeadForm

logger = logging.getLogger(__name__)

# Anti-bot : durée minimale (secondes) entre l'affichage du form et le submit.
# Sous ce seuil, on considère que c'est un bot scripté.
MIN_FORM_FILL_SECONDS = 3

# Notification : adresse interne qui reçoit les nouvelles demandes.
NOTIFICATION_RECIPIENT = "tariel.vincent@gmail.com"


def landing_page_view(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)

        # ------------------------------------------------------------------
        # 1. Anti-bot — honeypot + time-trap
        # ------------------------------------------------------------------
        # Honeypot : le champ `website` doit rester vide (caché en CSS).
        # Si un bot l'a rempli → on jette silencieusement.
        if request.POST.get('website', '').strip():
            logger.warning("Soumission rejetée (honeypot rempli) — IP %s",
                           request.META.get('REMOTE_ADDR'))
            messages.success(request, "Merci ! Votre demande a bien été prise en compte.")
            return redirect('landing_page')

        # Time-trap : si le form est soumis trop vite après affichage → bot.
        loaded_at = request.POST.get('loaded_at', '').strip()
        try:
            elapsed = time.time() - int(loaded_at)
            if elapsed < MIN_FORM_FILL_SECONDS:
                logger.warning("Soumission rejetée (time-trap %.1fs) — IP %s",
                               elapsed, request.META.get('REMOTE_ADDR'))
                messages.success(request, "Merci ! Votre demande a bien été prise en compte.")
                return redirect('landing_page')
        except (ValueError, TypeError):
            # Pas de timestamp ou invalide : suspect mais pas bloquant — on log.
            logger.warning("Soumission sans timestamp valide — IP %s",
                           request.META.get('REMOTE_ADDR'))

        # ------------------------------------------------------------------
        # 2. Validation Django
        # ------------------------------------------------------------------
        if form.is_valid():
            lead = form.save()

            # 3. Notification à Vincent (priorité haute — c'est l'objectif business)
            _send_notification_to_vincent(lead, request)

            # 4. Email lead-magnet au prospect
            _send_lead_magnet(lead)

            messages.success(
                request,
                "Merci ! Votre demande a bien été reçue. Vincent vous recontacte sous 24 heures."
            )
            return redirect('landing_page')

    else:
        # GET → on injecte le timestamp courant pour le time-trap.
        form = LeadForm(initial={'loaded_at': int(time.time())})

    return render(request, 'core/landing.html', {'form': form})


# ============================================================================
# Helpers email
# ============================================================================

def _send_notification_to_vincent(lead, request):
    """Envoie un email de notification à Vincent à chaque nouvelle demande."""
    sujet = (
        f"[Atelier IA] Nouvelle demande — "
        f"{lead.get_formation_interessee_display()} — "
        f"{lead.prenom} {lead.nom}"
    )

    admin_url = request.build_absolute_uri(f"/admin/core/lead/{lead.id}/change/")

    corps = (
        f"Nouvelle demande reçue le {lead.date_inscription:%d/%m/%Y à %Hh%M} "
        f"(heure de Nouméa).\n\n"
        f"Identité\n"
        f"--------\n"
        f"  Prénom     : {lead.prenom}\n"
        f"  Nom        : {lead.nom}\n"
        f"  Email      : {lead.email}\n"
        f"  Téléphone  : {lead.telephone or '—'}\n"
        f"  Entreprise : {lead.entreprise or '—'}\n\n"
        f"Sujet\n"
        f"-----\n"
        f"  {lead.get_formation_interessee_display()}\n\n"
        f"Pour répondre directement au prospect, utilisez 'Répondre' :\n"
        f"votre message partira vers {lead.email}.\n\n"
        f"Voir/éditer dans l'admin : {admin_url}\n\n"
        f"--\n"
        f"Notification automatique Atelier IA"
    )

    try:
        email = EmailMessage(
            subject=sujet,
            body=corps,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[NOTIFICATION_RECIPIENT],
            reply_to=[lead.email],  # 'Répondre' va directement vers le prospect
        )
        email.send(fail_silently=False)
    except Exception as e:
        logger.error(
            "Échec envoi notification interne pour lead %s (%s) : %s",
            lead.id, lead.email, e,
        )


def _send_lead_magnet(lead):
    """Envoie le PDF lead-magnet au prospect."""
    sujet = "Votre guide Atelier IA — Claude Desktop au quotidien"
    corps = (
        f"Bonjour {lead.prenom},\n\n"
        f"Merci de votre intérêt pour Atelier IA.\n\n"
        f"Vous trouverez ci-joint le guide promis. Je vous recontacte "
        f"sous 24 heures pour la suite.\n\n"
        f"À très bientôt,\n"
        f"Vincent Tariel\n"
        f"Atelier IA — Coaching Claude Desktop · Nouméa\n"
        f"+687 95 07 86\n"
        f"https://atelier-ia.ovh"
    )

    try:
        email = EmailMessage(
            subject=sujet,
            body=corps,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[lead.email],
            reply_to=['tariel.vincent@gmail.com'],
        )

        # Attache le PDF s'il existe (en attendant le nouveau lead-magnet)
        pdf_path = settings.BASE_DIR / 'core' / 'templates' / 'pdf' / 'Atelier_IA_Niveau_1.pdf'
        if pdf_path.exists():
            email.attach_file(str(pdf_path))
        else:
            logger.warning("PDF lead-magnet introuvable : %s", pdf_path)

        email.send(fail_silently=False)
    except Exception as e:
        logger.error(
            "Échec envoi lead-magnet à %s pour lead %s : %s",
            lead.email, lead.id, e,
        )
