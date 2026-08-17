---
theme: ../themes/noonlabs
title: Functions & Scope — Chapter 04
info: NoonLabs - Module I, chapitre 04
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

<div class="nl-eyebrow">Chapter 04</div>

# Functions & Scope

<div class="mt-4" style="max-width: 42ch">

Naming a piece of behaviour, and knowing which names it can see

</div>

<div class="nl-type mt-6">
  <NlIcon name="box" /> Definition
  <span class="mx-3">·</span>
  <NlIcon name="split" /> Arguments
  <span class="mx-3">·</span>
  <NlIcon name="layers" /> Scope
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~8 seconds.

"Chapitre quatre. Jusqu'ici on écrivait des instructions. Maintenant on
leur donne un nom, et on les réutilise."

Frame the second half of the title, because scope sounds abstract until you
have been bitten:
"Et une fonction, ce n'est pas seulement du code qui a un nom. C'est du code
qui a son propre espace de noms. C'est la deuxième moitié du chapitre."
-->

---
layout: default
class: nl-deck
---

# Defining a Function

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> The anatomy</div>

```python
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"

result = greet("Alice")
```

<div class="nl-recap mt-3" style="font-size: 1.02rem">
  <div class="n">def</div><div><span class="why">creates the function object</span></div>
  <div class="n">name</div><div><span class="why">snake_case, verb-based</span></div>
  <div class="n">params</div><div><span class="why">what it needs</span></div>
  <div class="n">"""…"""</div><div><span class="why">what it promises</span></div>
</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="box" /> The docstring is the contract</div>

Short description first. Then `Args`, `Returns`, and `Raises` if it can fail.
Anyone calling your function should not need to read its body.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>calculate_area</code>, <code>get_user</code>, <code>is_valid</code></li>
<li class="nl-bad"><code>f</code>, <code>func</code>, <code>doStuff</code>, <code>process2</code></li>
</ul>

<div class="nl-type mt-3"><NlIcon name="prompt" /> Read it back</div>

<div style="font-size: 1.05rem">

`help(greet)` and `greet.__doc__` — the docstring lives on the object, exactly
as in chapter two.

</div>

</div>

</div>

<div class="nl-statement mt-3">
A function name is a promise. The docstring is the fine print.
</div>

<!--
SLIDE 3 - Anatomy
On screen ~55 seconds.

Name the shift explicitly, because it is the real subject of the chapter:
"`def` ne fait pas tourner le code. Il crée un objet - une fonction - et
lui colle une étiquette. Comme pour une variable. Le corps ne s'exécute que
quand vous appelez."

The naming rule is worth a beat, because it is a code-review reflex:
"Un nom de fonction commence par un verbe. `calculer`, `obtenir`,
`valider`. Si vous n'arrivez pas à trouver le verbe, votre fonction fait
probablement deux choses."

Then `help(greet)` in VS Code - callback to chapter two's docstring slide.
-->

---
layout: default
class: nl-deck
---

# return: One Value, None, or Many

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="arrow" /> One, or several</div>

```python
def square(x):
    return x ** 2

def min_max(xs):
    return min(xs), max(xs)

low, high = min_max([3, 1, 4])
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> No return at all</div>

```python
def show(name):
    print(name)      # returns None
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="split" /> What return actually does</div>

It **exits immediately** — nothing after it in the function runs. A function
with no `return` still returns `None`, and so does a bare `return`.

"Several values" is really one value: Python packs them into a tuple, and the
caller unpacks it. There is no special multiple-return mechanism.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Return a value; let the caller decide what to print</li>
<li class="nl-bad">Printing inside a function that should compute</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
A function that prints cannot be reused. A function that returns can.
</div>

<!--
SLIDE 4 - return
On screen ~50 seconds.

The tuple point removes a whole category of confusion:
"Il n'y a pas de « retour multiple » en Python. Vous renvoyez un tuple, et
l'appelant le déballe. C'est le même déballage qu'au chapitre deux."

Then the statement, and give it the production framing - this is the single
most common beginner mistake in function design:
"Une fonction qui affiche est inutilisable ailleurs. Vous ne pouvez pas la
tester, vous ne pouvez pas l'appeler depuis une autre fonction, vous ne
pouvez pas en réutiliser le résultat. Calculez et renvoyez. L'affichage,
c'est le travail de l'appelant."

PAUSE. Then: "C'est vrai pour print. C'est vrai aussi pour écrire dans un
fichier ou appeler une API."
-->

---
layout: default
class: nl-deck
---

# Positional, Keyword & Default Arguments

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="indent" /> Three ways to pass</div>

```python
def greet(first, last, sep=" "):
    return f"{first}{sep}{last}"

greet("Alice", "Smith")
greet(last="Smith", first="Alice")
greet("Alice", "Smith", sep="-")
```

<div class="nl-type mt-2"><NlIcon name="box" /> Rules</div>

<div style="font-size: 1.02rem">

Positional args must come first, and parameters with defaults must come after
those without.

</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="check" /> Keywords are documentation</div>

`send(data, True, False)` tells the reader nothing. `send(data, retry=True,
compress=False)` tells them everything — at the call site, where they are
looking.

<div class="nl-type mt-3"><NlIcon name="split" /> One fact to hold on to</div>

A default value is evaluated **once**, when the `def` line runs — not on each
call. For a number or a string that is invisible.

<div style="font-size: 1.02rem">

Remember it anyway. The next slide is about the case where it is not
invisible at all.

</div>

</div>

</div>

<div class="nl-statement mt-3">
Pass anything ambiguous by keyword — the reader is at the call, not the def
</div>

<!--
SLIDE 5 - Arguments
On screen ~55 seconds.

The boolean-argument point lands with everyone who has read someone else's
code:
"`envoyer(données, vrai, faux)`. Qu'est-ce que ça veut dire ? Il faut aller
lire la définition. Avec des mots-clés, la réponse est sous vos yeux."

Then PLANT the payoff, calmly, and do NOT explain the consequence:
"Et une chose à retenir, sans que je vous dise encore pourquoi : la valeur
par défaut est évaluée UNE fois, quand la ligne `def` est lue. Pas à chaque
appel."

PAUSE.

"Pour un nombre, ça ne change rien. Diapositive suivante."
-->

---
layout: default
class: nl-deck
---

# The Mutable Default Trap

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Looks harmless</div>

```python
def add(item, items=[]):
    items.append(item)
    return items

add("a")   # ['a']
add("b")   # ['a', 'b']  ← !
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> The fix</div>

```python
def add(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why it happens</div>

The default was evaluated once, so **one list** exists — attached to the
function object itself. Every call that omits the argument appends to that
same list.

This is chapter two's lesson with teeth: the name `items` points at an object,
and that object outlives the call.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-bad">Never default to <code>[]</code>, <code>{}</code>, or <code>set()</code></li>
<li class="nl-good">Default to <code>None</code>, build inside the body</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Mutable defaults are shared across every call — use <code>None</code> instead
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 6 - Mutable defaults
On screen ~70 seconds. THIS IS THE CHAPTER'S PAYOFF. Do it live, do not
narrate over the slide.

In VS Code, define the broken version. Call add("a"). Then call add("b").

PAUSE on the output. Let them read ['a', 'b'].

"On n'a jamais passé la liste. On s'attendait à ['b']. Où est le 'a' ?"

Then the explanation, tied straight back to the previous slide:
"Souvenez-vous : la valeur par défaut est évaluée une fois. Une seule liste
a été créée, au moment du `def`. Elle est accrochée à la fonction. Chaque
appel écrit dans la même liste."

Show it: add.__defaults__ - the list is right there on the object.

Then the chapter-two callback, which is the real lesson:
"Un nom pointe sur un objet. Cet objet survit à l'appel. C'est exactement ce
qu'on disait au chapitre deux, sauf que là ça coûte cher."

Close on the rule: jamais de liste, de dictionnaire ou d'ensemble comme
valeur par défaut. None, et on construit dans le corps.
-->

---
layout: default
class: nl-deck
---

# *args and **kwargs

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> Collect what you did not name</div>

```python
def total(*args):        # a tuple
    return sum(args)

def config(**kwargs):    # a dict
    for k, v in kwargs.items():
        print(k, v)
```

<div class="nl-type mt-2"><NlIcon name="arrow" /> The same stars unpack</div>

```python
total(*[1, 2, 3])        # 6
config(**{"debug": True})
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> One star, two directions</div>

In a **definition**, `*` collects extra positional arguments into a tuple and
`**` collects extra keyword arguments into a dict.

At a **call**, the same symbols do the reverse — they spread a sequence or a
mapping back out into individual arguments.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Wrappers that forward arguments they do not care about</li>
<li class="nl-bad">A signature nobody can read — <code>**kwargs</code> hides the API</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
In a def they gather. At a call they spread. Same symbol, opposite direction.
</div>

<!--
SLIDE 7 - args and kwargs
On screen ~60 seconds.

The gather-versus-spread symmetry is the whole slide, and stating it once
saves people months of confusion:
"Le même symbole fait deux choses opposées selon l'endroit. Dans la
définition, l'étoile RASSEMBLE. À l'appel, elle DISPERSE."

Say the names are conventions, not keywords:
"`args` et `kwargs`, ce ne sont que des noms. Ce qui compte, c'est l'étoile.
Vous pourriez écrire `*nombres`. Mais tout le monde écrit args, donc écrivez
args."

Then the honest warning, because **kwargs is over-used:
"Attention quand même. Une fonction avec juste `**kwargs` dans sa signature
ne documente rien. L'appelant ne sait pas quoi passer. Utilisez-le pour
transmettre, pas pour éviter de réfléchir à votre API."
-->

---
layout: default
class: nl-deck
---

# Argument Ordering Rules

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="indent" /> The full signature</div>

```python
def f(pos_only, /, standard,
      *args, kw_only, **kwargs):
    ...
```

<div class="nl-recap mt-3" style="font-size: 1.02rem">
  <div class="n">before /</div><div><span class="why">positional only</span></div>
  <div class="n">middle</div><div><span class="why">positional or keyword</span></div>
  <div class="n">*args</div><div><span class="why">extra positionals</span></div>
  <div class="n">after *</div><div><span class="why">keyword only</span></div>
  <div class="n">**kwargs</div><div><span class="why">extra keywords</span></div>
</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="check" /> The two markers earn their keep</div>

A bare `*` forces everything after it to be passed by name. That is how you
stop `send(data, True, False)` from being possible at all.

A `/` marks parameters that **cannot** be named — useful when the parameter
name is an implementation detail you may want to rename later.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>def send(data, *, retry=False)</code></li>
<li class="nl-bad">Booleans that can be passed positionally</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
A bare <code>*</code> in a signature makes the call site explain itself
</div>

<!--
SLIDE 8 - Ordering
On screen ~55 seconds.

The ordering table is reference material - read it once, quickly.

The bare `*` is the part worth selling, because it is the design tool almost
nobody teaches:
"Regardez `def envoyer(données, *, retry=False)`. L'étoile toute seule veut
dire : tout ce qui suit doit être nommé. Il devient IMPOSSIBLE d'écrire
`envoyer(données, vrai)`."

PAUSE.

"C'est de la conception d'API. Vous ne demandez pas gentiment à l'appelant
d'être lisible - vous rendez l'illisible impossible."

The `/` is thirty seconds: it exists so a library author can rename a
parameter without breaking anyone. Most of you will read it more than write
it.
-->

---
layout: default
class: nl-deck
---

# Lambda: Functions as Values

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> The same function, twice</div>

```python
def square(x):
    return x ** 2

square = lambda x: x ** 2
```

<div class="nl-type mt-2"><NlIcon name="check" /> Where it belongs</div>

```python
sorted(names, key=lambda s: s.lower())
sorted(rows, key=lambda r: r["age"])
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Functions are objects</div>

A function is a value like any other: you can store it, pass it to another
function, or return it. `sorted(..., key=...)` works because it takes a
function as an argument.

`lambda` is nothing more than a way to write a small one without giving it a
name. One expression, implicit return, no statements.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">A throwaway key or callback, inline</li>
<li class="nl-bad">Assigning one to a name — just use <code>def</code></li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
If your lambda needs a name, it needed a <code>def</code>
</div>

<!--
SLIDE 9 - Lambda
On screen ~55 seconds.

Lead with first-class functions, not with the lambda syntax. That is the
concept; lambda is a detail:
"Une fonction est une valeur. Vous pouvez la ranger dans une variable, la
passer en argument, la renvoyer. C'est pour ça que `sorted` peut prendre une
fonction en paramètre `key`."

Then lambda as convenience: "Et lambda, c'est juste une façon d'en écrire une
petite sans lui donner de nom."

The rule at the end is the one that matters, and PEP 8 agrees:
"Si vous écrivez `carré = lambda x: ...`, vous venez de donner un nom à une
fonction anonyme. Écrivez `def`. Vous y gagnez un nom dans les traces
d'erreur, une docstring, et des annotations."

Demo sorted with key in VS Code - two lines, and the value is obvious.
-->

---
layout: default
class: nl-deck
---

# Scope: The LEGB Rule

<div class="nl-cols mt-4">

<div>

<div class="nl-recap mt-1" style="font-size: 1.05rem">
  <div class="n">L</div><div><span class="what">Local</span> &nbsp;<span class="why">inside this function</span></div>
  <div class="n">E</div><div><span class="what">Enclosing</span> &nbsp;<span class="why">a function around it</span></div>
  <div class="n">G</div><div><span class="what">Global</span> &nbsp;<span class="why">module level</span></div>
  <div class="n">B</div><div><span class="what">Built-in</span> &nbsp;<span class="why">print, len, list</span></div>
</div>

<div class="nl-type mt-3"><NlIcon name="file" /> Three x, one name</div>

```python
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)    # local
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="arrow" /> Reading searches outward</div>

Python looks in the local scope, then any enclosing function, then the module,
then the builtins — and stops at the first match.

<div class="nl-type mt-3"><NlIcon name="split" /> Writing does not</div>

Assigning to a name makes it **local for the whole function**, from the first
line. That is why reading a global then assigning to it raises
`UnboundLocalError`.

<div style="font-size: 1.02rem">

This is also why shadowing a builtin hurts: name a variable `list` and the B
in LEGB is never reached.

</div>

</div>

</div>

<div class="nl-statement mt-3">
Reading looks outward. Assigning creates a local — always.
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 10 - LEGB
On screen ~65 seconds.

Read the ladder once, then get to the asymmetry, which is the actual lesson:
"La lecture cherche vers l'extérieur. L'affectation, non. Dès que vous
assignez un nom dans une fonction, ce nom est local - pour toute la
fonction, dès la première ligne."

Demo the UnboundLocalError live. It is the confusing one:

count = 0
def bump():
    print(count)   # UnboundLocalError
    count = count + 1

"Python a lu toute la fonction avant de l'exécuter. Il a vu une affectation.
Donc `count` est local. Donc le print lit une variable locale qui n'existe
pas encore."

PAUSE. This explains a bug they will absolutely hit.

Then the builtin callback to chapter two: appeler une variable `list` casse
le B de LEGB.
-->

---
layout: default
class: nl-deck
---

# global and nonlocal

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> global</div>

```python
count = 0

def bump():
    global count
    count += 1
```

<div class="nl-type mt-2"><NlIcon name="split" /> nonlocal</div>

```python
def counter():
    n = 0
    def step():
        nonlocal n
        n += 1
        return n
    return step
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> What they really are</div>

Both are declarations, not assignments: they tell Python *"this name is not
local"*. `global` reaches the module level; `nonlocal` reaches the nearest
enclosing function.

`counter` above is a **closure** — `step` keeps access to `n` after `counter`
has returned. That is the useful half of the enclosing scope.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-bad"><code>global</code> — almost always return a value instead</li>
<li class="nl-good"><code>nonlocal</code> — for closures, which is what it is for</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Two functions sharing a global are two functions you cannot test separately
</div>

<!--
SLIDE 11 - global and nonlocal
On screen ~60 seconds.

Be direct about global. Do not present it neutrally:
"`global` marche. Et dans du code de production, c'est presque toujours le
mauvais choix. Une fonction qui modifie un état global ne se teste pas
isolément - son résultat dépend de ce qui s'est passé avant."

PAUSE.

"La correction est presque toujours la même : prenez la valeur en paramètre,
renvoyez la nouvelle valeur."

`nonlocal` is different and worth defending, because closures are genuinely
useful. Run `counter` in VS Code: call step() three times, and show that `n`
survives even though `counter` has already returned.

"C'est ça, une fermeture. La fonction interne garde son environnement. On
s'en resservira quand on fera les décorateurs."
-->

---
layout: default
class: nl-deck
---

# Type Hints: The Modern Syntax

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> Write this</div>

```python
def greet(name: str) -> str: ...

def tally(xs: list[int]) -> dict[str, int]:

def find(x: str) -> int | None: ...
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> Not this any more</div>

```python
from typing import List, Dict, Optional
def tally(xs: List[int]) -> Dict[str, int]:
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> The syntax changed</div>

Since 3.9 the builtin containers are subscriptable, so `list[int]` needs no
import. Since 3.10, `X | None` replaces `Optional[X]` and `X | Y` replaces
`Union[X, Y]`.

<div class="nl-recap mt-3" style="font-size: 1.02rem">
  <div class="n">List[int]</div><div><span class="why">→ <code>list[int]</code></span></div>
  <div class="n">Dict[str, int]</div><div><span class="why">→ <code>dict[str, int]</code></span></div>
  <div class="n">Optional[int]</div><div><span class="why">→ <code>int | None</code></span></div>
  <div class="n">Union[str, int]</div><div><span class="why">→ <code>str | int</code></span></div>
</div>

</div>

</div>

<div class="nl-statement mt-3">
You will read the old form in existing code — write the new one
</div>

<!--
SLIDE 12 - Type hints syntax
On screen ~55 seconds.

Say plainly that most tutorials online are out of date here, because they
will notice the mismatch and it undermines trust if you do not name it:
"Si vous cherchez « python type hints » aujourd'hui, la moitié des résultats
vous montrera `from typing import List`. Ce n'est pas faux, c'est vieux. Ça
date d'avant Python 3.9."

Then the two changes, and why they happened:
"Depuis 3.9, les types intégrés s'écrivent en minuscules et sans import.
Depuis 3.10, la barre verticale remplace Optional et Union. C'est plus court
et ça se lit."

The table is the translation guide. Tell them to screenshot it.

Close on the honest bit: vous LIREZ l'ancienne forme, dans du code existant
et dans des bibliothèques. Sachez la reconnaître. Mais n'en écrivez plus.
-->

---
layout: default
class: nl-deck
---

# What Type Hints Do and Do Not Do

<div class="nl-cols mt-4">

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> They are not enforced</div>

Python does not check them at runtime. `greet(42)` runs happily, annotation or
not. Hints are metadata, and nothing raises on its own.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> A checker enforces them</div>

`mypy` reads your annotations and fails the build before anything runs:

<div style="font-size: 1rem">

`error: Argument 1 to "greet" has incompatible type "int"; expected "str"`

</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why bother, then</div>

- The editor can complete and refactor with confidence
- The signature documents itself, and cannot drift from the code
- A whole class of bug is caught in CI instead of in production

<div class="nl-type mt-3"><NlIcon name="check" /> Where to start</div>

<ul style="font-size: 1.05rem">
<li class="nl-good">Annotate public functions first</li>
<li class="nl-good">Run <code>mypy</code> in CI, not just locally</li>
<li class="nl-bad">Annotating every local variable</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Hints are a promise to the reader — <code>mypy</code> is what makes it a check
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 13 - What hints do
On screen ~60 seconds.

Kill the misconception first, because it is universal:
"Une annotation n'empêche rien. Vous pouvez passer un entier à une fonction
qui annonce une chaîne, et Python l'exécutera sans broncher."

Demo it: greet(42) runs and produces "Hello, 42!".

PAUSE.

"Alors à quoi ça sert ? À rien - tant que vous ne lancez pas de
vérificateur."

Then run mypy on the same file in the terminal and let it fail. That contrast
is the whole slide: same code, Python says yes, mypy says no.

"C'est ça, la différence entre un tutoriel et de la production. Le tutoriel
annote pour faire joli. En production, mypy tourne dans la CI et bloque la
fusion."

Point at the starter template: mypy strict is already configured there.
-->

---
layout: default
class: nl-deck
---

# if __name__ == "__main__"

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> The pattern</div>

```python
# calculator.py
def add(a, b):
    return a + b

def main():
    print(f"2 + 3 = {add(2, 3)}")

if __name__ == "__main__":
    main()
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> One file, two roles</div>

`__name__` is `"__main__"` when the file is run directly, and the module's own
name when it is imported. So the guard lets one file be **both** a script and
a library.

Without it, `import calculator` would execute your demo code — printing,
writing files, hitting the network — as a side effect of importing.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Put the work in <code>main()</code>, call it under the guard</li>
<li class="nl-bad">Loose statements at module level that run on import</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Importing a module should never <em>do</em> anything
</div>

<!--
SLIDE 14 - main guard
On screen ~55 seconds.

Callback to chapter one, and it closes a loop nicely:
"Au chapitre un, on a dit : l'invite c'est pour demander, le fichier c'est
pour garder. Voilà comment un fichier devient les deux à la fois - un script
qu'on lance, et un module qu'on importe."

Demo the failure, because that is what makes the guard obvious. Remove the
guard, import the module from another file, and let the demo output appear
uninvited.

"Vous avez juste importé. Et le programme a tourné. Imaginez que ce code
écrive dans une base de données."

PAUSE.

Then the habit: tout ce qui agit va dans main(). Le niveau du module ne
contient que des définitions.
-->

---
layout: default
class: nl-deck
---

# map(), filter(), reduce()

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="arrow" /> Apply, keep, fold</div>

```python
list(map(str.upper, names))
list(filter(str.isdigit, tokens))

from functools import reduce
reduce(lambda a, b: a * b, nums)
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Usually clearer</div>

```python
[n.upper() for n in names]
[t for t in tokens if t.isdigit()]
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Know them, reach for them rarely</div>

`map` and `filter` return **lazy iterators** — nothing runs until you consume
them, and consuming them empties them, exactly as with `zip`.

A comprehension does the same job in fewer moving parts, and Python's own
style guide prefers it.

<div class="nl-type mt-3"><NlIcon name="check" /> Better than reduce</div>

<div style="font-size: 1.05rem">

`sum()`, `min()`, `max()`, `any()`, `all()`, `math.prod()` — a named builtin
beats a fold nobody can read.

</div>

</div>

</div>

<div class="nl-statement mt-3">
If a builtin already has a name for it, use the name
</div>

<!--
SLIDE 15 - functional helpers
On screen ~55 seconds.

Be honest that this is cultural knowledge more than daily tooling:
"Vous allez rencontrer map et filter dans du code existant, et dans d'autres
langages ils sont partout. En Python, la compréhension de liste fait la même
chose plus lisiblement - et c'est ce que recommande le guide de style."

The laziness point pays off chapter three:
"Et attention : map et filter renvoient des itérateurs paresseux. Comme zip.
Vous les consommez une fois, et ils sont vides."

Then reduce, and be blunt:
"reduce demande un import, et neuf fois sur dix il existe déjà une fonction
avec un nom. `sum`. `max`. `any`. `math.prod`. Un nom vaut mieux qu'un pli."

Note we will meet comprehensions properly in chapter five.
-->

---
layout: default
class: nl-deck
---

# Functions You Can Trust

<div class="nl-cols mt-4" style="font-size: 1.05rem">

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> One job, named by a verb</div>

If the docstring needs the word "and", the function probably needs splitting.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Return early, stay flat</div>

Guard clauses at the top, the real work unindented below — the same fix for
nesting we used in chapter three.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Pure where you can</div>

Takes inputs, returns an output, touches nothing else. Those are the functions
you can test without building a world first.

</div>

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Hidden side effects</div>

Printing, writing files, calling APIs, mutating an argument. Necessary — but
keep them in a thin layer, not scattered through your logic.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> Too many parameters</div>

More than about four usually means a missing object, or a function doing two
jobs.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> Deep recursion</div>

Elegant on trees, but Python caps the stack near 1000 frames and does not
optimise tail calls. For depth, iterate.

</div>

</div>

<div class="nl-statement mt-3">
A function you can test without setting up the world is a function you can trust
</div>

<!--
SLIDE 16 - Design
On screen ~65 seconds. Close the chapter on judgement, not syntax.

The "and" test is a gift - it is a rule they can apply today without
experience:
"Écrivez la docstring d'abord. Si vous avez besoin du mot « et » pour
décrire ce que fait la fonction, coupez-la en deux."

Guard clauses tie back to chapter three:
"Au chapitre trois on a dit : sortez tôt pour éviter l'imbrication. Dans une
fonction, sortir tôt s'appelle un return anticipé, et c'est la même
victoire."

Purity is the production point, and it is worth the full explanation:
"Une fonction pure prend des entrées et renvoie une sortie. Elle ne lit pas
de global, elle n'écrit pas de fichier, elle ne modifie pas ses arguments.
Vous pouvez la tester en une ligne. Une fonction qui fait dix choses demande
de reconstruire tout un contexte avant de pouvoir l'appeler."

PAUSE on the statement - it is the sentence that carries the chapter.

Recursion gets twenty seconds and no more. Mention sys.setrecursionlimit
exists and that reaching for it is usually a sign to iterate instead.
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 05 — DATA STRUCTURES</strong>

</div>

<!--
SLIDE 17 - Closing card
On screen ~12 seconds.
Say the next chapter's topic out loud while this is up.
Then: "À mardi." Hold two beats of silence before you stop recording.
-->
