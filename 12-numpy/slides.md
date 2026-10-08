---
theme: ../themes/noonlabs
title: NumPy — Chapter 12
info: NoonLabs - Module I, chapitre 12
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

<div class="nl-eyebrow">Chapter 12</div>

# NumPy

<div class="mt-4" style="max-width: 42ch">

Whole arrays of numbers in one operation, the base layer of data science and AI in Python

</div>

<div class="nl-type mt-6">
  <NlIcon name="cells" /> Arrays
  <span class="mx-3">·</span>
  <NlIcon name="split" /> Broadcasting
  <span class="mx-3">·</span>
  <NlIcon name="layers" /> Linear algebra
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~8 seconds.

"Chapitre douze. Le premier pas vers le calcul numérique et l'IA, comme
promis. Tout ce qui vient ensuite - pandas, scikit-learn, PyTorch - repose
sur ce qu'on voit aujourd'hui."

Restate the format so nobody wonders:
"Les diapositives, c'est pour les concepts. Le code, on l'écrit ensemble
dans VS Code."
-->

---
layout: default
class: nl-deck
---

# Why NumPy: Vectorization

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> The same sum, twice</div>

```python
import numpy as np

data = [i * 0.5 for i in range(1_000_000)]
arr = np.array(data)

sum(x * x for x in data)    # a Python loop
(arr * arr).sum()           # one expression
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="arrow" /> One operation, a million numbers</div>

`arr * arr` multiplies every element in compiled C. No Python bytecode and no
type check per element: on the build machine, about ten times faster.

<div class="nl-type mt-3"><NlIcon name="box" /> Why it can</div>

<div style="font-size: 1.05rem">

An array holds raw numbers of one type, side by side in memory — not a list
of pointers to Python objects.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Write the operation once for the whole array — NumPy runs the loop in C
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 3 - Vectorization
On screen ~60 seconds.

Pay off a line from chapter three, the nested loops slide:
"Au chapitre trois, sur les boucles imbriquées, il y avait une ligne :
« sur des grilles de nombres, passez à NumPy ». On y est."

Time both lines live with perf_counter, chapter nine. Read your own numbers:
on the build machine, about thirty-five milliseconds for the loop, about
three for NumPy. The two sums agree.

PAUSE.

"Ce n'est pas que Python soit lent. C'est que la boucle tourne en C, une
seule fois, sur des nombres rangés côte à côte. Pas un objet Python par
élément."

Callback to chapter eleven: au chapitre onze, on mesurait la mémoire de cent
mille objets. Un tableau NumPy, c'est l'inverse : pas d'objet par élément,
juste des octets.

[CLICK]
"Écrivez l'opération une fois, pour tout le tableau. NumPy fait la boucle en
C."

Time-sensitive: the speed-up depends on the machine and the NumPy version.
Say "environ dix fois" only if your run agrees.
-->

---
layout: default
class: nl-deck
---

# Creating Arrays

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Five constructors</div>

```python
np.zeros((2, 3))      # 2 rows of 0.0
np.ones(3)            # three 1.0
np.eye(2)             # identity matrix
np.arange(0, 10, 2)   # 0 2 4 6 8
np.linspace(0, 1, 5)  # 5 points, end included
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> A float step</div>

```python
>>> np.arange(1, 1.3, 0.1)
array([1. , 1.1, 1.2, 1.3])
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="split" /> Step or count</div>

`arange` counts by a step and stops before the end, like `range` in chapter
03. `linspace` takes a number of points and includes the end.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> Why 1.3 is there</div>

<div style="font-size: 1.05rem">

0.1 is not exact in binary (chapter 02), so the stop slips. For fractional
steps, use `linspace`.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>arange</code> for integer steps, <code>linspace</code> for anything fractional
</div>

<!--
SLIDE 4 - Creating arrays
On screen ~55 seconds. Concept slide, no live coding needed.

Read the five constructors quickly. zeros et ones pour réserver un tableau,
eye pour la matrice identité, arange et linspace pour des suites. Random
aura sa propre diapositive.

Then the trap, slowly, because nobody expects it:
"arange de un à un virgule trois, par pas de zéro virgule un. La fin est
exclue, comme range. Et pourtant, un virgule trois est dans le résultat."

PAUSE.

"Zéro virgule un n'est pas exact en binaire - chapitre deux. Les erreurs
s'additionnent, et la borne de fin glisse. Quatre éléments au lieu de trois."

[CLICK]
"arange pour des pas entiers. linspace dès que le pas est fractionnaire :
vous donnez le nombre de points, et la fin est incluse exactement."
-->

---
layout: default
class: nl-deck
---

# Array Attributes

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> Ask the array</div>

```python
>>> a = np.zeros((3, 4))
>>> a.shape, a.ndim, a.dtype
((3, 4), 2, dtype('float64'))
>>> a.itemsize, a.nbytes
(8, 96)
>>> np.arange(4).sum()
np.int64(6)
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Five attributes</div>

<div class="nl-recap mt-2">
  <div class="n">shape</div><div><span class="why">the size along each axis</span></div>
  <div class="n">ndim</div><div><span class="why">the number of axes</span></div>
  <div class="n">dtype</div><div><span class="why">one type for every element</span></div>
  <div class="n">itemsize</div><div><span class="why">bytes per element</span></div>
  <div class="n">nbytes</div><div><span class="why">itemsize times the element count</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

Since NumPy 2.0, one value prints with its type: `np.int64(6)`, not `6`.
Older tutorials show the bare number.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>shape</code> and <code>dtype</code> tell you almost everything about an array
</div>

<!--
SLIDE 5 - Attributes
On screen ~50 seconds. Concept slide, no live coding needed.

Read the recap against the code: trois lignes, quatre colonnes, deux axes,
des float64. Huit octets par élément, douze éléments, quatre-vingt-seize
octets.

"Quand un calcul NumPy vous surprend, regardez d'abord shape et dtype. Neuf
fois sur dix, la réponse est là."

PAUSE.

The NumPy 2 point, because they will meet the old style online:
"Et remarquez la dernière ligne : np.int64 de six. Depuis NumPy 2.0, une
valeur seule s'affiche avec son type. Si un tutoriel affiche juste six, il
date d'avant 2024."

[CLICK]
"shape et dtype vous disent presque tout d'un tableau."
-->

---
layout: default
class: nl-deck
---

# Data Types & `astype`

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Fixed size, silent wrap</div>

```python
>>> np.array([200], dtype=np.uint8) + 100
array([44], dtype=uint8)
>>> np.array([2**62]) * 4
array([0])
>>> 2**62 * 4
18446744073709551616
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> No error, no warning</div>

A `uint8` holds 0 to 255: 300 wraps to 44. An `int64` wraps too. Python's own
`int` never overflows, as in chapter 02.

<div class="nl-type mt-3"><NlIcon name="check" /> astype converts</div>

<div style="font-size: 1.05rem">

`astype(int)` truncates: `[1.7, -1.7]` becomes `[1, -1]`. `astype(float)`
parses strings, like `float()` in chapter 02.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A NumPy integer has a fixed size — and overflows without a word
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 6 - Data types
On screen ~60 seconds.

Callback to chapter two, where Python integers were unbounded:
"Au chapitre deux, un entier Python n'avait pas de limite. Deux puissance
soixante-deux, fois quatre : Python vous donne le nombre exact. Vingt
chiffres."

Type the two NumPy lines live:
"NumPy : zéro. Pas d'erreur, pas d'avertissement. Un entier NumPy a une
taille fixe - soixante-quatre bits - et quand il déborde, il recommence à
zéro."

PAUSE.

"Et avec uint8, la limite est à deux cent cinquante-cinq. Deux cents plus
cent, quarante-quatre. C'est le type des pixels d'une image : une
luminosité qu'on augmente trop revient au noir."

[CLICK]
"Un entier NumPy a une taille fixe. Et il déborde sans prévenir."

astype in one breath: astype int tronque vers zéro, astype float lit des
chaînes. Time-sensitive: depuis NumPy 2.0, un scalaire Python garde le type
du tableau - un uint8 plus cent reste un uint8. C'est la règle NEP 50.
-->

---
layout: default
class: nl-deck
---

# Reshape, Flatten, Transpose

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Same numbers, new shape</div>

```python
>>> m = np.arange(6).reshape(2, 3)
>>> m.reshape(3, -1).shape
(3, 2)
>>> m.T.shape
(3, 2)
>>> np.arange(3)[:, np.newaxis].shape
(3, 1)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> What each does</div>

`reshape` reads the same numbers along new axes; `-1` means "work this one
out". `.T` swaps the axes. `np.newaxis` adds an axis of size 1.

<div class="nl-type mt-3"><NlIcon name="split" /> ravel or flatten</div>

<div style="font-size: 1.05rem">

Both give one dimension: `ravel` returns a view when it can, `flatten`
always copies. Never assign to `.shape`: deprecated in NumPy 2.5.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Reshaping never changes the numbers — only the axes they are read along
</div>

<!--
SLIDE 7 - Reshape
On screen ~55 seconds. Concept slide, no live coding needed.

"Six nombres. Deux lignes de trois, ou trois lignes de deux : ce sont les
mêmes six nombres, lus différemment. reshape ne recopie rien."

Point at the minus one: « débrouille-toi ». Vous donnez trois lignes, NumPy
calcule le nombre de colonnes.

PAUSE.

np.newaxis in one sentence: une colonne à partir d'une ligne. On s'en sert
dans deux diapositives, pour le broadcasting.

[CLICK]
"Changer la forme ne change jamais les nombres. Seulement les axes le long
desquels on les lit."

ravel versus flatten is a preview of the views slide: ravel partage la
mémoire quand il peut, flatten copie toujours. Time-sensitive: depuis NumPy
2.5, modifier .shape directement est déprécié. Utilisez reshape.
-->

---
layout: default
class: nl-deck
---

# Indexing & Slicing

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Rows, columns, picks</div>

```python
>>> m = np.arange(6).reshape(2, 3)
>>> m[1, 2], m[:, 1]
(np.int64(5), array([1, 4]))
>>> np.arange(10)[[1, 3, 5]]
array([1, 3, 5])
>>> a = np.arange(6)
>>> s = a[2:4]; s[0] = 99
>>> a
array([ 0,  1, 99,  3,  4,  5])
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> One index per axis</div>

`m[1, 2]` is row 1, column 2, with a comma, not `m[1][2]`. A colon takes the
whole axis: `m[:, 1]` is the second column.

<div class="nl-type mt-3"><NlIcon name="split" /> Fancy indexing</div>

<div style="font-size: 1.05rem">

A list of positions picks exactly those elements, in that order.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Index every axis at once, with commas — <code>m[row, col]</code>
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 8 - Indexing. This is the chapter's PLANT.
On screen ~60 seconds.

Callback to chapter five, slicing mastery: les tranches marchent comme sur
les listes, avec une virgule entre les axes. m de un, deux : ligne un,
colonne deux. m de deux-points, un : toute la deuxième colonne.

Fancy indexing in one breath: une liste de positions, et NumPy prend
exactement ces éléments.

PAUSE.

Now type the last three lines live, and react to the result:
"Je prends une tranche de a. Je modifie la tranche. Et je regarde a..."

"Quatre-vingt-dix-neuf. Dans a. Je n'ai jamais touché a."

[CLICK]

PLANT the payoff and do not explain it:
"Retenez-le : je modifie la tranche, et le tableau d'origine a changé. En
NumPy, couper ne copie pas. On y revient dans deux diapositives."
-->

---
layout: default
class: nl-deck
---

# Boolean Masks & `np.where`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> A comparison is an array</div>

```python
>>> v = np.array([1, 5, 3, 8, 2])
>>> v[v > 2]
array([5, 3, 8])
>>> v[(v > 2) & (v < 6)]
array([5, 3])
>>> np.where(v > 2, v, 0)
array([0, 5, 3, 8, 0])
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> The mask</div>

`v > 2` is an array of `True` and `False`. Used as an index, it keeps the
`True` positions. `np.where(cond, a, b)` is an element-wise if/else.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> &, |, and parentheses</div>

<div style="font-size: 1.05rem">

`and`, and `v > 2 & v < 6` without parentheses, both raise: "The truth value
of an array with more than one element is ambiguous".

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A comparison makes a mask; a mask selects — with <code>&amp;</code>, <code>|</code> and parentheses
</div>

<!--
SLIDE 9 - Boolean masks and where
On screen ~60 seconds. Concept slide, no live coding needed.

"v plus grand que deux ne renvoie pas vrai ou faux. Il renvoie un tableau de
vrais et de faux, un par élément. Et ce tableau sert d'index : on garde les
positions vraies."

The trap, because every beginner hits it in the first hour:
"Pour combiner deux conditions, le and du chapitre deux ne marche pas. Il
faut l'esperluette. Et des parenthèses autour de chaque condition, parce
que l'esperluette passe avant la comparaison."

PAUSE.

np.where as chapter three's if/else, applied to every element at once: là où
la condition est vraie, v ; sinon, zéro.

[CLICK]
"Une comparaison fabrique un masque. Un masque sélectionne. Avec
esperluette, barre verticale, et des parenthèses."
-->

---
layout: default
class: nl-deck
---

# Views vs Copies

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> Ask, do not guess</div>

```python
>>> np.shares_memory(a, a[2:4])
True
>>> np.shares_memory(a, a[[2, 3]])
False
>>> safe = a[2:4].copy()
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Which is which</div>

<div class="nl-recap mt-2">
  <div class="n">a[2:4]</div><div><span class="why">a view: same memory</span></div>
  <div class="n">reshape, .T</div><div><span class="why">views when possible</span></div>
  <div class="n">a[[2, 3]]</div><div><span class="why">fancy indexing: a copy</span></div>
  <div class="n">a[a > 2]</div><div><span class="why">a boolean mask: a copy</span></div>
  <div class="n">.copy()</div><div><span class="why">always a copy</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

In chapter 05, a list slice copied. A NumPy slice does not.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A slice is a view — edit it and you edit the original
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 10 - Views vs copies. This is the chapter's PAYOFF.
On screen ~60 seconds.

Then land the payoff planted on the indexing slide. Do this live:
"Souvenez-vous du quatre-vingt-dix-neuf apparu tout seul dans a. La tranche
était une vue : la même mémoire, un autre regard."

Type shares_memory on the slice, then on the fancy index:
"La tranche partage la mémoire : True. L'indexation par liste en fabrique
une nouvelle : False."

PAUSE.

The chapter five callback, said plainly:
"Au chapitre cinq, une tranche de liste copiait. En NumPy, non. C'est voulu :
copier un tableau d'un million d'éléments à chaque tranche serait
ruineux."

[CLICK]
"Une tranche est une vue. La modifier, c'est modifier l'original."

The rule to take away: si vous devez modifier un morceau sans toucher
l'original, copy. Et en cas de doute, np.shares_memory répond.
-->

---
layout: default
class: nl-deck
---

# Element-wise Operations & ufuncs

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Every element at once</div>

```python
>>> a = np.array([1, 4, 9])
>>> a + 1, a * a
(array([ 2,  5, 10]), array([ 1, 16, 81]))
>>> np.sqrt(a)
array([1., 2., 3.])
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Operators and ufuncs</div>

`+`, `*`, `**` and `<` work element by element. `np.sqrt`, `np.exp` and
`np.log` are ufuncs: the same idea, as functions.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> np.vectorize is not vectorization</div>

<div style="font-size: 1.05rem">

Its own documentation says it: "essentially a for loop". The call looks
vectorized; the speed is a Python loop's.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Element-wise by default — and <code>np.vectorize</code> is still a Python loop
</div>

<!--
SLIDE 11 - Element-wise operations
On screen ~55 seconds. Concept slide, no live coding needed.

"Chaque opérateur travaille élément par élément. a plus un ajoute un à chaque
élément. a fois a, ce n'est pas un produit de matrices : c'est le carré de
chaque élément. Le produit de matrices, c'est l'arobase, plus loin."

The ufuncs: sqrt, exp, log. Les fonctions de math du chapitre neuf, mais pour
un tableau entier.

PAUSE.

The trap, with the documentation as the authority:
"np.vectorize a un nom trompeur. Sa propre documentation le dit : c'est
essentiellement une boucle for. Pratique, pas rapide. Si vous voulez de la
vitesse, écrivez l'expression avec des opérations de tableau."

[CLICK]
"Élément par élément, par défaut. Et np.vectorize reste une boucle Python."
-->

---
layout: default
class: nl-deck
---

# Broadcasting

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> A column plus a row</div>

```python
>>> col = np.arange(3).reshape(3, 1)
>>> row = np.arange(4)
>>> col + row
array([[0, 1, 2, 3],
       [1, 2, 3, 4],
       [2, 3, 4, 5]])
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> The rule</div>

<div class="nl-recap mt-2">
  <div class="n">(3, 1) + (4,)</div><div><span class="why">→ (3, 4)</span></div>
  <div class="n">(3,) + (4,)</div><div><span class="why">ValueError</span></div>
  <div class="n">array + 10</div><div><span class="why">10 reaches every element</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

Compare shapes from the right. Two sizes fit if they are equal, or if one of
them is 1. A missing axis counts as 1.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Shapes are compared from the right — equal, or 1, or it fails
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 12 - Broadcasting
On screen ~65 seconds.

Start with the simplest case, which they already used: un tableau plus dix.
Le dix est « étiré » sur tous les éléments. C'est du broadcasting.

Then build the table live, column plus row:
"Une colonne de trois, une ligne de quatre. NumPy étire la colonne vers la
droite et la ligne vers le bas. Résultat : une grille de trois sur quatre.
Une table d'addition, sans boucle - la table de multiplication du chapitre
trois, en une ligne."

PAUSE.

Then show the failure: arange trois plus arange quatre. ValueError :
« operands could not be broadcast together with shapes (3,) (4,) ».

"La règle tient en une phrase. On compare les formes en partant de la
droite. Deux tailles vont ensemble si elles sont égales, ou si l'une vaut
un. Trois et quatre : ni égales, ni un. Erreur."

[CLICK]
"On compare les formes depuis la droite. Égales, ou un, ou ça échoue."
-->

---
layout: default
class: nl-deck
---

# Aggregation Along Axes

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Two rows, three columns</div>

```python
>>> g = np.array([[1, 2, 3], [4, 5, 6]])
>>> g.sum()
np.int64(21)
>>> g.sum(axis=0)
array([5, 7, 9])
>>> g.sum(axis=1)
array([ 6, 15])
>>> g.argmax(), g.argmin(axis=1)
(np.int64(5), array([0, 0]))
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> The axis disappears</div>

`axis=0` collapses the rows: one result per column. `axis=1` collapses the
columns: one result per row.

<div class="nl-type mt-3"><NlIcon name="check" /> argmax, keepdims</div>

<div style="font-size: 1.05rem">

`argmax` gives a position, not a value. `keepdims=True` keeps the collapsed
axis as size 1, ready to broadcast back.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>axis</code> names the dimension that disappears
</div>

<!--
SLIDE 13 - Aggregation
On screen ~60 seconds. Concept slide, no live coding needed.

The axis argument confuses everyone, so give them the one sentence that
works:
"axis désigne la dimension qui disparaît. axis égale zéro : les lignes
disparaissent, il reste une valeur par colonne - cinq, sept, neuf. axis
égale un : les colonnes disparaissent, une valeur par ligne - six, quinze."

argmax: une position, pas une valeur. Sans axis, c'est une position dans le
tableau aplati : cinq, le dernier élément.

PAUSE.

keepdims, tied to the previous slide: g moins g.mean axis un, keepdims True.
La moyenne de chaque ligne garde sa forme de colonne, et le broadcasting la
retire de chaque élément de sa ligne. On centre les données en une ligne.

[CLICK]
"axis désigne la dimension qui disparaît."

mean, std, min, max: tous prennent le même argument axis.
-->

---
layout: default
class: nl-deck
---

# Missing Values: NaN

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> It spreads</div>

```python
>>> n = np.array([1.0, np.nan, 3.0])
>>> n.mean()
np.float64(nan)
>>> np.nanmean(n)
np.float64(2.0)
>>> np.nan == np.nan
False
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Not a number</div>

NaN marks a missing float. Any arithmetic with it gives NaN, and it is not
even equal to itself.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Find it, skip it</div>

<div style="font-size: 1.05rem">

`np.isnan` finds it; `nanmean`, `nansum`, `nanmax` skip it. `np.NaN` was
removed in NumPy 2.0: write `np.nan`.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
NaN spreads through every calculation — test it with <code>np.isnan</code>, never <code>==</code>
</div>

<!--
SLIDE 14 - NaN
On screen ~55 seconds. Concept slide, no live coding needed.

This is not in the curriculum, and it is the first thing real data throws at
you. Next chapter's pandas is built on it:
"Une mesure manquante, une cellule vide dans un CSV : en NumPy, c'est NaN.
Not a Number."

Read the mean:
"Une seule valeur manquante, et la moyenne entière devient NaN. NaN se
propage dans tout ce qu'il touche. nanmean l'ignore : deux."

PAUSE.

"Et NaN n'est même pas égal à lui-même. Tester avec double égal ne trouve
rien, jamais. C'est np.isnan."

Callback to chapter two: comme pour les floats, on ne compare pas avec ==.
Pour deux floats proches, np.isclose ; pour NaN, np.isnan.

[CLICK]
"NaN se propage dans tous les calculs. Testez-le avec np.isnan, jamais avec
double égal."

Time-sensitive: np.NaN, avec deux majuscules, a été supprimé dans NumPy 2.0.
Beaucoup de tutoriels l'utilisent encore.
-->

---
layout: default
class: nl-deck
---

# Combining, Sorting & Unique

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Join, order, count</div>

```python
>>> np.concatenate([[1, 2], [3]])
array([1, 2, 3])
>>> np.stack([[1, 2], [3, 4]]).shape
(2, 2)
>>> np.argsort([3, 1, 2])
array([1, 2, 0])
>>> np.unique(["Resto", "Courses", "Resto"],
...           return_counts=True)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Three jobs</div>

`concatenate` joins along an existing axis; `stack` makes a new one.
`argsort` returns the positions that would sort, so you can apply the same
order to another array.

<div class="nl-type mt-3"><NlIcon name="check" /> unique, with counts</div>

<div style="font-size: 1.05rem">

The sorted values and how often each appears: Courses 1, Resto 2. A
`Counter`, from chapter 05, for arrays.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>argsort</code> gives the order — apply it to every array that must stay aligned
</div>

<!--
SLIDE 15 - Combining, sorting, unique
On screen ~55 seconds. Concept slide, no live coding needed.

Three everyday jobs that are not in the curriculum, and that the official
NumPy beginners' guide covers.

concatenate versus stack in one sentence: concatenate colle bout à bout,
stack empile et crée une dimension.

argsort is the useful one:
"argsort ne trie pas. Il vous donne l'ordre. Un, deux, zéro : l'élément en
position un d'abord. Et cet ordre, vous pouvez l'appliquer à un autre
tableau - les noms qui vont avec les montants, par exemple."

PAUSE.

unique with counts: le Counter du chapitre cinq, pour un tableau. Courses
une fois, Resto deux fois.

[CLICK]
"argsort donne l'ordre. Appliquez-le à chaque tableau qui doit rester
aligné."

Time-sensitive: NumPy 2.5 ajoute descending égale True à sort et argsort.
-->

---
layout: default
class: nl-deck
---

# Random with `default_rng`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> One seeded generator</div>

```python
>>> rng = np.random.default_rng(42)
>>> rng.integers(1, 7, size=5)
array([1, 5, 4, 3, 3])
>>> rng.normal(0, 1, size=3).shape
(3,)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Seeded, and yours</div>

`default_rng(42)` builds your own generator: same seed, same numbers.
`integers(1, 7)` excludes 7, like `range`.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> np.random.seed is legacy</div>

<div style="font-size: 1.05rem">

It sets one global state for every module that draws numbers. Pass a
generator around instead.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
One seeded generator per experiment, passed around — not a global seed
</div>

<!--
SLIDE 16 - Random
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter nine, the dice:
"Au chapitre neuf, random.seed quarante-deux, et les dés retombaient
toujours pareil. NumPy fait la même chose, mais pour des tableaux entiers -
et sans état global."

Read the generator line:
"default_rng, avec une graine. Vous obtenez votre propre générateur. Et
integers de un à sept exclut le sept, comme range : un dé à six faces."

PAUSE.

"L'ancienne façon, np.random.seed, règle un état unique pour tout le
programme. Une bibliothèque qui tire un nombre au hasard décale tous les
vôtres. Avec un générateur qu'on passe en argument, chaque expérience a le
sien."

[CLICK]
"Un générateur avec sa graine par expérience, qu'on passe en argument. Pas
de graine globale."

Time-sensitive: NumPy ne garantit pas que la même graine donne les mêmes
nombres d'une version à l'autre - la 2.5 a changé le tirage binomial. Pour
reproduire une expérience, notez aussi la version de NumPy.
-->

---
layout: default
class: nl-deck
---

# Statistical Functions

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Same data, two answers</div>

```python
>>> np.median([13.16, 5.5, 23.62])
np.float64(13.16)
>>> np.percentile([1, 2, 3, 4], 50)
np.float64(2.5)
>>> np.std([1, 2, 3, 4])
np.float64(1.118033988749895)
>>> statistics.stdev([1, 2, 3, 4])
1.2909944487358056
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> Two standard deviations</div>

`np.std` divides by n: the population, `ddof=0`. `statistics.stdev` divides
by n − 1: a sample. `np.std(x, ddof=1)` matches it.

<div class="nl-type mt-3"><NlIcon name="layers" /> And more</div>

<div style="font-size: 1.05rem">

`median`, `percentile`, `var`, and `corrcoef` for how two series move
together.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Check <code>ddof</code> — <code>np.std</code> and <code>statistics.stdev</code> disagree by default
</div>

<!--
SLIDE 17 - Statistics
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter nine, statistics: la médiane de treize seize, cinq
cinquante et vingt-trois soixante-deux. Treize seize, comme au chapitre neuf.
Même réponse.

Then the trap, which costs people real time:
"Écart type des mêmes quatre nombres. NumPy : un virgule un un huit. Le
module statistics : un virgule deux neuf. Les deux ont raison."

PAUSE.

"NumPy divise par n : l'écart type de la population. statistics divise par
n moins un : l'écart type d'un échantillon. ddof égale un, et NumPy donne la
même réponse."

[CLICK]
"Vérifiez ddof. np.std et statistics.stdev ne sont pas d'accord par défaut."

corrcoef in one line: un pour deux séries qui montent exactement ensemble,
moins un pour deux séries opposées.
-->

---
layout: default
class: nl-deck
---

# Linear Algebra

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Solve Ax = b</div>

```python
>>> A = np.array([[2., 1.], [1., 3.]])
>>> b = np.array([3., 5.])
>>> np.linalg.solve(A, b)
array([0.8, 1.4])
>>> A @ np.linalg.solve(A, b)
array([3., 5.])
>>> np.linalg.det(A)
np.float64(5.000000000000001)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> @ is the matrix product</div>

`*` stays element-wise. `solve` is faster and more accurate than
`inv(A) @ b`. `det` is a float computation: compare it with `isclose`.

<div class="nl-type mt-3"><NlIcon name="split" /> eigvals, since NumPy 2.5</div>

<div style="font-size: 1.05rem">

It always returns complex numbers. For a symmetric matrix, `eigvalsh`
returns reals.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>@</code> multiplies matrices — and <code>solve</code> beats <code>inv</code> for Ax = b
</div>

<!--
SLIDE 18 - Linear algebra
On screen ~65 seconds. Concept slide, no live coding needed.

The arobase first, tied to the element-wise slide:
"L'étoile multiplie élément par élément. L'arobase, c'est le produit de
matrices. Deux symboles, deux opérations différentes."

Then solve, as two equations: deux x plus y égale trois, x plus trois y
égale cinq. solve répond zéro virgule huit et un virgule quatre. Et A fois
la solution redonne trois et cinq.

PAUSE.

"Pour résoudre, on ne calcule pas l'inverse. solve est plus rapide et plus
précis. Et le déterminant vaut cinq virgule zéro zéro zéro... un. Un calcul
en flottants, chapitre deux : on compare avec isclose."

[CLICK]
"L'arobase multiplie des matrices. Et pour Ax égale b, solve bat inv."

Time-sensitive, worth ten seconds because it breaks existing code: depuis
NumPy 2.5, eigvals renvoie toujours des nombres complexes. Pour une matrice
symétrique - une matrice de covariance, par exemple - eigvalsh renvoie des
réels. inv d'une matrice singulière lève LinAlgError, « Singular matrix ».
-->

---
layout: default
class: nl-deck
---

# Saving & Loading

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="download" /> Binary in, binary out</div>

```python
np.save("scores.npy", arr)
arr = np.load("scores.npy")

np.savez("run.npz", x=x, y=y)
np.load("run.npz")["x"]

np.loadtxt("depenses.csv", delimiter=",",
           skiprows=1, usecols=2)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> .npy and .npz</div>

`.npy` keeps the dtype and the shape exactly. `.npz` bundles several arrays
by name. `np.load` refuses pickled objects unless you allow them.

<div class="nl-type mt-3"><NlIcon name="file" /> Text at the edges</div>

<div style="font-size: 1.05rem">

`loadtxt` reads the montant column of the January CSV: 247 floats. Mixed
columns and missing cells are chapter 13.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>.npy</code> for arrays, text only at the edges of your program
</div>

<!--
SLIDE 19 - Saving and loading
On screen ~50 seconds. Concept slide, no live coding needed.

Not in the curriculum, and every ML project needs it: sauvegarder un
tableau, et le recharger exactement.

".npy garde tout : le type, la forme, chaque octet. Un seul fichier, une
seule lecture. .npz en range plusieurs, chacun sous un nom."

Callback to chapter six, pickle: np.load refuse les objets Python sérialisés
par défaut. C'est le même danger qu'au chapitre six - charger un pickle,
c'est exécuter du code.

PAUSE.

Then loadtxt on the first video's file:
"La colonne des montants de janvier : deux cent quarante-sept nombres. Leur
somme vaut cinq mille trois cent huit virgule trente-huit neuf neuf neuf...
des floats, encore. Pour l'argent exact, c'était Decimal, au chapitre neuf."

[CLICK]
".npy pour les tableaux. Le texte, seulement aux bords du programme."

For a CSV with mixed columns and missing cells, say it: c'est le chapitre
treize, pandas.
-->

---
layout: default
class: nl-deck
---

# NumPy Pitfalls

<div class="nl-cols mt-4" style="font-size: 1.05rem">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Editing a slice</div>

The original changes with it: a slice is a view.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> A small integer dtype</div>

`uint8` or `int32` arithmetic wraps around, silently.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> A NaN in a mean</div>

One missing value, and the whole result is `nan`.

</div>

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> .copy() when it must be independent</div>

Or check with `np.shares_memory`.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> int64 or float64, or check the range</div>

Know the largest value your data can reach.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> np.isnan, and the nan functions</div>

`nanmean`, `nansum`, `nanmax`.

</div>

</div>

<div v-click class="nl-statement mt-3">
NumPy is fast because it trusts you — it will not stop you from any of these
</div>

<!--
SLIDE 20 - Pitfalls
On screen ~60 seconds. Close the chapter on the mistakes, not a summary.

Read the left column, then the right, pair by pair. Ten seconds each.

"Une tranche modifiée : l'original bouge avec elle. Un petit type entier :
il déborde sans rien dire. Un NaN dans une moyenne : tout le résultat
devient NaN."

PAUSE.

[CLICK]
"NumPy est rapide parce qu'il vous fait confiance. Il ne vérifie pas les
débordements, il ne copie pas les tranches, il ne saute pas les valeurs
manquantes. C'est à vous de savoir."

Callback to chapters nine and eleven: même famille d'erreurs - le code tourne
et le résultat est faux. And the tutorial trap, one last time: si un tutoriel
écrit np.NaN ou np.float_, il date d'avant NumPy 2.
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 13 — PANDAS &amp; DATAFRAMES</strong>

</div>

<!--
SLIDE 21 - Closing card
On screen ~12 seconds.

One sentence of chapter summary before the sign-off:
"Une opération pour tout le tableau, une forme qu'on vérifie, et une tranche
qui n'est jamais une copie."

Say the next chapter's topic out loud while this is up: chapitre treize,
pandas et les DataFrames - des tableaux avec des noms de colonnes et des
valeurs manquantes.
Then: "À mardi." Hold two beats of silence before you stop recording.
-->
