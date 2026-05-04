# Prompt Claude for Chrome — Envoi des 7 demandes de connexion LinkedIn

> **Objectif** : envoyer les 7 demandes de connexion personnalisées du batch 01.
> **Mode opératoire** : copilote — Claude for Chrome PRÉPARE chaque demande
> (ouvre profil, clique "Se connecter", colle la note), puis Vincent confirme
> AVANT que Claude clique "Envoyer". Sécurité maximale, zéro risque d'envoi
> en rafale qui ferait flagger LinkedIn.

---

## Le prompt à coller (tout ce qui suit)

```
# CONTEXTE

Je m'appelle Vincent Tariel. Je suis solopreneur à Nouméa
(Nouvelle-Calédonie), je lance Atelier IA — du coaching individuel
sur Claude Desktop pour les responsables com/marketing en PME
calédoniennes.

Tu vas m'aider à envoyer 7 demandes de connexion LinkedIn aux
prospects que tu as toi-même sourcés au tour précédent. Les notes
de connexion sont déjà rédigées (≤ 300 caractères chacune, conformes
aux règles Atelier IA — ton sobre, pas de pitch produit, accroche
personnalisée).

# RÈGLE DE SÉCURITÉ — MODE COPILOTE STRICT

Tu NE DOIS PAS cliquer toi-même sur "Envoyer". Pour chaque demande,
tu fais ceci, dans cet ordre :

  1. Ouvre l'URL du profil LinkedIn dans un nouvel onglet.
  2. Clique sur le bouton "Se connecter" (parfois caché derrière
     "Plus" si LinkedIn le masque).
  3. Dans la fenêtre qui s'ouvre, clique sur "Ajouter une note".
  4. Colle exactement la note rédigée pour ce prospect (rien de plus,
     rien de moins).
  5. ARRÊTE-TOI là. Affiche en chat :
        "Demande [N°] prête pour [Prénom Nom] — relisez et cliquez
         Envoyer dans la fenêtre LinkedIn."
  6. ATTENDS que je te dise "OK suivant" avant de passer au prospect
     suivant.

Si à un moment tu ne trouves pas le bouton "Se connecter" (parce que
le prospect n'a pas activé ce paramètre, ou que LinkedIn me limite),
indique-le clairement et passe au prospect suivant après mon accord.

# CADENCE

LinkedIn surveille les comportements automatisés. Pour rester invisible :

  - Maximum 3 à 4 demandes par séance.
  - Espacement minimum 90 secondes entre deux demandes (le temps
    que je relise et clique Envoyer).
  - Si je te dis "stop pour aujourd'hui", tu archives où on en est
    et on reprendra demain.

# LES 7 DEMANDES À ENVOYER

Tableau ci-dessous : pour chaque prospect, l'URL et la note exacte.
Tu colles la note TELLE QUELLE (pas de variation, pas d'amélioration
de ta part — elles ont été calibrées).

----------------------------------------------------------------------
PROSPECT 1 : Thi Mai Huong Julie Nguyen — Hyper U Païta
URL : https://www.linkedin.com/in/thi-mai-huong-julie-nguyen-822997340/

NOTE :
Bonjour Julie,

Vincent Tariel — docteur de l'École Polytechnique. Je propose à Nouméa un coaching individuel sur Claude Desktop, l'IA d'Anthropic.

Le travail de fidélisation sur la zone Païta-Dumbéa que vous menez chez Hyper U m'intéresse — j'aimerais qu'on échange à l'occasion.

Cordialement,
Vincent
----------------------------------------------------------------------
PROSPECT 2 : Nina Néris — Groupe Cuenet
URL : https://www.linkedin.com/in/ninaneris/

NOTE :
Bonjour Nina,

Vincent Tariel — docteur de l'École Polytechnique. Coaching individuel sur Claude Desktop à Nouméa, pour les responsables com.

La com transverse multi-marques d'un groupe familial comme Cuenet est exactement le terrain où l'IA bien configurée fait gagner le plus de temps. Échange ?

Cordialement,
Vincent
----------------------------------------------------------------------
PROSPECT 3 : Marine Gachet — Quincaillerie Calédonienne
URL : https://www.linkedin.com/in/marinehg/

NOTE :
Bonjour Marine,

Vincent Tariel — docteur de l'École Polytechnique. Je propose à Nouméa du coaching individuel sur Claude Desktop.

Animer un catalogue B2B/B2C aussi large que celui de la Quincaillerie Calédonienne en com hebdo, c'est un cas d'usage intéressant — j'aimerais en parler avec vous.

Cordialement,
Vincent
----------------------------------------------------------------------
PROSPECT 4 : Elise Millou — MDF
URL : https://www.linkedin.com/in/elise-millou/

NOTE :
Bonjour Elise,

Vincent Tariel — docteur de l'École Polytechnique. Coaching individuel sur Claude Desktop à Nouméa.

Votre intitulé "culture mutualiste" m'a accroché : le travail de pédagogie auprès des adhérents MDF est précisément ce que l'IA bien encadrée peut amplifier. J'aimerais en discuter.

Cordialement,
Vincent
----------------------------------------------------------------------
PROSPECT 5 : Laura Klotz — GBNC
URL : https://www.linkedin.com/in/laura-klotz-5ba8bb50/

NOTE :
Bonjour Laura,

Vincent Tariel — docteur de l'École Polytechnique. Je propose à Nouméa un coaching individuel sur Claude Desktop.

Un poste mixte com & sustainability chez GBNC suggère beaucoup de production écrite (interne et externe) à articuler. C'est exactement là où le coaching apporte. Échange à l'occasion ?

Cordialement,
Vincent
----------------------------------------------------------------------
PROSPECT 6 : Axelle Venard — Groupe Jeandot
URL : https://www.linkedin.com/in/axelle-venard-094b50291/

NOTE :
Bonjour Axelle,

Vincent Tariel — docteur de l'École Polytechnique. Coaching individuel sur Claude Desktop à Nouméa, pour les responsables com.

Décliner une com cohérente sur les multiples enseignes du Groupe Jeandot, c'est un cas typique où Claude bien configuré rend des heures par semaine. Discutons ?

Cordialement,
Vincent
----------------------------------------------------------------------
PROSPECT 7 : Maurane Néris — Austral Import (Groupe SOL)
URL : https://www.linkedin.com/in/maurane-n%C3%A9ris-66201b1b3/

NOTE :
Bonjour Maurane,

Vincent Tariel — docteur de l'École Polytechnique. Je propose à Nouméa un coaching individuel sur Claude Desktop.

Tenir 5 marques aux univers différents en gardant chacun son ton, c'est l'archétype du cas où Claude bien encadré fait économiser des heures. J'aimerais en parler avec vous.

Cordialement,
Vincent
----------------------------------------------------------------------

# PROGRAMME DE LA SÉANCE

Aujourd'hui (mardi/mercredi/jeudi de préférence) : on en envoie 3 ou 4.
Demain ou après-demain : on envoie les restants.

Cas particuliers à signaler immédiatement :
- Profil indisponible (compte supprimé, blocage)
- Pas de bouton "Se connecter" visible
- Vincent et le prospect sont déjà en relation (auquel cas on saute la
  demande de connexion et on note "déjà connecté — passer direct au
  message post-connexion")
- LinkedIn affiche "Vous avez atteint votre limite hebdomadaire"
  (improbable à 7 demandes, mais possible si Vincent en a déjà fait)

# REPORTING — À LA FIN DE LA SÉANCE

Quand on s'arrête (parce qu'on a fini OU parce que je te dis "stop"),
retourne-moi un tableau ainsi :

| N° | Prénom Nom | Statut | Notes |
|----|------------|--------|-------|
| 1  | Julie Nguyen | Demande envoyée | OK |
| 2  | Nina Néris | Demande envoyée | OK |
| 3  | Marine Gachet | À refaire | Bouton non trouvé, profil masqué |
| ... | ... | ... | ... |

Je l'utiliserai pour mettre à jour mon CSV de prospection.

# COMMENCE PAR LE PROSPECT 1

Ouvre le profil LinkedIn de Julie Nguyen, prépare la demande avec
la note ci-dessus, et signale-moi quand c'est prêt à envoyer.
```

---

## Après la séance

1. Récupérer le tableau de reporting que Claude for Chrome retourne.
2. Mettre à jour `acquisition/prospects.csv` :
   - Pour chaque demande envoyée : `statut` → `Connexion demandée` + `date_premier_contact` → date du jour
   - Pour chaque "À refaire" : laisser `À contacter` et noter le souci dans `notes`
3. **Surveiller les notifications LinkedIn** dans les 7 prochains jours :
   - Acceptation → déclencher le message post-connexion sous 24-48h
     (cf. `acquisition/linkedin_templates/02_message_post_connexion.md`)
   - Refus / pas de réponse à J+21 → passer en `Sans suite`
