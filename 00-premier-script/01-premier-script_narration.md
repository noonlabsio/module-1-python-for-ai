# SCRIPT COMPLET — VIDÉO 1
**« Votre premier script Python utile en moins de 20 minutes »**
*Slides in English · Narration in French · VS Code live coding*

---

## SECTION 1 — Cold open (0:00–0:32)

> **[Écran : CSV ouvert dans VS Code, terminal en dessous. Pas de logo, pas de carte d'intro.]**
>
> « Combien j'ai dépensé au restaurant ce mois-ci ? Et en courses ? »
>
> **[beat — scroll le CSV pour montrer le volume de lignes]**
>
> « 247 transactions sur mon relevé bancaire. Pour répondre, je peux ouvrir Excel et passer une heure à filtrer. Ou je peux juste écrire 30 lignes de Python qui me donnent la réponse en deux secondes — et qui marchent pour n'importe quel mois, pour n'importe quelle question sur mes dépenses. »
>
> **[Slide : NounLab — Le code et l'IA comme on les écrit en production]**
>
> « Bienvenue sur NounLab, où on apprend Python, le ML et l'IA comme on les écrit vraiment en production. Aujourd'hui : votre premier vrai script Python. Pas de théorie, pas d'installation compliquée — un outil qui marche, en moins de vingt minutes. »
>
> **[Cut vers VS Code.]**

---

## SECTION 2 — Les données (0:32–1:45)

> **[VS Code, fichier CSV ouvert]**
>
> « Voilà les données. C'est un fichier CSV — l'export standard de n'importe quelle banque. Vous pouvez télécharger exactement le même fichier dans le repo GitHub, lien en description, pour coder avec moi. »
>
> **[surligner les colonnes]**
>
> « Quatre colonnes : la date, la description, le montant, la catégorie. 247 lignes. En fait, un CSV, c'est juste du texte. Des valeurs séparées par des virgules — d'où le nom : Comma-Separated Values. Un tableau, écrit en texte brut. »
>
> **[créer le nouveau fichier]**
>
> « On crée un fichier Python à côté. Je l'appelle `analyse_depenses.py` — sans accent, on verra plus tard pourquoi c'est une bonne habitude. Et c'est parti. »

---

## SECTION 3 — Lire le fichier (1:45–5:00)

> **[typing `import csv`]**
>
> « Première ligne : `import csv`. Python sait déjà lire les fichiers CSV — il y a un module intégré, on n'installe rien. `import`, ça veut dire : va chercher cet outil et rends-le disponible ici. »
>
> **[typing la ligne `with open`]**
>
> « Ensuite on ouvre le fichier. `with open`, entre parenthèses le nom du fichier. Ce `with`, c'est la façon propre d'ouvrir un fichier en Python : il se ferme tout seul quand on a fini, même si quelque chose plante. On en reparlera dans une vidéo dédiée. »
>
> **[typing `DictReader`]**
>
> « `csv.DictReader` — ça lit le fichier et transforme chaque ligne en dictionnaire. Concrètement : au lieu d'accéder aux valeurs par leur position, on y accède par le nom de la colonne. `row['montant']`. Beaucoup plus lisible. »
>
> « Petite remarque au passage : les noms de colonnes viennent du fichier, donc ils sont en français. Le code, lui, reste en anglais — c'est la convention. »
>
> **[typing la boucle + print]**
>
> « Et on boucle. Pour chaque ligne, on affiche. »
>
> **[RUN — le terminal se remplit]**
>
> « Et voilà. 247 dictionnaires. Chaque ligne du CSV est maintenant un objet Python qu'on peut manipuler. »
>
> « Et si vous connaissez déjà pandas — oui, on pourrait faire ça en deux lignes. On le fera, dans une vidéo dédiée. Mais aujourd'hui on utilise ce qui est déjà dans Python, sans rien installer. Et surtout : quand vous saurez ce que pandas fait pour vous, vous l'utiliserez beaucoup mieux. »
>
> **[réduire à la première ligne seulement]**
>
> « Regardons juste la première pour y voir clair. »

---

## SECTION 4 — L'erreur volontaire (5:00–8:30)

> **[supprimer la boucle d'exploration]**
>
> « On efface cette boucle d'exploration, on a vu ce qu'on voulait voir. Maintenant, la vraie question : combien j'ai dépensé au total ? »
>
> **[typing]**
>
> « On part d'un total à zéro. Pour chaque ligne, on ajoute le montant. Et on affiche à la fin. »
>
> **[RUN — TypeError]**
>
> « Erreur. Et c'est parfait. »
>
> **[beat]**
>
> « Ne fuyez jamais un message d'erreur. Celui-là vous dit exactement ce qui se passe : `unsupported operand type for plus, int and str`. Traduction : Python ne sait pas additionner un nombre et du texte. »
>
> « Pourquoi du texte ? Parce que tout ce qui sort d'un fichier CSV, c'est du texte. On l'a dit au début — un CSV, c'est du texte. Quand Python lit `47.20`, il ne voit pas un nombre. Il voit cinq caractères : quatre, sept, point, deux, zéro. Pour lui, c'est une chaîne de caractères. »
>
> **[fix avec `float()`]**
>
> « La solution : on convertit. `float(row['montant'])`. `float`, c'est le type des nombres à virgule. On dit à Python : ce texte-là, transforme-le en nombre. »
>
> **[RUN — ça marche]**
>
> « 3847 euros et 62 centimes. Ça marche. »
>
> « Et retenez ce réflexe, parce que vous allez le revoir toute votre vie de développeur, de data scientist, d'ingénieur ML ou IA : quand quelque chose ne marche pas comme prévu, la première question c'est toujours "dans quel type sont mes données ?" »

---

## SECTION 5 — Filtrer, puis tout regrouper (8:30–13:00)

> « On a le total général. Mais la question du début, c'était : combien au restaurant ? Donc on filtre. »
>
> **[typing le `if`]**
>
> « `if` — si. Si la catégorie de cette ligne est égale à "Restaurant", alors on ajoute. Sinon, on passe à la suivante. Notez le double égal : un seul égal, ça veut dire "assigne". Deux égal, ça veut dire "compare". C'est l'erreur classique du débutant. »
>
> **[RUN]**
>
> « 287 euros au restaurant. Question du début : répondue. »
>
> **[beat]**
>
> « Mais on peut faire beaucoup mieux. Là, si je veux les courses, je dois changer le mot et relancer. Si je veux les sept catégories, je relance sept fois. C'est idiot. Ce qu'on veut vraiment, c'est tout, d'un coup. »
>
> **[remplacer `total = 0` par `totals = {}`]**
>
> « Pour ça, il nous faut une structure qui associe chaque catégorie à son total. En Python, ça s'appelle un dictionnaire. Les accolades vides, c'est un dictionnaire vide. »
>
> « Un dictionnaire, c'est exactement ce que le nom dit : vous cherchez un mot, vous obtenez sa définition. Ici : vous cherchez "Restaurant", vous obtenez 287. Une clé, une valeur. »
>
> **[typing le corps de la boucle]**
>
> « Pour chaque ligne, je récupère la catégorie et le montant. Ensuite : si cette catégorie n'existe pas encore dans mon dictionnaire, je la crée à zéro. Et dans tous les cas, j'ajoute le montant. »
>
> « Il existe une façon plus courte d'écrire ces trois lignes — on la verra quand on fera les dictionnaires en profondeur. Pour l'instant, celle-là est la plus claire. »
>
> **[RUN — dictionnaire brut]**
>
> « Et voilà. Toutes mes catégories, tous mes totaux, en une seule exécution. C'est moche à lire, on va régler ça dans une minute. Mais l'information est là. »

---

## SECTION 6 — Un affichage lisible (13:00–15:30)

> « L'information est là, mais c'est illisible. Un dictionnaire brut, c'est fait pour Python, pas pour un humain. On va le formater. »
>
> **[typing la boucle `.items()`, sans `sorted` pour l'instant]**
>
> « `.items()` sur un dictionnaire, ça donne les paires clé-valeur. Donc à chaque tour de boucle je récupère deux choses d'un coup : la catégorie et le montant. »
>
> **[typing la f-string]**
>
> « Et là, une f-string. Le `f` avant les guillemets. Entre accolades, je mets des variables directement dans le texte. C'est la façon moderne de formater en Python — si vous voyez encore des tutoriels avec des `%` ou du `.format()`, c'est de l'ancien code. »
>
> « Et ce `:.2f` : deux chiffres après la virgule. Parce que `47.199999` sur un relevé bancaire, ça ne va pas. »
>
> **[RUN — propre mais non trié]**
>
> « Mieux. Mais il manque une chose : l'ordre. Là, les catégories sortent dans l'ordre où elles apparaissent dans le fichier. Ce qu'on veut, c'est le plus gros poste en premier. »
>
> **[envelopper dans `sorted(...)`]**
>
> « Python a une fonction `sorted` qui trie n'importe quelle séquence. Mais ici on ne trie pas des nombres simples — on trie des paires. Donc il faut dire à Python : *trie sur quoi ?* »
>
> « C'est le rôle de `key`. Je lui donne une petite fonction qui dit : pour chaque paire, prends le deuxième élément — c'est-à-dire le montant. Ce `lambda`, c'est juste une façon d'écrire une fonction très courte sur une seule ligne. Et `x[1]`, c'est l'élément numéro 1 de la paire : en Python on compte à partir de zéro, donc zéro c'est la catégorie, un c'est le montant. »
>
> « Et `reverse=True` : du plus grand au plus petit. Sans ça, on aurait le plus petit d'abord. »
>
> **[RUN — trié]**
>
> « Voilà. Le plus gros poste de dépenses en haut. Ça, c'est présentable. »
>
> **[beat]**
>
> « Et si le `lambda` vous paraît obscur, c'est normal — c'est la notion la plus avancée de cette vidéo. On y reviendra en détail dans la vidéo sur les fonctions. Pour aujourd'hui, retenez juste : `sorted` trie, et `key` dit sur quoi trier. »
>
> **[beat]**
>
> « Dernier point, et c'est important : le code marchait déjà avant qu'on formate. Mais du code qui marche, c'est pas du code fini. Du code fini, c'est du code qu'un autre humain peut lire — ou vous, dans six mois. »

---

## SECTION 7 — Synthèse et CTA (15:30–19:00)

> **[Slide : les 6 notions, révélées une par une]**
>
> « Récapitulons. En moins de vingt minutes, vous avez utilisé six notions fondamentales de Python. Pas en théorie — pour résoudre un vrai problème. »
>
> « Des **variables**, pour stocker vos données. Une **boucle**, pour parcourir 247 lignes sans les écrire une par une. Une **condition**, pour filtrer. Un **dictionnaire**, pour regrouper. La **conversion de types**, quand Python vous a dit non. Et les **f-strings**, pour un affichage propre. »
>
> « Ces six notions, c'est le socle. Tout le reste de Python se construit dessus. »
>
> **[retour VS Code, script final à l'écran]**
>
> « Et vous avez un outil qui marche. Changez le fichier CSV, il marche pour février. Changez la colonne, il marche pour n'importe quelle analyse. »
>
> **[beat — pivot vers vidéo 2]**
>
> « Mais soyons honnêtes sur une chose. Ce script marche — il n'est pas *propre*. Il n'y a pas d'environnement virtuel. Pas de gestion d'erreur si le fichier n'existe pas. Pas de tests. Le nom du fichier est écrit en dur dans le code. Si je vous donne ce script tel quel en entreprise, il ne passerait pas une revue de code. Et c'est normal — vous venez d'écrire votre premier script. Mais entre "ça marche" et "c'est du code de production", il y a un écart. Cet écart, c'est tout le sujet de cette chaîne. »
>
> « C'est exactement ce qu'on corrige dans la prochaine vidéo : on prend ce script et on lui donne la structure d'un vrai projet Python. Les outils modernes — uv, pyproject, ruff. Ceux que les ingénieurs utilisent vraiment. »
>
> **[CTA]**
>
> « Le code complet est dans le repo GitHub, avec le fichier CSV, lien en description — vous pouvez le télécharger et le faire tourner tout de suite. »
>
> « Et si vous voulez le template de projet Python que j'utilise pour tous mes projets — pyproject configuré, ruff, pytest, type hints, tout est prêt — il est gratuit, le lien est en description aussi. C'est exactement ce qu'on va déballer dans la vidéo 2. »
>
> « Si cette approche vous parle, abonnez-vous — on publie une vidéo tous les mardis. Activez la cloche si vous ne voulez pas rater la suite. À la prochaine. »

---
---

# LE CODE

## Progression à l'écran (5 états)

**Étape 1 — Lire et explorer** *(Section 3)*
```python
import csv

with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

**Étape 2 — L'erreur volontaire** *(Section 4 — supprimer la boucle ci-dessus d'abord)*
```python
import csv

total = 0

with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = total + row["montant"]

print(total)
```
→ `TypeError: unsupported operand type(s) for +: 'int' and 'str'`

**Étape 3 — Le fix `float()`**
```python
import csv

total = 0

with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = total + float(row["montant"])

print(total)
```

**Étape 4 — Filtrer une catégorie** *(Section 5)*
```python
import csv

total = 0

with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["categorie"] == "Restaurant":
            total = total + float(row["montant"])

print(total)
```

**Étape 5 — Toutes les catégories**
```python
import csv

totals = {}

with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        category = row["categorie"]
        amount = float(row["montant"])
        if category not in totals:
            totals[category] = 0
        totals[category] = totals[category] + amount

print(totals)
```

## Version finale — `analyse_depenses.py`

```python
import csv

totals = {}

with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        category = row["categorie"]
        amount = float(row["montant"])
        if category not in totals:
            totals[category] = 0
        totals[category] = totals[category] + amount

print("Dépenses de janvier")
print("-" * 30)

for category, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
    print(f"{category}: {amount:.2f} €")
```

## Le CSV — `depenses_janvier.csv`

Schéma verrouillé. Colonnes sans accent, point décimal, virgule comme séparateur, montants positifs.

```csv
date,description,montant,categorie
2026-01-02,Carrefour Market,47.20,Courses
2026-01-03,Le Petit Bistrot,32.50,Restaurant
2026-01-03,SNCF Connect,89.00,Transport
2026-01-04,Loyer Janvier,850.00,Logement
2026-01-05,Pharmacie du Centre,18.90,Sante
2026-01-05,Spotify,10.99,Abonnements
2026-01-06,Cinema Pathe,12.50,Loisirs
```

**Catégories :** Restaurant, Courses, Transport, Loisirs, Sante, Abonnements, Logement
**À générer :** 247 lignes réparties sur janvier 2026, noms de marchands français réalistes. Tâche de préparation au tournage — pas aujourd'hui.
