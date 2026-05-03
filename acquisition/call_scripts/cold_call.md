# Script — Appel à froid

> À utiliser **après** au moins un email envoyé (jamais en premier contact). L'objectif n'est PAS de vendre au téléphone, c'est de **caler un RDV de 30 min**.

---

## Contexte avant d'appeler

- Avoir l'email envoyé sous les yeux (savoir quel template, quelle date).
- Avoir noté **1 info concrète** sur l'entreprise (secteur, actu récente, taille).
- Heure d'appel : éviter lundi matin, vendredi après-midi, et la pause déjeuner (11h30-13h30).

---

## Ouverture (15 secondes max)

```
"Bonjour, Vincent Tariel à l'appareil — je vous appelle suite 
à un email envoyé la semaine dernière. Vous l'avez peut-être vu 
passer, sur l'utilisation de Claude — l'IA d'Anthropic — au 
quotidien dans votre métier. Vous avez deux minutes ?"
```

→ Si "non, pas le temps" : "Pas de souci, je peux vous rappeler quand ?" (caler un créneau précis).
→ Si "oui" : continuer.

---

## Pitch (30 secondes max)

```
"En résumé : je propose un coaching individuel à Nouméa pour 
les pros qui veulent intégrer Claude dans leur quotidien — 
pour gagner du temps sur la rédaction, les synthèses, les 
préparations de RDV, ce genre de choses. Pas du tout une 
formation théorique, on travaille sur vos vrais dossiers, 
vous repartez avec des workflows opérationnels.

Si ça vous parle, je propose un échange de 30 minutes en 
présentiel ou en visio pour voir concrètement ce que ça 
pourrait vous apporter. C'est gratuit et sans engagement."
```

---

## Demande de RDV

```
"Vous seriez disponible plutôt en début ou en fin de semaine 
prochaine ?"
```

→ Toujours offrir un **choix binaire** plutôt qu'une question ouverte.

```
[Si début] "Mardi 10h ou jeudi 16h, qu'est-ce qui vous arrange ?"
[Si fin] "Vendredi 9h ou jeudi en fin de journée ?"
```

---

## Réponses aux objections fréquentes

### "Je suis pas intéressé."
```
"Sans problème — par curiosité, qu'est-ce qui vous fait dire ça ? 
C'est le sujet IA, le format coaching, ou autre chose ?"
```
→ Récolter une info utile pour ajuster les prochaines campagnes. Ne pas insister.

### "C'est trop cher / je n'ai pas de budget."
```
"On n'a pas encore parlé de prix — vous voulez qu'on prenne 
20 minutes pour que je vous donne une fourchette précise selon 
votre cas ?"
```

### "J'ai déjà essayé l'IA, ça ne marche pas."
```
"C'est l'objection la plus fréquente, et c'est exactement la 
raison du coaching. La différence entre 'ça sert à rien' et 
'j'ai gagné une heure par jour', c'est trois ou quatre réflexes 
qu'on transmet en quelques heures. On peut en faire un test 
sur l'un de vos cas réels en RDV ?"
```

### "Envoyez-moi de la doc / un lien."
```
"Bien sûr, je vous envoie un PDF de 10 cas d'usage par email. 
Mais franchement, le coaching ne s'apprécie qu'en discutant de 
votre cas concret — je peux vous rappeler dans 2 semaines pour 
voir si ça vous a parlé ?"
```

### "Je vous rappelle."
```
"Très bien — je vous renvoie un mail récap aujourd'hui pour 
que vous ayez tout sous les yeux. Si je n'ai pas de retour, 
je me permets un coup de fil dans 10 jours, ça vous convient ?"
```

---

## Après l'appel

- [ ] Mettre à jour `crm/leads/{nom}.md` avec la date de l'appel + résumé en 3 lignes
- [ ] Mettre à jour `prospects.csv` (statut + prochaine action + date)
- [ ] Si RDV calé : créer l'invitation calendrier + envoyer email de confirmation
- [ ] Si renvoi à plus tard : créer un rappel dans son agenda
