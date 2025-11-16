# TXT_2_Word - Générateur de Documents Word

Ce dossier contient les scripts pour convertir des fichiers texte brut en documents Word formatés en utilisant python-docx-template.

## Fichiers

- `parser.py` : Script de parsing des fichiers texte avec délimiteurs `===END===`
- `generate_document.py` : Script principal de génération de documents Word
- `example_data.txt` : Exemple de fichier de données
- `parsed_data.json` : Données parsées au format JSON (pour inspection)

## Format du fichier texte d'entrée

Le fichier texte doit suivre ce format :

```
nom_variable = valeur
===END===

autre_variable =
valeur sur
plusieurs lignes
===END===
```

Chaque variable est séparée par `===END===`. Les valeurs peuvent être sur une ou plusieurs lignes.

## Utilisation

### 1. Préparer votre template Word

Créez un fichier Word (.docx) avec des placeholders Jinja2 :

```
Nom du travailleur: {{ nom }}
Numéro CNESST: {{ numcnesst }}
Dossier: {{ numdossier }}

{{ discussion }}
```

### 2. Préparer votre fichier de données

Créez un fichier texte avec vos données au format ci-dessus.

### 3. Générer le document

```bash
python generate_document.py \
    -t template_claude.docx \
    -d mes_donnees.txt \
    -o rapport_genere.docx
```

**Paramètres:**
- `-t` ou `--template` : Chemin vers le template Word
- `-d` ou `--data` : Chemin vers le fichier de données texte
- `-o` ou `--output` : Chemin du fichier Word à générer

## Exemple

```bash
# Tester le parser uniquement
python parser.py

# Générer un document (une fois que vous avez le template)
python generate_document.py \
    -t template_claude.docx \
    -d example_data.txt \
    -o rapport_BEM.docx
```

## Variables disponibles dans votre template

Basé sur l'exemple fourni, les variables suivantes sont disponibles :

- `nom` - Nom du patient
- `numcnesst` - Numéro CNESST
- `numdossier` - Numéro de dossier
- `employeur` - Employeur
- `ilelle`, `ilellemaj`, `luielle` - Pronoms
- `travailleure`, `travailleursee` - Variations du mot travailleur
- `heuredebut`, `heurefin` - Heures de l'évaluation
- `sujets` - Liste des sujets traités
- `raison` - Raison de l'évaluation
- `declaration` - Déclarations standard
- `age` - Âge du patient
- `dominance` - Dominance manuelle
- `emploi` - Information sur l'emploi
- `atcdmed`, `atcdchir`, `atcdcnesst`, `atcdsaaq` - Antécédents
- `rx` - Médication
- `allergie` - Allergies
- `habitus` - Habitudes de vie
- `sociofamiliaux` - Contexte socio-familial
- `anamnese` - Anamnèse
- `revuedossier` - Revue du dossier
- `etatactuel` - État actuel
- `examenobjectif` - Examen objectif
- `discussion` - Discussion générale
- `discussiondiag` - Discussion diagnostic
- `discussiondate` - Discussion consolidation
- `discussionnature` - Discussion nature des soins
- `discussionpourcentage` - Discussion atteinte permanente
- `discussionlf` - Discussion limitations fonctionnelles
- `conclusion` - Conclusion

## Syntaxe Jinja2 dans le template

Dans votre template Word, vous pouvez utiliser :

- Variables simples : `{{ nom }}`
- Conditions : `{% if ilelle == "il" %}masculin{% else %}féminin{% endif %}`
- Boucles : `{% for item in liste %}{{ item }}{% endfor %}`

## Prochaines étapes

1. Uploadez votre `template_claude.docx` dans ce dossier
2. Testez la génération avec vos données
3. Ajustez le template selon vos besoins
