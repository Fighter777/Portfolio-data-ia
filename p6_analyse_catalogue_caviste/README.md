# P6 — Analyse du catalogue d'un caviste

## Contexte

Projet réalisé dans le cadre du parcours **Data Analyst OpenClassrooms**.


## Besoin métier

Réconcilier le catalogue issu de l'ERP avec les produits publiés sur le site e-commerce, puis analyser les ventes, les prix et les stocks afin d'identifier des anomalies et des produits à surveiller.

## Données

Trois sources Excel sont exploitées : le catalogue ERP, les produits du site e-commerce et une table de liaison entre leurs références.

- 825 références ERP ;
- 714 produits rapprochés avec les données web ;
- 111 références non rapprochées à investiguer ;
- variables principales : prix, quantité en stock, ventes cumulées et métadonnées de publication.

## Démarche

1. compréhension du besoin ;
2. audit des données ;
3. nettoyage ;
4. analyse exploratoire ;
5. visualisation ;
6. interprétation ;
7. recommandations.

## Technologies

- Python ;
- Pandas ;
- Plotly.

## Résultats

Le notebook produit un jeu de données consolidé, contrôle les incohérences de prix et de stock, et présente les ventes cumulées par produit. L'analyse met notamment en évidence des valeurs négatives à vérifier dans les données de prix ou de stock, ainsi que les références sans correspondance entre ERP et site.

## Compétences mobilisées

- préparation des données ;
- EDA ;
- contrôle qualité ;
- visualisation ;
- interprétation métier ;
- documentation.

## Limites

- les ventes sont disponibles sous forme cumulée, sans historique de transactions ;
- les dates de publication WordPress ne correspondent pas à des dates d'achat ;
- il n'est donc pas possible d'établir une prévision saisonnière fiable à partir de ce jeu de données seul.

## Livrables

- [Notebook d'analyse](livrables/P6_analyse_catalogue_caviste.ipynb)
- [Présentation de synthèse (PDF)](livrables/P6_presentation_analyse_catalogue_caviste.pdf)
