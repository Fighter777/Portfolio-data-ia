# P9 — Analyse des ventes de LaPage

## Contexte

Application Streamlit réalisée à partir du brief OpenClassrooms P9 pour explorer les ventes et les profils clients de la librairie fictive LaPage.

## Objectif

Mettre à disposition une lecture interactive des performances commerciales, des produits et des comportements clients.

## Fonctionnalités

- vue de pilotage : KPI, évolution du chiffre d'affaires et moyenne mobile ;
- analyse produits : meilleures et moins bonnes ventes, catégories ;
- analyse clients : segmentation B2B potentielle, courbe de Lorenz et recherches de corrélations ;
- filtres par période, catégorie et genre.

## Compétences mobilisées

Python, Pandas, Streamlit, visualisation de données, analyse de clientèle et tests automatisés.

## Livrables

- [Analyse exploratoire des ventes](livrables/P9_analyse_ventes_lapage.ipynb)
- [Analyse statistique des profils clients](livrables/P9_analyse_statistique_lapage.ipynb)
- [Présentation de synthèse (PDF)](livrables/P9_presentation_analyse_ventes_lapage.pdf)

## Aperçu du dashboard

La page d'accueil regroupe les KPI, la couverture des données, le mix produit et les clients B2B potentiels.

![Accueil du dashboard LaPage](assets/dashboard_accueil.png)

La vue exécutive met en regard l'évolution du chiffre d'affaires, les commandes, les clients actifs et la contribution des catégories.

![KPI exécutifs LaPage](assets/dashboard_kpi_executifs.png)

La page produit permet d'identifier les références les plus contributrices, les moins performantes et les volumes vendus par catégorie.

![Analyse des produits LaPage](assets/dashboard_analyse_produits.png)

La page client croise les catégories achetées avec le genre et l'âge, et représente la concentration du chiffre d'affaires par une courbe de Lorenz.

![Analyse des clients LaPage](assets/dashboard_analyse_clients.png)

## Exécution du projet source

```bash
python -m streamlit run dashboard/app.py
```

Les tests du projet sont lancés avec `pytest` depuis le dépôt source.
