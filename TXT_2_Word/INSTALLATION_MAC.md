# Installation sur Mac

## Étape 1: Créer le dossier

Ouvrez le Terminal sur votre Mac et exécutez:

```bash
cd /Users/jessop/Documents/Anesthésie/BEM
mkdir -p TXT_2_Word
cd TXT_2_Word
```

## Étape 2: Copier les fichiers

Copiez tous les fichiers Python que j'ai créés dans ce dossier:
- `parser.py`
- `generate_document.py`
- `convert.py`
- `requirements.txt`
- `README.md`

## Étape 3: Installer Python (si nécessaire)

Vérifiez si Python 3 est installé:

```bash
python3 --version
```

Si Python n'est pas installé, installez-le via Homebrew:

```bash
# Installer Homebrew (si pas déjà installé)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installer Python 3
brew install python3
```

## Étape 4: Créer un environnement virtuel (recommandé)

```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
source venv/bin/activate
```

## Étape 5: Installer les dépendances

```bash
pip install -r requirements.txt
```

Ou manuellement:

```bash
pip install python-docx docxtpl lxml jinja2 pillow
```

## Étape 6: Ajouter votre template

Copiez votre fichier `template_claude.docx` dans le dossier TXT_2_Word:

```bash
cp /Users/jessop/Downloads/template_claude.docx .
```

## Étape 7: Tester

```bash
# Créer un fichier de test
python3 parser.py

# Générer un document (une fois le template en place)
python3 convert.py example_data.txt
```

## Utilisation quotidienne

### Méthode simple

```bash
# Activer l'environnement virtuel (si vous l'avez créé)
source venv/bin/activate

# Convertir votre fichier
python3 convert.py mes_donnees.txt
```

Le document sera généré automatiquement avec un nom incluant la date et l'heure.

### Méthode avec nom de fichier personnalisé

```bash
python3 convert.py mes_donnees.txt rapport_BEM_Jessop.docx
```

### Méthode complète (avec tous les paramètres)

```bash
python3 generate_document.py \
    -t template_claude.docx \
    -d mes_donnees.txt \
    -o rapport_final.docx
```

## Résolution de problèmes

### Erreur: "command not found: python3"

Utilisez `python` au lieu de `python3`:

```bash
python convert.py mes_donnees.txt
```

### Erreur: "Template non trouvé"

Assurez-vous que `template_claude.docx` est dans le même dossier que les scripts:

```bash
ls -la template_claude.docx
```

### Erreur d'encodage

Si vous avez des problèmes avec les accents, assurez-vous que votre fichier texte est encodé en UTF-8.

## Créer un alias pour plus de simplicité

Ajoutez ceci à votre `~/.zshrc` ou `~/.bash_profile`:

```bash
alias txt2word='cd /Users/jessop/Documents/Anesthésie/BEM/TXT_2_Word && source venv/bin/activate && python3 convert.py'
```

Puis vous pourrez simplement faire:

```bash
txt2word mes_donnees.txt
```

## Structure finale du dossier

```
/Users/jessop/Documents/Anesthésie/BEM/TXT_2_Word/
├── venv/                      # Environnement virtuel Python
├── parser.py                  # Script de parsing
├── generate_document.py       # Script de génération (méthode complète)
├── convert.py                 # Script de conversion (méthode simple)
├── requirements.txt           # Dépendances Python
├── README.md                  # Documentation
├── INSTALLATION_MAC.md        # Ce fichier
├── template_claude.docx       # VOTRE TEMPLATE (à ajouter)
├── example_data.txt           # Exemple de données
└── parsed_data.json           # Données parsées (généré automatiquement)
```
