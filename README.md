# Portfolio Data & Intelligence Artificielle

> **Analyse de données, IA appliquée et expérimentation technique** — des projets OpenClassrooms aux prototypes et études R&D.

Ce portfolio rassemble les projets réalisés dans le cadre du parcours **Data Analyst d'OpenClassrooms**, complétés par des réalisations personnelles autour de l'IA locale, de la vision par ordinateur, du traitement de la parole, de l'IoT et de l'acquisition de données.

Chaque sous-projet dispose de sa propre documentation : **contexte → besoin → données → démarche → résultats → limites → prochaines étapes**.


---

## Profil

**Data Analyst orienté IA appliquée**, avec un intérêt particulier pour la qualité des données, l'intégration de modèles dans des applications concrètes et l'expérimentation sur données réelles.

Deux axes structurent ce portfolio :

- **Data pour la décision** — SQL, Python, analyse exploratoire, Business Intelligence, Machine Learning, pipelines et qualité des données ;
- **IA appliquée & R&D** — vision, voix, LLM locaux, traitement de données non structurées, IoT et instrumentation.

---

# Compétences & outils

## <img src="assets/icons/openclassrooms.svg" width="30" valign="middle" alt="OpenClassrooms"> Parcours OpenClassrooms

| Outil | [P3](#p3) | [P4](#p4) | [P5](#p5) | [P6](#p6) | [P7](#p7) | [P8](#p8) | [P9](#p9) | [P10](#p10) | [P11](#p11) | [P12](#p12) | [P13](#p13) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| <img src="assets/logos/python.svg" width="20" alt="Python"> **Python** |  | ✓ |  | ✓ |  | ✓ | ✓ |  | ✓ | ✓ | ✓ |
| <img src="assets/logos/sql.svg" width="20" alt="SQL"> **SQL** | ✓ |  | ✓ |  |  | ✓ |  |  |  |  |  |
| <img src="assets/logos/pandas.svg" width="20" alt="Pandas"> **Pandas** |  | ✓ |  | ✓ |  | ✓ | ✓ |  | ✓ | ✓ | ✓ |
| <img src="assets/logos/powerbi.svg" width="20" alt="Power BI"> **Power BI** |  |  |  |  | ✓ |  |  | ✓ |  |  |  |
| <img src="assets/logos/powerbi.svg" width="20" alt="Power Query"> **Power Query / DAX** |  |  |  |  | ✓ |  |  | ✓ |  |  |  |
| <img src="assets/logos/dbt.svg" width="20" alt="dbt"> **dbt** |  |  |  |  |  | ✓ |  |  |  |  |  |
| <img src="assets/logos/snowflake.svg" width="20" alt="Snowflake"> **Snowflake** |  |  |  |  |  | ✓ |  |  |  |  |  |
| <img src="assets/logos/streamlit.svg" width="20" alt="Streamlit"> **Streamlit** |  |  |  |  |  |  | ✓ |  |  |  |  |
| <img src="assets/logos/plotly.svg" width="20" alt="Plotly"> **Plotly** |  |  |  | ✓ |  |  | ✓ |  | ✓ | ✓ |  |
| <img src="assets/logos/sklearn.svg" width="20" alt="scikit-learn"> **scikit-learn** |  |  |  |  |  |  |  |  | ✓ | ✓ | ✓ |

## <img src="assets/icons/rnd.svg" width="30" valign="middle" alt="R&D"> Projets personnels & R&D

| Projet | Data | IA / ML | Vision | Audio | API / App | GPU | IoT / embarqué | R&D / expérimentation |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [Transcription locale](#transcription) | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ |
| [Vocal Weather](#vocal-weather) | ✓ | ✓ |  | ✓ | ✓ |  |  | ✓ |
| [Identification d'oiseaux](#oiseaux) | ✓ | ✓ | ✓ |  |  | ✓ |  | ✓ |
| [Atelier IA](#atelier-ia) |  | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |
| [OCR sur manuel ancien](#ocr) | ✓ |  | ✓ |  |  |  |  | ✓ |
| [Tracker GPS / LoRa](#lora) | ✓ |  |  |  |  |  | ✓ | ✓ |
| [Diagnostic vibratoire](#vibrations) | ✓ |  |  |  |  |  | ✓ | ✓ |
| [Détection de moustiques](#moustiques) |  | ✓ | ✓ |  |  |  |  | ✓ |
| [LLM locaux](#llm-locaux) |  | ✓ |  |  | ✓ | ✓ |  | ✓ |
| [Batterie résidentielle DIY](#batterie) | ✓ |  |  |  |  |  | ✓ | ✓ |
| [Veille Data & IA](#veille-data-ia) | ✓ | ✓ |  |  | ✓ |  |  |  | ✓ |
| [Assistant IA de notebook](#assistant-notebook-ia) | ✓ | ✓ |  |  | ✓ |  |  |  | ✓ |

---

# <img src="assets/icons/openclassrooms.svg" width="34" valign="middle" alt="OpenClassrooms"> Projets OpenClassrooms

<a id="p3"></a>
## <img src="assets/icons/p3-database.svg" width="30" alt="Base de données"> P3 — Modélisation et interrogation SQL

<p>
  <img src="assets/logos/sql.svg" width="26" alt="SQL" title="SQL">
</p>

Construction d'un modèle relationnel à partir d'un besoin de gestion : dictionnaire de données, clés primaires et étrangères, contrôle d'intégrité puis requêtes d'analyse.

Le projet documente le chemin complet **modélisation → chargement → vérification → interrogation SQL**.

➡️ [Voir le projet et les livrables](p3_modelisation_sql/)

---

<a id="p4"></a>
## <img src="assets/icons/p4-health.svg" width="30" alt="Santé publique"> P4 — Étude de santé publique

<p>
  <img src="assets/logos/python.svg" width="26" alt="Python" title="Python">
  <img src="assets/logos/pandas.svg" width="26" alt="Pandas" title="Pandas">
  <img src="assets/logos/jupyter.svg" width="26" alt="Jupyter" title="Jupyter">
</p>

Analyse exploratoire de **quatre jeux de données FAO** : population, disponibilité alimentaire, sous-nutrition et aide alimentaire. Le travail porte sur l'harmonisation des sources, les jointures, la construction d'indicateurs et leur représentation géographique.

> **Point clé —** les résultats sont présentés dans leur contexte statistique, sans transformer une corrélation descriptive en relation causale.

➡️ [Voir le projet et les visualisations](p4_etude_sante_publique/)

---

<a id="p5"></a>
## <img src="assets/icons/p5-real-estate.svg" width="30" alt="Immobilier"> P5 — Exploitation de données immobilières avec SQL

<p>
  <img src="assets/logos/sql.svg" width="26" alt="MySQL" title="MySQL">
</p>

Structuration d'une base immobilière reliant ventes, biens, communes, départements et régions. Les requêtes permettent ensuite d'étudier les volumes de transactions, les prix régionaux et les prix au m².

➡️ [Voir le projet et le schéma relationnel](p5_donnees_immobilieres/)

---

<a id="p6"></a>
## <img src="assets/icons/p6-wine.svg" width="30" alt="Caviste"> P6 — Analyse du catalogue d'un caviste

<p>
  <img src="assets/logos/python.svg" width="26" alt="Python" title="Python">
  <img src="assets/logos/pandas.svg" width="26" alt="Pandas" title="Pandas">
  <img src="assets/logos/plotly.svg" width="26" alt="Plotly" title="Plotly">
</p>

Réconciliation de trois sources ERP / e-commerce puis analyse des prix, ventes, marges et stocks.

> **Résultat —** sur **825 références ERP**, **714 produits** sont rapprochés avec les données web et **111 références** restent à investiguer. L'analyse met aussi en évidence les références à forte couverture de stock.

➡️ [Voir le projet et les analyses](p6_analyse_catalogue_caviste/)

---

<a id="p7"></a>
## <img src="assets/icons/p7-dashboard.svg" width="30" alt="Dashboard"> P7 — Tableau de bord de pilotage

<p>
  <img src="assets/logos/powerbi.svg" width="26" alt="Power BI" title="Power BI">
</p>

Conception d'un dashboard Power BI pour suivre les projets IT et Marketing de l'entreprise fictive **Sanitoral** : coûts, délais, livrables et projets en alerte, avec navigation du niveau global jusqu'au détail projet.

<p align="center">
  <a href="p7_tableau_bord_powerbi/"><img src="p7_tableau_bord_powerbi/assets/tableau_bord_vue_globale.png" width="720" alt="Vue globale du tableau de bord Sanitoral"></a>
</p>

➡️ [Voir le projet Power BI](p7_tableau_bord_powerbi/)

---

<a id="p8"></a>
## <img src="assets/icons/p8-pipeline.svg" width="30" alt="Pipeline"> P8 — Pipeline sociodémographique

<p>
  <img src="assets/logos/dbt.svg" width="26" alt="dbt" title="dbt">
  <img src="assets/logos/snowflake.svg" width="26" alt="Snowflake" title="Snowflake">
  <img src="assets/logos/python.svg" width="26" alt="Python" title="Python">
</p>

Pipeline Data Engineering sur **4 646 inscrits**, enrichis par des données INSEE. L'architecture dbt sépare les couches brutes, `staging`, intermédiaires et mart analytique.

> **Résultat —** le pipeline produit une table sociodémographique consolidée et exécute avec succès **43 modèles/tests/vérifications** lors du `dbt build` documenté.

➡️ [Voir le pipeline et le lineage dbt](p8_pipeline_sociodemographique/)

---

<a id="p9"></a>
## <img src="assets/icons/p9-books.svg" width="30" alt="Librairie"> P9 — Analyse des ventes LaPage

<p>
  <img src="assets/logos/python.svg" width="26" alt="Python" title="Python">
  <img src="assets/logos/pandas.svg" width="26" alt="Pandas" title="Pandas">
  <img src="assets/logos/streamlit.svg" width="26" alt="Streamlit" title="Streamlit">
  <img src="assets/logos/plotly.svg" width="26" alt="Plotly" title="Plotly">
</p>

Application Streamlit permettant d'explorer les ventes, les KPI, les produits et les profils clients de la librairie fictive **LaPage**, avec filtres temporels et analyses statistiques complémentaires.

➡️ [Voir le dashboard et les notebooks](p9_analyse_ventes_lapage/)

---

<a id="p10"></a>
## <img src="assets/icons/p10-water.svg" width="30" alt="Eau"> P10 — Accès à l'eau potable

<p>
  <img src="assets/logos/powerbi.svg" width="26" alt="Power BI" title="Power BI">
</p>

Tableau de bord de priorisation pour l'organisation fictive **DWFA**. Les indicateurs croisent accès à l'eau, mortalité liée à l'eau/assainissement/hygiène, population et stabilité politique.

Le dashboard associe cartes, lecture régionale et matrice de priorisation afin d'orienter l'analyse vers les zones nécessitant une étude plus approfondie.

➡️ [Voir le projet et les cartes](p10_acces_eau_potable/)

---

<a id="p11"></a>
## <img src="assets/icons/p11-world.svg" width="30" alt="International"> P11 — Étude de marché internationale

<p>
  <img src="assets/logos/python.svg" width="26" alt="Python" title="Python">
  <img src="assets/logos/pandas.svg" width="26" alt="Pandas" title="Pandas">
  <img src="assets/logos/sklearn.svg" width="26" alt="scikit-learn" title="scikit-learn">
</p>

Étude destinée à prioriser des marchés export dans la filière volaille à partir de données FAO, Banque mondiale, WGI et CEPII. ACP, CAH et K-means sont utilisés conjointement pour construire une segmentation interprétable.

> **Résultat —** **quatre profils de marchés** sont retenus ; la recommandation privilégie les marchés riches, stables et importateurs, puis les marchés intermédiaires équilibrés.

➡️ [Voir l'étude, l'ACP et le clustering](p11_etude_marche_internationale/)

---

<a id="p12"></a>
## <img src="assets/icons/p12-banknote.svg" width="30" alt="Billet"> P12 — Détection de faux billets

<p>
  <img src="assets/logos/python.svg" width="26" alt="Python" title="Python">
  <img src="assets/logos/pandas.svg" width="26" alt="Pandas" title="Pandas">
  <img src="assets/logos/sklearn.svg" width="26" alt="scikit-learn" title="scikit-learn">
</p>

Comparaison de régression logistique, KNN, Random Forest et K-means sur **1 500 billets**, avec traitement des valeurs manquantes, validation croisée et analyse du coût métier des erreurs.

> **Résultat —** avec le modèle retenu et un seuil de **0,65**, les essais atteignent **100 % de rappel sur les faux billets** du jeu de test, au prix de trois vrais billets classés comme suspects. Ce seuil reste à revalider sur données indépendantes.

➡️ [Voir le projet, le modèle et la matrice de confusion](p12_detection_faux_billets/)

---

<a id="p13"></a>
## <img src="assets/icons/p13-ai.svg" width="30" alt="IA"> P13 — Projet Data augmenté avec l'IA

<p>
  <img src="assets/logos/python.svg" width="26" alt="Python" title="Python">
  <img src="assets/logos/pandas.svg" width="26" alt="Pandas" title="Pandas">
  <img src="assets/logos/sklearn.svg" width="26" alt="scikit-learn" title="scikit-learn">
</p>

Dernier projet du parcours : amélioration critique du P6 avec l'IA, veille technologique, cahier des charges, comparaison d'options, traçabilité des essais et construction du portfolio. Deux applications Streamlit locales complètent la démarche : la veille Data & IA et l'assistant de lecture du notebook de segmentation.

**État actuel :** la partie portfolio est engagée ; l'amélioration IA du P6 reste à réaliser et sera documentée séparément avec ses prompts, variantes, décisions et limites.

➡️ [Voir l'état du P13](p13_data_augmente_ia/)

---

# <img src="assets/icons/atelier-ai.svg" width="34" valign="middle" alt="IA appliquée"> Projets personnels — IA appliquée

<a id="veille-data-ia"></a>
## <img src="assets/icons/p13-ai.svg" width="30" alt="Veille IA"> Veille Data & IA

Application Streamlit de collecte RSS/Atom, avec archivage SQLite, pré-classification locale par Qwen et traduction d'extraits RSS.

➡️ [Voir le projet](veille_data_ia/)

---

<a id="assistant-notebook-ia"></a>
## <img src="assets/icons/p13-ai.svg" width="30" alt="Assistant IA de notebook"> Assistant IA de lecture de notebook

Application Streamlit locale pour interroger un notebook Jupyter : code, documentation, sorties sauvegardées et graphiques. Un modèle Qwen compatible OpenAI répond à partir du contexte sélectionné ; l'administration permet aussi de remplacer le notebook avec sauvegarde préalable.

➡️ [Voir le projet](assistant_notebook_ia/)

---

<a id="transcription"></a>
## <img src="assets/icons/transcription.svg" width="30" alt="Microphone"> Transcription locale et assistée de réunions

<p>
  <img src="assets/logos/python.svg" width="26" alt="Python" title="Python">
  <img src="assets/logos/whisper.svg" width="26" alt="Whisper" title="Whisper large-v3">
  <img src="assets/logos/huggingface.svg" width="26" alt="pyannote" title="pyannote / diarisation">
  <img src="assets/logos/nvidia.svg" width="26" alt="NVIDIA CUDA" title="CUDA / RTX 3090">
</p>

Application locale destinée à transformer de longues réunions en documents exploitables sans envoyer les médias vers un service de transcription distant : Whisper large-v3, diarisation optionnelle, exports TXT/SRT/VTT et correction humaine traçable.

> **Contrôle qualité —** les **30 segments acoustiquement les moins fiables** sont remontés pour réécoute et redécodage ciblé, sans retraiter l'intégralité de la réunion.

<p align="center">
  <a href="transcription_locale_reunions/"><img src="transcription_locale_reunions/assets/relecture_ciblee_transcription.jpg" width="760" alt="Relecture ciblée d'un segment de transcription"></a>
</p>

➡️ [Voir l'application et son pipeline](transcription_locale_reunions/)

---

<a id="vocal-weather"></a>
## <img src="assets/icons/weather.svg" width="30" alt="Météo"> Vocal Weather — Assistant météo vocal

<p>
  <img src="assets/logos/flutter.svg" width="26" alt="Flutter" title="Flutter">
  <img src="assets/logos/fastapi.svg" width="26" alt="FastAPI" title="FastAPI">
  <img src="assets/logos/whisper.svg" width="26" alt="Whisper" title="faster-whisper">
  <img src="assets/logos/ollama.svg" width="26" alt="Ollama" title="Ollama">
  <img src="assets/logos/sqlite.svg" width="26" alt="SQLite" title="SQLite">
</p>

Prototype fonctionnel combinant application Flutter et API FastAPI : **voix → transcription → extraction du lieu et de l'horizon → Open-Meteo → réponse → synthèse vocale**.

Chaque requête est historisée et les étapes du pipeline sont journalisées avec leur durée, ce qui permet d'observer les latences réelles plutôt que d'annoncer une valeur théorique unique.

<p align="center">
  <a href="vocal_weather/"><img src="vocal_weather/assets/architecture_pipeline_vocal_weather.png" width="760" alt="Architecture du pipeline Vocal Weather"></a>
</p>

➡️ [Voir le prototype](vocal_weather/)

---

<a id="oiseaux"></a>
## <img src="assets/icons/bird.svg" width="30" alt="Oiseau"> Détection et identification d'oiseaux

<p>
  <img src="assets/logos/python.svg" width="26" alt="Python" title="Python">
  <img src="assets/logos/pytorch.svg" width="26" alt="PyTorch" title="PyTorch">
  <img src="assets/logos/nvidia.svg" width="26" alt="CUDA" title="CUDA">
</p>

Pipeline de vision combinant détection d'animaux, classification d'espèces et analyse vidéo sur des séquences de mangeoire. Plusieurs versions ConvNeXt-Small ont été entraînées et comparées sur GPU.

> **Résultat —** le modèle de référence **ConvNeXt-Small v4 atteint 91,11 % d'accuracy** sur **4 094 images de test**, après entraînement sur **19 061 images** couvrant 12 espèces locales.

<p align="center">
  <a href="detection_especes_animales/"><img src="detection_especes_animales/assets/detection_oiseaux_video_annotee.png" width="760" alt="Détection et identification d'oiseaux sur une vidéo de mangeoire"></a>
</p>

➡️ [Voir le projet et le suivi des entraînements](detection_especes_animales/)

---

<a id="atelier-ia"></a>
## <img src="assets/icons/atelier-ai.svg" width="30" alt="IA"> Atelier « Comprendre l'IA par la démonstration »

<p>
  <img src="assets/logos/python.svg" width="26" alt="Python" title="Python">
  <img src="assets/logos/pytorch.svg" width="26" alt="PyTorch" title="Vision / IA">
  <img src="assets/logos/whisper.svg" width="26" alt="LLM et voix" title="LLM / voix">
</p>

Conception d'un atelier de **45 minutes** pour Place du Numérique 2026. Six démonstrations rendent visibles les briques techniques derrière la voix, la vision, la biométrie et l'IA générative, tout en abordant biais, consentement et vérification des contenus.

**Démonstrations :** assistant météo vocal · classification d'oiseaux · comptage de véhicules · reconnaissance faciale · face swap · conversion vocale.

➡️ [Voir l'atelier et les supports PDF](atelier_ia_place_du_numerique/)

---

# <img src="assets/icons/rnd.svg" width="34" valign="middle" alt="R&D"> Études & projets R&D

Ces projets sont présentés selon leur **état réel** : retour d'expérience, étude de faisabilité, préparation expérimentale ou prototype. Une hypothèse ou une simulation n'est pas présentée comme une mesure terrain.

<a id="ocr"></a>
## <img src="assets/icons/ocr.svg" width="28" alt="Document"> OCR sur manuel ancien

<img src="assets/badges/retour-experience.svg" height="24" alt="Retour d'expérience">

Essai d'OCR sur un bulletin technique CIMA de 1957. La dégradation du support, le contraste irrégulier et les typographies anciennes produisent trop d'erreurs pour obtenir un résultat exploitable.

> **Décision technique —** ne pas présenter un traitement non fiable comme une solution aboutie ; conserver l'essai comme retour d'expérience sur les limites de l'OCR.

➡️ [Voir le retour d'expérience](ocr_documentaire/)

---

<a id="vibrations"></a>
## <img src="assets/icons/vibration.svg" width="28" alt="Vibrations"> Diagnostic vibratoire automobile

<p>
  <img src="assets/logos/arduino.svg" width="26" alt="ESP32" title="ESP32">
  <img src="assets/logos/python.svg" width="26" alt="Python" title="Python / analyse prévue">
</p>

<img src="assets/badges/preparation-experimentale.svg" height="24" alt="Préparation expérimentale">

Instrumentation prévue avec **2 EVAL-ADXL357Z**, ESP32 et vitesse véhicule OBD2 afin de corréler accélérations, vitesse et fréquences dominantes. La campagne instrumentée sur véhicule reste à réaliser.

➡️ [Voir le protocole et le schéma d'acquisition](diagnostic_vibrations_automobile/)

---

<a id="lora"></a>
## <img src="assets/icons/lora.svg" width="28" alt="Radio"> Tracker GPS / LoRa basse consommation

<img src="assets/badges/rnd-en-cours.svg" height="24" alt="R&D en cours">

Conception d'un tracker GNSS/LoRa/BLE adapté à un animal, avec adaptation des cycles de localisation à l'activité et à l'état de batterie.

> **Essai terrain —** des cartes Heltec WiFi LoRa 32 V3 / SX1262 avec antennes d'origine ont atteint environ **2,5 km** dans les conditions du test avec **SF10**. Les anciennes estimations d'autonomie restent explicitement séparées des futures mesures sur prototype final.

<p align="center">
  <a href="collier_gps_lora/"><img src="collier_gps_lora/assets/maquette_interface_lora_gps.png" width="360" alt="Maquette de suivi GPS LoRa"></a>
</p>

➡️ [Voir le projet R&D](collier_gps_lora/)

---

<a id="moustiques"></a>
## <img src="assets/icons/mosquito.svg" width="28" alt="Moustique"> Détection et suivi automatisé de moustiques

<img src="assets/badges/etude-faisabilite.svg" height="24" alt="Étude de faisabilité">

Étude d'une architecture capable de détecter une cible de quelques millimètres, d'estimer sa trajectoire et d'assurer un suivi temps réel. Vision, mesure optique/LiDAR et galvanomètres sont comparés avant prototypage.

> **Verrou identifié —** la détection fiable constitue le principal problème ; une reconstruction 3D complète n'est pas nécessairement indispensable si la zone de détection peut être contrainte.

➡️ [Voir le schéma conceptuel](rnd_detection_moustiques/)

---

<a id="llm-locaux"></a>
## <img src="assets/icons/llm.svg" width="28" alt="LLM local"> Évaluation de LLM locaux

<p>
  <img src="assets/logos/ollama.svg" width="26" alt="Ollama" title="Ollama">
  <img src="assets/logos/nvidia.svg" width="26" alt="GPU" title="GPU / inférence locale">
</p>

<img src="assets/badges/benchmark-formaliser.svg" height="24" alt="Benchmark à formaliser">

Expérimentation de modèles exécutés localement pour des usages de développement : compatibilité, vitesse, mémoire, respect des consignes et comportement sur du code. Les essais existent, mais le benchmark reproductible reste à formaliser avant publication de conclusions comparatives.

➡️ [Voir l'état de l'étude](evaluation_llm_locaux/)

---

<a id="batterie"></a>
## <img src="assets/icons/battery.svg" width="28" alt="Batterie"> Batterie résidentielle DIY

<img src="assets/badges/etude-faisabilite.svg" height="24" alt="Étude de faisabilité">

Étude technique et économique d'un stockage résidentiel DIY : dimensionnement, coût/kWh, cyclabilité, rendement, contraintes de sécurité et comparaison de chimies, notamment autour du zinc-ion.

Le projet reste volontairement au stade de l'étude : aucune batterie résidentielle complète n'est présentée comme réalisée ou validée.

➡️ [Voir l'étude et le schéma conceptuel](rnd_batterie_residentielle_diy/)

---

# Environnement technique

<p>
  <img src="assets/logos/python.svg" width="34" alt="Python" title="Python">
  <img src="assets/logos/pandas.svg" width="34" alt="Pandas" title="Pandas">
  <img src="assets/logos/sql.svg" width="34" alt="SQL / MySQL" title="SQL / MySQL">
  <img src="assets/logos/powerbi.svg" width="34" alt="Power BI" title="Power BI">
  <img src="assets/logos/dbt.svg" width="34" alt="dbt" title="dbt">
  <img src="assets/logos/snowflake.svg" width="34" alt="Snowflake" title="Snowflake">
  <img src="assets/logos/sklearn.svg" width="34" alt="scikit-learn" title="scikit-learn">
  <img src="assets/logos/pytorch.svg" width="34" alt="PyTorch" title="PyTorch">
  <img src="assets/logos/flutter.svg" width="34" alt="Flutter" title="Flutter">
  <img src="assets/logos/fastapi.svg" width="34" alt="FastAPI" title="FastAPI">
  <img src="assets/logos/nvidia.svg" width="34" alt="NVIDIA CUDA" title="NVIDIA CUDA">
  <img src="assets/logos/streamlit.svg" width="34" alt="Streamlit" title="Streamlit">
  <img src="assets/logos/git.svg" width="34" alt="Git" title="Git">
</p>

---

## À propos du portfolio

Les projets OpenClassrooms utilisent des données pédagogiques, fictives ou ouvertes selon les cas. Les projets personnels ne publient que les données, médias et éléments techniques pouvant être diffusés.

Les fiches distinguent volontairement **résultat mesuré**, **prototype fonctionnel**, **hypothèse**, **étude de faisabilité** et **travail à poursuivre**.

**GitHub :** [Fighter777](https://github.com/Fighter777)
