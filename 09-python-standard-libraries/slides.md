---
theme: ../themes/noonlabs
title: Python Standard Library — Chapter 09
info: NoonLabs - Module I, chapitre 09
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

<div class="nl-eyebrow">Chapter 09</div>

# Python Standard Library

<div class="mt-4" style="max-width: 42ch">

Everything Python already does, before you write it yourself

</div>

<div class="nl-type mt-6">
  <NlIcon name="box" /> Data
  <span class="mx-3">·</span>
  <NlIcon name="terminal" /> System
  <span class="mx-3">·</span>
  <NlIcon name="lock" /> Security
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~8 seconds.

"Chapitre neuf. Jusqu'ici, on a appris à écrire du Python. Aujourd'hui, on
apprend à ne pas en écrire : tout ce que Python sait déjà faire, livré avec
lui."

Restate the format so nobody wonders:
"Les diapositives, c'est pour les concepts. Le code, on l'écrit ensemble
dans VS Code."
-->

---
layout: default
class: nl-deck
---

# Before You `pip install` or `uv add`

<div class="nl-cols mt-4">

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="download" /> Already installed</div>

Every module in this chapter ships with CPython itself. No `pip install`, no
`uv add`, no version to pin, no extra package to audit.

<div class="nl-type mt-3"><NlIcon name="check" /> The habit</div>

Before you add a dependency, spend thirty seconds checking whether the
standard library already has it. It usually does.

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> The map of this chapter</div>

<div class="nl-recap mt-2">
  <div class="n">time</div><div><span class="why">datetime, time</span></div>
  <div class="n">data</div><div><span class="why">collections, itertools</span></div>
  <div class="n">numbers</div><div><span class="why">math, random, decimal</span></div>
  <div class="n">text</div><div><span class="why">re</span></div>
  <div class="n">system</div><div><span class="why">os, sys, subprocess, shutil</span></div>
  <div class="n">storage</div><div><span class="why">configparser, tomllib, sqlite3</span></div>
  <div class="n">tools</div><div><span class="why">argparse, logging</span></div>
  <div class="n">security</div><div><span class="why">hashlib, secrets</span></div>
</div>

</div>

</div>

<div v-click class="nl-statement mt-4">
Before you install a package, check whether Python already shipped one
</div>

<!--
SLIDE 3 - Before you install
On screen ~40 seconds. Concept slide, no live coding needed.

Pay off the promise from the end of chapter eight:
"Au chapitre huit, je vous ai promis tout ce que Python sait déjà faire et
que vous êtes en train de réécrire. Le voilà. Tout ce qui est à droite est
installé en même temps que Python."

Callback to chapter one, where uv became our tool:
"Que ce soit pip install ou uv add, comme au chapitre un : rien de tout ça
n'en a besoin. Pas de ligne en plus dans pyproject.toml."

Sweep the map rather than reading it: huit familles, une vidéo.

PAUSE.

[CLICK]
"Le réflexe à prendre : avant d'ajouter une dépendance, trente secondes dans
la bibliothèque standard. Une dépendance, c'est du code que vous n'avez pas
écrit et que vous devrez quand même maintenir."
-->

---
layout: default
class: nl-deck
---

# `datetime`: Dates and Durations

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Parse, shift, format</div>

```python
from datetime import datetime, timedelta

d = datetime.strptime("31/01/2026", "%d/%m/%Y")
print(d + timedelta(days=1))
# 2026-02-01 00:00:00
d.strftime("%Y-%m-%d")      # '2026-01-31'
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="split" /> p for parse, f for format</div>

`strptime` turns text into a `datetime`. `strftime` turns it back into text.
The format codes are the same in both directions.

<div class="nl-type mt-3"><NlIcon name="layers" /> A duration is a type</div>

A `timedelta` handles the calendar for you: month ends, and leap years.
`datetime(2028, 2, 28) + timedelta(days=1)` is the 29th.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>fromisoformat</code> for ISO dates, no format string</li>
<li class="nl-bad">Splitting <code>"31/01/2026"</code> on <code>"/"</code> by hand</li>
</ul>

</div>

</div>

<div v-click class="nl-statement mt-4">
<code>strptime</code> parses, <code>strftime</code> formats — never split a date by hand
</div>

<!--
SLIDE 4 - datetime
On screen ~60 seconds.

Read the three operations as one sentence:
"On lit une date écrite à la française, on avance d'un jour, et on la
réécrit au format ISO. Trois lignes, et le passage de janvier à février est
géré pour vous."

The p/f mnemonic is worth saying out loud, because everybody mixes them up:
"strptime, p comme parse : du texte vers une date. strftime, f comme
format : de la date vers du texte."

PAUSE.

Callback to chapter two: au chapitre deux, on découpait des chaînes avec
split. Pour une date, ne le faites pas - la fin de mois et le 29 février
vous attendent.

[CLICK]
"Une date n'est pas une chaîne. Dès que vous la lisez, convertissez-la."

Time-sensitive: fromisoformat accepts most ISO 8601 forms, such as a
trailing Z, only since Python 3.11.
-->

---
layout: default
class: nl-deck
---

# Timezones, and the `time` Module

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Naive meets aware</div>

```python
>>> from datetime import datetime, timezone
>>> datetime.now() < datetime.now(timezone.utc)
TypeError: can't compare offset-naive
and offset-aware datetimes
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Store UTC, show local</div>

<div style="font-size: 1.05rem">

`datetime.now(timezone.utc)` to store, then `.astimezone(ZoneInfo("Europe/Paris"))`
to display.

</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Two kinds of datetime</div>

A naive datetime is a wall-clock reading with no place attached. An aware one
carries its offset. Python refuses to compare them rather than guess.

<div class="nl-type mt-3"><NlIcon name="arrow" /> And the time module</div>

<div style="font-size: 1.05rem">

`time.time()` for a timestamp. `time.perf_counter()` to measure a duration: it
is monotonic, so a clock change cannot make it jump.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Store aware UTC — Python will not compare naive with aware
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 5 - Timezones
On screen ~65 seconds.

Type the comparison live. It fails, and the failure is the lesson:
"datetime.now() sans argument vous donne l'heure de votre machine, sans
fuseau. Avec timezone.utc, vous avez une heure qui sait où elle est. Et
Python refuse de comparer les deux."

PAUSE.

"Il a raison. Neuf heures, mais neuf heures où ? Paris, Montréal ? Plutôt
que de deviner, il lève une erreur."

[CLICK]
"La règle de production : on stocke en UTC, avec le fuseau. On convertit en
heure locale uniquement pour l'affichage."

Show ZoneInfo("Europe/Paris") on a July date: two hours ahead of UTC. In
January it is one. The library knows the daylight-saving rules.

Time-sensitive, say it once: datetime.utcnow() is deprecated since Python
3.12, and it returned a naive datetime anyway. zoneinfo exists since 3.9;
on Windows it needs the tzdata package from PyPI.

Then perf_counter in one line: pour chronométrer, perf_counter. Il ne recule
jamais, même si l'horloge système est corrigée.
-->

---
layout: default
class: nl-deck
---

# `collections`, Beyond Counter

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> Met in chapter 05</div>

<div class="nl-recap mt-2">
  <div class="n">Counter</div><div><span class="why">a dict that counts</span></div>
  <div class="n">defaultdict</div><div><span class="why">creates the missing key</span></div>
  <div class="n">namedtuple</div><div><span class="why">a tuple with field names</span></div>
</div>

<div class="nl-type mt-3"><NlIcon name="file" /> deque, with a limit</div>

```python
from collections import deque

last = deque(maxlen=3)
for x in [1, 2, 3, 4, 5]:
    last.append(x)
# deque([3, 4, 5], maxlen=3)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="arrow" /> deque: both ends, constant time</div>

`list.pop(0)` shifts every remaining element left. `deque.popleft()` does not.
For a queue, that is linear time against constant time.

<div class="nl-type mt-3"><NlIcon name="layers" /> OrderedDict, after 3.7</div>

<div style="font-size: 1.05rem">

A plain `dict` keeps insertion order now. `OrderedDict` still adds
`move_to_end()` and an `==` that compares order.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A queue is a <code>deque</code>, not a list you pop from the front
</div>

<!--
SLIDE 6 - collections
On screen ~60 seconds.

Callback to chapter five, ten seconds, no more:
"Counter, defaultdict, namedtuple : on les a vus au chapitre cinq. Ce sont
les trois que vous utiliserez le plus. Aujourd'hui, les deux autres."

The maxlen deque is the one that gets a reaction, so read the output:
"Cinq éléments entrent, trois restent. Les plus anciens tombent tout seuls.
Les trois dernières lignes d'un log, les cinq dernières mesures d'un
capteur : une ligne."

PAUSE.

[CLICK]
"Une file d'attente, c'est une deque. pop zéro sur une liste décale tous les
éléments à chaque appel. popleft sur une deque ne décale rien."

Close on OrderedDict honestly: depuis Python 3.7, un dict ordinaire garde
l'ordre d'insertion. OrderedDict garde deux raisons d'exister - move_to_end,
et une égalité qui tient compte de l'ordre. C'est ce qu'il faut pour un cache
LRU. Sinon, un dict suffit.
-->

---
layout: default
class: nl-deck
---

# `itertools`: Lazy Building Blocks

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Infinite, then cut</div>

```python
>>> from itertools import count, islice
>>> list(islice(count(10, 5), 4))
[10, 15, 20, 25]
>>> from itertools import combinations
>>> list(combinations("ABC", 2))
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Four families</div>

<div class="nl-recap mt-2">
  <div class="n">infinite</div><div><span class="why">count, cycle, repeat</span></div>
  <div class="n">combinatoric</div><div><span class="why">product, permutations, combinations</span></div>
  <div class="n">chaining</div><div><span class="why">chain</span></div>
  <div class="n">filtering</div><div><span class="why">islice, takewhile, filterfalse</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

Every one returns an iterator: nothing is computed until you ask, and once
walked, it is empty.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>itertools</code> hands you iterators — lazy, and consumed once
</div>

<!--
SLIDE 7 - itertools
On screen ~65 seconds.

Start with count, because it sounds impossible:
"count part de dix et avance de cinq. Pour toujours. Ce n'est pas une liste
infinie en mémoire - c'est une promesse. islice en prend quatre, et le reste
n'est jamais calculé."

Then combinations: toutes les paires possibles, sans les écrire. Trois
lettres, trois paires.

PAUSE.

Callback to chapter three, the iterator payoff from the zip slide:
"Souvenez-vous du chapitre trois : un itérateur se consomme. Tout ce que
renvoie itertools est un itérateur. Appelez list deux fois sur le même, et
la deuxième fois vous obtenez une liste vide."

[CLICK]
"itertools ne calcule rien d'avance. C'est ce qui lui permet de travailler
sur des millions de lignes sans les charger."

One trap worth ten seconds: takewhile s'arrête au premier élément qui ne
passe pas. Sur 1, 2, 3, 1 avec « moins que trois », vous obtenez 1, 2 - et
le dernier 1 n'est jamais regardé.
-->

---
layout: default
class: nl-deck
---

# `math`, `random` & `statistics`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> A seed fixes the dice</div>

```python
>>> import random
>>> random.seed(42)
>>> [random.randint(1, 6) for _ in range(5)]
[6, 1, 1, 6, 3]
```

<div class="nl-type mt-2"><NlIcon name="box" /> Floats, compared properly</div>

```python
>>> 0.1 + 0.2 == 0.3
False
>>> math.isclose(0.1 + 0.2, 0.3)
True
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> statistics, for a quick look</div>

`statistics.mean`, `median` and `stdev` work on any list of numbers. The
median of 13.16, 5.5 and 23.62 is 13.16.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>random.seed()</code> to make an experiment reproducible</li>
<li class="nl-good"><code>math.isclose</code>, never <code>==</code>, on floats</li>
</ul>

</div>

</div>

<div v-click class="nl-statement mt-3">
Same seed, same numbers — <code>random</code> is a sequence you can replay
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 8 - math, random, statistics. This is the chapter's PLANT.
On screen ~60 seconds.

Run the seed demo live, twice in a row, and read the numbers out loud both
times:
"Graine quarante-deux. Six, un, un, six, trois. Je recommence. Graine
quarante-deux. Six, un, un, six, trois."

PAUSE.

"En machine learning, c'est exactement ce qu'on veut : la même expérience,
les mêmes résultats, sur votre machine et sur celle d'un collègue."

PLANT the payoff and do not explain it:
"Même graine, mêmes dés. Retenez-le : le hasard de random est un hasard
qu'on peut rejouer."

[CLICK]

Callback to chapter two on the float line: zéro virgule un plus zéro
virgule deux n'est pas égal à zéro virgule trois. math.isclose est la bonne
comparaison.

The fourth module of the curriculum line, secrets, gets one sentence only:
"Il y a un quatrième module de hasard, secrets. On y revient à la fin du
chapitre."
-->

---
layout: default
class: nl-deck
---

# `decimal`: Exact Decimals, Explicit Rounding

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Ten payments of 0.10</div>

```python
>>> total = 0
>>> for _ in range(10):
...     total += 0.10
>>> total
0.9999999999999999
>>> from decimal import Decimal
>>> Decimal("0.10") * 10
Decimal('1.00')
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="file" /> The first video, again</div>

Restaurant printed 880.41. The float underneath was `880.4100000000003`; the
`:.2f` hid it. Built with `Decimal(row["montant"])`, it is 880.41 exactly.

<div class="nl-type mt-3"><NlIcon name="split" /> Rounding is a choice</div>

<div style="font-size: 1.05rem">

`quantize(Decimal("0.01"))` rounds half to even: 13.165 becomes 13.16. Pass
`rounding=ROUND_HALF_UP` for 13.17.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Money is a <code>Decimal</code> built from a string — never from a float
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 9 - decimal
On screen ~60 seconds.

Callback to chapter two, where this was promised and never shown:
"Au chapitre deux, je vous ai dit : l'argent, c'est decimal. Je ne vous ai
jamais montré pourquoi. Le voilà."

Type the loop live: dix paiements de dix centimes.
"Un euro, non ? Zéro virgule neuf, neuf, neuf... Il manque une miette, et
elle ne partira jamais."

PAUSE.

Then the callback to the first video, live: total the January CSV by
category with floats, and print the raw value instead of the formatted one.
"Restaurant : 880,4100000000003. Le script de la première vidéo affichait
880,41 parce que le deux-points-point-deux-f arrondissait à l'affichage.
L'erreur était là depuis le début, cachée."

[CLICK]
"De l'argent, c'est un Decimal, construit à partir d'une chaîne - directement
depuis la cellule du CSV. Jamais à partir d'un float : Decimal de 0,1 garde
l'erreur du float, sur cinquante-cinq décimales."

Rounding, in one breath: quantize arrondit au pair par défaut, donc 13,165
devient 13,16. Pour de la comptabilité, ROUND_HALF_UP donne 13,17. Décidez-le,
ne le subissez pas.

Time-sensitive: depuis Python 3.12, sum() sur une liste de floats compense
l'erreur, et sum de dix fois 0,1 donne bien 1.0. Une boucle avec plus égal ne
le fait pas. Ne comptez pas sur la chance.

One line for fractions: fractions.Fraction garde un tiers exact, pour les rares
calculs en fractions.
-->

---
layout: default
class: nl-deck
---

# `re`: search, match, findall

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Three ways to look</div>

```python
>>> import re
>>> re.match(r"\d+", "Total: 42")
>>> re.search(r"\d+", "Total: 42").group()
'42'
>>> re.findall(r"\d+\.\d+", "13.16 et 5.50")
['13.16', '5.50']
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> match is anchored</div>

`match` only looks at the start of the string. `search` scans all of it. The
first line returned `None`, so the REPL printed nothing.

<div class="nl-type mt-3"><NlIcon name="check" /> Always a raw string</div>

<div style="font-size: 1.05rem">

With `r"..."`, the backslashes reach `re` intact. Without it, Python's own
escapes get there first: `"\b"` is a backspace, not a word boundary.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>match</code> only checks the start — when in doubt, use <code>search</code>
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 10 - re, part one
On screen ~60 seconds.

Type the three calls live, in order, and stop on the first one:
"re.match, un nombre, dans « Total: 42 ». Entrée. Et... rien. Pas d'erreur,
pas de résultat. match a renvoyé None."

PAUSE.

"Parce que match ne regarde que le début de la chaîne. Et la chaîne commence
par T, pas par un chiffre. search, lui, parcourt toute la chaîne, et trouve
quarante-deux."

findall in one breath: tous les montants d'une ligne, en une liste de
chaînes. Ce sont des chaînes - float derrière, comme au chapitre six.

[CLICK]
"Si vous hésitez entre match et search, c'est search."

The raw string point, briefly: toujours un r devant le motif. Sans lui,
anti-slash b devient un retour arrière avant même que re le voie.

Last habit, one sentence: re.IGNORECASE pour ignorer la casse, et re.compile
pour nommer une fois un motif qui sert partout.
-->

---
layout: default
class: nl-deck
---

# `re`: Groups and sub

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Capture, then reorder</div>

```python
>>> m = re.search(r"(\d{4})-(\d{2})-(\d{2})",
...               "paid 2026-01-31")
>>> m.group(1), m.group(3)
('2026', '31')
>>> re.sub(r"(\d{4})-(\d{2})-(\d{2})",
...        r"\3/\2/\1", "2026-01-31")
'31/01/2026'
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="split" /> Parentheses capture</div>

Each pair of parentheses is a group, numbered from 1 in the order it opens.
`sub` puts them back with `\1`, `\2`, `\3`.

<div class="nl-type mt-3"><NlIcon name="check" /> Name the groups</div>

<div style="font-size: 1.05rem">

`(?P<year>\d{4})`, then `m["year"]`. The pattern documents itself, and adding
a group does not renumber the others.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A group captures, <code>sub</code> puts it back — reorder text without splitting it
</div>

<!--
SLIDE 11 - re, part two
On screen ~50 seconds. Concept slide, no live coding needed.

Point at the parentheses first:
"Chaque paire de parenthèses capture ce qu'elle reconnaît. L'année, le
mois, le jour. Trois groupes, numérotés dans l'ordre où ils s'ouvrent."

Then sub, and read the replacement slowly:
"Anti-slash trois, anti-slash deux, anti-slash un. Le jour, le mois,
l'année. La date ISO devient une date à la française, sans découper la
chaîne."

PAUSE.

[CLICK]
"Un groupe capture, sub remet en place. C'est tout ce qu'il faut pour
réécrire du texte."

Close on named groups, as a production habit: un groupe nommé se lit tout
seul, et ajouter un groupe au milieu ne décale pas les numéros des autres.

Be honest about the limit: une expression régulière illisible est une dette.
Au-delà d'une ligne, nommez les groupes ou écrivez un vrai parseur.
-->

---
layout: default
class: nl-deck
---

# `os`, `sys` & `subprocess`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="terminal" /> Run another program</div>

```python
import subprocess, sys

r = subprocess.run(
    [sys.executable, "-c", "print(6 * 7)"],
    capture_output=True, text=True,
    check=True,
)
r.stdout        # '42\n'
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Who does what</div>

<div class="nl-recap mt-2">
  <div class="n">os</div><div><span class="why">environment, working directory</span></div>
  <div class="n">sys</div><div><span class="why">argv, exit, path, executable</span></div>
  <div class="n">subprocess</div><div><span class="why">run another program</span></div>
</div>

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> A string and shell=True</div>

<div style="font-size: 1.05rem">

The shell parses your string, so a `;` inside a value starts a second
command. Pass a list. `check=True` turns a failure into an exception.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Give <code>subprocess.run</code> a list and <code>check=True</code>, never a shell string
</div>

<!--
SLIDE 12 - os, sys, subprocess
On screen ~65 seconds.

The recap first, twenty seconds. os parle au système : l'environnement, le
dossier courant. Pour les chemins, c'est pathlib - chapitre six. sys parle à
l'interpréteur : les arguments, la sortie, le chemin d'import.

Then the code, line by line:
"On lance un autre Python, il calcule six fois sept, et on récupère sa
sortie : quarante-deux, avec le retour à la ligne. capture_output garde la
sortie, text la décode en chaîne."

PAUSE.

The shell trap, concretely:
"Avec une chaîne et shell égale True, c'est le shell qui découpe la commande.
« echo a ; echo b » affiche deux lignes, parce que le point-virgule a lancé
une deuxième commande. Avec une liste, le même texte reste un seul argument,
et s'affiche tel quel."

[CLICK]
"Une liste, et check égale True. Sans check, un programme qui échoue renvoie
un code de sortie non nul, et votre script continue comme si de rien
n'était."
-->

---
layout: default
class: nl-deck
---

# `shutil` & Archives

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Whole files, whole folders</div>

```python
import shutil

shutil.copy2("depenses.csv", "backup/")
shutil.move("export.csv", "archive/")
shutil.make_archive("janvier", "zip", "data")
# creates janvier.zip
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Four calls</div>

<div class="nl-recap mt-2">
  <div class="n">copy2</div><div><span class="why">the file, and its timestamps</span></div>
  <div class="n">move</div><div><span class="why">renames, or copies then deletes</span></div>
  <div class="n">make_archive</div><div><span class="why">zip or tar a folder in one call</span></div>
  <div class="n">rmtree</div><div><span class="why">deletes a whole tree, no undo</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

`zipfile` and `gzip` read archives directly: `gzip.open(path, "rt")` reads a
compressed file like any text file.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>shutil</code> handles whole files and trees — and <code>rmtree</code> never asks twice
</div>

<!--
SLIDE 13 - shutil and archives
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter six:
"Au chapitre six, pathlib pour un fichier : le lire, l'écrire, le supprimer.
Pour des fichiers entiers et des dossiers entiers, c'est shutil."

Read the recap, one line each. copy2 copie le fichier et garde ses dates.
move renomme, ou copie puis supprime quand on change de disque. make_archive
zippe un dossier en un seul appel.

PAUSE.

The warning, said slowly:
"rmtree supprime un dossier et tout ce qu'il contient. Pas de corbeille. Pas
de confirmation. Vérifiez le chemin avant de l'appeler, surtout s'il vient
d'une variable."

[CLICK]
"shutil travaille sur des fichiers entiers et des arborescences entières. Et
rmtree ne demande jamais deux fois."

Then gzip in one line: gzip.open s'utilise comme open, sur un fichier
compressé. Un gros CSV compressé se lit ligne par ligne, sans le décompresser
d'abord sur le disque.
-->

---
layout: default
class: nl-deck
---

# `argparse`: A Script Becomes a Tool

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> depenses.py</div>

```python
import argparse

p = argparse.ArgumentParser()
p.add_argument("--top", type=int, default=5)
args = p.parse_args()
```

<div class="nl-type nl-bad mt-2"><NlIcon name="terminal" /> A bad value</div>

```text
$ python3 depenses.py --top trois
usage: depenses.py [-h] [--top TOP]
depenses.py: error: argument --top:
invalid int value: 'trois'
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="check" /> What you did not write</div>

<ul style="font-size: 1.05rem">
<li class="nl-good"><code>--help</code>, generated from your arguments</li>
<li class="nl-good">The conversion to <code>int</code>, and its error message</li>
<li class="nl-good">Exit status 2 on bad input</li>
</ul>

<div class="nl-type mt-3"><NlIcon name="layers" /> Instead of sys.argv</div>

<div style="font-size: 1.05rem">

`sys.argv` is a list of strings. Everything above is what you would otherwise
write by hand for each of them.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>argparse</code> writes your <code>--help</code>, your type checks and your error messages
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 14 - argparse
On screen ~60 seconds.

Build it live from the expense script of the first video. Three lines at the
top, then run it twice.

First with python3 depenses.py --help, and let them read the generated help:
"Je n'ai écrit aucune aide. argparse l'a écrite à partir de mes arguments."

PAUSE.

Then with --top trois:
"Trois en toutes lettres. argparse essaie de le convertir en entier, échoue,
et affiche un message qui dit exactement quel argument et quelle valeur. Le
message tient sur une ligne dans le terminal - je l'ai coupé pour la
diapositive. Et le code de sortie est deux, pour qu'un autre script sache
que ça a échoué."

Callback to the previous slide: sys.argv vous donne une liste de chaînes. La
conversion, la vérification, le message : tout ça, il faudrait l'écrire à la
main.

[CLICK]
"Votre script est devenu un outil. Quelqu'un d'autre peut s'en servir sans
lire votre code."

And for --top itself: heapq.nlargest donne les trois plus grands éléments
sans trier toute la liste.
-->

---
layout: default
class: nl-deck
---

# `configparser`, and the Formats You Know

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> app.ini</div>

```ini
[database]
path = depenses.db
timeout = 30
```

```python
cfg = configparser.ConfigParser()
cfg.read("app.ini")
cfg["database"]["timeout"]          # '30'
cfg.getint("database", "timeout")   # 30
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Which format, for what</div>

<div class="nl-recap mt-2">
  <div class="n">json</div><div><span class="why">data you exchange — chapter 06</span></div>
  <div class="n">csv</div><div><span class="why">tables — chapter 06</span></div>
  <div class="n">ini</div><div><span class="why">settings a human edits</span></div>
  <div class="n">toml</div><div><span class="why">pyproject.toml — tomllib, 3.11+</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

An ini value is always a string: `getint`, `getfloat`, `getboolean` convert.
`tomllib` keeps TOML's types, and only reads.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
An ini value is a string until you ask for a type — TOML keeps its types
</div>

<!--
SLIDE 15 - configparser
On screen ~50 seconds. Concept slide, no live coding needed.

Callback to chapter six, and keep it short:
"json et csv, on les a faits au chapitre six. Je ne les refais pas. La
bibliothèque standard en a un troisième : le fichier ini, pour les réglages
qu'un humain modifie à la main."

Read the file, then the two last lines:
"Des sections entre crochets, des clés, des valeurs. Et timeout revient en
chaîne : « trente » entre guillemets. getint vous le donne en entier."

PAUSE.

[CLICK]
"Comme une cellule de CSV, comme une variable d'environnement : dans un
fichier ini, tout est du texte tant que vous ne demandez pas un type."

Then TOML, and tie it to uv:
"Le pyproject.toml que uv add modifie, c'est du TOML. tomllib le lit depuis
Python 3.11, et là, trente reste un entier."

Two details: ouvrez le fichier en binaire, rb, sinon tomllib lève une
TypeError. Et tomllib ne sait que lire - jamais écrire.

getboolean reads yes, on, true and 1 - say it if someone asks.

The trap worth saying: cfg.read sur un fichier qui n'existe pas ne lève
rien. Il renvoie une liste vide. Vérifiez cette liste.
-->

---
layout: default
class: nl-deck
---

# `sqlite3`: A Database in One File

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="server" /> Insert, the safe way</div>

```python
import sqlite3

con = sqlite3.connect("depenses.db")
with con:
    con.execute(
        "insert into depenses values (?, ?)",
        ("La Fontaine", "Restaurant"),
    )
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> Never build SQL with an f-string</div>

With `x = "Loisirs' OR '1'='1"`, an f-string query returns every row of the
table. Through a `?` placeholder, the same value returns none: it is compared
as text, never run as SQL.

<div class="nl-type mt-3"><NlIcon name="check" /> What with con does</div>

<div style="font-size: 1.05rem">

It commits on success and rolls back on an exception. It does not close the
connection.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Values go in <code>?</code> placeholders — an f-string in SQL is an injection
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 16 - sqlite3
On screen ~65 seconds.

Set the scene: une base de données complète, dans un seul fichier, sans
serveur. Elle est livrée avec Python.

Demo the injection live, on a table with three rows from the January CSV.
First the f-string query, with x set to the string on the slide:
"Je cherche la catégorie Loisirs. Sauf que ma valeur contient une
apostrophe, puis « OR un égale un ». Résultat : trois lignes. Toute la
table."

PAUSE.

"La valeur est devenue du SQL. C'est ça, une injection."

Then the same value through the placeholder: zéro ligne. La valeur est
comparée comme du texte. Aucune catégorie ne s'appelle comme ça.

[CLICK]
"Les valeurs vont dans des points d'interrogation. Toujours. Une f-string
dans une requête SQL, c'est une faille."

Close on with con, because it surprises people: il valide la transaction,
ou l'annule en cas d'exception. Il ne ferme pas la connexion.

One habit for reading: con.row_factory égale sqlite3.Row, et chaque ligne se
lit par nom de colonne, comme un dictionnaire.
-->

---
layout: default
class: nl-deck
---

# `logging`: Levels and Loggers

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> The default</div>

```python
>>> import logging
>>> logging.info("fichier chargé")
>>> logging.warning("disque presque plein")
WARNING:root:disque presque plein
```

<div class="nl-type mt-2"><NlIcon name="check" /> One logger per module</div>

```python
log = logging.getLogger(__name__)
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Five levels</div>

<div class="nl-recap mt-2">
  <div class="n">DEBUG 10</div><div><span class="why">detail for you, while developing</span></div>
  <div class="n">INFO 20</div><div><span class="why">the program is doing its job</span></div>
  <div class="n">WARNING 30</div><div><span class="why">the default threshold</span></div>
  <div class="n">ERROR 40</div><div><span class="why">something failed</span></div>
  <div class="n">CRITICAL 50</div><div><span class="why">the program cannot go on</span></div>
</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Below WARNING, logging is silent until you configure it
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 17 - logging, part one
On screen ~60 seconds.

Callback to chapter seven, where this was promised:
"Au chapitre sept, on a remplacé print par log.exception, et je vous ai dit
que le logging aurait son chapitre. Le voilà."

Type the two calls live in a fresh interpreter:
"info, fichier chargé. Entrée. Rien. warning, disque presque plein. Entrée.
Et là, une ligne."

PAUSE.

"Ce n'est pas un bug. Par défaut, le seuil est WARNING. Tout ce qui est en
dessous est ignoré, tant que vous n'avez rien configuré."

[CLICK]
"En dessous de WARNING, le logging se tait. C'est la première chose qui
déroute tout le monde."

Then the habit: un logger par module, avec getLogger de underscore
underscore name underscore underscore. Le nom du module apparaît dans chaque
ligne, et vous savez quel fichier a parlé.
-->

---
layout: default
class: nl-deck
---

# `logging`: Handlers, Formatters & Rotation

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> A log that cannot fill the disk</div>

```python
from logging.handlers import RotatingFileHandler

h = RotatingFileHandler(
    "app.log",
    maxBytes=1_000_000,
    backupCount=3,
)
h.setFormatter(logging.Formatter(
    "%(asctime)s %(levelname)s %(message)s"))
logging.basicConfig(level="INFO", handlers=[h])
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Three parts</div>

<div class="nl-recap mt-2">
  <div class="n">logger</div><div><span class="why">what happened, and in which module</span></div>
  <div class="n">handler</div><div><span class="why">where it goes: console, file</span></div>
  <div class="n">formatter</div><div><span class="why">what one line looks like</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

Past `maxBytes`, the file rolls over and `backupCount` old ones are kept:
`app.log.1` to `app.log.3`. The oldest is deleted.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Loggers decide what to say, handlers decide where it goes
</div>

<!--
SLIDE 18 - logging, part two
On screen ~50 seconds. Concept slide, no live coding needed.

Name the three parts with the recap, one line each. Le logger décide quoi
dire, le handler décide où l'écrire, le formatter décide à quoi ressemble la
ligne.

Then the rotation, concretely:
"Un fichier de log qui grossit pour toujours finit par remplir un disque. En
général à trois heures du matin. RotatingFileHandler le plafonne : au-delà
d'un mégaoctet, il le renomme en app.log point un, et en commence un neuf.
Il en garde trois. Le plus ancien est supprimé."

PAUSE.

[CLICK]
"Le logger dit quoi. Le handler dit où. Vous pouvez changer la destination
sans toucher à une seule ligne qui écrit un message."

The rule from chapter seven, repeated because it matters: basicConfig, une
fois, dans l'application. Jamais dans une bibliothèque. Et s'il y a déjà un
handler, basicConfig ne fait rien du tout - sauf avec force égale True.
-->

---
layout: default
class: nl-deck
---

# `hashlib` & `secrets`

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> A token you can replay</div>

```python
>>> random.seed(42)
>>> f"{random.getrandbits(128):032x}"
'bdd640fb06671ad11c80317fa3b1799d'
```

<div class="nl-type nl-good mt-2"><NlIcon name="lock" /> A token nobody can</div>

```python
>>> import secrets
>>> len(secrets.token_hex(16))
32
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="check" /> hashlib, a fingerprint</div>

`hashlib.sha256(data).hexdigest()` is 64 hex characters. The same bytes always
give the same digest; change one byte and it changes completely.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> Not for passwords</div>

<div style="font-size: 1.05rem">

SHA-256 is fast, which is exactly wrong for a password. Use a slow, salted
hash: `hashlib.scrypt`, or a dedicated library such as `argon2-cffi`.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>random</code> is for experiments, <code>secrets</code> is for anything worth guessing
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 19 - hashlib and secrets. This is the chapter's PAYOFF. Do not rush.
On screen ~70 seconds.

Then land the payoff planted on the random slide. Do this live:
random.seed(42), then the getrandbits line, twice.

"Souvenez-vous des dés. Même graine, mêmes dés. Je fabrique un jeton de cent
vingt-huit bits avec random. Je recommence avec la même graine... et c'est
le même jeton. Caractère pour caractère."

PAUSE.

"Quelqu'un qui connaît ou devine la graine rejoue votre « hasard » à
l'identique - y compris un jeton de session. Ce qui rendait votre expérience
reproductible rend votre jeton devinable."

Then secrets.token_hex(16), twice: trente-deux caractères, différents à
chaque appel, et impossibles à rejouer.

[CLICK]
"Pour une expérience, random. Pour un secret, secrets. Jamais l'inverse."

Then hashlib in thirty seconds: une empreinte. Les mêmes octets donnent
toujours la même empreinte, un octet changé la change entièrement. Parfait
pour vérifier qu'un fichier n'a pas bougé.

Time-sensitive, and say it plainly: pas de SHA-256 nu pour un mot de passe.
C'est rapide, donc facile à attaquer par force brute. hashlib.scrypt, ou une
bibliothèque dédiée comme argon2-cffi.

And to compare two tokens: secrets.compare_digest, jamais le double égal. Le
double égal s'arrête au premier caractère différent, et le temps de réponse
trahit combien de caractères étaient justes.
-->

---
layout: default
class: nl-deck
---

# Standard Library Pitfalls

<div class="nl-cols mt-4" style="font-size: 1.05rem">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> A naive datetime in storage</div>

It works until it meets an aware one, and then the comparison raises.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> Values pasted into SQL or a shell</div>

An f-string query or a `shell=True` string runs whatever the value says.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> random for a token</div>

Anyone with the seed replays it.

</div>

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> Aware UTC, local for display</div>

`datetime.now(timezone.utc)`, then `astimezone` at the very end.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Data stays data</div>

A `?` placeholder for SQL, a list for `subprocess.run`.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> secrets for anything secret</div>

`secrets.token_hex`, `secrets.token_urlsafe`.

</div>

</div>

<div v-click class="nl-statement mt-3">
Every one of these runs without an error. That is the problem.
</div>

<!--
SLIDE 20 - Pitfalls
On screen ~60 seconds. Close the chapter on the mistakes, not a summary.

Read the left column, then the right, pair by pair. Three mistakes, three
fixes, ten seconds each.

"Une date naïve en base : tout marche, jusqu'au jour où elle croise une date
avec fuseau. Une valeur collée dans du SQL ou dans un shell : elle s'exécute.
random pour un jeton : il se rejoue."

PAUSE.

[CLICK]
"Aucune de ces trois erreurs ne lève d'exception le jour où vous l'écrivez.
C'est exactement pour ça qu'elles arrivent en production."

Callback to chapter seven: au chapitre sept, on apprenait à lire une erreur.
Ici, le danger, c'est qu'il n'y en a pas.
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 10 — FUNCTIONAL PROGRAMMING</strong>

</div>

<!--
SLIDE 21 - Closing card
On screen ~12 seconds.

One sentence of chapter summary before the sign-off:
"La meilleure ligne de code, c'est celle que la bibliothèque standard a déjà
écrite pour vous."

Say the next chapter's topic out loud while this is up: chapitre dix, la
programmation fonctionnelle.
Then: "À mardi." Hold two beats of silence before you stop recording.
-->
