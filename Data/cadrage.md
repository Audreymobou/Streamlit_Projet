# Cadrage — Dashboard Premier League 2019–2024

## Message clé
> **L'avantage du terrain en Premier League s'est structurellement érodé depuis la saison COVID (2019/20) et ne s'est jamais totalement rétabli : miser sur la seule "force du domicile" est un pari de plus en plus faible, l'efficacité offensive et la discipline pèsent davantage sur les points.**

Ce constat est documenté par plusieurs études indépendantes (Opta Analyst, Sky Sports, PLOS One 2024) : le taux de victoires à domicile est tombé à son plus bas niveau historique lors de la saison à huis clos (37,9 %) et n'est jamais revenu à son niveau d'avant 2019, même après le retour du public. Le dashboard permet de vérifier ce phénomène sur les 5 dernières saisons complètes de Premier League et d'en tirer des implications concrètes pour un club.

## Audience cible
**Direction sportive d'un club de Premier League** (directeur sportif, cellule de recrutement / stratégie). Cette audience doit arbitrer un budget entre :
- investir dans l'exploitation du calendrier / de l'effet domicile,
- recruter pour l'efficacité offensive,
- travailler la discipline collective.

Le dashboard doit donc porter une **conclusion actionnable**, pas un simple constat descriptif du dataset.

## KPIs retenus

| KPI | Formule | Vanity ou Actionable ? | Justification |
|---|---|---|---|
| **Écart Points/Match Domicile − Extérieur** | PPG(dom.) − PPG(ext.), par saison | **Actionable** | Mesure directement si "jouer à domicile" rapporte encore des points — sert à arbitrer la valeur perçue des abonnements/atmosphère du stade. Comparé à la saison 2019/20 (baseline), il révèle une tendance, pas une photo isolée. |
| **Taux de conversion offensive** (Buts / Tirs cadrés, %) | par équipe | **Actionable** | Différencie une équipe qui "tire beaucoup" (vanity : nombre de tirs) d'une équipe qui **transforme** — un vrai critère de recrutement, contrairement au nombre brut de buts qui dépend du volume de matchs. |
| **Cartons par match vs Points/Match** | (Jaunes + 2×Rouges)/matchs, mis en regard du PPG | **Actionable** | Relie un comportement contrôlable (discipline) à la performance en points — permet de dire si l'indiscipline coûte réellement des points à l'équipe, argument pour le staff. |

**Métriques volontairement écartées (vanity metrics)** : nombre total de buts marqués sur la saison (dépend du nombre de matchs, ne dit rien de l'efficacité), nombre de tirs bruts (sans mise en relation avec la conversion), nombre de victoires brutes (sans normalisation par le nombre de matchs joués).

## Structure du dashboard

- **Titre** : porte le message ("L'avantage du terrain s'érode...") plutôt que le nom du dataset.
- **Zone KPIs** (haut de page, 3 indicateurs contextualisés avec `st.metric` et delta vs saison 2019/20) : écart PPG dom./ext., taux de victoires à domicile, cartons/match.
- **Zone filtres (sidebar)** : sélection des saisons (2019/20 → 2023/24), sélection des équipes, sélection du lieu (Domicile / Extérieur / Tous).
- **Zone détail (3 onglets, réactifs aux filtres)** :
  1. *Avantage domicile* — évolution PPG dom./ext. et % victoires dom. par saison.
  2. *Efficacité offensive* — classement des équipes par taux de conversion, nuage de points conversion vs points/match.
  3. *Discipline* — cartons/match par équipe vs points/match, pour objectiver le coût de l'indiscipline.

## Source des données
[football-data.co.uk](https://www.football-data.co.uk/englandm.php) — division E0 (Premier League), saisons 2019/20 à 2023/24. Le script télécharge automatiquement les 5 fichiers CSV officiels si absents du dossier `data/`.
