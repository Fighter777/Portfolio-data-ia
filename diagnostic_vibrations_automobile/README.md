# Étude expérimentale de vibrations automobile par acquisition accélérométrique

## Contexte

Projet expérimental visant à caractériser des vibrations apparaissant sur un véhicule à certaines vitesses après un changement de pneumatiques.

Le projet est actuellement en **phase de préparation expérimentale** : le matériel est disponible et le protocole de mesure est défini, mais la campagne instrumentée sur véhicule reste à réaliser.

## Besoin / objectif

Remplacer une appréciation subjective par des mesures permettant d'étudier la corrélation entre :

- accélérations mesurées ;
- vitesse du véhicule ;
- fréquence de rotation des roues ;
- position du capteur.

## Matériel

- 2 cartes Analog Devices **EVAL-ADXL357Z** ;
- ESP32 pour les premiers essais ;
- récupération de la vitesse via OBD2 envisagée ;
- véhicule équipé de roues de 20 pouces.

<img src="assets/schema_acquisition_vibrations.png" alt="Schéma de l'architecture d'acquisition vibratoire automobile" width="900">

## Données prévues

- accélérations multiaxes ;
- horodatage ;
- vitesse véhicule ;
- position du capteur ;
- conditions d'essai.

## Protocole envisagé

1. validation des capteurs ;
2. définition de la fixation ;
3. acquisition synchronisée ;
4. récupération de la vitesse ;
5. essais à plusieurs vitesses ;
6. analyse temporelle ;
7. analyse fréquentielle ;
8. comparaison entre positions.

## Analyse prévue

- amplitude vibratoire selon la vitesse ;
- fréquence dominante ;
- harmoniques ;
- corrélation fréquence / vitesse ;
- comparaison avant / arrière.

## État actuel

Deux cartes **EVAL-ADXL357Z** ont été acquises.

Les observations routières initiales à instrumenter sont :
- vibration faible autour de 90 km/h ;
- plus sensible vers 130 km/h ;
- maximale autour de 150 km/h ;
- fortement atténuée vers 165 km/h.

Ces observations servent à définir le protocole ; elles ne constituent pas un diagnostic.

## Compétences mobilisées

- instrumentation ;
- capteurs MEMS ;
- séries temporelles ;
- synchronisation ;
- traitement du signal ;
- analyse fréquentielle ;
- conception d'un protocole expérimental.

## Limites actuelles

Aucune conclusion physique ne peut encore être tirée sans acquisition instrumentée.

Les résultats dépendront notamment :
- de la fixation ;
- du bruit mécanique ;
- de la synchronisation ;
- de la position des capteurs.

## Prochaines étapes

- valider l'acquisition ADXL357 ;
- définir le format des données ;
- intégrer la vitesse OBD2 ;
- effectuer la première campagne sur l'essieu avant ;
- analyser les signaux et FFT.
