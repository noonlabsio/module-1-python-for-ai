---
theme: ../themes/noonlabs
title: Control Flow & Loops — Chapter 03
info: NoonLabs - Module I, chapitre 03
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

<div class="nl-eyebrow">Chapter 03</div>

# Control Flow & Loops

<div class="mt-4" style="max-width: 42ch">

Deciding what runs, and repeating work without repeating yourself

</div>

<div class="nl-type mt-6">
  <NlIcon name="split" /> Conditionals
  <span class="mx-3">·</span>
  <NlIcon name="arrow" /> Iteration
  <span class="mx-3">·</span>
  <NlIcon name="layers" /> Complexity
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~8 seconds.

"Chapitre trois. Jusqu'ici, nos programmes lisaient de haut en bas, une
ligne après l'autre. À partir de maintenant, ils choisissent, et ils
répètent."

Restate the format so nobody wonders:
"Les diapositives, c'est pour les concepts. Le code, on l'écrit ensemble
dans VS Code."
-->

---
layout: default
class: nl-deck
---

# if, elif, else

<div class="nl-cols mt-4">

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="indent" /> The shape</div>

- `if condition:` then an indented block
- The colon is required; the indent is the block
- `elif` chains as many tests as you need
- `else` catches everything left over, and is optional

<div class="nl-type mt-3"><NlIcon name="arrow" /> How it executes</div>

Conditions are tested **top to bottom**. The first true branch runs, and every
remaining branch is skipped — even if it would also be true.

</div>

<div>

<div class="nl-type"><NlIcon name="file" /> A chain</div>

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
```

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Order branches by likelihood, then by narrowness</li>
<li class="nl-bad">Deep nesting — return or continue early instead</li>
</ul>

</div>

</div>

<div class="nl-statement mt-4">
Only the first true branch runs — the order is part of the logic
</div>

<!--
SLIDE 3 - Conditionals
On screen ~55 seconds.

The thing that bites beginners is not the syntax, it is the ordering. Point
at the chain and reverse it out loud:
"Si vous mettiez « supérieur à soixante » en premier, un score de
quatre-vingt-quinze recevrait un D. La condition est vraie, donc elle
gagne. L'ordre n'est pas cosmétique - c'est la logique."

PAUSE.

On nesting, give them the production habit:
"Trois niveaux d'indentation dans un if, c'est un signe. Sortez tôt avec un
return, et le reste du corps redevient plat et lisible."

Recall chapter two in one line: everything in the condition is evaluated for
truthiness, so an empty list is already false. No need to write `len(x) == 0`.
-->

---
layout: default
class: nl-deck
---

# Ternary Expressions

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> The form</div>

```python
value_if_true if cond else value_if_false
```

<div class="nl-type mt-2"><NlIcon name="check" /> In practice</div>

```python
status = "adult" if age >= 18 else "minor"
return x if x > 0 else 0
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why it exists</div>

`if` is a **statement** — it does something. A ternary is an **expression** —
it *is* a value. So it fits where a statement cannot: inside a function call,
a comprehension, an f-string, a default argument.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Choosing between two values</li>
<li class="nl-good">A single return with two outcomes</li>
<li class="nl-bad">Two actions — that needs a real <code>if</code></li>
<li class="nl-bad">Chaining them: <code>a if x else b if y else c</code></li>
</ul>

</div>

</div>

<div class="nl-statement mt-4">
A ternary chooses a value. It does not do two things.
</div>

<!--
SLIDE 4 - Ternary
On screen ~50 seconds. Concept slide, no live coding needed.

The statement-versus-expression distinction is the whole slide, and almost
nobody teaches it:
"Un if fait quelque chose. Un ternaire EST quelque chose. C'est pour ça
qu'on peut le mettre dans un appel de fonction, et pas un if."

Read the form out loud in English order once - it reads like a sentence, and
that is the point:
"Ceci, si la condition, sinon cela."

Then the limit, stated as a rule they can apply without judgement:
"Si vous avez besoin de deux ternaires imbriqués, écrivez un if. La
question n'est pas « est-ce que ça marche » - c'est « est-ce qu'on le relit
dans six mois »."
-->

---
layout: default
class: nl-deck
---

# Structural Pattern Matching (3.10+)

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="split" /> match / case</div>

```python
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown")
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Not a switch statement</div>

There is **no fall-through** — the first matching case runs and the block
ends. `case _` is the wildcard, and it is the only way to catch the rest.

A `match` with no matching case simply does nothing. No error, no default.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Several discrete values, or a shape to take apart</li>
<li class="nl-bad">Two branches — an <code>if</code> is shorter and clearer</li>
</ul>

</div>

</div>

<div class="nl-statement mt-4">
<code>match</code> tests the shape of a value, not only its value
</div>

<!--
SLIDE 5 - match/case, part one
On screen ~55 seconds.

Set the expectation before they map it onto something they know:
"Si vous venez de C ou de JavaScript, vous allez penser « switch ». Ce
n'est pas ça. Il n'y a pas de fall-through, et il n'y a pas de break à
écrire."

The silent no-match is worth calling out, because it is a real source of
bugs:
"Et attention : si aucun cas ne correspond et qu'il n'y a pas de
case underscore, il ne se passe rien. Pas d'erreur. Rien."

PAUSE.

Then honesty about when not to use it:
"Pour deux cas, un if reste plus court. match commence à payer à partir de
trois ou quatre, ou dès qu'on veut décomposer une structure - ce qu'on voit
sur la diapositive suivante."
-->

---
layout: default
class: nl-deck
---

# Patterns, Captures & Guards

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> Take the shape apart</div>

```python
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"X-axis at {x}")
    case (x, y):
        print(f"Point ({x}, {y})")
```

<div class="nl-type mt-2"><NlIcon name="check" /> Add a condition</div>

```python
case n if n < 13:
    print("Child")
```

</div>

<div style="font-size: 1.05rem">

<div class="nl-type"><NlIcon name="layers" /> What can be a pattern</div>

- **Literals** — numbers, strings, `True`, `None`
- **Sequences** — tuples and lists, with `*rest`
- **Mappings** — dictionaries, by key
- **Classes** — by type and attribute
- `_` — the wildcard, matching anything

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> The one real trap</div>

A bare name in a pattern **captures**, it does not compare. `case LIMIT:`
matches everything and rebinds `LIMIT`. To compare against a constant, use a
dotted name: `case Status.OK:`.

</div>

</div>

<div class="nl-statement mt-3">
A pattern names the parts while it tests the shape
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 6 - Patterns and guards
On screen ~65 seconds.

Destructuring is the feature, so demo it in VS Code rather than describing
it. Take a tuple apart, then a dictionary, then add a guard.

"Regardez ce que fait `case (x, 0)`. Il teste la forme - un couple dont le
second élément vaut zéro - ET il donne un nom au premier. Un test et une
affectation, en même temps."

The capture trap deserves its own thirty seconds, because it fails silently
and everyone hits it once:
"Un nom tout seul dans un case ne compare pas. Il capture. Si vous écrivez
`case LIMITE`, ça matche TOUT, et ça écrase votre constante. Pour comparer,
il faut un nom pointé : `Statut.OK`."

Show it failing live. Reading about this does not stick.
-->

---
layout: default
class: nl-deck
---

# for Loops & the Iterable Protocol

<div class="nl-cols mt-4">

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="arrow" /> A for loop does not count</div>

It asks the object for an **iterator**, then asks that iterator for the next
item until it says there are none left. The object decides the order.

That is why the same `for` works on a list, a string, a dictionary, an open
file, or something that generates values as you go.

<div class="nl-type mt-3"><NlIcon name="split" /> And it is one-way</div>

An iterator is **consumed** as you walk it. Once exhausted, it is empty —
not rewound. Remember that; it comes back later in this chapter.

</div>

<div>

<div class="nl-type"><NlIcon name="file" /> The same loop, four sources</div>

```python
for fruit in fruits:      # list
for char in "Python":     # str
for line in open(path):   # file
for key in config:        # dict
```

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Iterate the object itself</li>
<li class="nl-bad"><code>for i in range(len(items))</code> — almost never</li>
</ul>

</div>

</div>

<div class="nl-statement mt-4">
A for loop asks the object for an iterator — the object decides the order
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 7 - for loops
On screen ~60 seconds. This slide sets up two later payoffs, so do not rush.

"En Python, un for ne compte pas. Il demande. Il dit à l'objet : donne-moi
ton itérateur. Puis il demande l'élément suivant, jusqu'à ce que l'objet
dise stop."

Demo the four sources in VS Code - list, string, file, dict. Four different
things, one loop. That is the protocol made visible.

Then PLANT the payoff and do not explain it:
"Et un itérateur se consomme. Quand il est épuisé, il est vide - pas
rembobiné. Retenez ça. On y revient sur la diapositive de zip."

Callback to chapter two: iterating a string works because a string is a
sequence of characters - the same boxes we drew for slicing.
-->

---
layout: default
class: nl-deck
---

# range(): start, stop, step

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> Three forms</div>

```python
range(5)          # 0 1 2 3 4
range(2, 6)       # 2 3 4 5
range(0, 10, 2)   # 0 2 4 6 8
range(5, 0, -1)   # 5 4 3 2 1
```

<div class="nl-type mt-2"><NlIcon name="box" /> Defaults</div>

<div style="font-size: 1.05rem">

`start` is `0`, `step` is `1`, and `stop` is required — and excluded.

</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> It is not a list</div>

`range` stores three integers and computes each value on demand. So
`range(10**9)` is instant and costs nothing, while the list of a billion
numbers would not fit in memory.

It still behaves like a sequence: `len()`, indexing, and `in` all work — and
`in` is O(1) because it does arithmetic rather than a search.

<div class="nl-type mt-3"><NlIcon name="check" /> Where it belongs</div>

<div style="font-size: 1.05rem">

Counting and arithmetic sequences. **Not** for walking a collection you
already have.

</div>

</div>

</div>

<div class="nl-statement mt-4">
<code>range</code> stores three numbers, not a million
</div>

<!--
SLIDE 8 - range
On screen ~55 seconds.

`stop` being excluded is the same asymmetry as slicing in chapter two.
Say the connection out loud, it saves them relearning it:
"Fin exclue. Exactement comme les tranches. `range(5)` donne cinq valeurs,
de zéro à quatre."

The laziness is the interesting part, so demo it:
range(10**9) is instant. list(range(10**9)) is not - do NOT actually run the
second one on camera, just say what would happen.

"Trois entiers en mémoire. C'est tout. Le milliard de valeurs n'existe
jamais en même temps."

Close with the rule that makes the next slides land:
"Utilisez range pour compter. Pour parcourir une collection que vous avez
déjà, il y a mieux - et c'est la diapositive sur enumerate."
-->

---
layout: default
class: nl-deck
---

# while Loops & Sentinel Patterns

<div class="nl-cols mt-4">

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="split" /> When the count is unknown</div>

A `for` loop needs something to walk. A `while` loop needs a condition that
can **become false** — and something in the body has to make that happen.

Reading until end of file, validating input, waiting for a state, driving a
game loop: none of these know their length in advance.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> The failure mode</div>

If nothing in the body changes the condition, the loop never ends. That is
not a Python quirk — it is the whole risk of `while`.

</div>

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> The sentinel form</div>

```python
while True:
    raw = input("A number: ")
    try:
        n = int(raw)
        break
    except ValueError:
        print("Try again.")
```

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>while True</code> plus an explicit <code>break</code></li>
<li class="nl-bad">A flag variable you have to keep in sync</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
A <code>while</code> loop is a promise that something will change
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 9 - while
On screen ~60 seconds.

Frame the choice first, so `while` does not look like a worse `for`:
"On utilise while quand on ne sait pas combien de fois. Lire un fichier
jusqu'au bout. Attendre une saisie correcte. Ces boucles n'ont pas de
longueur connue à l'avance."

Then the honest part about `while True`:
"Ça a l'air dangereux, et c'est en fait la forme la plus claire. Une
condition compliquée en haut de la boucle est plus dure à relire qu'un
`while True` avec un break explicite là où la sortie a lieu."

Demo the validation loop live and type a bad value on purpose. The
try/except is chapter two's ValueError, so name the callback.

Truthiness callback: `while items:` is enough. No `len(items) > 0`.
-->

---
layout: default
class: nl-deck
---

# Choosing a Loop

<div class="nl-cols mt-4" style="font-size: 1.05rem">

<div>

<div class="nl-type"><NlIcon name="arrow" /> Reach for <code>for</code></div>

<div class="nl-recap mt-2">
  <div class="n">collection</div><div><span class="why">you already have the items</span></div>
  <div class="n">count known</div><div><span class="why">n times, or a range</span></div>
  <div class="n">definite</div><div><span class="why">it ends because the data ends</span></div>
</div>

<div class="nl-type mt-3"><NlIcon name="split" /> Reach for <code>while</code></div>

<div class="nl-recap mt-2">
  <div class="n">unknown</div><div><span class="why">until a condition flips</span></div>
  <div class="n">external</div><div><span class="why">input, network, a device</span></div>
  <div class="n">waiting</div><div><span class="why">retry, poll, game loop</span></div>
</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Three shapes cover most loops</div>

- **Accumulate** — build one result from many items
- **Search** — stop as soon as you find it
- **Transform** — produce a new collection from an old one

Name which one you are writing before you write it, and the body usually
falls out on its own.

<div style="font-size: 1.02rem">

If you find yourself incrementing a counter by hand inside a `while`, you
almost certainly wanted a `for`.

</div>

</div>

</div>

<div class="nl-statement mt-3">
<code>for</code> by default. <code>while</code> when you cannot know the count.
</div>

<!--
SLIDE 10 - Choosing
On screen ~50 seconds. Pure concept, stays on the slide.

The three shapes are the useful part - most beginners write loops without
deciding what kind of loop it is:
"Avant d'écrire une boucle, dites lequel des trois vous écrivez. Accumuler,
chercher, transformer. Une fois nommé, le corps s'écrit presque tout seul."

Then the counter heuristic, which is a real code-review reflex:
"Si vous incrémentez un compteur à la main dans un while, vous vouliez un
for. Neuf fois sur dix."

Mention that "transformer" has a shorter form we will meet later
(comprehensions) without naming the chapter.
-->

---
layout: default
class: nl-deck
---

# break, continue, pass

<div class="grid grid-cols-3 gap-6 mt-4" style="font-size: 0.98rem">

<div class="nl-card">

<div class="nl-type"><NlIcon name="cross" /> break</div>

Leaves the loop immediately. The rest of the body and every remaining item are
skipped.

Use for: search — stop when found.

</div>

<div class="nl-card">

<div class="nl-type"><NlIcon name="arrow" /> continue</div>

Skips the rest of this iteration and moves to the next item. The loop itself
carries on.

Use for: filtering — reject and move on.

</div>

<div class="nl-card">

<div class="nl-type"><NlIcon name="box" /> pass</div>

Does nothing at all. It exists because Python needs a statement where a block
is syntactically required.

Use for: a placeholder you will fill.

</div>

</div>

<div class="nl-cols mt-3" style="font-size: 1.05rem">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> The nesting trap</div>

`break` leaves the **innermost** loop only. From a nested loop it does not
escape both — extract a function and `return`, or use a flag.

</div>

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> pass is not continue</div>

`pass` falls through to the rest of the body. `continue` skips it. Swapping
them silently changes behaviour.

</div>

</div>

<div class="nl-statement mt-3">
<code>break</code> escapes one loop — nesting does not change that
</div>

<!--
SLIDE 11 - Loop control
On screen ~55 seconds.

The three cards are twenty seconds. The two notes underneath are the lesson.

The pass-versus-continue confusion is worth demonstrating, because the source
material for this chapter gets it wrong in a way that is instructive: with
`pass`, the print still runs, so the output is 0 1 2 3 4. With `continue`, it
does not: 0 1 3 4. Same shape, different output.

"Ces deux mots ressemblent au même geste. Ils sont opposés. `pass` ne fait
rien et continue dans le corps. `continue` saute le reste du corps."

Then the nesting point, said plainly:
"Un break sort d'UNE boucle. La plus proche. Si vous êtes dans deux boucles
imbriquées, vous êtes encore dans la première. La solution propre : extraire
une fonction et faire return."
-->

---
layout: default
class: nl-deck
---

# The else Clause on Loops

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="check" /> Search, then report</div>

```python
for item in items:
    if item == target:
        print("Found")
        break
else:
    print("Not found")
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> Without it</div>

```python
found = False
for item in items:
    if item == target:
        found = True
        break
if not found:
    print("Not found")
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Read it as "no break"</div>

The `else` on a loop runs **only if the loop finished without breaking**. It
is not the else of an `if`, and the keyword is genuinely badly named.

Say "no break" in your head every time you read it and it stops being
strange.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Search loops, validation, primality tests</li>
<li class="nl-good">Removes the flag variable entirely</li>
<li class="nl-bad">Any loop with no <code>break</code> — then it always runs</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Loop <code>else</code> means "no break happened" — read it that way
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 12 - for/else
On screen ~60 seconds.

Do not defend the keyword. Say it is badly named and give them the
translation:
"Ce mot-clé est mal choisi, tout le monde est d'accord. Ne lisez pas
« sinon ». Lisez « si aucun break ». À chaque fois."

Then the comparison, and let the flag version look as heavy as it is:
"À gauche en haut, cinq lignes. En dessous, huit lignes et une variable à
tenir à jour. C'est le même programme."

Demo both in VS Code with a target that is absent, then present. Two runs,
fifteen seconds, and the semantics are clear.

The trap to state before someone discovers it: on a loop with no break at
all, the else always runs - which means it was pointless.
-->

---
layout: default
class: nl-deck
---

# enumerate(): Index and Value

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Counting by hand</div>

```python
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Asking for both</div>

```python
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

for i, fruit in enumerate(fruits, 1):
    print(f"{i}: {fruit}")
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> What it gives you</div>

`enumerate(iterable, start=0)` yields `(index, value)` pairs. The second
argument only changes the number reported — it does not skip anything.

It works on **any** iterable, including ones with no length and no indexing:
a file, a generator, a stream.

<div class="nl-type mt-3"><NlIcon name="split" /> Why the left version is worse</div>

<div style="font-size: 1.05rem">

It needs `len()` and `[]`, so it only works on sequences — and it indexes on
every pass.

</div>

</div>

</div>

<div class="nl-statement mt-3">
If you wrote <code>range(len(...))</code>, you wanted <code>enumerate</code>
</div>

<!--
SLIDE 13 - enumerate
On screen ~50 seconds.

This is the most immediately useful thing in the chapter for someone who has
written a few loops, so sell it as a fix:
"Si vous avez déjà écrit `for i in range(len(quelque chose))`, vous
n'aviez pas tort - il y a juste mieux."

The `start=1` argument is worth ten seconds because it is a real reporting
need: "Les humains comptent à partir de un. Vos utilisateurs aussi. Le
deuxième argument ne change que le numéro affiché."

The deeper reason is the protocol from earlier - name it:
"Et enumerate marche sur n'importe quel itérable. Même sur un fichier, qui
n'a ni longueur ni index. `range(len(...))` ne peut pas faire ça."
-->

---
layout: default
class: nl-deck
---

# zip(): Parallel Iteration

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="split" /> Walk two lists together</div>

```python
for name, age in zip(names, ages):
    print(f"{name} is {age}")

data = dict(zip(names, ages))
rows = list(zip(*columns))   # transpose
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> Consumed once</div>

```python
>>> z = zip(names, ages)
>>> list(z)
[('Alice', 25), ('Bob', 30)]
>>> list(z)
[]
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> It stops at the shortest</div>

Give `zip` a list of three and a list of five and you get three pairs. No
warning, no error — the extra two are simply gone.

That is the silent data-loss bug in this chapter. Since 3.10, `strict=True`
turns the mismatch into a `ValueError`.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>zip(a, b, strict=True)</code> when lengths must agree</li>
<li class="nl-bad">Trusting two lists to stay the same length</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>zip</code> stops at the shortest — silently, unless you pass <code>strict=True</code>
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 14 - zip
On screen ~70 seconds. This slide carries the chapter's payoff. Do not rush.

Start with the useful part - parallel iteration, dict(zip(...)), and the
transpose trick, which always gets a reaction.

Then the truncation, framed as a bug and not a feature:
"Trois noms, cinq âges. zip vous donne trois paires. Les deux derniers âges
ont disparu. Pas d'erreur, pas d'avertissement. Vos données sont
silencieusement tronquées."

PAUSE.

"Depuis Python 3.10, il y a `strict=True`. Utilisez-le dès que les deux
longueurs SONT censées être égales - c'est-à-dire presque toujours."

Then land the payoff planted on the for-loop slide. Do this live:
z = zip(names, ages); list(z); list(z)

The second call returns an empty list. Let the silence sit.

"Souvenez-vous : un itérateur se consomme. On l'a dit il y a dix minutes.
Voilà ce que ça veut dire concrètement. Ce n'est pas une liste - c'est un
robinet, et vous venez de le vider."
-->

---
layout: default
class: nl-deck
---

# Nested Loops & Complexity

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="layers" /> Inner runs fully, every pass</div>

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end="")
    print()
```

<div class="nl-recap mt-3" style="font-size: 1.05rem">
  <div class="n">n = 100</div><div><span class="why">10,000 steps — instant</span></div>
  <div class="n">n = 1,000</div><div><span class="why">1 million — noticeable</span></div>
  <div class="n">n = 10,000</div><div><span class="why">100 million — too slow</span></div>
</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="split" /> Every level multiplies</div>

Total iterations are outer **×** inner. Two nested loops over the same data
is O(n²); three is O(n³). The cost does not grow — it explodes.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Before you nest</div>

<ul style="font-size: 1.05rem">
<li class="nl-good">Move work that does not change out of the inner loop</li>
<li class="nl-good">Replace an inner search with a <code>dict</code> lookup — O(n) not O(n²)</li>
<li class="nl-good">On numeric grids, reach for NumPy</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Each level of nesting multiplies the work — that is all of complexity, for now
</div>

<!--
SLIDE 15 - Nested loops
On screen ~65 seconds.

The multiplication table uses the format spec from chapter two - `{i*j:3}`
aligns the columns. Point that out, it is a free callback.

The numbers table is the whole slide. Read it out loud, slowly:
"Cent éléments : dix mille étapes, instantané. Mille : un million, ça se
sent. Dix mille : cent millions, votre programme ne répond plus."

PAUSE.

"Vous n'avez pas besoin de la théorie de la complexité aujourd'hui. Vous
avez besoin de ce réflexe : chaque niveau d'imbrication multiplie."

The dict-lookup point is the one that matters in production, so give it a
concrete shape: chercher chaque élément d'une liste dans une autre liste,
c'est n². Construire un dictionnaire d'abord, c'est n.

Do not go further. This is chapter three of eighteen.
-->

---
layout: default
class: nl-deck
---

# Loop Pitfalls

<div class="nl-cols mt-4" style="font-size: 1.05rem">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Editing while iterating</div>

Removing items from the list you are looping over makes the loop skip
elements. The iterator keeps its position while the list shifts underneath it.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> Recomputing in the body</div>

A call whose result never changes does not belong inside the loop. It runs n
times for one answer.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> Mutable state across passes</div>

A list built up outside the loop and appended to conditionally is where
off-by-one bugs live.

</div>

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> Iterate a copy, or build a new list</div>

Loop over `items[:]` and mutate `items`, or better, build the result you want
and rebind the name.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Hoist it, or bind it once</div>

Compute above the loop. Inside a condition, `:=` from the last chapter binds
it once and uses it in the same breath.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Prefer producing over patching</div>

A loop that returns a new collection is easier to test than one that edits a
collection in place.

</div>

</div>

<div class="nl-statement mt-3">
Never change the thing you are iterating over
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 16 - Pitfalls
On screen ~65 seconds. Close the chapter on the mistakes, not a summary.

The first one has to be demonstrated, because the failure is
counter-intuitive and silent. In VS Code:

nums = [1, 2, 3, 4]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)   ->  [1, 3] is what they expect; show what actually happens

"L'itérateur garde sa position. La liste, elle, se décale. Résultat : il
saute des éléments. Pas d'erreur - juste un résultat faux."

PAUSE.

Then the fix, and say why the second version is better than the copy:
"On peut itérer sur une copie. Mais mieux : construisez la liste que vous
voulez, et réaffectez. Un programme qui produit se teste. Un programme qui
rafistole se débugge."

The walrus callback closes the loop with chapter two - point at it.
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 04 — FUNCTIONS</strong>

</div>

<!--
SLIDE 17 - Closing card
On screen ~12 seconds.
Say the next chapter's topic out loud while this is up.
Then: "À mardi." Hold two beats of silence before you stop recording.
-->
