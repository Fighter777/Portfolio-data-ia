# Transcription locale et assistée de réunions

## Contexte

Application locale de transcription conçue pour traiter de longs enregistrements de réunions liés à un projet autoroutier, sans envoyer les médias ni les résultats vers un service de transcription distant.

Le traitement est exécuté sur une **NVIDIA RTX 3090**.

## Besoin métier

Transformer des enregistrements audio ou vidéo en documents exploitables tout en conservant un mécanisme explicite de validation humaine.

Les besoins couverts sont notamment :

- transcription française horodatée ;
- export texte et sous-titres ;
- séparation optionnelle des intervenants ;
- identification des segments acoustiquement les moins fiables ;
- réécoute ciblée d'un passage ;
- nouvelle transcription locale d'un court extrait ;
- correction manuelle traçable.

## Architecture

**audio / vidéo → FFmpeg → Whisper large-v3 → corrections validées → TXT / SRT / VTT**

Branche optionnelle :
**audio → pyannote → diarisation**

Contrôle qualité :
**segments de faible confiance → extrait audio → décodages alternatifs → validation utilisateur**

## Technologies

- Python 3.12 ;
- Gradio ;
- Whisper large-v3 ;
- faster-whisper ;
- CTranslate2 ;
- WhisperX ;
- pyannote ;
- FFmpeg ;
- CUDA ;
- RTX 3090.

## Démarche

Le projet ne considère pas la sortie de transcription comme une vérité automatique.

Les passages les moins fiables sont remontés à l'utilisateur afin qu'il puisse :
1. écouter le segment ;
2. élargir la fenêtre audio ;
3. demander deux décodages alternatifs ;
4. choisir ou saisir le texte retenu ;
5. appliquer la correction aux exports sans retranscrire toute la réunion.

Une normalisation du volume et un gain supplémentaire peuvent être appliqués avant transcription pour les enregistrements faibles ou irréguliers. Les corrections persistantes ne sont enregistrées qu'après validation explicite.

## Confidentialité

- interface limitée à `127.0.0.1` ;
- médias et résultats traités localement ;
- jeton de diarisation utilisé uniquement en mémoire ;
- aucun service distant de transcription utilisé.

## Résultats

L'application produit :
- `TXT` ;
- `SRT` ;
- `VTT`.

Elle permet également une relecture ciblée des **30 segments présentant la confiance acoustique la plus faible**.

<img src="assets/relecture_ciblee_transcription.jpg" alt="Interface de relecture ciblée d'un segment à vérifier" width="900">

## Compétences mobilisées

- Speech-to-Text ;
- traitement de données non structurées ;
- inférence GPU ;
- diarisation ;
- UX de validation humaine ;
- traçabilité ;
- confidentialité ;
- orchestration locale de modèles.

## Limites

- transcription susceptible de produire des erreurs malgré un audio intelligible ;
- diarisation indicative ;
- chevauchements de voix et microphones éloignés difficiles à traiter ;
- une seule transcription simultanée pour préserver la mémoire GPU.

## Prochaines pistes

- mesurer précisément le temps de traitement ;
- quantifier les corrections nécessaires par heure d'audio ;
- comparer plusieurs configurations de décodage ;
- évaluer la diarisation sur plusieurs configurations de réunion.
