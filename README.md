# Module I — Python Fundamentals for Modern AI

Les slides et le code de la série **Python de zéro à production** sur la
chaîne [NoonLabs](https://youtube.com/@noonlabsio).

**Learn fundamentals. Build modern AI.**
From mathematical foundations to modern AI systems.

Chaque dossier correspond à une vidéo. Il contient les slides (`slides.md`)
et, à partir du chapitre 08, un script `verify-facts.py` qui revérifie chaque
fait affiché à l'écran : sorties, messages d'erreur, versions.

## Prérequis

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) pour la gestion des dépendances
- Node.js 22 pour les slides (voir `.nvmrc`)
- VS Code (optionnel mais recommandé)

Pour démarrer un projet propre, utilisez le
[starter template](https://github.com/noonlabsio/python-starter-template).

## Les vidéos

| № | Sujet | Dossier | Vidéo |
|---|-------|---------|-------|
| 00 | Votre premier script Python utile | [`00-premier-script/`](00-premier-script/) | *à venir* |
| 01 | Installer Python et son environnement | [`01_env_setup/`](01_env_setup/) | *à venir* |
| 02 | Syntaxe et types de données | [`02-syntax-and-types/`](02-syntax-and-types/) | *à venir* |
| 03 | Conditions et boucles | [`03-control-flow-and-loops/`](03-control-flow-and-loops/) | *à venir* |
| 04 | Fonctions et portée | [`04-functions-and-scope/`](04-functions-and-scope/) | *à venir* |
| 05 | Structures de données | [`05-data-structures/`](05-data-structures/) | *à venir* |
| 06 | Fichiers et formats de données | [`06-file-io-data-formats/`](06-file-io-data-formats/) | *à venir* |
| 07 | Erreurs et exceptions | [`07-error-handling-and-exceptions/`](07-error-handling-and-exceptions/) | *à venir* |
| 08 | Programmation orientée objet | [`08-object-oriented-programming/`](08-object-oriented-programming/) | *à venir* |
| 09 | La bibliothèque standard | [`09-python-standard-libraries/`](09-python-standard-libraries/) | *à venir* |
| 10 | Programmation fonctionnelle | [`10-functional-programming/`](10-functional-programming/) | *à venir* |
| 11 | Python avancé | [`11-advanced-python/`](11-advanced-python/) | *à venir* |
| 12 | NumPy | [`12-numpy/`](12-numpy/) | *à venir* |
| 13 | pandas, Polars et DuckDB | [`13-pandas-and-modern-dataframe-libraries/`](13-pandas-and-modern-dataframe-libraries/) | *à venir* |

*Le tableau se remplit au fil des publications. Une vidéo tous les mardis.*

[`00-master/`](00-master/) rassemble les chapitres 01 à 13 en une seule
présentation.

## Slides

Les slides sont en Markdown, propulsées par [Slidev](https://sli.dev), avec le
thème du dépôt dans [`themes/noonlabs/`](themes/noonlabs/).

```bash
nvm use            # Node 22, lu dans .nvmrc
npm install
npm run dev -- 03-control-flow-and-loops/slides.md
```

Exporter un chapitre en PDF :

```bash
npm run export -- 03-control-flow-and-loops/slides.md \
  --output exports/03-control-flow-and-loops.pdf
```

Les versions PDF sont rangées dans [`exports/`](exports/).

Après avoir ajouté ou retiré une slide dans un chapitre, régénérez la
présentation complète :

```bash
python3 build-master.py
npm run dev -- 00-master/slides.md
```

## Vérifier les faits

Les chapitres 08 à 11 n'utilisent que la bibliothèque standard :

```bash
python3 11-advanced-python/verify-facts.py
```

Les chapitres 12 et 13 ont besoin de leurs bibliothèques, aux versions de
l'enregistrement. uv les installe dans un environnement temporaire, sans
toucher au dépôt :

```bash
uv run --no-project --with numpy==2.5.3 python 12-numpy/verify-facts.py

uv run --no-project --python 3.12 --with pandas==3.0.6 --with pyarrow==25.0.1 \
  --with polars==2.0.0 --with duckdb==1.5.6 \
  python 13-pandas-and-modern-dataframe-libraries/verify-facts.py
```

Chaque script affiche `ALL FACTS HOLD`, ou la liste des slides à corriger.

## Licence

MIT — utilisez ce code comme vous voulez.
