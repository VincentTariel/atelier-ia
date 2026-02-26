# TÂCHE : CRÉATION DE LA BASE DE DONNÉES (MODELS ET ADMIN)

En te basant sur le CONTEXTE GLOBAL et l'ARCHITECTURE TECHNIQUE, crée la structure de base de données.

## Instructions :
Génère le code Python pour l'application Django `core`.

1. **Fichier `models.py`** :
   - Crée un modèle `Lead`.
   - Champs de base : `prenom` (CharField), `nom` (CharField), `email` (EmailField), `date_inscription` (DateTimeField auto_now_add).
   - Champs optionnels : `entreprise` (CharField, blank=True, null=True), `telephone` (CharField, blank=True, null=True).
   - **Nouveau champ :** `formation_interessee` (CharField avec `choices`). Les choix doivent être : 'Niveau 1 (Assistants sur-mesure)', 'Niveau 2 (Automatisation n8n)', 'Les deux'.
   - Ajoute une méthode `__str__`.

2. **Fichier `admin.py`** :
   - Enregistre le modèle `Lead`.
   - Crée `LeadAdmin` pour afficher proprement les colonnes (`list_display`), filtres (`list_filter` sur la date et formation_interessee) et barre de recherche (`search_fields`).

Renvoie UNIQUEMENT le code Python commenté en français, bien séparé par fichiers.