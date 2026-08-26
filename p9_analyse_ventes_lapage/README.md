<p align="right"><a href="../README.md">← Retour au portfolio</a></p>

# <img src="../assets/icons/p9-books.svg" width="38" valign="middle" alt="Librairie"> P9 — Analyse des ventes de LaPage

<p>
  <img src="../assets/logos/python.svg" width="30" alt="Python" title="Python">
  <img src="../assets/logos/pandas.svg" width="30" alt="Pandas" title="Pandas">
  <img src="../assets/logos/streamlit.svg" width="30" alt="Streamlit" title="Streamlit">
  <img src="../assets/logos/plotly.svg" width="30" alt="Plotly" title="Plotly">
</p>

---

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

<p align="center">
  <img src="assets/dashboard_accueil.png" width="760" alt="Accueil du dashboard LaPage">
</p>

La vue exécutive met en regard l'évolution du chiffre d'affaires, les commandes, les clients actifs et la contribution des catégories.

<p align="center">
  <img src="assets/dashboard_kpi_executifs.png" width="760" alt="KPI exécutifs LaPage">
</p>

La page produit permet d'identifier les références les plus contributrices, les moins performantes et les volumes vendus par catégorie.

<p align="center">
  <img src="assets/dashboard_analyse_produits.png" width="760" alt="Analyse des produits LaPage">
</p>

La page client croise les catégories achetées avec le genre et l'âge, et représente la concentration du chiffre d'affaires par une courbe de Lorenz.

<p align="center">
  <img src="assets/dashboard_analyse_clients.png" width="760" alt="Analyse des clients LaPage">
</p>

## Exécution du projet source

```bash
python -m streamlit run dashboard/app.py
```

Les tests du projet sont lancés avec `pytest` depuis le dépôt source.

---

[← Retour au portfolio](../README.md)
