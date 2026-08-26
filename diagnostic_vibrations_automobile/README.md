<p align="right"><a href="../README.md">← Retour au portfolio</a></p>

# <img src="../assets/icons/vibration.svg" width="38" valign="middle" alt="Vibrations"> Étude expérimentale de vibrations automobile par acquisition accélérométrique

<p>
  <img src="../assets/logos/arduino.svg" width="30" alt="ESP32" title="ESP32">
  <img src="../assets/logos/python.svg" width="30" alt="Python / analyse" title="Python / analyse">
</p>

<img src="../assets/badges/preparation-experimentale.svg" height="24" alt="Statut : Préparation expérimentale">

---


<p align="center">
  <img src="assets/schema_acquisition_vibrations.png" width="720" alt="Architecture prévue pour l’acquisition des vibrations et de la vitesse véhicule">
  <br>
  <sub>Architecture prévue pour l’acquisition des vibrations et de la vitesse véhicule</sub>
</p>

## ![](../assets/sections/context.svg) Contexte

Projet expérimental visant à caractériser des vibrations apparaissant sur un véhicule à certaines vitesses après un changement de pneumatiques.

Le projet est actuellement en **phase de préparation expérimentale** : le matériel est disponible et le protocole de mesure est défini, mais la campagne instrumentée sur véhicule reste à réaliser.

## ![](../assets/sections/goal.svg) Besoin / objectif

Remplacer une appréciation subjective par des mesures permettant d'étudier la corrélation entre :

- accélérations mesurées ;
- vitesse du véhicule ;
- fréquence de rotation des roues ;
- position du capteur.

## ![](../assets/sections/hardware.svg) Matériel

- 2 cartes Analog Devices **EVAL-ADXL357Z** ;
- ESP32 pour les premiers essais ;
- récupération de la vitesse via OBD2 envisagée ;
- véhicule équipé de roues de 20 pouces.

## ![](../assets/sections/data.svg) Données prévues

- accélérations multiaxes ;
- horodatage ;
- vitesse véhicule ;
- position du capteur ;
- conditions d'essai.

## ![](../assets/sections/method.svg) Protocole envisagé

1. validation des capteurs ;
2. définition de la fixation ;
3. acquisition synchronisée ;
4. récupération de la vitesse ;
5. essais à plusieurs vitesses ;
6. analyse temporelle ;
7. analyse fréquentielle ;
8. comparaison entre positions.

## ![](../assets/sections/method.svg) Analyse prévue

- amplitude vibratoire selon la vitesse ;
- fréquence dominante ;
- harmoniques ;
- corrélation fréquence / vitesse ;
- comparaison avant / arrière.

## ![](../assets/sections/results.svg) État actuel

Deux cartes **EVAL-ADXL357Z** ont été acquises.

Les observations routières initiales à instrumenter sont :
- vibration faible autour de 90 km/h ;
- plus sensible vers 130 km/h ;
- maximale autour de 150 km/h ;
- fortement atténuée vers 165 km/h.

Ces observations servent à définir le protocole ; elles ne constituent pas un diagnostic.

## ![](../assets/sections/skills.svg) Compétences mobilisées

- instrumentation ;
- capteurs MEMS ;
- séries temporelles ;
- synchronisation ;
- traitement du signal ;
- analyse fréquentielle ;
- conception d'un protocole expérimental.

## ![](../assets/sections/limits.svg) Limites actuelles

Aucune conclusion physique ne peut encore être tirée sans acquisition instrumentée.

Les résultats dépendront notamment :
- de la fixation ;
- du bruit mécanique ;
- de la synchronisation ;
- de la position des capteurs.

## ![](../assets/sections/next.svg) Prochaines étapes

- valider l'acquisition ADXL357 ;
- définir le format des données ;
- intégrer la vitesse OBD2 ;
- effectuer la première campagne sur l'essieu avant ;
- analyser les signaux et FFT.

---

[← Retour au portfolio](../README.md)
