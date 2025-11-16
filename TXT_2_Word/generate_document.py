#!/usr/bin/env python3
"""
Script de génération de documents Word à partir de fichiers texte brut
en utilisant python-docx-template
"""

import argparse
import sys
from pathlib import Path
from docxtpl import DocxTemplate
from parser import parse_text_file, parse_text_content


def generate_document(template_path: str, data_path: str, output_path: str):
    """
    Génère un document Word à partir d'un template et de données texte

    Args:
        template_path: Chemin vers le template .docx
        data_path: Chemin vers le fichier texte contenant les données
        output_path: Chemin où sauvegarder le document généré
    """
    # Vérifier que le template existe
    template_file = Path(template_path)
    if not template_file.exists():
        raise FileNotFoundError(f"Template non trouvé: {template_path}")

    # Parser les données
    print(f"Parsing des données depuis: {data_path}")
    data = parse_text_file(data_path)
    print(f"  → {len(data)} variables extraites")

    # Charger le template
    print(f"Chargement du template: {template_path}")
    doc = DocxTemplate(template_path)

    # Remplir le template avec les données
    print("Remplissage du template...")
    doc.render(data)

    # Sauvegarder le document généré
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    doc.save(output_path)
    print(f"Document généré avec succès: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Génère un document Word à partir d'un template et de données texte"
    )
    parser.add_argument(
        '-t', '--template',
        required=True,
        help='Chemin vers le fichier template .docx'
    )
    parser.add_argument(
        '-d', '--data',
        required=True,
        help='Chemin vers le fichier texte contenant les données'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Chemin où sauvegarder le document généré'
    )

    args = parser.parse_args()

    try:
        generate_document(args.template, args.data, args.output)
        return 0
    except Exception as e:
        print(f"Erreur: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
