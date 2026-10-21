---
theme: ../themes/noonlabs
title: Data Structures — Chapter 05
info: NoonLabs - Module I, chapitre 05
layout: cover
transition: fade
mdc: true
---

# NoonLabs

Code and AI as written in production

<!--
SLIDE 1 - Brand stamp
On screen ~4 seconds. Say "Bienvenue sur NoonLabs" over it and move on.
-->

---
layout: section
class: nl-deck
---

<div class="nl-eyebrow">Chapter 05</div>

# Data Structures

<div class="mt-4" style="max-width: 42ch">

Four containers, and the reference model that explains all of their surprises

</div>

<div class="nl-type mt-6">
  <NlIcon name="layers" /> Containers
  <span class="mx-3">·</span>
  <NlIcon name="split" /> Mutability
  <span class="mx-3">·</span>
  <NlIcon name="arrow" /> References
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~8 seconds.

"Chapitre cinq. Quatre conteneurs : listes, tuples, dictionnaires,
ensembles. Vous allez les utiliser tous les jours."

Then set up the second half, which is the part that matters:
"Et la deuxième moitié du chapitre explique pourquoi ils vous surprennent
parfois. Ce n'est pas une bizarrerie de Python - c'est un modèle, et une
fois qu'on l'a vu, tout devient prévisible."
-->

---
layout: default
class: nl-deck
---

# Lists: The Workhorse Sequence

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Four ways to make one</div>

```python
empty = []
fruits = ["apple", "banana"]
chars = list("hello")
numbers = list(range(5))
```

<div class="nl-type mt-2"><NlIcon name="box" /> Properties</div>

<div style="font-size: 1.02rem">

Ordered · mutable · duplicates allowed · any mix of types

</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="arrow" /> A list holds references</div>

A list does not contain your objects. It contains **references** to them —
which is why a list of mixed types costs nothing, and why two lists can point
at the same inner object.

<div style="font-size: 1.05rem">

Hold on to that sentence. It explains three surprises later in this chapter.

</div>

<div class="nl-type mt-3"><NlIcon name="check" /> When a list is the right answer</div>

<ul style="font-size: 1.05rem">
<li class="nl-good">Order matters, and the contents will change</li>
<li class="nl-bad">You only ever ask "is this in it?" — use a set</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
A list is an ordered, growable sequence of references
</div>

<!--
SLIDE 3 - Lists
On screen ~50 seconds.

Move fast through the construction - they have seen lists already in video
one.

Slow down and PLANT the payoff, without explaining it:
"Une liste ne contient pas vos objets. Elle contient des références vers vos
objets. C'est pour ça qu'une liste peut mélanger un entier, une chaîne et un
booléen sans effort - elle ne stocke que des adresses."

PAUSE.

"Retenez cette phrase. Elle explique trois surprises qu'on va voir dans ce
chapitre, dont une qui casse du code en production."

Callback to chapter two: this is the same names-and-objects model, applied to
a container.
-->

---
layout: default
class: nl-deck
---


# List Operators

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="arrow" /> Four you will use daily</div>

```python
[1, 2] + [3, 4]    # [1, 2, 3, 4]
[0] * 3            # [0, 0, 0]
3 in [1, 2, 3]     # True
len([1, 2, 3])     # 3
```

<div class="nl-type mt-2"><NlIcon name="split" /> In place, or new?</div>

```python
a += [5]      # extends a itself
b = a + [5]   # builds a new list
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> What <code>*</code> actually repeats</div>

`[0] * 3` gives three zeros, and that is safe — an integer is immutable, so
sharing one costs nothing.

`[[]] * 3` gives three references to **one** list. Nothing was duplicated.

<div style="font-size: 1.05rem">

Hold on to that. It is the last surprise in this chapter, and the largest.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>in</code> on a short list — on a set when it is hot</li>
<li class="nl-bad"><code>*</code> to build the rows of a grid</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>*</code> repeats the reference, not the object
</div>

<!--
SLIDE 4 - List operators
On screen ~50 seconds.

The four operators are twenty seconds - they are obvious and they are needed.

The `+=` versus `+` distinction is worth ten more: `+=` modifies the list in
place, so every other name pointing at it sees the change. `+` builds a new
one. Same asymmetry as sort versus sorted.

Then PLANT the payoff, and do not resolve it:
"`[0]` fois trois, ça donne trois zéros. Sans danger - un entier est
immuable, le partager ne coûte rien."

PAUSE.

"`[[]]` fois trois, ça donne trois références vers UNE seule liste. Rien n'a
été dupliqué. Gardez ça. C'est la dernière surprise du chapitre, et la plus
grosse."

Do not demonstrate it here. It lands on the copy slide.
-->

---
layout: default
class: nl-deck
---

# List Methods

<div class="nl-cols mt-4" style="font-size: 1.02rem">

<div>

<div class="nl-type"><NlIcon name="arrow" /> Add and remove</div>

<div class="nl-recap mt-2">
  <div class="n">append(x)</div><div><span class="why">one item, at the end</span></div>
  <div class="n">extend(it)</div><div><span class="why">every item of an iterable</span></div>
  <div class="n">insert(i, x)</div><div><span class="why">at a position</span></div>
  <div class="n">remove(x)</div><div><span class="why">first match, by value</span></div>
  <div class="n">pop(i)</div><div><span class="why">remove and return</span></div>
  <div class="n">reverse()</div><div><span class="why">flip the order in place</span></div>
  <div class="n">clear()</div><div><span class="why">empty it in place</span></div>
</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="split" /> In place, or a new list?</div>

`items.sort()` sorts the list and returns `None`. `sorted(items)` leaves it
alone and returns a new list. `reverse()` also returns `None`; `reversed()`
returns an iterator, not a list.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-bad"><code>items = items.sort()</code> — now <code>items</code> is <code>None</code></li>
<li class="nl-good"><code>items.sort()</code> or <code>items = sorted(items)</code></li>
</ul>

<div style="font-size: 1.02rem">

Both take `key=` and `reverse=` — the lambda from chapter four goes here.

</div>

</div>

</div>

<div class="nl-statement mt-3">
In-place methods return <code>None</code> — <code>pop()</code> is the one that returns what it removed
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 5 - List methods
On screen ~60 seconds. Table on screen, demo in the terminal.

The sort/sorted mistake is the one to demonstrate, because it fails silently
and everyone makes it once:

items = [3, 1, 2]
items = items.sort()
print(items)     ->  None

"Votre liste a disparu. Pas d'erreur. `sort` trie sur place et ne renvoie
rien - et vous venez d'écraser la liste avec ce rien."

PAUSE.

Then the design reason, which turns a gotcha into a rule:
"Et ce n'est pas un accident. En Python, une méthode qui modifie sur place
renvoie None, exprès, pour que vous ne l'enchaîniez pas par erreur. C'est
une convention - `append`, `extend`, `sort`, `reverse`, toutes pareilles.
Une exception, et elle a une raison : pop renvoie l'élément qu'il retire -
c'est tout son intérêt."

And reversed, said once: reversed ne renvoie pas une liste, mais un
itérateur - le même objet paresseux que zip au chapitre trois.

Callback to chapter four: key=lambda goes here.
-->

---
layout: default
class: nl-deck
---

# Slicing Mastery

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> Beyond the basics</div>

```python
items[::2]      # every second
items[::-1]     # reversed
items[-3:]      # last three
items[:-3]      # all but the last three
items[5:2:-1]   # backwards, 5 down to 3
items[::-2]     # every second, reversed
```

<div class="nl-type mt-2"><NlIcon name="box" /> A slice is an object</div>

```python
first_three = slice(0, 3)
items[first_three]
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Slices assign, too</div>

On a list, a slice is not read-only. `items[1:3] = ["a", "b", "c"]` replaces
two elements with three, and `del items[1:3]` removes them.

<div class="nl-type mt-3"><NlIcon name="split" /> And a slice copies</div>

`items[:]` builds a **new list** with the same references. That is the
shallow copy we come back to at the end of the chapter.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Any sequence: list, tuple, str, range — and NumPy, where it returns a <em>view</em></li>
<li class="nl-bad">Chaining three slices — name the intermediate</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
A slice out of range returns empty. An index out of range raises.
</div>

<!--
SLIDE 6 - Slicing
On screen ~55 seconds.

They met slicing on strings in chapter two, so lead with what is new: on a
mutable sequence, a slice is also a target.

"Sur une liste, une tranche n'est pas seulement une lecture. Vous pouvez
affecter dedans. `items[1:3] = trois éléments` remplace deux éléments par
trois, et la liste change de taille."

The slice object is thirty seconds and mostly for recognition:
"Et une tranche est un objet. Vous pouvez la nommer, la stocker, la
réutiliser. Vous le verrez surtout dans du code NumPy."

Then PLANT the copy point, without resolving it:
"Et notez : `items[:]` fabrique une nouvelle liste. Une nouvelle liste avec
les mêmes références. Gardez ça, on y revient à la fin du chapitre."
-->

---
layout: default
class: nl-deck
---

# List Comprehensions

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> The loop</div>

```python
squares = []
for x in range(10):
    squares.append(x ** 2)
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> The comprehension</div>

```python
squares = [x ** 2 for x in range(10)]

evens = [x for x in nums if x % 2 == 0]

labels = ["even" if x % 2 == 0 else "odd"
          for x in nums]
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="indent" /> Two different positions</div>

A filter goes **after** the loop: `[x for x in xs if cond]` — it decides
whether an item appears at all.

A conditional expression goes **before** it: `[a if cond else b for x in xs]`
— every item appears, transformed one way or the other.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">One loop, one condition, one expression</li>
<li class="nl-bad">Two nested loops and a filter — write the loop</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
A comprehension builds a value. A loop performs an action.
</div>

<!--
SLIDE 7 - Comprehensions
On screen ~60 seconds.

The two-positions distinction is the whole slide, and it is where beginners
get stuck:
"Le filtre va APRÈS la boucle, et il décide si l'élément existe. Le ternaire
va AVANT, et tous les éléments existent - seulement transformés
différemment."

Say it twice. Then show both in VS Code with the same input list, and let
them count the outputs: le filtre en donne moins, le ternaire en donne
autant.

The statement is the rule that keeps comprehensions readable:
"Une compréhension construit une valeur. Une boucle fait une action. Si votre
compréhension ne construit rien - si vous l'écrivez pour ses effets de bord -
c'était une boucle."

Callback to chapter four: this is what replaces map and filter.
-->

---
layout: default
class: nl-deck
---

# Tuples: Immutable Records

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="lock" /> Creating them</div>

```python
point = (3, 4)
coords = 3, 4, 5      # parens optional
single = (5,)         # the comma matters
empty = ()
```

<div class="nl-type mt-2"><NlIcon name="split" /> Unpacking</div>

```python
x, y = point
first, *rest = (1, 2, 3, 4)
a, b = b, a           # swap
name, _, city = person
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Immutable, and hashable if its contents are</div>

You cannot change a tuple, so Python can hash it — which is why a tuple can
be a dictionary key and a list cannot.

<div style="font-size: 1.05rem">

Careful: a tuple *containing* a list is not hashable. Immutability is not
inherited by what it references.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">A fixed record: coordinates, a row, a return pair</li>
<li class="nl-bad">A collection you will add to — that is a list</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
It is the comma that makes a tuple, not the parentheses
</div>

<!--
SLIDE 8 - Tuples
On screen ~55 seconds.

The single-element comma is worth demonstrating because it bites everyone:
type (5) and show it is an int; type (5,) and show it is a tuple.

"Ce ne sont pas les parenthèses qui font le tuple. C'est la virgule. Les
parenthèses ne servent qu'à grouper."

Unpacking is chapter four's multiple return, so name the callback:
"Vous avez déjà utilisé ça au chapitre quatre. Une fonction qui « renvoie
deux valeurs » renvoie un tuple, et vous le déballez."

The nested-list caveat is the sentence that prevents a confusing error later:
"Un tuple est immuable. Mais s'il contient une liste, il n'est plus
hachable. L'immuabilité ne se transmet pas à ce qu'il référence."
-->

---
layout: default
class: nl-deck
---

# namedtuple, and What Replaced It

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> Fields instead of positions</div>

```python
from collections import namedtuple
Point = namedtuple("Point", "x y")

p = Point(3, 4)
p.x           # 3
x, y = p      # still unpacks
```

<div class="nl-type mt-2"><NlIcon name="check" /> Modern equivalent</div>

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="split" /> Why bother</div>

`p[0]` tells the reader nothing. `p.x` tells them everything — and a
`namedtuple` still behaves like a tuple everywhere a tuple is expected.

<div class="nl-type mt-3"><NlIcon name="layers" /> Which to choose</div>

<ul style="font-size: 1.05rem">
<li class="nl-good"><code>namedtuple</code> — a lightweight row, tuple behaviour needed</li>
<li class="nl-good"><code>dataclass</code> — type hints, defaults, methods, mutability if you want it</li>
<li class="nl-bad">A bare tuple of five things nobody can name</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
If you are indexing a tuple by number, it wanted names
</div>

<!--
SLIDE 9 - namedtuple
On screen ~55 seconds.

Frame it as a readability fix, not a new type to learn:
"`p[0]` et `p[1]`. Six mois plus tard, lequel est la latitude ? Avec un
namedtuple, la question ne se pose pas."

Be honest about the modern landscape - this is where a lot of courses stop
too early:
"namedtuple existe depuis longtemps et vous en verrez beaucoup. Mais dans du
code neuf, on écrit plutôt une dataclass : vous avez les annotations de
type, des valeurs par défaut, des méthodes, et vous choisissez si c'est
mutable ou pas."

Show both in VS Code side by side. Twenty seconds each.

The `frozen=True` is the bridge: une dataclass gelée, c'est un tuple nommé
avec des annotations.
-->

---
layout: default
class: nl-deck
---

# Dictionaries: Keys and Values

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Creating and reading</div>

```python
person = {"name": "Alice", "age": 25}
person["age"] = 26
person["city"] = "NYC"

person.get("email")        # None
person.get("email", "n/a")  # 'n/a'
```

<div class="nl-type mt-2"><NlIcon name="arrow" /> Iterating</div>

```python
for key, value in person.items():
    print(key, value)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Keys must be hashable</div>

Strings, numbers, tuples: fine. Lists, dicts, sets: not allowed — they can
change, so their hash would change with them.

Keys are unique; values may repeat as often as you like.

<div class="nl-type mt-3"><NlIcon name="check" /> Order is guaranteed</div>

<div style="font-size: 1.05rem">

Since 3.7, insertion order is part of the language, not an implementation
detail. You can rely on it.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>.get(k, default)</code> when the key may be absent</li>
<li class="nl-bad"><code>d[k]</code> on untrusted input — that is a <code>KeyError</code></li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>in</code> on a dictionary tests the keys, never the values
</div>

<!--
SLIDE 10 - Dictionaries
On screen ~60 seconds.

They built a dict in video one, so lead with what they did not know then.

The hashability rule needs its reason, or it sounds arbitrary:
"Pourquoi une liste ne peut pas être une clé ? Parce qu'une clé est rangée
selon son hachage. Si la liste change, son hachage change, et Python ne
retrouve plus la case. L'immuabilité n'est pas un caprice - c'est ce qui
rend la recherche possible."

The ordering point is a correction worth making explicitly:
"Vous lirez encore que les dictionnaires sont « non ordonnés ». C'était vrai
avant 3.7. Depuis, l'ordre d'insertion est garanti par le langage."

Then the statement, demoed in one line: "nom" in person is True, "Alice" in
person is False. Ten seconds, and it prevents a real bug.
-->

---
layout: default
class: nl-deck
---

# Dictionary Techniques

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> Counting, the short way</div>

```python
from collections import Counter
Counter(words).most_common(3)
```

<div class="nl-type mt-2"><NlIcon name="split" /> Grouping, the short way</div>

```python
from collections import defaultdict
groups = defaultdict(list)
for row in rows:
    groups[row.kind].append(row)
```


</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> The pattern behind both</div>

Every one replaces "check whether the key exists, then initialise it, then
update it" — three lines that are easy to get subtly wrong.

<div style="font-size: 1.05rem">

`defaultdict(list)` creates the empty list on first access. `Counter` is a
dict that counts. Neither needs a guard.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Reach into <code>collections</code> before writing the guard</li>
<li class="nl-bad"><code>if k not in d: d[k] = []</code> on every insert</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
If you are writing "if the key is missing", something in <code>collections</code> already did it
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 11 - Dict techniques
On screen ~65 seconds. This is the highest-value slide in the chapter for
someone who already writes Python.

Do the word-count three times in VS Code, in order:
1. with `if word not in counts` - six lines
2. with `.get(word, 0)` - four lines
3. with `Counter(words)` - one line

"Le même programme. Six lignes, quatre lignes, une ligne. Et la version
d'une ligne est aussi la plus rapide, parce qu'elle est écrite en C."

PAUSE.

One line for merging, which left the slide: depuis Python 3.9, base barre
verticale overrides fusionne deux dictionnaires, et les valeurs de droite
gagnent.

Then the general lesson, which is the real point:
"La leçon n'est pas « apprenez Counter ». C'est : quand vous écrivez « si la
clé n'existe pas », arrêtez-vous et regardez dans `collections`. Quelqu'un
l'a déjà fait, et mieux."
-->

---
layout: default
class: nl-deck
---

# Dict &amp; Set Comprehensions

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> Dict — key and value</div>

```python
{x: x ** 2 for x in range(5)}

{k: v for k, v in data.items()
 if v is not None}

dict(zip(keys, values))
```

<div class="nl-type mt-2"><NlIcon name="layers" /> Set — deduplicated</div>

```python
{c for c in "hello world"}
{len(w) for w in words}
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="indent" /> Same shape, four results</div>

The brackets decide the type, and nothing else changes:

<div class="nl-recap mt-2" style="font-size: 1.02rem">
  <div class="n">[ ]</div><div><span class="why">list — ordered, duplicates kept</span></div>
  <div class="n">{k: v}</div><div><span class="why">dict — later keys win</span></div>
  <div class="n">{ }</div><div><span class="why">set — unordered, deduplicated</span></div>
  <div class="n">( )</div><div><span class="why">generator — lazy, one pass</span></div>
</div>

<div style="font-size: 1.02rem">

`{}` alone is an empty **dict**. For an empty set you must write `set()`.

</div>

</div>

</div>

<div class="nl-statement mt-3">
One syntax, four containers — the brackets choose
</div>

<!--
SLIDE 12 - Dict and set comprehensions
On screen ~55 seconds.

The four-brackets table is the slide. Say it as one idea:
"C'est la même construction. Ce sont les délimiteurs qui décident du type."

The generator row deserves a flag, because it connects to chapter three and
to chapter ten:
"Les parenthèses donnent un générateur - paresseux, consommable une seule
fois. Comme zip. On y reviendra."

The empty-set trap is ten seconds and saves confusion:
"Et attention : accolades vides, c'est un dictionnaire vide. Pour un
ensemble vide, il faut écrire set() - il n'y a pas de syntaxe littérale."

Show `type({})` in the terminal. It settles it instantly.
-->

---
layout: default
class: nl-deck
---

# Sets &amp; frozensets

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="layers" /> Unique, unordered, fast</div>

```python
unique = set(items)
seen = {"a", "b"}
empty = set()          # not {}
```

<div class="nl-type mt-2"><NlIcon name="split" /> Algebra, not loops</div>

```python
a | b     # union
a & b     # intersection
a - b     # difference
a ^ b     # in one, not both
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="check" /> What they are for</div>

Deduplicating, and answering "is this in it?" — membership on a set is O(1)
because it hashes, while a list has to scan.

<div class="nl-type mt-3"><NlIcon name="lock" /> frozenset</div>

<div style="font-size: 1.05rem">

An immutable set, and therefore hashable — so it can be a dict key or an
element of another set. Same operations, no `add`.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Comparing two collections — use the operators</li>
<li class="nl-bad">Anything where order matters; a set has none</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
If you wrote a nested loop to compare two lists, you wanted sets
</div>

<!--
SLIDE 13 - Sets
On screen ~60 seconds.

The operators are the sell. Do the comparison live: find the items in list A
that are not in list B, first with a nested loop, then with `set(a) - set(b)`.

"Neuf lignes et n au carré. Contre une ligne et n. Et la version courte dit
ce qu'elle veut dire."

Callback to chapter three's complexity slide - name it:
"On a dit au chapitre trois : chaque niveau d'imbrication multiplie. Voilà
comment on supprime le niveau."

frozenset gets thirty seconds and one reason: hashable, so it can be a key.
Show the failure first - putting a set inside a set raises - then fix it with
frozenset.
-->

---
layout: default
class: nl-deck
---


# Dictionary &amp; Set Methods

<div class="nl-cols mt-4" style="font-size: 1.02rem">

<div>

<div class="nl-type"><NlIcon name="box" /> dict</div>

<div class="nl-recap mt-2">
  <div class="n">keys()</div><div><span class="why">a live view of the keys</span></div>
  <div class="n">values()</div><div><span class="why">a live view of the values</span></div>
  <div class="n">items()</div><div><span class="why">(key, value) pairs</span></div>
  <div class="n">setdefault()</div><div><span class="why">read, inserting a default if absent</span></div>
  <div class="n">update()</div><div><span class="why">merge another dict in place</span></div>
  <div class="n">pop() clear()</div><div><span class="why">remove one, or all</span></div>
</div>

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> set</div>

<div class="nl-recap mt-2">
  <div class="n">add()</div><div><span class="why">one element</span></div>
  <div class="n">remove()</div><div><span class="why">raises <code>KeyError</code> if absent</span></div>
  <div class="n">discard()</div><div><span class="why">silent if absent</span></div>
  <div class="n">update()</div><div><span class="why">merge another set in place</span></div>
  <div class="n">issubset()</div><div><span class="why">containment, both directions</span></div>
</div>

<ul class="mt-2" style="font-size: 1.02rem">
<li class="nl-bad"><code>remove()</code> on a value that might not be there</li>
<li class="nl-good"><code>discard()</code> when absence is not an error</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>keys()</code> is a view, not a copy — it changes when the dictionary does
</div>

<!--
SLIDE 14 - Method reference
On screen ~45 seconds. Reference material, so read it fast and pick two
things to say properly.

First: remove versus discard. It is the same distinction as `[]` versus
`.get()` on a dictionary, and it is a real decision:
"`remove` lève une erreur si l'élément n'est pas là. `discard` ne dit rien.
Choisissez selon votre intention : est-ce que l'absence est un bug, ou est-ce
que c'est normal ?"

Second: views. Demonstrate it in the terminal, it takes fifteen seconds:

ks = person.keys()
person["city"] = "NYC"
print(ks)          # 'city' is already in there

"`keys()` ne renvoie pas une liste. C'est une vue sur le dictionnaire. Si le
dictionnaire change, la vue change. Si vous voulez un instantané, il faut
écrire `list(person.keys())`."
-->

---
layout: default
class: nl-deck
---


# Nested Structures

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> Dictionaries inside dictionaries</div>

```python
users = {
    "alice": {"age": 25, "city": "NYC"},
    "bob":   {"age": 30, "city": "LA"},
}
users["alice"]["city"]     # 'NYC'
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Reaching in safely</div>

```python
users.get("carol", {}).get("city")
```

</div>

<div>

<div class="nl-type"><NlIcon name="indent" /> Flatten, and transpose</div>

```python
flat = [x for row in grid for x in row]

cols = list(zip(*grid))
```

<div style="font-size: 1.05rem">

A nested comprehension reads **left to right in the same order as the loops
it replaces** — outer first, then inner. Two levels is the limit before a
real loop is clearer.

</div>

<div class="nl-type mt-2 nl-type--plain">

Every JSON response you will ever parse is this shape: dictionaries and lists,
nested.

</div>

</div>

</div>

<div class="nl-statement mt-3">
Two brackets deep is data. Four is a bug waiting to be found.
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 15 - Nested structures
On screen ~60 seconds.

Lead with why this matters rather than with the syntax:
"Toute réponse d'API que vous parserez a cette forme. Des dictionnaires dans
des dictionnaires, avec des listes dedans. Ce n'est pas un cas exotique -
c'est le cas normal."

The safe-access chain is the production habit, so demo the failure first:
users["carol"]["city"]     ->  KeyError

Then the chained get, and be honest about its limit:
"`.get` avec un dictionnaire vide par défaut, ça marche pour deux niveaux.
Au-delà, ça devient illisible - et là, ce qu'il vous faut, c'est une
dataclass ou un try/except, pas une chaîne de get."

The flatten reading order trips everyone, so say it slowly and point:
"On lit de gauche à droite, dans l'ordre des boucles. `pour chaque ligne`,
puis `pour chaque x dans la ligne`. C'est exactement l'ordre où vous les
écririez en boucles imbriquées."

Then the transpose with zip(*grid) - callback to chapter three, and it always
gets a reaction.
-->

---
layout: default
class: nl-deck
---

# Mutable vs Immutable

<div class="nl-cols mt-4">

<div>

<div class="nl-recap mt-1" style="font-size: 1.05rem">
  <div class="n">mutable</div><div><span class="why">list · dict · set · most classes</span></div>
  <div class="n">immutable</div><div><span class="why">int · float · str · tuple · frozenset · bool · None</span></div>
</div>

<div class="nl-type mt-3"><NlIcon name="split" /> The visible difference</div>

```python
items = [1, 2, 3]
items[0] = 99        # fine

text = "hello"
text[0] = "H"        # TypeError
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why the distinction earns a slide</div>

- Only hashable objects can be **dict keys** or **set elements**
- Immutable objects are safe to share between threads
- A mutable object passed to a function can be **changed by it**
- Mutable default arguments are shared across calls — chapter four

<div style="font-size: 1.02rem">

Mutating changes the object every reference can see. Rebinding only moves one
name.

</div>

</div>

</div>

<div class="nl-statement mt-3">
Mutating changes what everyone sees. Rebinding moves one name.
</div>

<!--
SLIDE 16 - Mutability
On screen ~55 seconds. Concept slide, stays on the slide.

The four consequences are the reason this matters. Read them as consequences,
not as trivia.

Point at the fourth one and name the callback:
"Le quatrième, vous l'avez déjà vu. Le piège de la liste par défaut au
chapitre quatre. C'était ça, exactement ça."

On the first line, be precise: la règle, c'est « hachable », pas
« immuable ». Une instance de classe ordinaire est modifiable et peut quand
même servir de clé. Un tuple qui contient une liste est immuable, et ne peut
pas.

Then the statement, slowly, because it is the sentence that unlocks the last
four slides:
"Muter, ça change l'objet - et toutes les références voient le changement.
Réaffecter, ça déplace UN nom, et les autres ne bougent pas."

PAUSE. Draw it if you can.
-->

---
layout: default
class: nl-deck
---

# The Memory Model

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="arrow" /> Two names, one object</div>

```python
a = [1, 2, 3]
b = a              # not a copy
b.append(4)
a                  # [1, 2, 3, 4]
```

<div class="nl-type mt-2"><NlIcon name="prompt" /> Proof</div>

```python
a is b             # True
id(a) == id(b)     # True

import sys
sys.getrefcount(a)  # 2, then 3
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Assignment never copies</div>

`b = a` binds a second name to the same object. Nothing is duplicated — not
for lists, not for anything.

Every object has an identity you can see with `id()`, and a reference count.
When the last reference goes, the object goes.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Pass a copy if the caller must not see your edits</li>
<li class="nl-bad">Assuming <code>=</code> protects the original</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>=</code> gives a name to an object. It never makes a second object.
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 17 - Memory model
On screen ~60 seconds. Do this live, it is four lines and it lands hard.

a = [1, 2, 3]
b = a
b.append(4)
print(a)

"On n'a jamais touché à a. Et a a changé."

PAUSE. Let them sit with it.

"Parce que b = a ne copie rien. Ça colle une deuxième étiquette sur le même
objet. Il n'y a qu'une seule liste depuis le début."

Then id(a) and id(b) to prove it, and `a is b`.

Chapter two callback, and say it is the third time we have met this idea:
"Un nom pointe sur un objet. Chapitre deux. Le piège de la valeur par défaut,
chapitre quatre. Et maintenant ça. C'est le même modèle à chaque fois."
-->

---
layout: default
class: nl-deck
---

# is vs ==

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="split" /> Different questions</div>

```python
a = [1, 2, 3]
b = [1, 2, 3]

a == b     # True  — same value
a is b     # False — different objects
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> Small integers are cached</div>

```python
256 is int("256")    # True
257 is int("257")    # False
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Which to use</div>

`==` asks *"same value?"* and calls a method the class defines. `is` asks
*"same object?"* and compares identities. They are not interchangeable.

<div style="font-size: 1.02rem">

CPython pre-allocates the integers −5 to 256 and interns short strings, so
`is` sometimes appears to work on values. It is an implementation detail —
never rely on it.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>is</code> for <code>None</code>, <code>True</code>, <code>False</code> — the singletons</li>
<li class="nl-bad"><code>is</code> on numbers or strings, ever</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>==</code> compares values. <code>is</code> compares addresses.
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 18 - is vs ==
On screen ~60 seconds.

WARNING about the demo, and this matters: the famous version of this trick -
typing `a = 257; b = 257; a is b` - does NOT work any more. Modern CPython
folds those literals into one constant, so you get True and the point is
lost. Python also emits a SyntaxWarning for `is` with a literal.

Use the version on the slide, with int("257"), which forces two objects:

256 is int("256")   ->  True
257 is int("257")   ->  False

"Deux fois le même code. Deux réponses différentes. La seule différence,
c'est que CPython garde en cache les entiers de moins cinq à deux cent
cinquante-six."

PAUSE.

"Et c'est exactement pour ça qu'on n'utilise jamais `is` sur des nombres.
Ça marche parfois. « Parfois », en production, c'est pire que jamais."

Callback: chapter two said use `is None` because None is a singleton. Same
rule, now with the mechanism behind it.
-->

---
layout: default
class: nl-deck
---

# Shallow vs Deep Copy

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Shallow copies</div>

```python
b = a[:]
b = a.copy()
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> The grid trap</div>

```python
grid = [[0] * 3] * 3
grid[0][0] = 9
# [[9,0,0], [9,0,0], [9,0,0]]
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Both fixes</div>

```python
grid = [[0] * 3 for _ in range(3)]
deep = copy.deepcopy(a)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> The payoff</div>

A shallow copy duplicates the **outer** container and reuses every inner
reference. `[[0]*3]*3` does not build three rows — it builds one row and
three references to it.

<div style="font-size: 1.05rem">

That is the sentence from the start of this chapter: a list holds references,
not values.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Flat list of immutables? Shallow is enough</li>
<li class="nl-good">Nested structure you will edit? <code>deepcopy</code></li>
<li class="nl-bad"><code>*</code> to build rows of a grid</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
A shallow copy copies the container, never the contents
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 19 - Copies
On screen ~75 seconds. This is the chapter's payoff. Give it the time.

Build the grid live and change one cell:

grid = [[0] * 3] * 3
grid[0][0] = 9
print(grid)

Three nines. Let the silence sit.

"On en a changé un. Il y en a trois."

Then prove why, in one line:
grid[0] is grid[1]     ->  True

"Il n'y a pas trois lignes. Il y a UNE ligne et trois références vers elle.
L'étoile n'a pas copié la liste - elle a copié la référence, trois fois."

PAUSE.

Then close the loop, and say it explicitly:
"Souvenez-vous du début du chapitre : une liste contient des références, pas
des valeurs. Voilà ce que ça coûte quand on l'oublie."

Then the comprehension fix, and deepcopy for the general case. Mention that
deepcopy is slow and follows every reference - it is a tool, not a default.
-->

---
layout: default
class: nl-deck
---

# Choosing a Structure

<div class="nl-cols mt-4" style="font-size: 1.02rem">

<div>

<div class="nl-type"><NlIcon name="check" /> Ask what you will do with it</div>

<div class="nl-recap mt-2">
  <div class="n">list</div><div><span class="why">order matters, contents change</span></div>
  <div class="n">tuple</div><div><span class="why">fixed record, needs to be a key</span></div>
  <div class="n">dict</div><div><span class="why">look up by name</span></div>
  <div class="n">set</div><div><span class="why">membership, deduplication</span></div>
  <div class="n">deque</div><div><span class="why">a queue — push and pop both ends</span></div>
</div>

</div>

<div style="font-size: 1.05rem">

<div class="nl-type"><NlIcon name="layers" /> The cost that decides it</div>

<div class="nl-recap mt-2">
  <div class="n">x in list</div><div><span class="why">O(n) — scans every element</span></div>
  <div class="n">x in set</div><div><span class="why">O(1) — hashes once</span></div>
  <div class="n">list.append</div><div><span class="why">O(1)</span></div>
  <div class="n">list.insert(0,x)</div><div><span class="why">O(n) — shifts everything</span></div>
  <div class="n">deque.appendleft</div><div><span class="why">O(1)</span></div>
</div>

<div style="font-size: 1rem">

A membership test in a loop over a list is the O(n²) from chapter three,
hiding in plain sight.

</div>

</div>

</div>

<div class="nl-statement mt-3">
The right container turns a nested loop into a single lookup
</div>

<!--
SLIDE 20 - Choosing
On screen ~60 seconds. Close the chapter on the decision, not a summary.

The left table is the question to ask. The right table is why the answer
matters.

Point at the two membership rows and connect them to chapter three:
"Chercher dans une liste, c'est parcourir. Chercher dans un ensemble, c'est
calculer une adresse. Sur dix éléments, aucune différence. Sur cent mille,
c'est la différence entre instantané et une minute."

Then the hidden-quadratic line, which is the production insight:
"Et le piège : un test d'appartenance sur une liste, à l'intérieur d'une
boucle, c'est du n au carré. Il n'y a pas de boucle imbriquée visible dans
votre code. Elle est cachée dans le `in`."

PAUSE.

Mention deque briefly - insérer au début d'une liste décale tout, une deque
ne décale rien. Vingt secondes, pas plus.
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 06 — FILE I/O &amp; DATA FORMATS</strong>

</div>

<!--
SLIDE 21 - Closing card
On screen ~12 seconds.
Say the next chapter's topic out loud while this is up.
Then: "À mardi." Hold two beats of silence before you stop recording.
-->
