from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    """
    Formulaire de capture de prospect.
    Les styles visuels sont entièrement gérés via CSS dans `base.html`
    (classe #contact-form). On ne pose ici que les attributs HTML utiles
    (placeholder, autocomplete) pour garder le markup propre.

    Anti-bot :
    - `website` est un honeypot (caché en CSS via .visually-hidden) — un humain
      ne peut pas le voir, donc le laisse vide. Les bots remplissent tous les
      champs et trahissent leur nature.
    - `loaded_at` est un timestamp Unix injecté au render du GET ; on
      vérifie côté view qu'au moins quelques secondes se sont écoulées avant
      le submit.
    """

    # Source unique de vérité pour les choix : Lead.FORMATION_CHOICES.
    # On ajoute juste un placeholder vide en tête pour forcer une sélection consciente.
    formation_interessee = forms.ChoiceField(
        choices=[('', '— Sélectionnez —')] + Lead.FORMATION_CHOICES,
        label="Sujet",
        required=True,
    )

    # Honeypot — invisible pour les humains (cf .visually-hidden dans base.html)
    website = forms.CharField(
        required=False,
        label="Site web",
        widget=forms.TextInput(attrs={
            'class': 'visually-hidden',
            'tabindex': '-1',
            'autocomplete': 'off',
            'aria-hidden': 'true',
        }),
    )

    # Time trap — timestamp Unix du moment où le form a été affiché (POST/GET round-trip).
    loaded_at = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = Lead
        fields = ['prenom', 'nom', 'email', 'entreprise', 'telephone', 'formation_interessee']

        widgets = {
            'prenom': forms.TextInput(attrs={
                'placeholder': 'Vincent',
                'autocomplete': 'given-name',
            }),
            'nom': forms.TextInput(attrs={
                'placeholder': 'Tariel',
                'autocomplete': 'family-name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'vincent.tariel@cabinet.nc',
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
