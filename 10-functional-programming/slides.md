---
theme: ../themes/noonlabs
title: Functional Programming — Chapter 10
info: NoonLabs - Module I, chapitre 10
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

<div class="nl-eyebrow">Chapter 10</div>

# Functional Programming

<div class="mt-4" style="max-width: 42ch">

Functions as building blocks, and data that flows instead of piling up

</div>

<div class="nl-type mt-6">
  <NlIcon name="check" /> Pure functions
  <span class="mx-3">·</span>
  <NlIcon name="arrow" /> Generators
  <span class="mx-3">·</span>
  <NlIcon name="layers" /> functools
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~8 seconds.

"Chapitre dix. Jusqu'ici, nos fonctions faisaient le travail. À partir de
maintenant, ce sont des pièces qu'on assemble, et les données circulent au
lieu de s'empiler en mémoire."

Restate the format so nobody wonders:
"Les diapositives, c'est pour les concepts. Le code, on l'écrit ensemble
dans VS Code."
-->

---
layout: default
class: nl-deck
---

# Imperative vs Functional

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="arrow" /> Imperative: say how</div>

```python
total = 0
for r in rows:
    if r["categorie"] == "Restaurant":
        total += Decimal(r["montant"])
```

<div class="nl-type mt-2"><NlIcon name="check" /> Functional: say what</div>

```python
total = sum(Decimal(r["montant"])
            for r in rows
            if r["categorie"] == "Restaurant")
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Same answer, two styles</div>

The loop describes the steps, and changes `total` as it goes. The expression
describes the result: no variable to keep in sync.

<div class="nl-type mt-3"><NlIcon name="split" /> Python is not a functional language</div>

<div style="font-size: 1.05rem">

It gives you the functional tools. Use them where they read better, and keep
the loop where it does not.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Imperative says how to get there; functional says what you want
</div>

<!--
SLIDE 3 - Imperative vs functional
On screen ~60 seconds. Concept slide, no live coding needed.

Pay off the promise from the end of chapter nine:
"Au chapitre neuf, je vous ai annoncé la programmation fonctionnelle. On
commence par ce que ça change concrètement : la même question, posée deux
fois."

Read the two versions out loud. Same data as chapter nine, the January
expenses, and the same answer: 880,41 for Restaurant.

"À gauche, je décris les étapes. Je crée une variable, je la modifie à chaque
tour. À droite, je décris le résultat. Il n'y a plus rien à tenir à jour."

PAUSE.

Callback to chapter four: une fonction est une valeur, et sum accepte
n'importe quel itérable. Tout ce chapitre repose là-dessus.

[CLICK]
"L'impératif dit comment y arriver. Le fonctionnel dit ce que vous voulez."

Be honest so nobody becomes a zealot: Python n'est pas un langage
fonctionnel. Il vous donne les outils. Utilisez-les quand ils se lisent mieux,
gardez la boucle sinon.
-->

---
layout: default
class: nl-deck
---

# Pure Functions

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Changes its argument</div>

```python
def add_fee(prices):
    for i, p in enumerate(prices):
        prices[i] = p + 1
    return prices
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Returns something new</div>

```python
def add_fee(prices):
    return [p + 1 for p in prices]
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> What pure means</div>

The result depends only on the arguments, and nothing outside the function
changes. Same input, same output, every time.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> The caller's list changed</div>

<div style="font-size: 1.05rem">

The first version hands back the caller's own list, modified. Anyone else
holding that list now sees the fee too.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Testable in one line, and safe to cache</li>
<li class="nl-bad">Printing, files, globals — keep them at the edges</li>
</ul>

</div>

</div>

<div v-click class="nl-statement mt-3">
Same input, same output, nothing else touched — that is all purity means
</div>

<!--
SLIDE 4 - Pure functions
On screen ~60 seconds.

Callback to chapter four, where "pure where you can" was one line. Today it
gets its slide:
"Au chapitre quatre, j'ai dit : pure quand vous pouvez. Voilà ce que ça veut
dire, précisément."

Read the left side top to bottom:
"La première version modifie la liste qu'on lui donne. Et elle la renvoie,
en plus. Celui qui a appelé la fonction se retrouve avec sa propre liste
changée - et tous ceux qui la partagent aussi."

PAUSE.

"La deuxième fabrique une nouvelle liste. L'originale ne bouge pas."

Callback to chapter five: même liste, deux noms. C'est le modèle mémoire du
chapitre cinq qui rend la première version dangereuse.

[CLICK]
"Mêmes entrées, même sortie, rien d'autre touché. C'est tout ce que veut dire
pur."

Then the honest part: un programme sans effets de bord ne fait rien. Il faut
bien écrire un fichier à la fin. La règle, c'est de les garder au bord, dans
une couche fine.
-->

---
layout: default
class: nl-deck
---

# Immutability in Practice

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="lock" /> A read-only view</div>

```python
>>> from types import MappingProxyType
>>> tva = MappingProxyType({"taux": 20})
>>> tva["taux"] = 0
TypeError: 'mappingproxy' object does
not support item assignment
```

</div>

<div>

<div class="nl-type"><NlIcon name="box" /> Immutable versions</div>

<div class="nl-recap mt-2">
  <div class="n">tuple</div><div><span class="why">an immutable list</span></div>
  <div class="n">frozenset</div><div><span class="why">an immutable set, hashable</span></div>
  <div class="n">frozen dataclass</div><div><span class="why">no field reassignment — chapter 08</span></div>
  <div class="n">MappingProxyType</div><div><span class="why">a read-only view of a dict</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

Immutability is shallow: a tuple or a frozen dataclass holding a list can still
change, and can no longer be hashed.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Data that cannot change cannot change behind your back
</div>

<!--
SLIDE 5 - Immutability
On screen ~55 seconds. Concept slide, no live coding needed.

The other half of purity: if the data cannot change, nobody can change it by
accident.

Read the recap quickly. tuple et frozenset, on les connaît. La dataclass
gelée, c'était le chapitre huit. Le nouveau, c'est MappingProxyType.

"Une vue en lecture seule sur un dictionnaire. Vous la donnez à n'importe
quelle fonction, et elle ne peut rien y modifier. Essayez, et Python lève
une TypeError."

PAUSE.

[CLICK]
"Une donnée qui ne peut pas changer ne peut pas changer dans votre dos."

The caveat, because it surprises people: l'immutabilité est superficielle.
Un tuple qui contient une liste ne peut pas changer de liste, mais la liste,
elle, peut toujours changer. C'est la copie superficielle du chapitre cinq,
vue de l'autre côté.
-->

---
layout: default
class: nl-deck
---

# `map` & `filter`, Deep Dive

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Several iterables, one pass</div>

```python
>>> list(map(pow, [2, 3], [3, 2]))
[8, 9]
>>> m = map(str.upper, ["a", "b"])
>>> list(m), list(m)
(['A', 'B'], [])
>>> list(filter(None, [0, 1, "", 2]))
[1, 2]
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> What the intro left out</div>

`map` takes as many iterables as the function takes arguments, and stops at
the shortest, like `zip`. `filter(None, ...)` keeps the truthy values.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>map(str.upper, names)</code> — the function already exists</li>
<li class="nl-bad"><code>map(lambda x: ..., xs)</code> — a comprehension reads better</li>
</ul>

</div>

</div>

<div v-click class="nl-statement mt-3">
Use <code>map</code> when the function already exists; write a comprehension when it does not
</div>

<!--
SLIDE 6 - map and filter
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter four, where map and filter got one slide:
"Au chapitre quatre, on a vu map et filter en surface. Trois choses qu'on
n'avait pas dites."

One: plusieurs itérables. pow reçoit deux arguments, donc map prend deux
listes et les parcourt ensemble. Deux puissance trois, trois puissance deux.

Two: map est paresseux et se consomme. Le deuxième list est vide - comme zip
au chapitre trois.

Three: filter avec None garde les valeurs vraies. Le zéro et la chaîne vide
disparaissent - la véracité du chapitre deux.

PAUSE.

[CLICK]
"map quand la fonction existe déjà : str.upper, int, float. Dès que vous
écrivez un lambda, la compréhension du chapitre cinq est plus lisible."
-->

---
layout: default
class: nl-deck
---

# `reduce`, and When Not To

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> Fold, two at a time</div>

```python
>>> from functools import reduce
>>> import operator
>>> reduce(operator.add, [1, 2, 3])
6
>>> reduce(operator.add, [])
TypeError: reduce() of empty iterable
with no initial value
>>> reduce(operator.add, [], 0)
0
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> How it folds</div>

`reduce` combines the first two items, then that result with the third, and
so on: `(1 + 2) + 3`.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> Empty input</div>

<div style="font-size: 1.05rem">

Without an initial value, an empty list is an error. With one, the initial
value is the answer for empty input.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Give <code>reduce</code> an initial value — or give it up for a builtin
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 7 - reduce
On screen ~55 seconds.

Read the fold out loud, it makes the mechanism obvious:
"Un plus deux, trois. Trois plus trois, six. reduce plie la liste deux
éléments à la fois."

Then type the empty case live:
"Et sur une liste vide ? TypeError. reduce ne sait pas quoi renvoyer : il n'a
rien à plier."

PAUSE.

"Avec une valeur initiale, zéro, il a sa réponse. C'est le cas qui arrive en
production : un mois sans dépense, un filtre qui ne garde rien."

[CLICK]
"Une valeur initiale à reduce, toujours. Ou mieux : pas de reduce du tout."

Callback to chapter four: sum, min, max, any, all, math.prod. Un nom vaut
mieux qu'un pli. math.prod de deux, trois, quatre donne vingt-quatre, sans
import de functools.
-->

---
layout: default
class: nl-deck
---

# Closures

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> A function that makes functions</div>

```python
def make_tax(rate):
    def apply(amount):
        return amount * (1 + rate)
    return apply

tva = make_tax(Decimal("0.20"))
tva(Decimal("100"))   # Decimal('120.00')
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> What apply remembers</div>

`apply` uses `rate` after `make_tax` has returned. The inner function keeps
that variable alive. The function plus the variables it captured is a closure.

<div class="nl-type mt-3"><NlIcon name="check" /> You can look inside</div>

<div style="font-size: 1.05rem">

`tva.__closure__[0].cell_contents` is `Decimal('0.20')`. A `lambda` captures
its surroundings in exactly the same way.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A closure is a function that remembers the variables around it
</div>

<!--
SLIDE 8 - Closures
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter four, the counter with nonlocal:
"Au chapitre quatre, step gardait son compteur après le retour de counter.
On avait un nom pour ça : une closure. Aujourd'hui, on s'en sert pour
fabriquer des fonctions."

Read the code: make_tax reçoit un taux, et renvoie une fonction qui
l'applique. tva est une fonction neuve, avec vingt pour cent enfermés
dedans. Decimal, comme au chapitre neuf : c'est de l'argent.

PAUSE.

"make_tax a terminé. Sa variable rate devrait avoir disparu. Mais apply en a
besoin, alors Python la garde en vie, attachée à la fonction."

[CLICK]
"Une closure, c'est une fonction qui se souvient des variables autour d'elle."

Show __closure__ only if there is time - it proves the variable is really
stored, not copied into the code.
-->

---
layout: default
class: nl-deck
---

# The Late Binding Gotcha

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Three functions, one answer</div>

```python
>>> fs = [lambda: i for i in range(3)]
>>> [f() for f in fs]
[2, 2, 2]
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Expected 0, 1, 2</div>

Each lambda was created while `i` was 0, then 1, then 2. All three answer 2.
A `def` inside the loop behaves the same.

<div class="nl-type mt-3"><NlIcon name="split" /> Why</div>

<div style="font-size: 1.05rem">

A closure stores the variable, not the value it had. Each lambda looks `i` up
when it is called, and by then the loop has finished: `i` is 2.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A closure captures the variable, not its value
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 9 - Late binding. This is the chapter's PLANT.
On screen ~60 seconds.

Type it live, and ask the question before pressing Enter:
"Trois fonctions. La première a été créée quand i valait zéro, la deuxième
un, la troisième deux. Qu'est-ce qu'elles vont répondre ?"

Enter.

"Deux, deux, deux."

PAUSE.

Explain the mechanism, slowly, because it is the whole slide:
"Une closure ne copie pas la valeur. Elle garde la variable. Chaque lambda
va chercher i au moment où on l'appelle - et à ce moment-là, la boucle est
finie depuis longtemps. i vaut deux."

[CLICK]

PLANT the payoff and do not explain it:
"Trois fonctions, et elles répondent toutes deux. Retenez-le : une closure
capture la variable, pas sa valeur. La solution arrive dans quelques
diapositives."
-->

---
layout: default
class: nl-deck
---

# Generator Functions with `yield`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> A function that pauses</div>

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

>>> g = countdown(3)
>>> next(g), next(g), next(g)
(3, 2, 1)
>>> next(g)
StopIteration
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Out, pause, resume</div>

`yield` hands a value out and pauses the function, local variables intact.
The next `next()` resumes it on the line after the `yield`.

<div class="nl-type mt-3"><NlIcon name="arrow" /> The end</div>

<div style="font-size: 1.05rem">

When the function ends, `next()` raises `StopIteration`, the signal a `for`
loop listens for. `next(g, None)` returns a default instead.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>yield</code> pauses the function — <code>next()</code> resumes it where it stopped
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 10 - Generator functions
On screen ~65 seconds.

Pay off the promise from chapter six:
"Au chapitre six, on a écrit un gestionnaire de contexte avec yield, et je
vous ai dit : ça paraît étrange, on l'explique au chapitre dix. On y est."

Type countdown live, then call next three times, one at a time:
"Trois. La fonction s'est arrêtée sur le yield. Elle attend. Deux. Elle a
repris juste après, a décrémenté n, est revenue au yield. Un."

PAUSE.

"Et la quatrième fois, il n'y a plus rien. StopIteration. C'est exactement le
signal qu'écoute une boucle for, depuis le chapitre trois. Une boucle for
appelle next jusqu'à StopIteration."

[CLICK]
"yield met la fonction en pause. next la reprend là où elle s'était
arrêtée."

next avec une valeur par défaut, en une phrase : au lieu de lever
l'exception, il renvoie la valeur.

One sentence for the curious, and no more: un générateur sait aussi
recevoir des valeurs, avec send. C'est la base d'asyncio, au chapitre onze.
-->

---
layout: default
class: nl-deck
---

# Generator Expressions

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Brackets become parentheses</div>

```python
>>> squares = (x * x for x in range(5))
>>> sum(squares)
30
>>> sum(squares)
0
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> A comprehension that waits</div>

Same syntax as a list comprehension, but nothing is computed until something
asks. Passed straight into a call, the extra parentheses go:
`sum(x * x for x in range(5))`.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> Consumed once</div>

<div style="font-size: 1.05rem">

The first `sum` walked it. The second found it empty, and returned 0 without
a word.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A generator expression is a comprehension that waits — and runs once
</div>

<!--
SLIDE 11 - Generator expressions
On screen ~55 seconds. Concept slide, no live coding needed.

Pay off the promise from chapter five:
"Au chapitre cinq, dans le tableau des compréhensions, les parenthèses
donnaient un générateur, et j'ai dit : on y reviendra. Voilà."

Point at the two sums:
"Trente. Puis zéro. Pas d'erreur. Le générateur a été parcouru par le premier
sum, il est vide."

PAUSE.

Callback to chapter three and chapter nine: c'est la même règle depuis zip au
chapitre trois et itertools au chapitre neuf. Un itérateur se consomme.

[CLICK]
"Une expression génératrice, c'est une compréhension qui attend - et qui ne
sert qu'une fois."

The syntax gift: dans un appel de fonction, les parenthèses en trop
disparaissent. sum de x fois x pour x dans range.
-->

---
layout: default
class: nl-deck
---

# Infinite Sequences & `yield from`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Never ends, never hurts</div>

```python
def ids():
    n = 1
    while True:
        yield f"TX-{n:04d}"
        n += 1

>>> list(islice(ids(), 3))
['TX-0001', 'TX-0002', 'TX-0003']
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> The consumer decides</div>

`while True` is safe in a generator: it only runs as far as someone asks.
`islice` from chapter 09 decides where it stops.

<div class="nl-type mt-3"><NlIcon name="split" /> yield from</div>

<div style="font-size: 1.05rem">

`yield from other()` hands over to another generator until it is exhausted.
One generator built from several, with no inner loop.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
An infinite generator is safe — the consumer decides when to stop
</div>

<!--
SLIDE 12 - Infinite sequences and yield from
On screen ~60 seconds. Concept slide, no live coding needed.

The while True is the point, so say it:
"Une boucle infinie. Dans une fonction normale, votre programme ne rend plus
la main. Dans un générateur, c'est sans danger : il ne produit que ce qu'on
lui demande."

Callback to chapter nine: islice en prend trois, et le reste n'est jamais
calculé. Des identifiants de transaction, à la demande.

PAUSE.

Then yield from:
"Et quand un générateur doit renvoyer tout ce que produit un autre, yield
from. Toutes les lignes de tous les fichiers, en une ligne, sans boucle
imbriquée."

[CLICK]
"Un générateur infini ne fait pas de mal. C'est celui qui consomme qui décide
quand s'arrêter."
-->

---
layout: default
class: nl-deck
---

# Pipelines

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> The January CSV, lazily</div>

```python
with open(path) as f:
    rows = csv.DictReader(f)
    resto = (r for r in rows
             if r["categorie"] == "Restaurant")
    total = sum(Decimal(r["montant"])
                for r in resto)
# Decimal('880.41')
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="arrow" /> One row at a time</div>

Each stage is a generator that pulls one row from the stage before it. The
whole file is never in memory: a row flows through, then the next.

<div class="nl-type mt-3"><NlIcon name="check" /> Add a stage, add a line</div>

<div style="font-size: 1.05rem">

Another filter or conversion is one more generator in the chain, not a rewrite
of the loop.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A pipeline pulls one item at a time through every stage
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 13 - Pipelines
On screen ~65 seconds.

Build it live on the first video's file, one stage at a time, and run it
after each line:
"Le fichier de dépenses de janvier. Étape un : DictReader, chapitre six.
Étape deux : on ne garde que les restaurants. Étape trois : on convertit en
Decimal, chapitre neuf, et on additionne."

"Huit cent quatre-vingts virgule quarante et un. Le même chiffre qu'au
chapitre neuf. Exact."

PAUSE.

"Et pendant tout ce temps, aucune liste. Chaque étape tire une ligne de
l'étape d'avant. Une ligne traverse tout le tuyau, puis la suivante. Ce
fichier aurait pu faire dix gigaoctets."

[CLICK]
"Un pipeline fait passer un élément à la fois à travers toutes les étapes."

One production remark: tout se passe dans le with. Si vous sortez le
générateur du bloc, le fichier est fermé avant d'être lu.
-->

---
layout: default
class: nl-deck
---

# Memory: Generators vs Lists

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> Measure it</div>

```python
>>> import sys
>>> n = range(1_000_000)
>>> sys.getsizeof([x * x for x in n])
8448728
>>> sys.getsizeof((x * x for x in n))
200
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Results or a recipe</div>

The list holds a million results at once, and that figure counts only its
array of pointers. The generator holds its position and a recipe.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Summing, filtering, streaming a file — a generator</li>
<li class="nl-bad">Data you walk twice or index into — that is a list</li>
</ul>

</div>

</div>

<div v-click class="nl-statement mt-3">
A list stores every result; a generator stores where it is
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 14 - Memory
On screen ~60 seconds.

Type both lines live and read the numbers:
"La liste : plus de huit millions d'octets. Le générateur : deux cents.
Pour le même calcul."

PAUSE.

"Et le chiffre de la liste est flatteur : il ne compte que le tableau de
pointeurs. Le million d'entiers vient en plus."

Then the honest price, because a generator is not free:
"Un générateur ne se parcourt qu'une fois. Pas de len, pas d'index. Si vous
avez besoin de relire les données, c'est une liste."

[CLICK]
"Une liste stocke chaque résultat. Un générateur stocke où il en est."

Time-sensitive: these two numbers are CPython 3.12 on a 64-bit machine. Run
verify-facts.py before recording; another version gives other numbers, and
the order of magnitude is what matters.
-->

---
layout: default
class: nl-deck
---

# `groupby` & `accumulate`

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Groups neighbours only</div>

```python
>>> from itertools import groupby
>>> data = ["Resto", "Courses", "Resto"]
>>> [k for k, _ in groupby(data)]
['Resto', 'Courses', 'Resto']
>>> [k for k, _ in groupby(sorted(data))]
['Courses', 'Resto']
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why Resto appears twice</div>

`groupby` starts a new group every time the key changes. Unsorted input gives
the same key twice. Sort by the same key first.

<div class="nl-type mt-3"><NlIcon name="arrow" /> accumulate: running totals</div>

<div style="font-size: 1.05rem">

On the expenses 13.16, 5.5 and 23.62, `accumulate` yields the balance after
each one: 13.16, 18.66, 42.28.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>groupby</code> only groups neighbours — sort by the same key first
</div>

<!--
SLIDE 15 - groupby and accumulate
On screen ~55 seconds. Concept slide, no live coding needed.

These two are not in most courses, and groupby is the one that bites:
"groupby a l'air de faire un GROUP BY de SQL. Ce n'est pas le cas. Il
regroupe les éléments voisins. Dès que la clé change, il ouvre un nouveau
groupe."

Point at the first output: Resto, Courses, Resto. Deux groupes Resto, parce
qu'ils ne se touchaient pas.

PAUSE.

"La règle : on trie par la même clé, puis on groupe. Ou alors, pour compter
et totaliser, le Counter et le defaultdict du chapitre cinq."

[CLICK]
"groupby ne regroupe que les voisins. Triez d'abord, par la même clé."

accumulate in one breath: le solde après chaque dépense. Avec des Decimal,
comme au chapitre neuf, et le total tombe juste.
-->

---
layout: default
class: nl-deck
---

# `partial` & the `operator` Module

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> The value, frozen now</div>

```python
>>> from functools import partial
>>> def show(i): return i
>>> fs = [partial(show, i) for i in range(3)]
>>> [f() for f in fs]
[0, 1, 2]
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> operator: lambdas with names</div>

<div class="nl-recap mt-2">
  <div class="n">itemgetter(1)</div><div><span class="why">lambda r: r[1]</span></div>
  <div class="n">attrgetter("total")</div><div><span class="why">lambda o: o.total</span></div>
  <div class="n">methodcaller("upper")</div><div><span class="why">lambda s: s.upper()</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

`partial` fixes some arguments now and returns a new function. Here it froze
each value of `i` at creation.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>partial</code> binds the value now — a closure looks it up later
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 16 - partial and operator. This is the chapter's PAYOFF.
On screen ~60 seconds.

Then land the payoff planted on the late binding slide. Do this live:
the same three functions, built with partial this time.

"Souvenez-vous des trois lambdas qui répondaient deux, deux, deux. Même
boucle, mais avec partial. Zéro, un, deux."

PAUSE.

"partial fige la valeur au moment où vous l'écrivez - exactement ce que la
closure ne faisait pas. La closure va chercher la variable plus tard.
partial a déjà la valeur."

Give the other fix too, because they will see it in other people's code: un
argument par défaut, lambda i égale i. La valeur par défaut est évaluée à la
création. Même effet, moins lisible.

[CLICK]
"partial lie la valeur maintenant. Une closure la cherche plus tard."

operator in twenty seconds: trois lambdas que vous écrivez tout le temps, déjà
écrites, avec un nom. sorted avec key égale itemgetter, et c'est lisible.
-->

---
layout: default
class: nl-deck
---

# `lru_cache`, `cache` & `cached_property`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Remember every answer</div>

```python
from functools import cache

@cache
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

>>> fib(100)
354224848179261915075
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Three ways to remember</div>

<div class="nl-recap mt-2">
  <div class="n">lru_cache</div><div><span class="why">keeps the last 128 results</span></div>
  <div class="n">cache</div><div><span class="why">keeps everything — 3.9+</span></div>
  <div class="n">cached_property</div><div><span class="why">once per object — 3.8+</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

Arguments become dict keys: a list raises `TypeError: unhashable type:
'list'`. On a method, the cache also keeps every `self` alive.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Cache only pure functions — a cached side effect happens once
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 17 - Caching
On screen ~65 seconds.

Type fib live, first without the decorator, with fib(32), and let them feel
the wait. Then add @cache and ask for fib(100).

"Sans cache, fib de cent demanderait plus de mille milliards de milliards
d'appels. Avec cache, c'est instantané : chaque valeur n'est calculée qu'une
fois."

Show fib.cache_info(): 98 hits, 101 misses. Cent une valeurs calculées, tout
le reste relu.

PAUSE.

Then the conditions, which are the real lesson:
"Ça ne marche que pour une fonction pure. Le cache renvoie le résultat
d'avant - si la fonction écrivait un fichier ou lisait l'heure, vous ne le
verrez qu'une fois."

[CLICK]
"Ne cachez que des fonctions pures. Un effet de bord mis en cache ne se
produit qu'une fois."

The two traps, briefly: les arguments servent de clés de dictionnaire, donc
une liste lève une TypeError. Et sur une méthode, le cache garde chaque self
en vie - pour une valeur calculée une fois par objet, c'est cached_property.

Time-sensitive: cache existe depuis Python 3.9, cached_property depuis 3.8.
lru_cache garde cent vingt-huit résultats par défaut.
-->

---
layout: default
class: nl-deck
---

# More `functools`: `wraps`, `total_ordering`, `singledispatch`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> Met in chapter 08</div>

<div class="nl-recap mt-2">
  <div class="n">wraps</div><div><span class="why">a decorated function keeps its name</span></div>
  <div class="n">total_ordering</div><div><span class="why">four comparisons from two</span></div>
</div>

<div class="nl-type mt-3"><NlIcon name="file" /> One function, per type</div>

```python
@singledispatch
def fmt(x):
    return repr(x)

@fmt.register
def _(x: Decimal):
    return f"{x:.2f} €"
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="split" /> Chosen by the first argument</div>

`fmt(Decimal("13.16"))` gives `'13.16 €'`; anything else falls back to
`repr`. A new type gets a new `register`, and `fmt` itself never changes.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> What it replaces</div>

<div style="font-size: 1.05rem">

An `isinstance` chain that grows, and gets edited, every time a type is
added.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>singledispatch</code> adds a type without editing the function
</div>

<!--
SLIDE 18 - More functools
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter eight, ten seconds:
"wraps et total_ordering, on les a vus au chapitre huit. wraps garde le nom
d'une fonction décorée. total_ordering déduit quatre comparaisons de deux."

Then the new one:
"singledispatch choisit l'implémentation selon le type du premier argument.
Une fonction de base, et une version par type, enregistrée à côté."

PAUSE.

Tie it to chapter eight's duck typing: le polymorphisme, mais pour des
fonctions. Au lieu d'une chaîne de isinstance qu'on rallonge à chaque nouveau
type, on enregistre une version de plus. La fonction d'origine ne bouge pas.

[CLICK]
"singledispatch ajoute un type sans toucher à la fonction."

Decorators themselves - writing them, with arguments - are chapter eleven.
Do not open that door here.
-->

---
layout: default
class: nl-deck
---

# Function Composition

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> pipe, from reduce</div>

```python
from functools import reduce

def pipe(*fs):
    return lambda x: reduce(
        lambda acc, f: f(acc), fs, x)

clean = pipe(str.strip, str.lower,
             str.title)
clean("  LA FONTAINE ")   # 'La Fontaine'
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> No operator, three lines</div>

Python has no composition operator. `reduce` builds one: each function's
output becomes the next one's input, left to right.

<div class="nl-type mt-3"><NlIcon name="split" /> Left to right, on purpose</div>

<div style="font-size: 1.05rem">

Maths writes composition right to left, `f(g(x))`. A pipe reads in the order
things happen. With no functions, `pipe()` returns its input unchanged.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Composition turns small functions into one, with no variable in between
</div>

<!--
SLIDE 19 - Composition
On screen ~55 seconds. Concept slide, no live coding needed.

Read pipe slowly, it is the whole chapter in three lines:
"Une fonction qui prend des fonctions, et renvoie une fonction. Dedans, un
reduce qui passe la valeur de l'une à l'autre."

Then clean: on enlève les espaces, on met en minuscules, puis une majuscule à
chaque mot. Trois petites fonctions existantes, une seule fonction neuve.
C'est le nettoyage des descriptions du CSV de janvier.

PAUSE.

Callback to the reduce slide: "Et la valeur initiale de reduce, c'est x.
C'est pour ça que pipe sans aucune fonction renvoie son entrée telle quelle.
La valeur initiale dont on parlait tout à l'heure fait le travail."

[CLICK]
"La composition transforme de petites fonctions en une seule, sans variable
intermédiaire."
-->

---
layout: default
class: nl-deck
---

# Functional Pitfalls

<div class="nl-cols mt-4" style="font-size: 1.05rem">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Closures built in a loop</div>

Every one of them sees the last value of the loop variable.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> A generator walked twice</div>

The second pass is empty, and nothing tells you.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> A cache on an impure function</div>

The side effect happens once, then the old result comes back forever.

</div>

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> partial, or a default argument</div>

Freeze the value when the function is created.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> A list, if you need it twice</div>

Or build the generator again; it is one line.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Cache pure functions only</div>

With hashable arguments, and <code>cached_property</code> on methods.

</div>

</div>

<div v-click class="nl-statement mt-3">
Each of these is a question of when a value is read
</div>

<!--
SLIDE 20 - Pitfalls
On screen ~60 seconds. Close the chapter on the mistakes, not a summary.

Read the left column, then the right, pair by pair. Ten seconds each.

"Des closures créées dans une boucle : elles voient toutes la dernière
valeur. Un générateur parcouru deux fois : le deuxième passage est vide, sans
erreur. Un cache sur une fonction impure : l'effet de bord n'arrive qu'une
fois."

PAUSE.

[CLICK]
"Les trois erreurs posent la même question : à quel moment la valeur est-elle
lue ? La closure la lit trop tard. Le générateur ne la relit pas. Le cache ne
la relit plus."

Callback to chapter three: le chapitre trois disait déjà qu'un itérateur se
consomme. Ce chapitre en a tiré toutes les conséquences.
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 11 — ADVANCED PYTHON</strong>

</div>

<!--
SLIDE 21 - Closing card
On screen ~12 seconds.

One sentence of chapter summary before the sign-off:
"Une fonction pure, des données qui ne bougent pas, et des générateurs qui ne
calculent que ce qu'on leur demande."

Say the next chapter's topic out loud while this is up: chapitre onze, le
Python avancé - les décorateurs qu'on écrit soi-même, et asyncio.
Then: "À mardi." Hold two beats of silence before you stop recording.
-->
