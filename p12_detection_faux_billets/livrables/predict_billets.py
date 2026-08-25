import argparse
from pathlib import Path

import joblib
import pandas as pd


FEATURE_COLUMNS = [
    "diagonal",
    "height_left",
    "height_right",
    "margin_low",
    "margin_up",
    "length",
]

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_MODEL_NAME = "best_billet_model_from_template.joblib"


#
# Construit et retourne les arguments de ligne de commande du script.
# Prend : rien.
# Retourne : un objet argparse.Namespace avec les options saisies.
def parse_args():
    parser = argparse.ArgumentParser(
        description="Prédire si un ou plusieurs billets sont vrais ou faux."
    )
    parser.add_argument(
        "--csv",
        help="Chemin vers un fichier CSV contenant les mesures des billets.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Chemin vers le modèle sauvegardé.",
    )
    parser.add_argument(
        "--output",
        help="Chemin du CSV de sortie. Si omis, aucun fichier n'est exporté.",
    )
    parser.add_argument(
        "--threshold",
        "--seuil",
        type=float,
        help="Seuil de décision à utiliser à la place de celui sauvegardé dans le modèle.",
    )
    parser.add_argument("--diagonal", type=float, help="Mesure diagonal.")
    parser.add_argument("--height-left", dest="height_left", type=float, help="Mesure height_left.")
    parser.add_argument("--height-right", dest="height_right", type=float, help="Mesure height_right.")
    parser.add_argument("--margin-low", dest="margin_low", type=float, help="Mesure margin_low.")
    parser.add_argument("--margin-up", dest="margin_up", type=float, help="Mesure margin_up.")
    parser.add_argument("--length", type=float, help="Mesure length.")
    return parser.parse_args()


#
# Recherche le fichier modèle dans le répertoire du script.
# Prend : rien.
# Retourne : le chemin du modèle trouvé.
def find_model_file():
    default_model_path = BASE_DIR / DEFAULT_MODEL_NAME
    if default_model_path.exists():
        return default_model_path

    joblib_files = sorted(BASE_DIR.glob("*.joblib"))
    if len(joblib_files) == 1:
        return joblib_files[0]

    if len(joblib_files) > 1:
        for joblib_file in joblib_files:
            if joblib_file.name == DEFAULT_MODEL_NAME:
                return joblib_file
        raise FileNotFoundError(
            "Plusieurs fichiers .joblib ont été trouvés dans le dossier du script. "
            "Merci de préciser --model."
        )

    raise FileNotFoundError(
        "Aucun fichier modèle .joblib trouvé dans le dossier du script."
    )


#
# Charge le modèle sauvegarde et récupère aussi le seuil de decision.
# Prend : le chemin du fichier modèle.
# Retourne : le pipeline charge et le seuil associé.
def load_model(model_path):
    if not model_path.exists():
        raise FileNotFoundError(f"Modele introuvable : {model_path}")

    loaded = joblib.load(model_path)
    if isinstance(loaded, dict) and "pipeline" in loaded:
        pipeline = loaded["pipeline"]
        threshold = float(loaded.get("threshold", 0.5))
    else:
        pipeline = loaded
        threshold = 0.5

    return pipeline, threshold


#
# Charge un fichier CSV avec detection automatique du séparateur.
# Prend : le chemin du fichier CSV.
# Retourne : un DataFrame pandas contenant les billets à prédire.
def load_csv(csv_path):
    if not csv_path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {csv_path}")

    return pd.read_csv(csv_path, sep=None, engine="python")


#
# Demande une valeur numérique à l'utilisateur jusqu'à obtenir une saisie valide.
# Prend : le nom de la mesure à demander.
# Retourne : un float correspondant à la valeur saisie.
def prompt_float(name):
    while True:
        raw_value = input(f"{name} : ").strip().replace(",", ".")
        try:
            return float(raw_value)
        except ValueError:
            print("Valeur invalide, merci de saisir un nombre.")


#
# Construit un DataFrame pour une saisie manuelle ou via arguments.
# Prend : les arguments saisis en ligne de commande.
# Retourne : un DataFrame avec une ligne et les 6 mesures du billet.
def build_manual_dataframe(args):
    values = {
        "diagonal": args.diagonal,
        "height_left": args.height_left,
        "height_right": args.height_right,
        "margin_low": args.margin_low,
        "margin_up": args.margin_up,
        "length": args.length,
    }

    if all(value is not None for value in values.values()):
        return pd.DataFrame([values])

    if any(value is not None for value in values.values()):
        missing = [name for name, value in values.items() if value is None]
        raise ValueError(
            "Saisie manuelle incomplete. Mesures manquantes : " + ", ".join(missing)
        )

    print("Saisie manuelle des mesures d'un billet :")
    return pd.DataFrame([{column: prompt_float(column) for column in FEATURE_COLUMNS}])


#
# Vérifie que les colonnes attendues sont présentes et isole les variables utiles.
# Prend : un DataFrame source.
# Retourne : un DataFrame X contenant uniquement les colonnes du modèle.
def prepare_features(df):
    missing_columns = [column for column in FEATURE_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(
            "Colonnes manquantes dans le fichier d'entrée : "
            + ", ".join(missing_columns)
        )

    return df[FEATURE_COLUMNS].copy()


#
# Vérifie qu'aucune ligne n'est entièrement vide sur les variables du modèle.
# Prend : un DataFrame X contenant les colonnes utiles.
# Retourne : le même DataFrame si tout est valide.
def check_empty_rows(X):
    empty_rows = X.isna().all(axis=1)
    if empty_rows.any():
        row_numbers = [str(index + 2) for index in X.index[empty_rows]]
        raise ValueError(
            "Ligne(s) entièrement vide(s) détectée(s) dans les mesures des billets : "
            + ", ".join(row_numbers)
        )

    return X


#
# Applique le modèle sur les billets et ajoute prédictions et probabilités.
# Prend : le DataFrame source, le pipeline chargé et le seuil de décision.
# Retourne : un DataFrame enrichi avec les résultats de prédiction.
def score_billets(df, pipeline, threshold):
    X = prepare_features(df)
    X = check_empty_rows(X)

    result = df.copy()
    result["prediction_is_genuine"] = pipeline.predict(X)

    if hasattr(pipeline, "predict_proba"):
        true_index = list(pipeline.classes_).index(True)
        proba_true = pipeline.predict_proba(X)[:, true_index]
        result["proba_true"] = proba_true
        result["proba_false"] = 1 - proba_true
        result["prediction_is_genuine"] = result["proba_true"] >= threshold

    result["prediction_label"] = result["prediction_is_genuine"].map(
        {True: "vrai", False: "faux"}
    )
    return result


#
# Affiche les résultats de prédiction de facon lisible dans le terminal.
# Prend : le DataFrame résultat et le seuil utilisé.
# Retourne : rien.
def print_results(result, threshold):
    print(f"Seuil utilise : {threshold}")
    print()

    has_id = "id" in result.columns
    for index, row in result.iterrows():
        billet_name = row["id"] if has_id else f"Billet {index + 1}"
        label = row["prediction_label"]

        if "proba_true" in result.columns:
            print(
                f"{billet_name} : {label} "
                f"(proba_vrai={row['proba_true']:.6f}, proba_faux={row['proba_false']:.6f})"
            )
        else:
            print(f"{billet_name} : {label}")

    print()
    print("Récapitulatif :")
    print(f"- Total billets analysés : {len(result)}")
    print(f"- Vrais billets prédits : {(result['prediction_is_genuine'] == True).sum()}")
    print(f"- Faux billets prédits : {(result['prediction_is_genuine'] == False).sum()}")


#
# Construit le chemin du fichier CSV de sortie par defaut.
# Prend : le chemin du fichier CSV d'entrée.
# Retourne : le chemin du fichier prédictions associé.
def default_output_path(csv_path):
    return csv_path.with_name(f"{csv_path.stem}_predictions.csv")


#
# fonction main de démarrage
def main():
    args = parse_args() #parse les arguments 
    model_path = Path(args.model) if args.model else find_model_file() #si le modèle est spécifié sinon chercher un modèle dans le repertoire
    pipeline, threshold = load_model(model_path) #chargement du pileline et seuil du modèle
    if args.threshold is not None:
        threshold = args.threshold

    if args.csv:
        input_path = Path(args.csv)
        df = load_csv(input_path)
        output_path = Path(args.output) if args.output else default_output_path(input_path)
    else:
        df = build_manual_dataframe(args)
        output_path = Path(args.output) if args.output else None

    result = score_billets(df, pipeline, threshold)
    print_results(result, threshold)

    if output_path is not None:
        result.to_csv(output_path, sep=";", index=False)
        print()
        print(f"Fichier exporté : {output_path}")


if __name__ == "__main__":
    main()
