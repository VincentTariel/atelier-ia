# TÂCHE : CRÉATION DE L'INTERFACE UTILISATEUR (URLS ET TEMPLATES)

Crée la Landing Page moderne et professionnelle de "Atelier IA".

## Instructions :

1. **Fichier `urls.py` (application `core`)** : Routes pour `landing_page_view`.

2. **Fichier `templates/core/base.html`** :
   - HTML5, CDN Tailwind CSS, gestion des `messages` Django, et bloc `content`.

3. **Fichier `templates/core/landing.html`** :
   - Hérite de `base.html`.
   - **Hero Section** : "Entrepreneurs Calédoniens : Paramétrez les assistants IA sur-mesure de votre entreprise en 3 heures."
   - **Section Programme** : 
     - *Niveau 1 :* L'Atelier de 3h (Consulting en groupe, création de l'architecture cerveau, travail sur dossiers réels avec l'expert).
     - *Niveau 2 :* L'automatisation avec n8n.
   - **Section Formulaire (Lead Magnet)** :
     - Affiche `{{ form }}` proprement (incluant la question sur la formation souhaitée).
     - Bouton de soumission : "Recevoir le support de l'Atelier 1 par email et le devis".
   - **Section Témoignages (Preuve Sociale) EN BAS DE PAGE** :
     - Ajoute une section avec 2 ou 3 faux témoignages réalistes d'entrepreneurs calédoniens.
     - Axe des témoignages : Le gain de temps grâce aux assistants sur-mesure. (Exemple d'idée : "Je pensais ne pas avoir 3 heures à consacrer à une formation. Mais dès le lendemain de l'atelier, mon nouvel 'Assistant Communication' m'a rédigé tous mes posts de la semaine en 10 minutes, avec mon ton exact. Les 30 000 F ont été rentabilisés en une seule matinée de travail gagnée. C'est le meilleur investissement de mon année.", "J'avais abandonné ChatGPT car je passais mon temps à lui réexpliquer mon métier, et les textes faisaient très 'robot'. Grâce à la méthode du Document Maître vue pendant l'atelier, mon IA connaît parfaitement ma cible calédonienne et mes offres. Je ne fais plus de prompts à rallonge, j'appuie sur un bouton et elle pond un texte qui ressemble à 100% à mon entreprise.").

Renvoie le code du fichier `urls.py` et le code HTML des deux templates. Design épuré, SaaS B2B, clair et vendeur.