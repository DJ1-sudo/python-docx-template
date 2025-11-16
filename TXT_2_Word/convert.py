#!/usr/bin/env python3
"""
Script simplifié pour convertir un fichier texte en document Word
Utilise automatiquement template_claude.docx comme template
"""

import sys
from pathlib import Path
from docxtpl import DocxTemplate
from parser import parse_text_file
from datetime import datetime


def convert_to_word(data_file: str, output_file: str = None, template_file: str = None):
    """
    Convertit un fichier texte en document Word

    Args:
        data_file: Chemin vers le fichier texte (.txt)
        output_file: Chemin de sortie (optionnel, auto-généré si non fourni)
        template_file: Chemin du template (optionnel, utilise template_claude.docx par défaut)
    """
    # Déterminer le template à utiliser
    if template_file is None:
        template_file = Path(__file__).parent / 'template_claude.docx'

    template_path = Path(template_file)
    if not template_path.exists():
        print(f"❌ Erreur: Template non trouvé: {template_file}")
        print(f"   Veuillez placer votre template_claude.docx dans le dossier TXT_2_Word")
        return False

    # Vérifier que le fichier de données existe
    data_path = Path(data_file)
    if not data_path.exists():
        print(f"❌ Erreur: Fichier de données non trouvé: {data_file}")
        return False

    # Déterminer le nom du fichier de sortie
    if output_file is None:
        # Générer un nom basé sur le fichier d'entrée
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = data_path.parent / f"{data_path.stem}_rapport_{timestamp}.docx"

    output_path = Path(output_file)

    try:
        # Parser les données
        print(f"📄 Lecture des données: {data_file}")
        data = parse_text_file(str(data_path))
        print(f"   ✓ {len(data)} variables extraites")

        # Charger le template
        print(f"📋 Chargement du template: {template_file}")
        doc = DocxTemplate(str(template_path))

        # Remplir le template
        print(f"⚙️  Génération du document...")
        doc.render(data)

        # Sauvegarder
        output_path.parent.mkdir(parents=True, exist_ok=True)
        doc.save(str(output_path))

        print(f"✅ Document généré avec succès!")
        print(f"   📁 {output_path.absolute()}")
        return True

    except Exception as e:
        print(f"❌ Erreur lors de la génération: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Point d'entrée principal"""
    if len(sys.argv) < 2:
        print("Usage:")
        print(f"  python {Path(__file__).name} <fichier_donnees.txt> [fichier_sortie.docx] [template.docx]")
        print()
        print("Exemples:")
        print(f"  python {Path(__file__).name} mes_donnees.txt")
        print(f"  python {Path(__file__).name} mes_donnees.txt rapport_final.docx")
        print(f"  python {Path(__file__).name} mes_donnees.txt rapport.docx mon_template.docx")
        print()
        print("Par défaut:")
        print("  - Template: template_claude.docx")
        print("  - Sortie: <nom_fichier>_rapport_<timestamp>.docx")
        return 1

    data_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    template_file = sys.argv[3] if len(sys.argv) > 3 else None

    success = convert_to_word(data_file, output_file, template_file)
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
