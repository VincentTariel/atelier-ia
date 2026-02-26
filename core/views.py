import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import LeadForm

# Configuration d'un logger pour tracer les erreurs potentielles d'envoi d'email
logger = logging.getLogger(__name__)

def landing_page_view(request):
    """
    Vue principale affichant la Landing Page et gérant le formulaire de capture (Lead Magnet).
    Sauvegarde le prospect en base de données et envoie l'email avec le PDF.
    """
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            # 1. Sauvegarde locale du prospect dans la base de données Django (SQLite)
            lead = form.save()
            
            # 2. Préparation de l'email
            sujet = "Votre support de présentation - Atelier IA"
            corps_message = (
                f"Bonjour {lead.prenom},\n\n"
                f"Merci de votre intérêt pour nos formations. "
                f"Comme promis, voici le support de présentation de l'Atelier Niveau 1.\n\n"
                f"À très bientôt,\n"
                f"Vincent Tariel"
            )
            
            # On utilise l'expéditeur configuré dans les settings (Gmail impose d'utiliser son propre email)
            expediteur = settings.DEFAULT_FROM_EMAIL
            destinataires = [lead.email]
            
            # 3. Envoi de l'email avec gestion des erreurs
            try:
                email = EmailMessage(
                    subject=sujet,
                    body=corps_message,
                    from_email=expediteur,
                    to=destinataires,
                    # L'adresse sur laquelle arriveront les réponses du prospect
                    reply_to=['tariel.vincent@gmail.com'],
                )
                
                # On attache le support de présentation
                pdf_path = settings.BASE_DIR / 'core' / 'templates' / 'pdf' / 'Atelier_IA_Niveau_1.pdf'
                if pdf_path.exists():
                    email.attach_file(str(pdf_path))
                else:
                    logger.error(f"Fichier PDF introuvable au chemin : {pdf_path}")
                
                email.send(fail_silently=False)
                
            except Exception as e:
                # Si l'envoi de l'email échoue, on loggue l'erreur sans bloquer l'expérience utilisateur.
                logger.error(f"Erreur lors de l'envoi de l'email pour le lead {lead.id} ({lead.email}) : {e}")
            
            # 4. Message de succès et redirection
            messages.success(
                request, 
                "Merci ! Le support de la formation a été envoyé dans votre boîte mail."
            )
            
            # Redirection Post-Redirect-Get
            return redirect('landing_page')
            
    else:
        # Requête GET : Affichage d'un formulaire vide
        form = LeadForm()
        
    context = {
        'form': form
    }
    
    return render(request, 'core/landing.html', context)
