# Étude R&D — Détection et suivi automatisé de moustiques

## Contexte

Étude de faisabilité portant sur un système capable de détecter et suivre automatiquement un moustique en vol.

Le projet est actuellement au stade **R&D / étude de faisabilité**.

## Besoin / objectif

Évaluer une architecture capable de :
- détecter une cible de très petite taille ;
- estimer sa position ou sa trajectoire ;
- assurer un suivi suffisamment rapide ;
- fonctionner avec un coût et une complexité compatibles avec un prototype expérimental.

## Contraintes

- cible de quelques millimètres ;
- déplacement rapide et imprévisible ;
- faible surface optique ;
- fréquence de mesure élevée ;
- risque de faux positifs ;
- coût du matériel ;
- contraintes de traitement temps réel.

## Technologies / approches étudiées

### Vision par ordinateur
- détection de mouvement ;
- suivi ;
- classification éventuelle.

### Mesure optique / LiDAR
- détection sur une zone ou une ligne ;
- étude d'une approche évitant une reconstruction 3D complète.

### Galvanomètres
- étude du suivi rapide sur deux axes ;
- problématique de précision et de distance.

## Démarche R&D

1. caractériser la cible ;
2. identifier les technologies possibles ;
3. comparer résolution spatiale et temporelle ;
4. estimer les besoins de calcul ;
5. comparer vision et mesure optique ;
6. analyser le coût ;
7. isoler les verrous techniques ;
8. définir un banc de validation minimal.

## Résultats de l'étude

L'étude a identifié la **détection fiable** comme principal verrou.

Elle a également montré qu'une reconstruction volumétrique complète n'est pas forcément nécessaire et qu'une zone de détection restreinte peut réduire la complexité.

## Compétences mobilisées

- veille technologique ;
- étude de faisabilité ;
- Computer Vision ;
- capteurs optiques ;
- traitement temps réel ;
- analyse coût / performances ;
- architecture système ;
- identification des risques.

## Limites

Le projet ne dispose pas encore :
- d'un prototype complet ;
- d'un dataset expérimental représentatif ;
- de métriques de détection ;
- d'une validation en conditions réelles.

## Prochaines étapes

- définir un banc de test ;
- tester la détection d'objets de taille comparable ;
- mesurer les performances ;
- constituer un premier dataset ;
- sélectionner l'architecture la plus pertinente.
