---
theme: ../themes/noonlabs
title: Pandas & Modern Dataframe Libraries — Chapter 13
info: NoonLabs - Module I, chapitre 13
layout: cover
transition: fade
mdc: true
---

# NoonLabs

Learn fundamentals. Build modern AI.

From mathematical foundations to modern AI systems.

<!--
SLIDE 1 - Brand stamp
On screen ~4 seconds. Say "Bienvenue sur NoonLabs" over it and move on.
-->

---
layout: section
class: nl-deck
---

<div class="nl-eyebrow">Chapter 13</div>

# Pandas & Modern Dataframe Libraries

<div class="mt-4" style="max-width: 42ch">

Tables with column names, missing values and dates, the shape most real data arrives in

</div>

<div class="nl-type mt-6">
  <NlIcon name="cells" /> pandas
  <span class="mx-3">·</span>
  <NlIcon name="arrow" /> Polars
  <span class="mx-3">·</span>
  <NlIcon name="server" /> DuckDB
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~8 seconds.

Pay off the promise from the end of chapter twelve:
"Chapitre treize. Au chapitre douze, je vous ai promis des tableaux avec des
noms de colonnes et des valeurs manquantes. C'est pandas. Et à la fin, deux
outils plus récents : Polars et DuckDB."

Restate the format so nobody wonders:
"Les diapositives, c'est pour les concepts. Le code, on l'écrit ensemble
dans VS Code."
-->

---
layout: default
class: nl-deck
---

# From CSV to DataFrame

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> The January expenses</div>

```python
import pandas as pd

df = pd.read_csv("depenses_janvier.csv")
df.shape        # (247, 4)
df.info()       # 3 str columns, 1 float64
df.describe()   # count, mean, std, quartiles
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Named columns, one index</div>

A DataFrame is a set of columns that share one index. Each column has a single
dtype, like a NumPy array from chapter 12.

<div class="nl-type mt-3"><NlIcon name="check" /> What loadtxt could not do</div>

<div style="font-size: 1.05rem">

`read_csv` reads all four columns, text included. In pandas 3, `info()` shows
`str` for text; pandas 2 tutorials show `object`.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Start every dataset with <code>shape</code>, <code>info()</code> and <code>describe()</code>
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 3 - From CSV to DataFrame
On screen ~60 seconds.

Callback to chapter twelve, the last slide on files:
"Au chapitre douze, loadtxt ne savait lire que la colonne des montants. Les
dates, les descriptions, les catégories : impossible. read_csv lit les
quatre colonnes, en une ligne."

Run the three calls live and read them:
"Deux cent quarante-sept lignes, quatre colonnes. info : trois colonnes de
texte, une de nombres, aucune valeur manquante. describe : une dépense
moyenne de vingt et un euros quarante-neuf, et un maximum de mille deux cent
cinquante - le loyer."

PAUSE.

Callback to chapter nine: la somme des montants affiche 5308,389999999999.
Des floats, encore. Pour de la comptabilité exacte, c'est Decimal, chapitre
neuf.

[CLICK]
"Chaque jeu de données commence par shape, info et describe. Trente secondes
qui évitent des heures."

Time-sensitive: ces sorties sont celles de pandas 3. Les colonnes de texte
s'affichent str, et la classe s'appelle pandas.DataFrame. Un tutoriel qui
montre object date de pandas 2.
-->

---
layout: default
class: nl-deck
---

# Series

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> One column, with labels</div>

```python
>>> s = pd.Series([13.16, 5.5],
...               index=["Resto", "Courses"])
>>> s["Courses"], s.dtype
(np.float64(5.5), dtype('float64'))
>>> s + pd.Series([1.0], index=["Resto"])
Courses      NaN
Resto      14.16
dtype: float64
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Values, dtype, index</div>

A Series is one column: an array of values, one dtype, and an index of
labels. `s["Courses"]` reads by label, `s.iloc[0]` by position.

<div class="nl-type mt-3"><NlIcon name="box" /> Attributes</div>

<div style="font-size: 1.05rem">

`.index`, `.values`, `.dtype`, `.name`. Every column of a DataFrame is a
Series.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A Series is an array with labels — and the labels matter
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 4 - Series. This is the chapter's PLANT.
On screen ~55 seconds.

"Une Series, c'est une colonne. Des valeurs, un type, et des étiquettes.
s de Courses lit par étiquette ; iloc de zéro, par position."

Then type the last addition live, and let the result surprise them:
"J'ajoute une autre Series, avec une seule valeur, pour Resto. Resto devient
quatorze seize. Et Courses... NaN."

PAUSE.

PLANT the payoff and do not explain it:
"Deux Series, et un NaN apparaît. Retenez-le : pandas aligne sur les
étiquettes, pas sur les positions. On verra plus loin pourquoi c'est une
force."

[CLICK]
"Une Series, c'est un tableau avec des étiquettes. Et les étiquettes
comptent."
-->

---
layout: default
class: nl-deck
---

# Selecting with `loc` & `iloc`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Row, then column</div>

```python
df.loc[0, "categorie"]       # 'Restaurant'
df.iloc[0, 2]                # 13.16
df.loc[:2, ["description", "montant"]]
df.iloc[:2, [1, 2]]
```

</div>

<div>

<div class="nl-type"><NlIcon name="split" /> Two indexers</div>

<div class="nl-recap mt-2">
  <div class="n">loc</div><div><span class="why">labels; the slice end is included</span></div>
  <div class="n">iloc</div><div><span class="why">positions; the end is excluded</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

`df.loc[:2]` returns three rows, 0 to 2. `df.iloc[:2]` returns two, like
`range` in chapter 03. One indexer, row then column, as in NumPy.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>loc</code> reads labels and includes the end; <code>iloc</code> reads positions and excludes it
</div>

<!--
SLIDE 5 - loc and iloc
On screen ~55 seconds. Concept slide, no live coding needed.

"Deux façons de désigner une case. loc, par étiquette : la ligne zéro, la
colonne catégorie. iloc, par position : la ligne zéro, la troisième
colonne."

PAUSE.

The trap, said slowly because it bites everyone:
"Et les tranches ne s'arrêtent pas au même endroit. loc deux-points deux
inclut la ligne deux : trois lignes. iloc deux-points deux l'exclut, comme
range : deux lignes."

Callback to chapter twelve: une seule paire de crochets, la ligne puis la
colonne, séparées par une virgule. Comme m de ligne, colonne en NumPy.

[CLICK]
"loc lit des étiquettes et inclut la fin. iloc lit des positions et
l'exclut."
-->

---
layout: default
class: nl-deck
---

# Boolean Filters & `query`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Two ways to say it</div>

```python
big = df[df["montant"] > 100]
resto = df[(df["categorie"] == "Restaurant")
           & (df["montant"] > 20)]

df.query("categorie == 'Restaurant' "
         "and montant > 20")    # 17 rows
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> The mask, again</div>

A comparison gives one `True` or `False` per row, as in chapter 12. Same
rules: `&`, `|`, and parentheses around each condition.

<div class="nl-type mt-3"><NlIcon name="split" /> query</div>

<div style="font-size: 1.05rem">

It takes the condition as a string and reads column names directly. Shorter,
but a typo only shows up when it runs.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Filter with a mask — or say it in <code>query</code> when that reads better
</div>

<!--
SLIDE 6 - Filters
On screen ~50 seconds. Concept slide, no live coding needed.

Callback to chapter twelve, the boolean masks:
"Le masque du chapitre douze, appliqué à une table : un vrai ou faux par
ligne, et on garde les lignes vraies. Mêmes règles : esperluette, barre
verticale, et des parenthèses."

One expense above a hundred euros: le loyer. Dix-sept restaurants à plus de
vingt euros - les deux écritures donnent les mêmes dix-sept lignes.

PAUSE.

[CLICK]
"Filtrez avec un masque. Ou dites-le avec query, quand ça se lit mieux."
-->

---
layout: default
class: nl-deck
---

# Adding & Modifying Columns

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Right, wrong, chained</div>

```python
df["ttc"] = df["montant"] * 1.2
df.loc[0, "montant"] = 0         # works

df["montant"][0] = 0             # never works

df = df.assign(ttc=pd.col("montant") * 1.2)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> Chained assignment</div>

`df["montant"]` hands back a new Series, so `[0] = 0` changes that copy and
it is lost. pandas 3 only warns: `ChainedAssignmentError`.

<div class="nl-type mt-3"><NlIcon name="layers" /> Copy-on-Write, pandas 3.0</div>

<div style="font-size: 1.05rem">

Every selection behaves like a copy. To change the original, assign on the
DataFrame itself: `df.loc[row, col]`, or `df["col"]`. `pd.col()` works in `assign`.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Assign on the DataFrame itself — a chained assignment changes a copy
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 7 - Adding and modifying columns
On screen ~65 seconds.

The first line is the easy part: une nouvelle colonne, calculée sur toute la
colonne d'un coup. Le montant toutes taxes comprises.

Then type the chained assignment live, and print the value after it:
"Je mets le premier montant à zéro... Un avertissement, ChainedAssignmentError.
Et le montant vaut toujours treize seize."

PAUSE.

Callback to chapter twelve, the views slide, because pandas chose the
opposite:
"En NumPy, une tranche était une vue : la modifier modifiait l'original.
pandas 3 a fait le choix inverse. Toute sélection se comporte comme une
copie. df de montant, puis crochet zéro : vous modifiez une copie, et elle
disparaît."

"Pour modifier l'original, on affecte directement sur le DataFrame : un seul
loc, la ligne et la colonne ensemble - ou df de colonne égale, pour une
colonne entière. Ce qui ne marche jamais, c'est deux paires de crochets à la
suite."

[CLICK]
"Affectez sur le DataFrame lui-même. Une affectation enchaînée modifie une
copie."

Time-sensitive: le Copy-on-Write est le seul mode depuis pandas 3.0, janvier
2026. pd.col est nouveau dans la 3.0. Les tutoriels pandas 2 parlent de
SettingWithCopyWarning, qui n'existe plus.
-->

---
layout: default
class: nl-deck
---

# Missing Data

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Find, fill, skip</div>

```python
>>> m = pd.Series([1.0, None, 3.0])
>>> m.isnull().tolist()
[False, True, False]
>>> m.fillna(0).tolist()
[1.0, 0.0, 3.0]
>>> m.interpolate().tolist()
[1.0, 2.0, 3.0]
>>> m.mean()
np.float64(2.0)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> NaN, from chapter 12</div>

An empty CSV cell or a `None` becomes NaN. `dropna` removes it, `fillna`
replaces it, `interpolate` fills it from its neighbours.

<div class="nl-type nl-bad mt-3"><NlIcon name="split" /> Not NumPy's default</div>

<div style="font-size: 1.05rem">

`mean()` skips NaN unless you pass `skipna=False`. In chapter 12, NumPy's
mean returned `nan`.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
pandas skips NaN by default — NumPy does not
</div>

<!--
SLIDE 8 - Missing data
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter twelve, the NaN slide:
"Au chapitre douze, une seule valeur manquante et la moyenne entière devenait
NaN. En pandas, même donnée : deux. pandas saute les NaN par défaut."

PAUSE.

"C'est pratique, et c'est dangereux. Une colonne à moitié vide donne une
moyenne tout à fait plausible. Commencez toujours par compter : isnull, puis
sum."

The three remedies, one line each: dropna supprime, fillna remplace, et
interpolate devine la valeur à partir de ses voisines - deux, entre un et
trois.

[CLICK]
"pandas saute les NaN par défaut. NumPy, non."
-->

---
layout: default
class: nl-deck
---

# Type Conversion

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Three converters</div>

```python
>>> pd.to_numeric(pd.Series(["1.5", "abc"]),
...               errors="coerce").tolist()
[1.5, nan]
>>> pd.to_datetime(df["date"]).dtype.name
'datetime64[us]'
>>> df["categorie"].astype("category")
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> Without errors="coerce"</div>

`to_numeric` raises: `Unable to parse string "abc" at position 1`. With it, a
bad value becomes NaN, and you count it.

<div class="nl-type mt-3"><NlIcon name="layers" /> Dates and categories</div>

<div style="font-size: 1.05rem">

pandas 3 parses dates to microseconds. `category` stores the 7 categories once
instead of 247 strings.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Convert when you load, and decide what a bad value becomes
</div>

<!--
SLIDE 9 - Type conversion
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter two, type conversion: float de « abc » levait une
ValueError. to_numeric aussi, par défaut.

"Avec errors égale coerce, la valeur illisible devient NaN au lieu de tout
arrêter. Et ensuite, on compte combien il y en a. Un NaN qu'on ne compte pas,
c'est une donnée perdue en silence."

PAUSE.

Dates: to_datetime transforme la colonne de texte en vraies dates. Le type
affiché : datetime64 en microsecondes.

category in one sentence: sept catégories stockées une fois, et chaque ligne
garde un petit numéro. Moins de mémoire, et des groupby plus rapides.

[CLICK]
"Convertissez au chargement. Et décidez ce que devient une valeur illisible."

Time-sensitive: depuis pandas 3, les dates sont en microsecondes, pas en
nanosecondes. Ça évite les erreurs sur des dates avant 1678 ou après 2262.
-->

---
layout: default
class: nl-deck
---

# The `.str` Accessor

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> String methods, per column</div>

```python
df["description"].str.upper()
df["description"].str.contains("Carrefour")
df["description"].str.split(" ").str[0]
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Chapter 02, whole columns</div>

`.str` applies a string method to every value of the column at once:
`upper`, `contains`, `split`, `replace`, `strip`.

<div class="nl-type mt-3"><NlIcon name="split" /> The str dtype</div>

<div style="font-size: 1.05rem">

In pandas 3 a text column has the `str` dtype: it holds only strings or NaN.
Code that tests for `object` breaks.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>.str</code> brings every string method to a whole column
</div>

<!--
SLIDE 10 - The str accessor
On screen ~50 seconds. Concept slide, no live coding needed.

Callback to chapter two, the string methods:
"Les méthodes de chaînes du chapitre deux. upper, split, replace. Point str
les applique à toute une colonne, en une fois."

Read the three lines: tout en majuscules ; les lignes qui contiennent
Carrefour - il y en a cinq ; et le premier mot de chaque description.

PAUSE.

[CLICK]
"Point str apporte toutes les méthodes de chaînes à une colonne entière."

Time-sensitive: depuis pandas 3, une colonne de texte a le type str, adossé
à PyArrow s'il est installé. Elle ne peut contenir que du texte ou NaN.
-->

---
layout: default
class: nl-deck
---

# Index, Labels & Duplicates

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Reshape the labels</div>

```python
df.rename(columns={"montant": "amount"})
df.set_index("date")     # dates become labels
df.reset_index()         # labels become a column
df.reindex([0, 1, 999])  # 999 is a new row
df.drop_duplicates()
df.duplicated(subset=["description"]).sum()
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> They return new frames</div>

`rename`, `set_index` and `drop_duplicates` return a new DataFrame: assign the
result. `reindex` gives a label that does not exist a row of NaN.

<div class="nl-type mt-3"><NlIcon name="split" /> Which duplicates?</div>

<div style="font-size: 1.05rem">

This file has no fully repeated row, but 178 repeated descriptions. It depends
on the columns you compare.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A duplicate is defined by the columns you compare
</div>

<!--
SLIDE 11 - Index and duplicates
On screen ~60 seconds. Concept slide, no live coding needed.

Read the labels part quickly. rename change des noms de colonnes. set_index
transforme une colonne en étiquettes de lignes, reset_index fait l'inverse.
reindex se conforme à la liste qu'on lui donne : une étiquette inconnue
reçoit une ligne de NaN.

The habit: ces méthodes renvoient un nouveau DataFrame. Si vous ne
réaffectez pas le résultat, rien n'a changé.

PAUSE.

Then the duplicates, because the number surprises:
"Aucune ligne entièrement en double. Mais cent soixante-dix-huit descriptions
répétées : on va souvent chez Carrefour. Les deux réponses sont justes. Un
doublon dépend des colonnes que vous comparez."

[CLICK]
"Un doublon se définit par les colonnes que vous comparez. Dites-les avec
subset."
-->

---
layout: default
class: nl-deck
---

# `apply`, `map` & `transform`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Three ways to run a function</div>

```python
df["montant"].map(round)
df["categorie"].map({"Sante": "Santé"})
df.apply(lambda r: r["montant"] * 2, axis=1)
df["montant"] * 2          # the same, fast
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> What each returns</div>

<div class="nl-recap mt-2">
  <div class="n">map</div><div><span class="why">one value in, one out, per element</span></div>
  <div class="n">apply</div><div><span class="why">a function per row or per column</span></div>
  <div class="n">transform</div><div><span class="why">a result the same shape as its input</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

`map` with a dict turns every unmatched value into NaN. `apply(axis=1)` calls
your function once per row: chapter 12's `np.vectorize`, again.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Reach for column arithmetic first — <code>apply</code> is a loop
</div>

<!--
SLIDE 12 - apply, map, transform
On screen ~55 seconds. Concept slide, no live coding needed.

The recap first: map transforme valeur par valeur, apply prend une ligne ou
une colonne entière, transform renvoie un résultat de la même forme - on le
revoit dans la diapositive suivante.

Then the dict trap, which corrupts data silently:
"map avec un dictionnaire : Sante devient Santé, avec l'accent. Et toutes les
autres catégories deviennent... NaN. Elles n'étaient pas dans le
dictionnaire. Pour ne remplacer que certaines valeurs, c'est replace."

PAUSE.

Callback to chapter twelve:
"apply avec axis égale un, c'est une boucle Python sur chaque ligne. Le même
piège que np.vectorize au chapitre douze. Si une opération sur la colonne
existe, elle est bien plus rapide - plus de dix fois, sur ce petit fichier."

[CLICK]
"L'arithmétique sur les colonnes d'abord. apply est une boucle."
-->

---
layout: default
class: nl-deck
---

# GroupBy

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Totals, then shares</div>

```python
>>> g = df.groupby("categorie")["montant"]
>>> g.sum().sort_values(ascending=False)
Logement       1670.03
Courses         955.33
Restaurant      880.41
...
>>> df["part"] = (df["montant"]
...               / g.transform("sum"))
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Split, apply, combine</div>

<div class="nl-recap mt-2">
  <div class="n">agg</div><div><span class="why">one row per group</span></div>
  <div class="n">transform</div><div><span class="why">one value per original row</span></div>
  <div class="n">filter</div><div><span class="why">keeps or drops whole groups</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

No sorting first, unlike `itertools.groupby` in chapter 10. `value_counts()`
is chapter 05's `Counter` for a column.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>transform</code> gives every row its group's result — the index lines them up
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 13 - GroupBy. This is the chapter's PAYOFF.
On screen ~65 seconds.

Run the sum live first:
"Logement, mille six cent soixante-dix. Courses, neuf cent cinquante-cinq.
Restaurant, huit cent quatre-vingts virgule quarante et un. Les totaux du
premier script de ce module - en une ligne."

Callback to chapter ten: itertools.groupby ne regroupait que les voisins, il
fallait trier d'abord. pandas groupby n'en a pas besoin.

PAUSE.

Then land the payoff planted on the Series slide. Do this live: the share of
each expense in its category.

"Souvenez-vous des NaN de l'alignement, sur la diapositive des Series. Ici,
l'alignement travaille pour vous. transform renvoie une valeur par ligne,
avec le même index. Chaque ligne retrouve le total de sa propre catégorie,
et la division tombe juste."

[CLICK]
"transform donne à chaque ligne le résultat de son groupe. C'est l'index qui
les aligne."

filter in one sentence: garder les catégories dont le total dépasse neuf
cents euros. Il reste Courses et Logement.
-->

---
layout: default
class: nl-deck
---

# Pivot Tables & `crosstab`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Category by week</div>

```python
df["semaine"] = (pd.to_datetime(df["date"])
                 .dt.isocalendar().week)
pd.pivot_table(df, index="categorie",
               columns="semaine",
               values="montant",
               aggfunc="sum")
pd.crosstab(df["categorie"], df["semaine"])
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="cells" /> A grid of groups</div>

`pivot_table`: one row per category, one column per week, the sum in each
cell. A groupby on two keys, laid out as a grid.

<div class="nl-type mt-3"><NlIcon name="check" /> crosstab counts</div>

<div style="font-size: 1.05rem">

How many expenses fall in each category and week. Every cell together adds up
to 247.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A pivot table is a two-key groupby, laid out as a grid
</div>

<!--
SLIDE 14 - Pivot tables
On screen ~50 seconds. Concept slide, no live coding needed.

"Une table croisée, c'est le groupby de la diapositive précédente, avec deux
clés au lieu d'une. Les catégories en lignes, les semaines en colonnes, et
la somme dans chaque case."

isocalendar gives ISO weeks, which start on Monday.

PAUSE.

crosstab: même grille, mais elle compte au lieu d'additionner. Toutes les
cases ensemble font deux cent quarante-sept, une par dépense.

[CLICK]
"Une table croisée, c'est un groupby à deux clés, présenté en grille."

If anyone knows spreadsheets, say it: c'est le tableau croisé dynamique
d'Excel, en une ligne de code.
-->

---
layout: default
class: nl-deck
---

# `merge`, `join` & `concat`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Two tables, one result</div>

```python
budget = pd.DataFrame({
    "categorie": ["Courses", "Logement"],
    "plafond": [900, 1700]})

df.merge(budget, on="categorie", how="left")
pd.concat([janvier, fevrier])      # rows
pd.concat([a, b], axis=1)          # columns
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> The how argument</div>

<div class="nl-recap mt-2">
  <div class="n">inner</div><div><span class="why">only keys found in both</span></div>
  <div class="n">left</div><div><span class="why">every row of the left table</span></div>
  <div class="n">outer</div><div><span class="why">every key from either side</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

`merge` matches column values, like a SQL JOIN; `join` matches the index. The
left merge keeps all 247 rows; the others get NaN.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>merge</code> on columns, <code>join</code> on the index, <code>concat</code> to stack
</div>

<!--
SLIDE 15 - merge, join, concat
On screen ~60 seconds. Concept slide, no live coding needed.

"Un petit tableau de budget : un plafond pour les courses et le logement. On
le colle aux dépenses par la colonne catégorie."

Read the recap: inner ne garde que les catégories présentes des deux côtés.
left garde toutes les dépenses, et celles sans budget reçoivent NaN. outer
garde tout.

PAUSE.

Callback to chapter nine, sqlite3: merge, c'est un JOIN SQL. join fait la
même chose, mais sur l'index.

concat, last: empiler janvier et février, ligne par ligne. Avec axis égale
un, côte à côte - et c'est l'index qui aligne les lignes.

[CLICK]
"merge sur des colonnes, join sur l'index, concat pour empiler."
-->

---
layout: default
class: nl-deck
---

# Time Series

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Dates as the index</div>

```python
df["date"] = pd.to_datetime(df["date"])
s = df.set_index("date")["montant"]
s.resample("ME").sum()     # 5308.39
w = s.resample("W").sum()  # 1741.86, ...
w.pct_change()             # nan, -0.526, ...
s.resample("D").sum().rolling(7).mean()
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> By any period</div>

With a `DatetimeIndex`, `resample` regroups by day, week or month-end.
`rolling(7)` averages a sliding week; `shift(1)` moves values one period.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> 'M' is gone</div>

<div style="font-size: 1.05rem">

pandas 3 raises on `resample("M")`: "'M' is no longer supported for offsets.
Please use 'ME' instead."

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Put dates in the index, then <code>resample</code> by any period
</div>

<!--
SLIDE 16 - Time series
On screen ~60 seconds. Concept slide, no live coding needed.

"Les dates deviennent l'index. Et à partir de là, resample regroupe par
période, comme un groupby sur le calendrier."

Read the numbers: le mois entier, 5308,39. Par semaine : mille sept cent
quarante et un la première - le loyer est tombé le trois janvier - puis
huit cent vingt-cinq. pct_change : moins cinquante-trois pour cent d'une
semaine à l'autre.

PAUSE.

rolling sept : la moyenne sur une semaine glissante, jour après jour. shift :
la valeur de la période précédente, pour comparer.

[CLICK]
"Les dates dans l'index, puis resample, sur n'importe quelle période."

Time-sensitive: depuis pandas 3, l'alias M pour « fin de mois » lève une
erreur. Écrivez ME. Même chose pour Q, devenu QE, et Y, devenu YE.
-->

---
layout: default
class: nl-deck
---

# Reading & Writing Files

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="download" /> Out, and back in</div>

```python
df.to_csv("out.csv", index=False)
df.to_parquet("depenses.parquet")
pd.read_parquet("depenses.parquet")
pd.read_json("depenses.json")
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Three formats</div>

<div class="nl-recap mt-2">
  <div class="n">CSV</div><div><span class="why">text, readable, no types — chapter 06</span></div>
  <div class="n">JSON</div><div><span class="why">nested data, APIs</span></div>
  <div class="n">Parquet</div><div><span class="why">columnar, compressed, keeps dtypes</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

Parquet needs `pyarrow` installed, and keeps the date type that a CSV turns
back into text. Without `index=False`, `to_csv` adds a column.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
CSV to exchange, Parquet to keep
</div>

<!--
SLIDE 17 - Files
On screen ~50 seconds. Concept slide, no live coding needed.

Callback to chapter six: un CSV, c'est du texte. Les types disparaissent à
l'écriture. On relit le fichier, et les dates sont redevenues des chaînes.

"Parquet garde les types. Les dates restent des dates, les nombres restent
des nombres. Et c'est compressé, colonne par colonne. C'est le format des
pipelines de données - et c'est ce que lisent Polars et DuckDB dans un
instant."

PAUSE.

The small trap: sans index égale False, to_csv écrit l'index comme une
colonne de plus. Relisez le fichier, et vous avez une colonne « Unnamed: 0 ».

[CLICK]
"CSV pour échanger. Parquet pour conserver."
-->

---
layout: default
class: nl-deck
---

# Pandas Pitfalls

<div class="nl-cols mt-4" style="font-size: 1.05rem">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Chained assignment</div>

`df["a"][0] = x` changes a copy; pandas 3 only warns.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> map with a dict</div>

Every value missing from the dict becomes NaN.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> A pandas 2 tutorial</div>

`object` dtype, `resample("M")`, `SettingWithCopyWarning`.

</div>

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> Assign on the DataFrame</div>

`df.loc[row, col] = x`, or `df["col"] = values`.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> replace, or map then fillna</div>

Keep the values you did not mean to change.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Check the version first</div>

`pd.__version__`: these notes are pandas 3.

</div>

</div>

<div v-click class="nl-statement mt-3">
Most pandas bugs return a plausible table — check it before you trust it
</div>

<!--
SLIDE 18 - Pitfalls
On screen ~60 seconds. Close pandas on its mistakes, before the two newcomers.

Read the left column, then the right, pair by pair. Ten seconds each.

"Une affectation enchaînée : elle modifie une copie, et pandas 3 se contente
d'un avertissement. map avec un dictionnaire : tout ce qui manque devient
NaN. Un tutoriel pandas 2 : object, M, SettingWithCopyWarning - trois signes
qu'il est daté."

PAUSE.

[CLICK]
"La plupart des bugs pandas renvoient une table qui a l'air correcte.
Vérifiez-la avant de lui faire confiance : shape, info, isnull, et un coup
d'œil aux valeurs."

Callback to chapter twelve: même famille que les pièges NumPy. Le code tourne,
le résultat est plausible, et il est faux.

Then the transition to the last two slides:
"pandas a aussi des limites, qui ne sont pas des bugs : la vitesse et la
taille. Deux outils récents y répondent. Juste une présentation aujourd'hui."
-->


---
layout: default
class: nl-deck
---

# Polars

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> The problem it solves</div>

<div style="font-size: 1.05rem">

pandas runs each step as soon as it is written, mostly on one core. On files
of several gigabytes, it gets slow, and memory runs out.

</div>

<div class="nl-type mt-3"><NlIcon name="file" /> An example: the same totals</div>

```python
top = (pl.scan_csv("depenses_janvier.csv")
         .group_by("categorie")
         .agg(pl.col("montant").sum())
         .sort("montant", descending=True)
         .collect())
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> How it answers</div>

<div class="nl-recap mt-2">
  <div class="n">Rust core</div><div><span class="why">multithreaded, columnar (Arrow)</span></div>
  <div class="n">scan_csv</div><div><span class="why">a LazyFrame: a plan, not data</span></div>
  <div class="n">collect()</div><div><span class="why">optimises the plan, then runs it</span></div>
  <div class="n">pl.col()</div><div><span class="why">expressions instead of lambdas</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

`to_pandas()` and `pl.from_pandas()` cross over. Covered in depth in a later
video.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Polars answers speed and size — it plans the whole query, then uses every core
</div>

<!--
SLIDE 19 - Polars
On screen ~50 seconds. Introduction only: the problem it solves, and a
promise. Concept slide, no live coding needed.

Name the problem first:
"pandas exécute chaque étape dès qu'on l'écrit, et surtout sur un seul cœur.
Sur notre petit fichier de janvier, aucune importance. Sur plusieurs
gigaoctets, c'est lent, et la mémoire ne suffit plus. C'est le problème que
Polars résout."

The example, quickly: même résultat que pandas - Logement, Courses,
Restaurant. scan_csv ne lit rien, il construit un plan ; collect l'optimise et
l'exécute sur tous les cœurs. La paresse du chapitre dix, appliquée à une
requête entière.

PAUSE.

[CLICK]
"Polars répond à la vitesse et à la taille : il planifie toute la requête,
puis il utilise tous les cœurs."

Make the promise, and keep it short:
"On y consacrera une vidéo complète plus tard. Pour aujourd'hui, retenez le
nom, et le problème qu'il résout."

Time-sensitive: Polars 2.0 vient de sortir. Vérifiez la syntaxe sur la
version installée avant d'enregistrer.
-->

---
layout: default
class: nl-deck
---

# DuckDB

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> The problem it solves</div>

<div style="font-size: 1.05rem">

You think in SQL and your data sits in files. A database server is heavy for
one question, and sqlite3 is built for transactions, not big aggregations.

</div>

<div class="nl-type mt-3"><NlIcon name="server" /> An example: SQL on a file</div>

```python
duckdb.sql("""
  SELECT categorie, round(sum(montant), 2)
  FROM 'depenses_janvier.csv'
  GROUP BY 1 ORDER BY 2 DESC LIMIT 3
""").fetchall()
duckdb.sql("SELECT count(*) FROM df")
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> How it answers</div>

<div class="nl-recap mt-2">
  <div class="n">files</div><div><span class="why">SQL straight on CSV, Parquet, JSON</span></div>
  <div class="n">DataFrames</div><div><span class="why">a pandas or Polars variable is a table</span></div>
  <div class="n">S3</div><div><span class="why">the httpfs extension reads s3:// paths</span></div>
  <div class="n">windows</div><div><span class="why">OVER (...) aggregations at scale</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

An analytical database inside your process. Covered in depth in a later
video.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
DuckDB answers SQL without a server — it queries your files and DataFrames where they are
</div>

<!--
SLIDE 20 - DuckDB
On screen ~50 seconds. Introduction only: the problem it solves, and a
promise. Concept slide, no live coding needed.

Name the problem first, with the chapter nine callback:
"Vous pensez en SQL, et vos données sont dans des fichiers. Monter un serveur
de base de données pour une seule question, c'est lourd. Et sqlite3, au
chapitre neuf, est fait pour des transactions, pas pour additionner des
millions de lignes. C'est le problème que DuckDB résout."

The example: du SQL directement sur le CSV de janvier, sans l'importer. Même
résultat que pandas et Polars. Et df, la variable pandas, se lit comme une
table.

PAUSE.

The curriculum asks "does it replace Spark?" - answer it honestly, in one
sentence: pour des données qui tiennent sur une seule machine, DuckDB évite
souvent de sortir Spark ; au-delà, Spark reste l'outil.

[CLICK]
"DuckDB répond au SQL sans serveur : il interroge vos fichiers et vos
DataFrames là où ils sont."

Make the promise:
"Lui aussi aura sa vidéo. Pour aujourd'hui : si vous pensez en SQL, DuckDB ;
en méthodes enchaînées, Polars. Et les deux lisent le même Parquet."

Time-sensitive: DuckDB 1.5.6 aujourd'hui ; la version 2.0 est annoncée pour
la fin octobre 2026.
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 14 — DATA VISUALIZATION</strong>

</div>

<!--
SLIDE 21 - Closing card
On screen ~12 seconds.

One sentence of chapter summary before the sign-off:
"Des colonnes avec des noms, des étiquettes qui s'alignent toutes seules, et
une affectation qui passe par loc."

Say the next chapter's topic out loud while this is up: chapitre quatorze,
la visualisation de données - ces mêmes dépenses, en graphiques.
Then: "À mardi." Hold two beats of silence before you stop recording.
-->
