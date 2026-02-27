from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    """
    Formulaire pour la capture de prospects.
    Intègre directement les classes Tailwind CSS pour un rendu esthétique et responsive.
    """
    class Meta:
        model = Lead
        fields = ['prenom', 'nom', 'email', 'entreprise', 'telephone', 'formation_interessee']
        
        # Définition des classes Tailwind CSS de base pour les champs de saisie
        base_input_classes = "w-full px-4 py-2 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900"
        
        widgets = {
            'prenom': forms.TextInput(attrs={
                'class': base_input_classes,
                'placeholder': 'Anjelai'
            }),
            'nom': forms.TextInput(attrs={
                'class': base_input_classes,
                'placeholder': 'Calonne'
            }),
            'email': forms.EmailInput(attrs={
                'class': base_input_classes,
                'placeholder': 'anjelai.calonne@entreprise.nc'
            }),
            'entreprise': forms.TextInput(attrs={
                'class': base_input_classes,
                'placeholder': 'Nom de votre entreprise (Optionnel)'
            }),
            'telephone': forms.TextInput(attrs={
                'class': base_input_classes,
                'placeholder': 'Votre numéro (Optionnel)'
            }),
            'formation_interessee': forms.Select(attrs={
                'class': base_input_classes
            }),
        }
