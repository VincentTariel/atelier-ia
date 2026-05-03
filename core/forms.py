from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    """
    Formulaire de capture de prospect.
    Les styles visuels sont entièrement gérés via CSS dans `base.html`
    (classe #contact-form). On ne pose ici que les attributs HTML utiles
    (placeholder, autocomplete) pour garder le markup propre.
    """

    # Source unique de vérité pour les choix : Lead.FORMATION_CHOICES.
    # On ajoute juste un placeholder vide en tête pour forcer une sélection consciente.
    formation_interessee = forms.ChoiceField(
        choices=[('', '— Sélectionnez —')] + Lead.FORMATION_CHOICES,
        label="Sujet",
        required=True,
    )

    class Meta:
        model = Lead
        fields = ['prenom', 'nom', 'email', 'entreprise', 'telephone', 'formation_interessee']

        widgets = {
            'prenom': forms.TextInput(attrs={
                'placeholder': 'Anjelai',
                'autocomplete': 'given-name',
            }),
            'nom': forms.TextInput(attrs={
                'placeholder': 'Calonne',
                'autocomplete': 'family-name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'anjelai.calonne@cabinet.nc',
                'autocomplete': 'email',
            }),
            'entreprise': forms.TextInput(attrs={
                'placeholder': 'Cabinet, étude, agence (facultatif)',
                'autocomplete': 'organization',
            }),
            'telephone': forms.TextInput(attrs={
                'placeholder': '+687 — facultatif',
                'autocomplete': 'tel',
                'inputmode': 'tel',
            }),
        }
