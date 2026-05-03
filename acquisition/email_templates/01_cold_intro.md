# Template — Cold email d'introduction (envoi initial)

> Variables à personnaliser : `{prenom}`, `{nom_entreprise}`, `{secteur_specifique}`, `{accroche_contextuelle}`

---

**Objet** (3 variantes à A/B tester) :

- A : `{prenom}, une question rapide sur votre temps de rédaction`
- B : `Claude Desktop pour {nom_entreprise} ?`
- C : `2h/jour de rédaction — vraiment nécessaire ?`

---

**Corps** :

```
Bonjour {prenom},

J'écris aux dirigeants de {secteur_specifique} en Nouvelle-Calédonie 
parce que j'ai constaté un point commun : entre les courriers, les 
comptes-rendus, les synthèses et les emails, beaucoup passent 
l'équivalent de deux heures par jour à écrire — du temps qui ne 
développe pas leur activité.

{accroche_contextuelle — 1 phrase qui montre que vous avez pris 30s 
pour regarder leur entreprise. Ex: "J'ai vu que vous avez ouvert 
votre cabinet en 2019, et que vous travaillez beaucoup avec les 
PME du BTP — un secteur où la production écrite est massive."}

Je propose un coaching individuel à Nouméa pour intégrer Claude 
Desktop (l'IA d'Anthropic) dans le quotidien — sur vos vrais 
dossiers, sans aucune ligne de code. L'objectif : récupérer 30 min 
à 1h par jour sur les tâches sans valeur ajoutée.

Seriez-vous ouvert à un échange de 30 minutes (sans engagement, 
chez vous ou en visio) pour voir si ça vous parle ?

Bien cordialement,

Vincent Tariel
Atelier IA — Nouméa
atelier-ia.ovh
+687 [téléphone]

PS : pour vous faire une idée sans m'écouter parler, j'ai préparé 
un guide de 10 cas d'usage à télécharger ici : [lien lead-magnet]
```

---

## Notes d'usage

- **Personnalisation obligatoire** : la phrase `{accroche_contextuelle}` ne doit JAMAIS être générique. Si vous n'avez pas le temps de la personnaliser, n'envoyez pas.
- **Longueur cible** : ~150 mots. Plus long = perte d'attention.
- **Heure d'envoi optimale en NC** : mardi-jeudi, 8h-9h ou 17h-18h locale.
- **Pas de pièce jointe** dans le premier email (déclenche les filtres anti-spam).
- **Signature simple** : pas de bannière image, pas de logo. Texte uniquement.
- **Tracking optionnel** : un pixel d'ouverture (Mailtrack ou équivalent) si vous voulez mesurer le taux d'ouverture.

## Checklist avant envoi

- [ ] L'email du destinataire est vérifié (pas un `contact@` générique)
- [ ] L'accroche contextuelle est réellement personnalisée
- [ ] Le statut du prospect est mis à jour dans `prospects.csv` (`Contacté` + date)
- [ ] Une fiche est créée dans `crm/leads/{nom}.md` si lead à fort potentiel
- [ ] Une relance J+7 est planifiée
