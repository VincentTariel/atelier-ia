from django.db import models

class Lead(models.Model):
    """
    Modèle représentant un prospect (Lead) ayant rempli le formulaire 
    pour recevoir le support de l'Atelier Niveau 1.
    """
    FORMATION_CHOICES = [
        ('niveau1', "Niveau 1 : Les Assistants IA"),
        ('niveau2', "Niveau 2 : L'Automatisation"),
        ('les_deux', "Les deux niveaux"),
    ]

    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse Email")
    
    # Champs optionnels pour qualifier le prospect B2B
    entreprise = models.CharField(max_length=200, blank=True, null=True, verbose_name="Entreprise")
    telephone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")
    
    # Nouveau champ pour le choix de la formation
    formation_interessee = models.CharField(
        max_length=20,
        choices=FORMATION_CHOICES,
        default='niveau1',
        verbose_name="Formation intéressée"
    )
    
    # Horodatage automatique lors de la création
    date_inscription = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")

    def __str__(self):
        """
        Affiche le lead sous la forme : Prénom Nom - Entreprise - [Formation]
        """
        base = f"{self.prenom} {self.nom}"
        if self.entreprise:
            base += f" - {self.entreprise}"
        base += f" - [{self.get_formation_interessee_display()}]"
        return base

    class Meta:
        verbose_name = "Prospect"
        verbose_name_plural = "Prospects"
        ordering = ['-date_inscription']
