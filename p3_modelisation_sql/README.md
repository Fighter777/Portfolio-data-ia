<p align="right"><a href="../README.md">← Retour au portfolio</a></p>

# <img src="../assets/icons/p3-database.svg" width="38" valign="middle" alt="Base de données"> P3 — Modélisation et interrogation SQL

<p>
  <img src="../assets/logos/sql.svg" width="30" alt="SQL" title="SQL">
</p>

---


<p align="center">
  <img src="assets/schema_relationnel.png" width="760" alt="Schéma relationnel du projet">
  <br>
  <sub>Schéma relationnel du projet</sub>
</p>

## 📋 Contexte

Projet du parcours Data Analyst d'OpenClassrooms consacré à la construction et à l'exploitation d'une base de données relationnelle.

## 🎯 Objectif

Transformer un besoin de gestion en un modèle de données cohérent, puis produire des requêtes SQL répondant aux questions métier.

## ⚙️ Démarche

- étude des entités, attributs et relations ;
- formalisation du schéma de données et du dictionnaire associé ;
- création des tables SQL, notamment autour des données d'étudiants, de régions et de contrats ;
- rédaction et vérification des requêtes demandées.

## 🎓 Compétences mobilisées

SQL, modélisation relationnelle, clés primaires et étrangères, intégrité référentielle, dictionnaire de données.

## 📈 Aperçu du projet

Le schéma relationnel matérialise le lien entre les contrats et leur contexte géographique. Il constitue la base des requêtes d'analyse et des contrôles d'intégrité.

Le dictionnaire de données formalise les champs, leurs types et leur rôle dans le modèle.

<p align="center">
  <img src="assets/dictionnaire_donnees.png" width="760" alt="Extrait du dictionnaire de données">
</p>

Le chargement de la base est vérifié avant l'analyse, notamment par des requêtes de comptage.

<p align="center">
  <img src="assets/verification_chargement.png" width="353" alt="Contrôle du chargement des données">
</p>

Les requêtes SQL permettent ensuite de comparer les contrats par région et d'examiner les cotisations moyennes selon le département.

<p align="center">
  <img src="assets/contrats_par_region.png" width="165" alt="Nombre de contrats par région">
</p>

<p align="center">
  <img src="assets/cotisation_moyenne_par_departement.png" width="290" alt="Cotisation moyenne par département">
</p>

## 📦 Livrables réalisés

Le projet d'origine contient le schéma, les scripts SQL, un dictionnaire de données et une documentation technique. Les données brutes ne sont pas dupliquées dans ce portfolio.

- [Document technique](livrables/P3_document_technique.pdf)
- [Liste des requêtes](livrables/P3_liste_requetes.pdf)
- [Méthodologie de requête SQL](livrables/P3_methodologie_requetes_sql.pdf)

---

[← Retour au portfolio](../README.md)
