# Cadrage stratégique — Dashboard Premier League 2019-2024

## Message clé

> **En Premier League, la victoire ne se joue pas seulement à domicile : dominer le jeu, convertir les tirs cadrés et maîtriser le risque disciplinaire constituent trois leviers déterminants de performance.**

## 1. Contexte et objectif

Ce dashboard interactif analyse les matchs de Premier League disputés entre les saisons **2019-20 et 2023-24**.

L'objectif n'est pas de reproduire l'analyse exploratoire des données, mais d'en restituer les principaux enseignements sous une forme synthétique, interactive et directement exploitable par une direction sportive.

L'analyse s'articule autour de trois dimensions :

- l'évolution de l'avantage domicile ;
- l'efficacité offensive ;
- la maîtrise du risque disciplinaire.

## 2. Audience cible

Le dashboard s'adresse principalement à la **direction sportive d'un club professionnel**.

Il peut également être utilisé par :

- la cellule de recrutement ;
- les analystes de la performance ;
- le staff technique ;
- les entraîneurs ;
- les consultants en stratégie sportive.

### Décisions à éclairer

Le dashboard vise à soutenir les décisions suivantes :

- évaluer l'importance réelle de l'avantage domicile ;
- comparer l'efficacité offensive des équipes ;
- identifier les équipes qui transforment le mieux leurs tirs cadrés ;
- repérer les équipes présentant une exposition disciplinaire élevée ;
- comparer un club aux standards de la Premier League ;
- orienter les analyses de recrutement et les axes de travail à l'entraînement.

Les résultats complètent l'expertise du staff et ne constituent pas des recommandations automatiques.

## 3. KPIs retenus

La zone de synthèse est volontairement limitée à **trois indicateurs**, afin de réduire la charge cognitive et de rendre l'essentiel visible en moins de cinq secondes.

### 3.1. Avantage domicile

**Définition :** différence entre les points obtenus par match à domicile et les points obtenus par match à l'extérieur.

```text
Avantage domicile =
Points par match à domicile - Points par match à l'extérieur
```

**Interprétation :**

- une valeur positive indique une meilleure performance à domicile ;
- une valeur proche de zéro indique des performances comparables selon le lieu ;
- une valeur négative indique une meilleure performance à l'extérieur.

**Pourquoi cet indicateur est actionnable :** il permet d'évaluer l'importance du contexte domicile-extérieur dans la préparation des rencontres et des déplacements.

**Pourquoi ce n'est pas une vanity metric :** il compare deux situations de jeu et présente une valeur normalisée par match, contextualisée par rapport à une saison de référence.

### 3.2. Taux de conversion des tirs cadrés

**Définition :** part des tirs cadrés transformés en buts.

```text
Taux de conversion =
Nombre de buts / Nombre de tirs cadrés x 100
```

**Exemple :** une équipe qui marque 15 buts à partir de 50 tirs cadrés présente un taux de conversion de 30 %.

**Pourquoi cet indicateur est actionnable :** il permet d'évaluer l'efficacité offensive au-delà du volume de tirs. Il peut soutenir l'analyse de la finition, l'évaluation des joueurs offensifs et l'identification des besoins de recrutement.

**Pourquoi ce n'est pas une vanity metric :** il rapporte les buts à un volume d'occasions cadrées, contrairement au nombre brut de buts ou de tirs.

**Limite :** il ne tient pas compte de la qualité des occasions. Les expected goals constitueraient un enrichissement utile.

### 3.3. Indice disciplinaire

**Définition :** indice combinant les cartons jaunes et rouges reçus par une équipe, rapporté au nombre de matchs.

```text
Indice disciplinaire =
(Cartons jaunes + 2 x Cartons rouges) / Nombre de matchs
```

**Pourquoi cet indicateur est actionnable :** il permet d'identifier les équipes exposées aux expulsions, suspensions et changements tactiques contraints.

**Pourquoi ce n'est pas une vanity metric :** les sanctions sont normalisées par match et mises en relation avec la performance sportive.

**Limite :** la pondération d'un carton rouge par un coefficient de 2 constitue une convention analytique interne, et non une mesure officielle de la Premier League.

## 4. Métriques écartées du premier niveau

Les indicateurs suivants ne figurent pas dans la zone KPI principale :

- **nombre total de buts**, car il dépend du nombre de matchs ;
- **nombre brut de tirs**, car il mesure le volume sans évaluer le rendement ;
- **nombre brut de victoires**, car il n'est pas normalisé ;
- **total de cartons**, car il est difficilement comparable sans rapport par match ;
- **possession**, car elle ne renseigne pas seule sur la création d'occasions dangereuses.

## 5. Structure du dashboard

### 5.1. Barre latérale

La barre latérale contient trois filtres interactifs :

- **saisons** ;
- **équipes** ;
- **lieu du match** : tous, domicile ou extérieur.

Les indicateurs et les graphiques réagissent aux filtres sélectionnés.

### 5.2. Zone de synthèse

La partie supérieure du dashboard présente :

- un titre portant la conclusion principale ;
- un sous-titre présentant les trois leviers étudiés ;
- trois KPIs contextualisés ;
- une comparaison avec la saison 2019-20.

### 5.3. Zone d'analyse détaillée

Le dashboard comprend quatre onglets.

#### Onglet 1 — Avantage domicile

- évolution des points par match à domicile et à l'extérieur ;
- comparaison selon les saisons ;
- analyse du lien entre domination par les tirs cadrés et victoire à domicile ;
- mise en perspective de la saison 2020-21 disputée largement à huis clos.

#### Onglet 2 — Efficacité offensive

- classement des équipes par taux de conversion ;
- mise en valeur du maximum en vert et du minimum en rouge ;
- atténuation des équipes intermédiaires en gris ;
- affichage de la valeur sur chaque barre ;
- relation entre taux de conversion et points par match.

#### Onglet 3 — Discipline

- comparaison entre l'indice disciplinaire et les points par match ;
- identification des équipes combinant sanctions élevées et rendement faible ;
- rappel qu'une association statistique ne démontre pas une relation causale.

#### Onglet 4 — Classement

- classement détaillé par saison ;
- affichage des matchs, victoires, nuls, défaites, buts et points ;
- mise en valeur du maximum en vert et du minimum en rouge ;
- atténuation des équipes intermédiaires pour accélérer la lecture.

## 6. Justification des visualisations

### Histogramme

L'histogramme est utilisée pour voir les points par match selon les saisons. Elle permet d'observer rapidement le rapprochement ou l'éloignement des performances à domicile et à l'extérieur.

Le principal canal pré-attentif est la **position verticale**, complétée par la distance entre les deux lignes.

### Barres horizontales

Les barres horizontales sont adaptées au classement des équipes. Leur longueur permet une comparaison quantitative précise, tandis que l'orientation horizontale facilite la lecture des noms.

La couleur est utilisée uniquement pour attirer l'attention sur les extrêmes. Elle ne remplace pas la longueur comme canal principal de comparaison.

### Nuages de points

Les nuages de points permettent d'étudier les relations entre :

- le taux de conversion et les points par match ;
- l'indice disciplinaire et les points par match.

La position horizontale et la position verticale représentent les deux variables quantitatives. La taille des points traduit le nombre de matchs observés.

### Tableau de classement

Le tableau apporte les valeurs précises nécessaires à une consultation détaillée : matchs joués, victoires, nuls, défaites, buts marqués, buts encaissés, différence de buts et points.

## 7. Hiérarchie visuelle

L'interface utilise une palette volontairement limitée :

- **bleu nuit** pour l'identité institutionnelle et les titres ;
- **vert** pour la performance maximale et les éléments positifs ;
- **rouge** pour la valeur minimale ou le risque ;
- **jaune** pour la discipline ;
- **gris** pour atténuer les informations intermédiaires ;
- **blanc** pour les cartes et les surfaces de lecture.

Les titres, axes, unités, infobulles et étiquettes suivent les mêmes conventions dans tous les graphiques.

## 8. Honnêteté et précautions d'interprétation

Les visualisations respectent les proportions des données. Les couleurs orientent l'attention sans modifier les longueurs, les positions ou les échelles.

Les analyses mettent en évidence des **associations statistiques** et non des relations causales.

Une association entre le taux de conversion et les points par match ne prouve pas qu'une amélioration isolée de ce taux entraînera automatiquement une augmentation équivalente du nombre de points.

La saison 2019-20 n'est pas une référence pré-COVID totalement neutre, car sa fin s'est déroulée sans public.

## 9. Limites de l'analyse

Le dataset ne contient pas toutes les dimensions nécessaires à une analyse complète de la performance. Il ne fournit notamment pas :

- les expected goals ;
- la qualité et la position des occasions ;
- les blessures ;
- les compositions de départ ;
- les changements tactiques ;
- la fatigue des joueurs ;
- le contexte du calendrier ;
- la situation au score au moment des sanctions.

Les résultats doivent donc être interprétés comme des signaux quantitatifs destinés à compléter l'analyse métier.

## 10. Données et périmètre

Les données couvrent les saisons :

- 2019-20 ;
- 2020-21 ;
- 2021-22 ;
- 2022-23 ;
- 2023-24.

La division utilisée est **E0**, correspondant à la Premier League.

**Source principale :** [football-data.co.uk](https://www.football-data.co.uk/englandm.php)

## 11. Choix techniques

Le dashboard a été développé avec :

- Python ;
- Streamlit ;
- Pandas ;
- Plotly ;
- Statsmodels.

Le chargement et la transformation des données utilisent `@st.cache_data` afin d'améliorer les performances de l'application.

Les fichiers sont chargés depuis le dossier local `data`. Si un fichier est absent, l'application peut tenter de le télécharger depuis la source.

## 12. Critères de réussite

Le dashboard est considéré comme réussi si l'utilisateur peut :

- comprendre le message principal en moins de cinq secondes ;
- identifier les trois indicateurs majeurs ;
- filtrer l'analyse sans difficulté ;
- comparer rapidement les équipes ;
- repérer les valeurs extrêmes ;
- comprendre les unités et les axes sans explication supplémentaire ;
- distinguer les constats statistiques des conclusions causales.

---

*Projet Bachelor Data et IA — MD4 Dashboards & Data Visualisation*
