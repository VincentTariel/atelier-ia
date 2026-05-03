from django.db import models

class Lead(models.Model):
    """
    Prospect ayant rempli le formulaire de la landing Atelier IA.
    Source unique pour l'inbound — voir CLAUDE.md §6 (stratégie CRM).
    """
    FORMATION_CHOICES = [
        ('decouverte', "Découvrir Claude Desktop pour mon métier"),
        ('cas_precis', "J'ai un cas précis en tête"),
        ('guide_pdf',  "Je veux juste recevoir le guide PDF"),
    ]

    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse Email")

    # Champs optionnels pour qualifier le prospect B2B
    entreprise = models.CharField(max_length=200, blank=True, null=True, verbose_name="Entreprise")
    telephone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")

    # Sujet d'intérêt sélectionné dans le formulaire de contact
    formation_interessee = models.CharField(
        max_length=20,
        choices=FORMATION_CHOICES,
        default='decouverte',
        verbose_name="Sujet d'intérêt"
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
