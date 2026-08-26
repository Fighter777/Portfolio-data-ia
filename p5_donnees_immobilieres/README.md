<p align="right"><a href="../README.md">← Retour au portfolio</a></p>

# <img src="../assets/icons/p5-real-estate.svg" width="38" valign="middle" alt="Immobilier"> P5 — Exploitation de données immobilières avec SQL

<p>
  <img src="../assets/logos/sql.svg" width="30" alt="SQL / MySQL" title="SQL / MySQL">
</p>

---

## Contexte

Projet du parcours Data Analyst d'OpenClassrooms portant sur l'organisation et l'interrogation de données immobilières.

## Objectif

Structurer les informations liées aux biens et aux communes afin de faciliter leur consultation et leur analyse dans une base relationnelle.

## Démarche

- analyse de la structure des données immobilières ;
- création et alimentation des tables SQL ;
- utilisation de clés et de contraintes pour relier les biens à leur contexte géographique ;
- écriture de requêtes d'exploration et de contrôle.

## Compétences mobilisées

MySQL, SQL, modélisation relationnelle, contraintes, indexation et contrôle de cohérence.

## Aperçu du projet

Le modèle relationnel relie les ventes, les biens, les communes, les départements et les régions pour permettre l'analyse des transactions immobilières.

<p align="center">
  <img src="assets/schema_relationnel_immobilier.png" width="760" alt="Schéma relationnel de la base immobilière">
</p>

Le chargement des différentes sources est vérifié avant l'exécution des requêtes d'analyse.

<p align="center">
  <img src="assets/controle_chargement_donnees.png" width="697" alt="Contrôle du chargement des données">
</p>

Les requêtes répondent ensuite à des questions métier sur les prix et les volumes de ventes.

<p align="center">
  <img src="assets/prix_moyen_par_region.png" width="261" alt="Prix moyen par région">
</p>

<p align="center">
  <img src="assets/evolution_ventes_t1_t2.png" width="130" alt="Évolution du nombre de ventes entre T1 et T2">
</p>

<p align="center">
  <img src="assets/prix_m2_ile_de_france.png" width="322" alt="Prix moyen au mètre carré en Île-de-France">
</p>

## Livrables réalisés

Les données brutes et les scripts sources ne sont pas recopiés ici afin de garder le portfolio léger.

- [Dictionnaire de données](livrables/P5_dictionnaire_de_donnees.xlsx)
- [Présentation de synthèse (PDF)](livrables/P5_presentation_donnees_immobilieres.pdf)

---

[← Retour au portfolio](../README.md)
