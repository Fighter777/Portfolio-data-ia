<p align="right"><a href="../README.md">← Retour au portfolio</a></p>

# <img src="../assets/icons/p6-wine.svg" width="38" valign="middle" alt="Catalogue caviste"> P6 — Analyse du catalogue d'un caviste

<p>
  <img src="../assets/logos/python.svg" width="30" alt="Python" title="Python">
  <img src="../assets/logos/pandas.svg" width="30" alt="Pandas" title="Pandas">
  <img src="../assets/logos/plotly.svg" width="30" alt="Plotly" title="Plotly">
  <img src="../assets/logos/jupyter.svg" width="30" alt="Jupyter" title="Jupyter">
</p>

---


<p align="center">
  <img src="assets/top_chiffre_affaires.png" width="760" alt="Principales références par chiffre d’affaires">
  <br>
  <sub>Principales références par chiffre d’affaires</sub>
</p>

## ![](../assets/sections/context.svg) Contexte

Projet réalisé dans le cadre du parcours **Data Analyst OpenClassrooms**.


## ![](../assets/sections/goal.svg) Besoin métier

Réconcilier le catalogue issu de l'ERP avec les produits publiés sur le site e-commerce, puis analyser les ventes, les prix et les stocks afin d'identifier des anomalies et des produits à surveiller.

## ![](../assets/sections/data.svg) Données

Trois sources Excel sont exploitées : le catalogue ERP, les produits du site e-commerce et une table de liaison entre leurs références.

- 825 références ERP ;
- 714 produits rapprochés avec les données web ;
- 111 références non rapprochées à investiguer ;
- variables principales : prix, quantité en stock, ventes cumulées et métadonnées de publication.

## ![](../assets/sections/method.svg) Démarche

1. compréhension du besoin ;
2. audit des données ;
3. nettoyage ;
4. analyse exploratoire ;
5. visualisation ;
6. interprétation ;
7. recommandations.


## ![](../assets/sections/results.svg) Résultats

Le notebook produit un jeu de données consolidé, contrôle les incohérences de prix et de stock, et présente les ventes cumulées par produit. L'analyse met notamment en évidence des valeurs négatives à vérifier dans les données de prix ou de stock, ainsi que les références sans correspondance entre ERP et site.

## ![](../assets/sections/results.svg) Aperçu de l'analyse

La distribution des prix met en évidence un catalogue majoritairement positionné sur des prix accessibles, complété par quelques références premium.

<p align="center">
  <img src="assets/repartition_prix_vente.png" width="760" alt="Répartition des prix de vente">
</p>

La marge moyenne varie fortement selon les familles de produits : ce résultat fournit un premier axe de priorisation commerciale.

<p align="center">
  <img src="assets/marge_moyenne_par_type.png" width="760" alt="Taux de marge moyen par type de produit">
</p>

La matrice permet de mettre en regard prix, coût d'achat, stock, ventes cumulées et taux de marge.

<p align="center">
  <img src="assets/matrice_correlation.png" width="760" alt="Matrice de corrélation">
</p>

Les classements par chiffre d'affaires et par quantités vendues distinguent les références qui génèrent le plus de valeur de celles qui génèrent le plus de volume.

<p align="center">
  <img src="assets/top_quantites_vendues.png" width="760" alt="Top 20 des articles en quantités vendues">
</p>

Enfin, la couverture de stock en mois identifie les références à surveiller pour éviter une immobilisation excessive.

<p align="center">
  <img src="assets/couverture_stock_mois.png" width="760" alt="Top 20 des produits avec le plus de mois de stock">
</p>

## ![](../assets/sections/skills.svg) Compétences mobilisées

- préparation des données ;
- EDA ;
- contrôle qualité ;
- visualisation ;
- interprétation métier ;
- documentation.

## ![](../assets/sections/limits.svg) Limites

- les ventes sont disponibles sous forme cumulée, sans historique de transactions ;
- les dates de publication WordPress ne correspondent pas à des dates d'achat ;
- il n'est donc pas possible d'établir une prévision saisonnière fiable à partir de ce jeu de données seul.

## ![](../assets/sections/deliverables.svg) Livrables

- [Notebook d'analyse](livrables/P6_analyse_catalogue_caviste.ipynb)
- [Présentation de synthèse (PDF)](livrables/P6_presentation_analyse_catalogue_caviste.pdf)

---

[← Retour au portfolio](../README.md)
