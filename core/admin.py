from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    """
    Configuration de l'interface d'administration Django pour la gestion des Leads.
    """
    # Colonnes affichées dans la liste des prospects
    list_display = ('prenom', 'nom', 'email', 'entreprise', 'telephone', 'formation_interessee', 'date_inscription')
    
    # Filtres latéraux (pratique pour segmenter par date ou formation)
    list_filter = ('date_inscription', 'formation_interessee', 'entreprise')
    
    # Recherche globale sur les informations d'identification
    search_fields = ('nom', 'prenom', 'email', 'entreprise')
    
    # Hiérarchie par date pour une navigation temporelle rapide
    date_hierarchy = 'date_inscription'
    
    # Rendre la date d'inscription consultable mais non modifiable
    readonly_fields = ('date_inscription',)
