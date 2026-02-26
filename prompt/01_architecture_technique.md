# ARCHITECTURE TECHNIQUE DU SITE : ATELIER IA

## 1. Stack Technique
- **Framework Backend :** Python avec Django.
- **Frontend :** Templates Django classiques + Tailwind CSS (via CDN).
- **Base de données :** SQLite.
- **Emailing :** Module `django.core.mail` natif de Django (configuration SMTP requise dans les settings).

## 2. Structure du projet Django
Projet `atelier_ia`, application `core`.
Arborescence visée :
atelier_ia/
│
├── atelier_ia/                
│   ├── settings.py            # Contiendra la config EMAIL_BACKEND
│   └── urls.py
│
├── core/                      
│   ├── models.py              # Modèle 'Lead'
│   ├── forms.py               # ModelForm
│   ├── views.py               # Logique d'affichage et envoi d'email
│   ├── urls.py                
│   ├── admin.py               
│   └── templates/
│       └── core/
│           ├── base.html      
│           └── landing.html   # Page de vente et formulaire
│
└── manage.py