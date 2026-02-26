# TÂCHE : CRÉATION DE LA LOGIQUE ET DE L'ENVOI D'EMAIL (FORMS ET VIEWS)

En te basant sur le modèle `Lead`, crée la logique pour capturer le prospect et lui envoyer son PDF directement via Django.

## Instructions :
Génère le code Python pour l'application Django `core`.

1. **Fichier `forms.py`** :
   - Crée un `LeadForm` basé sur le modèle `Lead`.
   - Ajoute des classes Tailwind CSS dans les `widgets` (y compris pour le champ `Select` de `formation_interessee`).

2. **Fichier `views.py`** :
   - Crée une vue `landing_page_view`.
   - Si POST, valide le formulaire et sauvegarde le `Lead`.
   - **Envoi d'email :** Utilise `send_mail` ou `EmailMessage` de `django.core.mail`. 
     - Sujet : "Votre support de formation Atelier IA"
     - Corps : Message de remerciement + lien vers le PDF (ou pièce jointe fictive pour l'exemple).
     - Expéditeur : `tariel.vincent@gmail.com`
     - Destinataire : L'email du prospect.
   - Gère les exceptions (`try/except`) lors de l'envoi de l'email.
   - Utilise `messages.success` pour afficher : "Merci ! Le support de la formation vient de vous être envoyé par email."
   - Redirige pour éviter la double soumission.

Renvoie UNIQUEMENT le code Python commenté en français, bien séparé par fichiers.