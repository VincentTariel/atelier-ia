# Gabarit — Dossier client

> Pour chaque client signé, copier ce dossier en `crm/clients/{nom-entreprise}/` et le remplir.

## Structure recommandée

```
crm/clients/{nom-entreprise}/
├── README.md                    ← infos générales du client (à partir du gabarit lead)
├── proposition_signee.pdf       ← PDF signé / accusé de réception
├── facture_acompte.pdf
├── factures/                    ← factures intermédiaires et solde
│   └── ...
├── sessions/                    ← compte-rendu de chaque session de coaching
│   ├── session_01_AAAA-MM-JJ.md
│   ├── session_02_AAAA-MM-JJ.md
│   └── ...
├── workflows_livres/            ← copie des Projects / workflows Claude Desktop livrés
│   └── ...
└── suivi_async/                 ← échanges email pendant les 30 jours de suivi
    └── ...
```

## Compte-rendu de session — gabarit

```markdown
# Session N°{X} — {AAAA-MM-JJ}

## Présents
- Vincent
- {nom client}

## Ce qui a été fait
- {workflow / sujet 1}
- {workflow / sujet 2}

## Workflows livrés (Projects Claude Desktop)
- {nom du Project} — {finalité}

## Difficultés rencontrées
- {ex: le client a du mal avec la notion de contexte → à reprendre en S2}

## Devoirs / pratique entre sessions
- {ex: utiliser le Project "Compte-rendu de réunion" 3 fois cette semaine}

## Prochaine session
- Date :
- Sujets prévus :
```

## Sécurité et confidentialité

- **Tout le contenu de `crm/clients/` est gitignored.** Aucune donnée client ne quitte la machine via git.
- Les sauvegardes se font via `[outil de backup à choisir — Time Machine, rsync vers disque externe, Nextcloud chiffré, etc.]`
- Sur demande client, fournir une attestation de destruction des données 12 mois après la fin de la prestation.
