#!/usr/bin/env python3
"""
Script de parsing pour les fichiers texte brut au format:
nom_variable = valeur
===END===
"""

import re
from typing import Dict, Any


def parse_text_file(file_path: str) -> Dict[str, Any]:
    """
    Parse un fichier texte avec le format:
    nom_variable = valeur
    ===END===

    Args:
        file_path: Chemin vers le fichier texte à parser

    Returns:
        Dictionnaire contenant toutes les variables et leurs valeurs
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    return parse_text_content(content)


def parse_text_content(content: str) -> Dict[str, Any]:
    """
    Parse le contenu texte avec le format:
    nom_variable = valeur
    ===END===

    Args:
        content: Contenu texte à parser

    Returns:
        Dictionnaire contenant toutes les variables et leurs valeurs
    """
    # Séparer par les blocs délimités par ===END===
    blocks = content.split('===END===')

    data = {}

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # Chercher le pattern "nom_variable = valeur"
        # La valeur peut être sur une ou plusieurs lignes
        match = re.match(r'^(\w+)\s*=\s*(.*)', block, re.DOTALL)

        if match:
            var_name = match.group(1).strip()
            var_value = match.group(2).strip()

            # Stocker la valeur (qui peut être multiligne)
            data[var_name] = var_value

    return data


def save_example_data(output_path: str):
    """
    Sauvegarde les données d'exemple dans un fichier texte
    """
    example_data = """nom = CONFIDENTIEL Jessop
===END===
numcnesst = NUMERO_TEL
===END===
numdossier = Q-NO_DOSSIER
===END===
employeur = CONFIDENTIEL Jessop MD Inc.
===END===
ilelle = il
===END===
ilellemaj = Il
===END===
luielle = lui
===END===
travailleure = au travailleur
===END===
travailleursee = Travailleur
===END===
heuredebut = 9h52
===END===
heurefin = 11h30
===END===

sujets =
1. Diagnostic
2. Date ou période prévisible de consolidation de la lésion
3. Nature, nécessité, suffisance ou durée des soins ou traitements administrés ou prescrits
4. Existence ou pourcentage d'atteinte permanente à l'intégrité physique ou psychique
5. Existence ou évaluation des limitations fonctionnelles
===END===

raison =

Il s'agit d'une demande d'évaluation médicale de la part de la CNESST suite à une divergence d'opinions portant sur la consolidation de la lésion et la suffisance des soins par rapport à l'événement du 27 janvier 2025.

D'une part, le professionnel de la santé qui a charge, CONFIDENTIEL, dans son rapport du 25 avril 2022, retient que la lésion est consolidée et que le travailleur pourrait bénéficier de physiothérapie.

D'autre part, le professionnel de la santé désigné par la CNESST, CONFIDENTIEL, physiothérapeute, dans son rapport du 8 mai, retient que l'entorse lombaire est consolidée et qu'il n'y a pas d'indication de reprendre ou continuer les traitements.

Le diagnostic faisant l'objet de la demande est:
- Entorse lombaire avec sciatique (2, 3, 4 et 5)

===END===

declaration =
1. Je me suis présenté à monsieur comme membre du Bureau d'évaluation médicale nommé par le ministre du Travail.
2. Je lui ai expliqué mon mandat et mon rôle d'expert qui est de donner un avis impartial sur les sujets en litige entre les parties.
3. Je l'ai informé que l'avis sera produit en conformité avec la Loi sur les accidents du travail et les maladies professionnelles (LATMP) et que l'original de mon rapport sera transmis à la CNESST, qu'il en recevra une copie ainsi que le médecin qui a charge, le professionnel de la santé désigné et l'employeur.
4. J'ai révisé avec lui le formulaire d'informations et de consentement qu'il a reçu préalablement à notre rencontre.
5. J'ai demandé au travailleur s'il comprenait bien la raison de sa présence, les risques (douleurs ou émotionnels) et s'il avait des questions à propos de l'entrevue et du consentement.
6. Il m'a donné son consentement écrit puis verbal pour procéder à l'évaluation.
7. L'entrevue a débuté à 9h52 et s'est terminée à 11h30.
===END===

age = 25 ans
===END===
dominance = Non spécifiée
===END===
emploi =
Au moment de l'événement, le travailleur occupait un poste à temps plein comme préposé bénéficiaire.

Au moment de l'évaluation, le travailleur a fait une formation en médecine spécialisée et est originaire du Québec à Montréal.
===END===

atcdmed =
Aucun antécédent contributoire
===END===
atcdchir =
Aucun antécédent contributoire
===END===
atcdcnesst =
Aucune réclamation antérieure
===END===
atcdsaaq =
Aucune réclamation antérieure
===END===
rx =
Acétaminophène (Tylenol)
===END===
allergie =
Pénicilline
===END===
habitus =
Tabac: Non
Alcool: Non
Drogues: Non
Activité physique: Il pratique le hockey sur glace.
===END===
sociofamiliaux =
Le travailleur habite dans un appartement 2½.
===END===

anamnese =

1. Le 27 janvier 2025, le travailleur subit un accident de travail. Il rapporte s'être blessé à la cheville, ressentant une douleur importante à ce niveau. Depuis cet événement, il présente des douleurs lombaires significatives qui persistent.

2. Suite à l'événement, le travailleur a complété sa demande de réclamation le 27 janvier. Il mentionne que le processus administratif a été difficile et n'a jamais bien fonctionné.

3. Aujourd'hui, il se présente devant l'évaluateur pour cette évaluation médicale dans le cadre du processus du Bureau d'évaluation médicale.

===END===

revuedossier =
bla bla bla bla bla seulement.
===END===

etatactuel =

1. Au moment de l'évaluation, le travailleur rapporte avoir encore des douleurs lombaires persistantes. Il exprime sa frustration en mentionnant que "ça n'a juste pas de sens" concernant l'intensité de ses symptômes actuels.

===END===

examenobjectif =
Il s'agit d'un homme de 25 ans pesant et mesurant non spécifiés.

Inspection générale
Le travailleur se présente sans signe de détresse aiguë apparent.

Rachis cervical
La région cervicale ne présente pas d'anomalie à l'inspection.

Rachis thoracique
Le rachis thoracique est normal à l'examen.

Rachis lombaire
À l'inspection, le rachis lombaire présente un alignement normal. À la palpation de la région lombaire, on note une sensibilité modérée.

Les amplitudes articulaires actives sont:
- Flexion antérieure: Complète avec un peu de douleur à droite
- Extension: Normale

Tests spécifiques lombaires
Les tests spécifiques lombaires sont normaux.

En résumé, l'examen physique objective principalement une sensibilité modérée au niveau de la région lombaire avec amplitudes articulaires préservées mais avec légère douleur à la flexion. Les tests spécifiques lombaires demeurent normaux. Ces findings sont compatibles avec le tableau clinique rapporté d'entorse lombaire.

===END===

discussion =

1. Le Bureau d'évaluation médicale me mandate pour me prononcer sur l'entorse lombaire avec sciatique (points 2, 3, 4 et 5) relative à l'événement survenu le 27 janvier 2025.

2. Au moment de l'évaluation, soit environ 10 mois après l'événement initial, le travailleur présente des symptômes lombaires persistants avec sensibilité modérée à la palpation de la région lombaire. L'examen clinique objective des amplitudes articulaires préservées avec légère douleur à la flexion antérieure droite, mais les tests spécifiques lombaires demeurent normaux.

===END===

discussiondiag =

**Diagnostic**

Entorse lombaire avec sciatique

Le diagnostic d'entorse lombaire est retenu basé sur le mécanisme lésionnel rapporté et la présentation clinique. Il s'agit effectivement d'une entorse lombaire, également décrite comme un lumbago ou une lombalgie selon les termes utilisés dans la transcription.

===END===

discussiondate =

**Date ou période prévisible de consolidation de la lésion**

Entorse lombaire avec sciatique

D'une part, le professionnel de la santé qui a charge, CONFIDENTIEL, dans son rapport du 25 avril 2022, retient que la lésion est consolidée.

D'autre part, le professionnel de la santé désigné par la CNESST, CONFIDENTIEL, physiothérapeute, dans son rapport du 8 mai, retient également que l'entorse lombaire est consolidée.

Ainsi, je ne peux souscrire à l'opinion que la lésion est consolidée pour les raisons suivantes:

Premièrement, l'examen clinique actuel objective la persistance de symptômes avec sensibilité modérée à la palpation de la région lombaire et douleur à la flexion antérieure, témoignant d'une condition médicale toujours active nécessitant des interventions thérapeutiques continues.

Deuxièmement, l'évolution clinique suggère que la lésion n'a pas atteint sa consolidation médicale optimale et pourrait bénéficier de traitements supplémentaires pour améliorer l'état fonctionnel du travailleur.

===END===

discussionnature =

**Nature, nécessité, suffisance ou durée des soins ou traitements administrés ou prescrits**

Entorse lombaire avec sciatique

D'une part, le professionnel de la santé qui a charge, CONFIDENTIEL, dans son rapport du 25 avril 2022, retient que le travailleur pourrait bénéficier de physiothérapie.

D'autre part, le professionnel de la santé désigné par la CNESST, CONFIDENTIEL, physiothérapeute, dans son rapport du 8 mai, retient qu'il n'y a pas d'indication de reprendre ou continuer les traitements.

Ainsi, je souscris à l'opinion du professionnel qui a charge pour les raisons suivantes:

Premièrement, la persistance de symptômes objectifs à l'examen clinique avec sensibilité lombaire et douleur à la mobilisation justifie la poursuite de traitements de physiothérapie pour optimiser la récupération fonctionnelle.

Deuxièmement, les traitements de physiothérapie sont indiqués pour améliorer la condition lombaire et favoriser une consolidation appropriée de la lésion.

===END===

discussionpourcentage =

**Existence ou pourcentage d'atteinte permanente à l'intégrité physique ou psychique**

Entorse lombaire avec sciatique

Considérant que la lésion n'est pas consolidée tel qu'établi précédemment, je retiens un déficit d'atteinte permanente de 5% avec le code NO_DOSSIER.

===END===

discussionlf =

**Existence ou évaluation des limitations fonctionnelles**

Entorse lombaire avec sciatique

Considérant la persistance des symptômes et l'état non consolidé de la lésion, je retiens des limitations fonctionnelles.

Pour ma part, je retiens les limitations fonctionnelles suivantes:

· Impossibilité d'aller à la selle selon tolérance
· Éviter positions lombaires contraignantes selon tolérance
· Possibilité cesser toute activité lors d'exacerbations douloureuses

===END===

conclusion =

DIAGNOSTIC
Entorse lombaire avec sciatique

DATE OU PÉRIODE PRÉVISIBLE DE CONSOLIDATION DE LA LÉSION
Non consolidée

NATURE, NÉCESSITÉ, SUFFISANCE OU DURÉE DES SOINS OU TRAITEMENTS ADMINISTRÉS OU PRESCRITS
· Poursuite des traitements de physiothérapie selon les recommandations du professionnel qui a charge
· Suivi médical régulier pour évaluation de l'évolution

EXISTENCE OU POURCENTAGE D'ATTEINTE PERMANENTE À L'INTÉGRITÉ PHYSIQUE OR PSYCHIQUE
Déficit d'atteinte permanente de 5% avec le code NO_DOSSIER

EXISTENCE OU ÉVALUATION DES LIMITATIONS FONCTIONNELLES
· Impossibilité d'aller à la selle selon tolérance
· Éviter positions lombaires contraignantes selon tolérance
· Possibilité cesser toute activité lors d'exacerbations douloureuses

===END==="""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(example_data)


if __name__ == '__main__':
    # Test du parser avec les données d'exemple
    import json

    # Créer le fichier d'exemple
    example_file = 'example_data.txt'
    save_example_data(example_file)
    print(f"Fichier d'exemple créé: {example_file}")

    # Parser le fichier
    data = parse_text_file(example_file)

    # Afficher les résultats
    print(f"\n{len(data)} variables parsées:\n")
    for key, value in data.items():
        value_preview = value[:100] + "..." if len(value) > 100 else value
        value_preview = value_preview.replace('\n', ' ')
        print(f"  {key}: {value_preview}")

    # Sauvegarder en JSON pour inspection
    with open('parsed_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\nDonnées sauvegardées dans: parsed_data.json")
