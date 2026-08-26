<p align="right"><a href="../README.md">← Retour au portfolio</a></p>

# <img src="../assets/icons/p11-world.svg" width="38" valign="middle" alt="Marché international"> P11 — Étude de marché internationale

<p>
  <img src="../assets/logos/python.svg" width="30" alt="Python" title="Python">
  <img src="../assets/logos/pandas.svg" width="30" alt="Pandas" title="Pandas">
  <img src="../assets/logos/sklearn.svg" width="30" alt="scikit-learn" title="scikit-learn">
  <img src="../assets/logos/jupyter.svg" width="30" alt="Jupyter" title="Jupyter">
</p>

---


<p align="center">
  <img src="assets/clusters_kmeans_plan_factoriel.png" width="760" alt="Projection des clusters K-means sur le plan factoriel">
  <br>
  <sub>Projection des clusters K-means sur le plan factoriel</sub>
</p>

## ![](../assets/sections/context.svg) Contexte

Projet d'analyse réalisé dans le parcours **Data Analyst OpenClassrooms** pour orienter le développement international d'un acteur de la filière volaille.

## ![](../assets/sections/goal.svg) Besoin métier

Comparer les marchés internationaux de la volaille afin de prioriser des pays cibles pour une stratégie d'export.

## ![](../assets/sections/data.svg) Données

Les données regroupent des indicateurs internationaux de consommation, production, importation et prix de la volaille, enrichis par des données économiques, démographiques, alimentaires et de gouvernance. Les sources mobilisées comprennent notamment la FAO, la Banque mondiale, les indicateurs de gouvernance WGI et le CEPII.

Les indicateurs de dynamique couvrent principalement la période 2013–2017, selon la disponibilité des sources.

## ![](../assets/sections/method.svg) Démarche

1. préparation et rapprochement des sources pays ;
2. construction d'indicateurs de marché, dépendance aux importations, demande et risque pays ;
3. analyse exploratoire et standardisation ;
4. ACP pour réduire la redondance entre variables ;
5. comparaison CAH et K-means ;
6. caractérisation des groupes ;
7. recommandations commerciales.


## ![](../assets/sections/skills.svg) Compétences mobilisées

- données externes ;
- EDA ;
- statistiques ;
- segmentation ;
- interprétation métier.

## ![](../assets/sections/deliverables.svg) Livrables

- [Préparation, nettoyage et analyse exploratoire](livrables/P11_preparation_nettoyage_analyse_exploratoire.ipynb)
- [Clustering et visualisations](livrables/P11_clustering_visualisations.ipynb)
- [Présentation de synthèse (PDF)](livrables/P11_presentation_etude_marche_volaille.pdf)

## ![](../assets/sections/results.svg) Résultats

L'ACP met notamment en évidence la maturité commerciale, la taille du marché de la volaille, le poids de la volaille dans l'alimentation et la dépendance aux importations. La sélection finale de **quatre clusters** s'appuie sur une lecture croisée du dendrogramme, du coude et du score de silhouette.

Les quatre profils identifiés sont :

- géants producteurs déjà installés ;
- marchés émergents, fragiles mais dynamiques ;
- marchés intermédiaires attractifs ;
- marchés riches, stables et importateurs.

La recommandation privilégie les marchés riches et importateurs, puis les marchés intermédiaires équilibrés. Il s'agit d'une aide à la priorisation et non d'une décision d'implantation autonome.

## ![](../assets/sections/results.svg) Aperçu des analyses

Le nombre de groupes a été confronté à plusieurs critères. Le score de silhouette permet notamment de comparer la cohésion des partitions testées.

<p align="center">
  <img src="assets/choix_clusters_silhouette.png" width="760" alt="Score de silhouette selon le nombre de clusters">
</p>

Le dendrogramme issu de la CAH par méthode de Ward donne une lecture complémentaire des rapprochements entre pays.

<p align="center">
  <img src="assets/dendrogramme_cah_ward.png" width="760" alt="Dendrogramme CAH par méthode de Ward">
</p>

La projection dans le plan factoriel rend visible la répartition des quatre clusters retenus.

Le cercle des corrélations aide à interpréter les axes de l'ACP et les familles d'indicateurs qui structurent les profils de marché.

<p align="center">
  <img src="assets/cercle_correlations_pc1_pc3.png" width="718" alt="Cercle des corrélations PC1 et PC3">
</p>

## ![](../assets/sections/limits.svg) Limites

- qualité variable des sources ;
- données manquantes ;
- décalages temporels ;
- limites de segmentation.
- les indicateurs « bio » éventuels décrivent un marché bio global, pas une demande spécifique de volaille bio.

## ![](../assets/sections/next.svg) Prochaines pistes

- actualiser les données ;
- intégrer de nouveaux indicateurs ;
- tester la stabilité des groupes ;
- compléter l'analyse par des contraintes réglementaires et des données de terrain pays par pays.

---

[← Retour au portfolio](../README.md)
