---
theme: ../themes/noonlabs
title: Python Syntax & Data Types — Chapter 02
info: NoonLabs - Module I, chapitre 02
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

<div class="nl-eyebrow">Chapter 02</div>

# Python Syntax & Data Types

<div class="mt-4" style="max-width: 42ch">

The building blocks, and the type system that decides what your code is allowed to do

</div>

<div class="nl-type mt-6">
  <NlIcon name="indent" /> Syntax
  <span class="mx-3">·</span>
  <NlIcon name="box" /> Types
  <span class="mx-3">·</span>
  <NlIcon name="prompt" /> Formatting
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~8 seconds.

"Chapitre deux. C'est le chapitre où on répond à la question qu'on a
laissée ouverte la dernière fois."

Do not say which question yet. Slide 14 answers it.

Set the format expectation once, here, so nobody wonders later:
"Les diapositives, c'est pour les concepts et les bonnes pratiques. Le
code, on l'écrit ensemble dans VS Code."
-->

---
layout: default
class: nl-deck
---

# Indentation: Syntax, Not Style

<div class="nl-cols mt-4">

<div style="font-size: 1.15rem">

<div class="nl-type"><NlIcon name="indent" /> The rule</div>

- **Four spaces** per level — PEP 8
- The colon opens a block; the indent **is** the block
- Be consistent throughout a file
- Mixing tabs and spaces raises `TabError`

<div class="nl-type mt-3"><NlIcon name="layers" /> Why this is a feature</div>

Braces let other languages run badly-structured code. Python refuses to
run it at all — so the structure you see is the structure that executes.

</div>

<div style="font-size: 1.15rem">

<div class="nl-type nl-good"><NlIcon name="check" /> Correct</div>

```python
if True:
    print("indented")
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> IndentationError</div>

```python
if True:
print("not indented")
```

<ul class="mt-3">
<li class="nl-good">One level = one logical step</li>
<li class="nl-bad">Never mix tabs and spaces</li>
</ul>

</div>

</div>

<div class="nl-statement mt-4">
In Python, whitespace is not formatting — it is the parse tree
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 3 - Indentation
On screen ~55 seconds. Read the rules off the slide, then switch to VS Code
and let the broken version fail in the terminal. Beginners need to see the
error, not read about it.

"Dans la plupart des langages, l'indentation est une politesse. En Python,
c'est de la grammaire. Si vous vous trompez, ça ne tourne pas."

PAUSE on the statement.

"Et c'est une bonne nouvelle. Du code Python mal structuré ne démarre pas.
Dans d'autres langages, il démarre, et vous découvrez le problème six mois
plus tard."

In VS Code, show the whitespace rendering setting and the ruler. Thirty
seconds that prevent a year of tab-versus-space pain.
-->

---
layout: default
class: nl-deck
---

# Comments & Docstrings

<div class="nl-cols mt-4">

<div style="font-size: 1.1rem">

<div class="nl-type nl-good"><NlIcon name="check" /> Good practice</div>

<ul>
<li class="nl-good">Explain **why**, not what</li>
<li class="nl-good">Document the assumption, not the syntax</li>
<li class="nl-good">Keep them current — a stale comment is worse than none</li>
</ul>

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> Avoid</div>

<ul>
<li class="nl-bad">Restating the line below it</li>
<li class="nl-bad">Commented-out code — git already remembers</li>
</ul>

</div>

<div>

<div class="nl-type"><NlIcon name="box" /> A docstring is not a comment</div>

```python
def area(l: float, w: float) -> float:
    """Area of a rectangle.

    Args:
        l: the length.
        w: the width.
    """
    return l * w
```

<div class="nl-recap mt-3">
  <div class="n">#</div><div><span class="why">stripped at parse time</span></div>
  <div class="n">"""…"""</div><div><span class="why">kept on the object at runtime</span></div>
</div>

</div>

</div>

<div class="nl-statement mt-4">
A comment explains why. The code already says what.
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 4 - Comments and docstrings
On screen ~60 seconds.

The distinction almost nobody teaches, and it is the point of the slide:
"Un commentaire disparaît à l'exécution. Une docstring reste dans l'objet.
C'est pour ça que help() marche et qu'un commentaire ne sert à rien à
l'exécution."

Then switch to VS Code and prove it: help(area), then area.__doc__.

On the discipline, be blunt:
"« Additionne un et deux » au-dessus d'une ligne qui additionne un et deux,
ça n'aide personne. Écrivez pourquoi le nombre est deux."

And the stale-comment point deserves the extra beat:
"Un commentaire faux est pire que pas de commentaire. Le lecteur lui fait
confiance."
-->

---
layout: default
class: nl-deck
---

# Variables & Dynamic Typing

<div class="nl-cols mt-4">

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="arrow" /> A name, not a box</div>

A variable does not contain a value. It is a label attached to an object,
and two labels can point at the same object.

The type belongs to the **object**, never to the name — so the same name can
reference an `int`, then a `str`, with nothing to stop it.

<div class="nl-type mt-3"><NlIcon name="split" /> The cost of that freedom</div>

Dynamic typing buys flexibility and moves the cost to testing. `type()` tells
you what something is; `isinstance()` is what you check with.

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="indent" /> Naming, per PEP 8</div>

- `snake_case` for variables and functions
- Start with a letter or `_`, never a digit
- Case-sensitive: `Name` and `name` differ
- Never shadow a builtin: `list`, `id`, `type`

<ul class="mt-3">
<li class="nl-good"><code>user_name</code> &nbsp; <code>_private</code> &nbsp; <code>count2</code></li>
<li class="nl-bad"><code>2count</code> &nbsp; <code>user-name</code> &nbsp; <code>class</code></li>
</ul>

</div>

</div>

<div class="nl-statement mt-4">
A variable is a name pointing at an object, not a box holding a value
</div>

<!--
SLIDE 5 - Variables
On screen ~60 seconds. This one stays on the slide - it is a mental model,
not a syntax demo.

Draw it in the air if you have to:
"Ce n'est pas une boîte qui contient cinq. C'est une étiquette collée sur un
objet qui vaut cinq. Et deux étiquettes peuvent être collées sur le même
objet."

Why it matters later, planted without resolving:
"Gardez ça. Quand on arrivera aux listes, cette différence va expliquer un
bug qui surprend absolument tout le monde."

On shadowing, say what actually happens:
"Si vous appelez une variable `list`, vous venez de casser la fonction
`list` pour tout le reste du fichier. Aucun avertissement."
-->

---
layout: default
class: nl-deck
---

# Numeric Types: int, float, complex

<div class="grid grid-cols-3 gap-6 mt-4" style="font-size: 0.98rem">

<div class="nl-card">

<div class="nl-type"><NlIcon name="box" /> int</div>

Whole numbers, **unlimited precision** — no overflow, ever. Underscores are
legal in literals: `1_000_000`.

Operators: `+ - * // % **`

</div>

<div class="nl-card">

<div class="nl-type"><NlIcon name="split" /> float</div>

Decimals as IEEE-754 doubles: 64 bits, about **15–17 significant digits**.
Scientific notation: `1.5e-3`.

`5 / 2` is `2.5`, `5 // 2` is `2`

</div>

<div class="nl-card">

<div class="nl-type"><NlIcon name="layers" /> complex</div>

Real and imaginary parts, written `3 + 4j`. Read them back with `z.real` and
`z.imag`.

Signal processing, engineering

</div>

</div>

<div class="nl-cols mt-3" style="font-size: 1.05rem">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Why <code>0.1 + 0.2</code> is not <code>0.3</code></div>

One tenth has no exact form in binary, exactly as one third has none in
decimal. The result is off by about 10⁻¹⁷ — and it always will be.

</div>

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> What to do instead</div>

<ul>
<li class="nl-good">Compare with <code>math.isclose</code>, never <code>==</code></li>
<li class="nl-good">Money and exact decimals go in <code>decimal</code></li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Floats are approximations — money and physics both need to know that
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 6 - Numeric types
On screen ~65 seconds. The three cards are twenty seconds. The float point
is the other forty-five and it is the most important thing here.

Read the cards fast, then switch to the terminal and type it yourself:
0.1 + 0.2 == 0.3   ->  False
0.1 + 0.2          ->  0.30000000000000004

Let the silence sit after False appears.

"Ce n'est pas un bug de Python. C'est le binaire. Un dixième ne s'écrit pas
exactement en base deux, comme un tiers ne s'écrit pas exactement en base
dix. Tous les langages ont ce comportement - la plupart vous le cachent."

Then the two rules, and stop there:
"Ne comparez jamais deux flottants avec égal-égal. Et ne stockez jamais de
l'argent dans un flottant."

Do not open the numerical-analysis door in chapter two. One sentence, move on.
-->

---
layout: default
class: nl-deck
---

# Strings: Creation & Immutability

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Four ways to quote</div>

```python
name = 'Alice'
city = "New York"
msg = """multi
line"""
path = r"C:\Users\name"
```

<div class="nl-type mt-2"><NlIcon name="box" /> Properties</div>

<div style="font-size: 1.05rem">

Immutable · a sequence of characters · Unicode throughout

</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> You cannot edit one</div>

`text[0] = "H"` raises `TypeError: 'str' object does not support item
assignment`.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> You build a new one</div>

`text = "H" + text[1:]` — the old string is untouched and, if nothing else
references it, discarded.

Single or double quotes are identical to Python. Pick one per project and let
the formatter enforce it.

</div>

</div>

<div class="nl-statement mt-4">
No operation changes a string — every one of them returns a new string
</div>

<!--
SLIDE 7 - Strings
On screen ~55 seconds.

The raw string earns a sentence, because Windows paths break people:
"Le r devant les guillemets veut dire : prends les antislashs
littéralement. Sans lui, backslash-n devient un saut de ligne, et votre
chemin de fichier est cassé."

Then switch to the terminal and trigger the TypeError yourself.

"Et voilà notre deuxième TypeError du module. Retenez la forme du message :
Python vous dit exactement ce qu'il refuse de faire, et pourquoi."

That is a deliberate rhyme with the CSV error in video one. Say it - they
will feel the pattern before they can name it.
-->

---
layout: default
class: nl-deck
---

# Indexing & Slicing

<div class="nl-cols mt-4">

<div>

<div class="nl-chars">
  <div class="nl-char">P</div>
  <div class="nl-char">y</div>
  <div class="nl-char">t</div>
  <div class="nl-char">h</div>
  <div class="nl-char">o</div>
  <div class="nl-char">n</div>
</div>

<div class="nl-type mt-3 nl-type--plain">0 &nbsp;&nbsp; 1 &nbsp;&nbsp; 2 &nbsp;&nbsp; 3 &nbsp;&nbsp; 4 &nbsp;&nbsp; 5 &nbsp;&nbsp; from the left</div>

<div class="nl-type mt-1 nl-type--plain">-6 &nbsp; -5 &nbsp; -4 &nbsp; -3 &nbsp; -2 &nbsp; -1 &nbsp; from the right</div>

<div class="nl-type mt-3"><NlIcon name="prompt" /> The form</div>

```python
text[start:stop:step]
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="indent" /> Three defaults, three rules</div>

- `start` is **inclusive**, and defaults to `0`
- `stop` is **exclusive**, and defaults to the length
- `step` defaults to `1`; a negative step walks backwards

So `text[0:3]` gives three characters, not four. Every off-by-one bug in
slicing comes from forgetting that one asymmetry.

A slice never fails on a bad range — `text[99:]` is `""`, not an error.
Indexing does: `text[99]` raises `IndexError`.

</div>

</div>

<div class="nl-statement mt-4">
start is included, stop is not — that is the whole convention
</div>

<!--
SLIDE 8 - Slicing
On screen ~55 seconds.

Point at the boxes, not the code. These are the same boxes we used for
"47.20" in video one, deliberately.

"Six caractères, six positions. Et six positions négatives, qui comptent
depuis la fin."

The rule that removes most slicing bugs:
"Le début est inclus, la fin est exclue. Une fois que vous avez ça, tout le
reste suit."

The last point is worth a demo in the terminal, because it surprises people:
"Une tranche hors limites ne plante pas, elle renvoie du vide. Un index hors
limites plante. Ce n'est pas une incohérence - c'est parce qu'une tranche
demande « ce qui existe », et un index demande « celui-là précisément »."

Finish on text[::-1] and let the reaction happen.
-->

---
layout: default
class: nl-deck
---

# String Methods

<div class="nl-cols mt-4" style="font-size: 1.02rem">

<div>

<div class="nl-type"><NlIcon name="indent" /> Clean and reshape</div>

<div class="nl-recap mt-2">
  <div class="n">strip()</div><div><span class="why">drop surrounding whitespace</span></div>
  <div class="n">upper() lower()</div><div><span class="why">change case</span></div>
  <div class="n">title()</div><div><span class="why">capitalise each word</span></div>
  <div class="n">replace()</div><div><span class="why">substitute a substring</span></div>
  <div class="n">zfill() center()</div><div><span class="why">pad to a width</span></div>
</div>

</div>

<div>

<div class="nl-type"><NlIcon name="split" /> Split, join, test</div>

<div class="nl-recap mt-2">
  <div class="n">split()</div><div><span class="why">text to list — on a separator</span></div>
  <div class="n">join()</div><div><span class="why">list back to text; the inverse</span></div>
  <div class="n">find()</div><div><span class="why">position, or -1 if absent</span></div>
  <div class="n">isdigit()</div><div><span class="why">every character a digit?</span></div>
  <div class="n">in</div><div><span class="why">membership — not a method</span></div>
</div>

</div>

</div>

<div class="nl-cols mt-3" style="font-size: 1.05rem">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> The trap</div>

`s.strip()` does not change `s`. If you do not store the result, nothing
happened.

</div>

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> The habit</div>

`s = s.strip()` — reassign, always. `strip()` on every field you read from a
user or a file.

</div>

</div>

<div class="nl-statement mt-3">
Every one of these returns a new string — <code>s</code> is never touched
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 9 - String methods
On screen ~65 seconds. The tables are the reference; the demo is the lesson.

Switch to the terminal with s = "  Hello, World!  " and do the trap live:
type s.strip(), then type s again and show it unchanged. Then s = s.strip().

"Quinze secondes qui vous éviteront un vrai bug."

split and join are the pair to name explicitly:
"Ces deux-là sont inverses l'une de l'autre. Et vous avez déjà utilisé split
sans le savoir - dans la première vidéo, sur chaque ligne du CSV."

Mention `in` is an operator, not a method, and move on - they will meet it
again in the next chapter.
-->

---
layout: default
class: nl-deck
---

# f-strings: Expressions & Debugging

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> Any expression, inline</div>

```python
f"{name} scored {score}"
f"{2 + 2}"           # '4'
f"{name.upper()}"    # 'ALICE'
f"{score:.2f}"       # '95.75'
```

<div class="nl-type mt-2"><NlIcon name="check" /> Self-documenting (3.8+)</div>

```python
f"{score=}"      # 'score=95.7532'
f"{score=:.2f}"  # 'score=95.75'
f"{name!r}"      # "'Alice'"
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why f-strings won</div>

They are evaluated at the point they are written, so the expression sits
where you read it. Concatenation with `+` forces you to convert every
non-string by hand — and forgetting is the `TypeError` we already met.

<ul class="mt-3">
<li class="nl-good">Prefer f-strings for anything a person reads</li>
<li class="nl-bad">Never build SQL or shell commands with them</li>
</ul>

<div style="font-size: 1rem">

`{x=}` prints the name, the equals sign and the value — the print-debugging
line you write ten times a day, in three characters.

</div>

</div>

</div>

<div class="nl-statement mt-4">
<code>f"{x=}"</code> is the debugging line you stop having to write twice
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 10 - f-strings, part one
On screen ~60 seconds.

Lead with the pain they already have:
"Vous déboguez. Vous écrivez print, le nom de la variable entre guillemets,
deux points, puis la variable. À chaque fois."

Then type f"{score=}" in the terminal.

PAUSE.

"Le nom, l'égal, la valeur. Trois caractères. Une fois que vous connaissez
ça, vous ne revenez pas en arrière."

The SQL warning is thirty seconds well spent, even in chapter two:
"Une seule interdiction : ne construisez jamais une requête SQL avec une
f-string. C'est comme ça qu'on se fait injecter. On y reviendra, mais
prenez l'habitude maintenant."
-->

---
layout: default
class: nl-deck
---

# f-strings: Alignment & Format Specs

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="indent" /> Align and pad</div>

```python
f"{score:>10.2f}"  # '     95.75'
f"{score:<10.2f}"  # '95.75     '
f"{score:^10.2f}"  # '  95.75   '
f"{name:*^11}"     # '***Alice***'
```

<div class="nl-type mt-2"><NlIcon name="box" /> Worth knowing</div>

```python
f"{1_000_000:,}"  # '1,000,000'
f"{0.1234:.1%}"   # '12.3%'
f"{255:#x}"       # '0xff'
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="prompt" /> The spec has an order</div>

```
[fill][align][width][.precision][type]
```

Read it left to right and it stops being cryptic. `*^11` is fill `*`, align
centre, width 11.

<div style="font-size: 1.05rem">

`>` pushes right, `<` left, `^` centre. The width can itself be computed:
`f"{score:{w}.2f}"`.

</div>

<ul class="mt-2">
<li class="nl-good">Thousands separators on every report figure</li>
<li class="nl-good">Fixed precision on anything in a column</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Everything after the colon is a formatting language of its own
</div>

<!--
SLIDE 11 - f-strings, part two
On screen ~60 seconds.

Give them the shape, not the catalogue. The bracket line on the right is the
whole slide:
"Remplissage, alignement, largeur, précision, type. Dans cet ordre. Vous
n'avez pas à mémoriser la table - il faut savoir qu'elle existe et savoir
la lire."

The chevrons are visual, so point at them:
"Supérieur pousse à droite. Inférieur, à gauche. Circonflexe, au centre."

Then the one that earns its keep in production:
"La virgule pour les milliers. Sur un tableau de chiffres, c'est la
différence entre un rapport lisible et un mur de chiffres. Et la précision
fixe, c'est ce qui fait que vos colonnes s'alignent."
-->

---
layout: default
class: nl-deck
---

# Boolean, Comparison & Logical Operators

<div class="nl-cols mt-4" style="font-size: 1.05rem">

<div>

<div class="nl-type"><NlIcon name="check" /> Comparison</div>

<div class="nl-recap mt-2">
  <div class="n">== !=</div><div><span class="why">equal, not equal</span></div>
  <div class="n">&lt; &gt;</div><div><span class="why">strictly less, greater</span></div>
  <div class="n">&lt;= &gt;=</div><div><span class="why">less or equal, greater or equal</span></div>
</div>

<div class="nl-type mt-3"><NlIcon name="split" /> Logic</div>

<div class="nl-recap mt-2">
  <div class="n">and</div><div><span class="why">both must be true</span></div>
  <div class="n">or</div><div><span class="why">at least one</span></div>
  <div class="n">not</div><div><span class="why">inverts</span></div>
</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="arrow" /> Two things other languages lack</div>

Comparisons **chain**: `0 < x < 100` is one expression, and `x` is evaluated
once. No `and` needed.

`and` and `or` **short-circuit** — `and` stops at the first false, `or` at
the first true. The right-hand side may never run.

<ul class="mt-3">
<li class="nl-good"><code>if data and data[0]</code> — the guard protects the access</li>
<li class="nl-bad"><code>if data[0] and data</code> — crashes on an empty list</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>0 &lt; x &lt; 100</code> is one expression, not two — Python chains comparisons
</div>

<!--
SLIDE 12 - Booleans and logic
On screen ~55 seconds. Concept slide, stays on the slide.

Sell the chaining:
"En C, en Java, en JavaScript, il faut deux conditions et un ET au milieu.
En Python, vous écrivez ce que vous diriez à voix haute : zéro inférieur à x
inférieur à cent."

Short-circuiting deserves the practical framing, never the truth table. The
two lines at the bottom are the entire lesson - point at them:
"Le ET s'arrête au premier faux. Donc la première condition protège la
seconde. Inversez les deux, et votre programme plante sur une liste vide."

PAUSE there. That pattern appears in every codebase they will ever read.
-->

---
layout: default
class: nl-deck
---

# NoneType & Truthiness

<div class="nl-cols mt-4">

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="split" /> What None is</div>

- A **singleton** — there is exactly one `None` in a program
- Falsy in a boolean test
- What a function returns when it returns nothing
- The right default for an optional parameter

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Use <code>is</code>, not <code>==</code></div>

`==` calls a method the class can redefine. `is` compares identity, and there
is only one `None` — so it cannot lie. PEP 8 requires it.

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Everything falsy</div>

- `False` and `None`
- `0`, `0.0`, `0j`
- `""`, `[]`, `{}`, `()`, `set()`

Everything else is truthy. Which means:

<ul class="mt-2">
<li class="nl-bad"><code>"0"</code> is truthy — it is a non-empty string</li>
<li class="nl-bad"><code>[0]</code> is truthy — it is a non-empty list</li>
</ul>

<div style="font-size: 1.02rem">

What counts is the container, never the contents.

</div>

</div>

</div>

<div class="nl-statement mt-3">
Use <code>is None</code>. <code>== None</code> asks the object, and an object can lie.
</div>

<!--
SLIDE 13 - None and truthiness
On screen ~60 seconds.

The two falsy traps catch everyone, so land them:
"La chaîne « zéro » entre guillemets est vraie. Une liste qui contient zéro
est vraie. Ce qui compte, c'est le contenant, pas le contenu."

Then the statement, and give it the full explanation - this is the
difference between knowing the rule and understanding it:
"Pourquoi `is` et pas `==` ? Parce que `==` appelle une méthode, et une
classe peut la redéfinir pour répondre n'importe quoi. `is` compare
l'identité de l'objet. Il n'y a qu'un seul None dans tout le programme, donc
`is None` ne peut pas mentir."

Say explicitly that this is PEP 8, not a taste preference.
-->

---
layout: default
class: nl-deck
---

# Type Conversion & Casting

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="arrow" /> Convert explicitly</div>

```python
int("42")       # 42
int(3.7)        # 3  (truncates)
float("47.20")  # 47.2
bool("")        # False
int("3.7")      # ValueError!
```

<div class="nl-type mt-2 nl-type--plain">
<code>input()</code> always returns a string. Always.
</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="check" /> Best practice</div>

- Validate anything that came from outside
- Convert **immediately** after reading, not later
- Wrap the conversion in `try` / `except ValueError`

<ul class="mt-3">
<li class="nl-good"><code>try: n = int(s)</code> — then handle the failure</li>
<li class="nl-bad"><code>n = int(input())</code> — crashes on any typo</li>
</ul>

<div style="font-size: 1.02rem">

`int(3.7)` truncates toward zero. `int("3.7")` refuses — a string converts to
an integer only if it *is* an integer.

</div>

</div>

</div>

<div class="nl-statement mt-3">
<code>"47.20" + 12</code> failed because Python refuses to guess
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 14 - Type conversion
On screen ~75 seconds. THIS IS THE PAYOFF SLIDE. Do not rush it.

Open by reopening the wound:
"Dans la première vidéo, notre programme a échoué. On avait « quarante-sept
virgule vingt » entre guillemets, plus douze, et Python a refusé. On a
corrigé avec float, et j'ai dit : on y reviendra."

PAUSE.

"On y est."

Then, slowly:
"Le plus entre deux chaînes, ça colle. Le plus entre deux nombres, ça
additionne. Entre une chaîne et un nombre, Python ne devine pas. D'autres
langages devinent - et c'est là que naissent les bugs qu'on ne trouve
jamais."

Switch to VS Code for int("3.7"). The ValueError surprises people who expect
truncation, because int(3.7) does truncate.

"Une chaîne se convertit en entier seulement si c'est un entier."

Close on input(): everything a user types is text, and the try/except is not
optional.
-->

---
layout: default
class: nl-deck
---

# The Walrus Operator :=

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Computed twice</div>

```python
if len(data) > 10:
    print(f"Too long: {len(data)}")
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Computed once (3.8+)</div>

```python
if (n := len(data)) > 10:
    print(f"Too long: {n}")
```

<div class="nl-type mt-2"><NlIcon name="terminal" /> Where it earns its keep</div>

```python
while chunk := f.read(8192):
    process(chunk)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="arrow" /> What it actually is</div>

An **assignment expression**: it binds a name *and* evaluates to the value, so
it can sit inside a condition where `=` is forbidden.

That restriction is deliberate — `=` inside an `if` is the classic C bug, and
Python made it a syntax error. `:=` gives back the useful half.

<ul class="mt-3">
<li class="nl-good">Use it to remove a repeated call</li>
<li class="nl-bad">Not to compress three readable lines into one</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Compute once, name it, and use it in the same breath
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 15 - Walrus
On screen ~60 seconds.

Frame it as a fix for a real annoyance, not a new toy:
"Regardez en haut. On appelle len deux fois. Ça marche, mais on a dit la
même chose deux fois - et si l'une change, l'autre devient fausse."

The history is worth twenty seconds because it explains the syntax:
"Pourquoi un nouvel opérateur, et pas juste égal ? Parce qu'en C, écrire
égal au lieu de égal-égal dans un if est le bug classique. Python l'a rendu
impossible. Le walrus rend la partie utile, avec une syntaxe qu'on ne peut
pas confondre."

Then the comprehension version live in VS Code - it is the one that
converts people:
"Sans le walrus, vous appelez la fonction deux fois par élément. Avec, une
seule."

Close on the caveat. This operator gets abused:
"Utilisez-le quand il enlève une répétition. Pas pour gagner des caractères."
-->

---
layout: default
class: nl-deck
---

# Python Keywords Reference

<div class="grid grid-cols-7 gap-x-4 gap-y-1 mt-4" style="font-family: var(--nl-mono); font-size: 0.98rem">
<div>False</div><div>None</div><div>True</div><div>and</div><div>as</div><div>assert</div><div>async</div>
<div>await</div><div>break</div><div>class</div><div>continue</div><div>def</div><div>del</div><div>elif</div>
<div>else</div><div>except</div><div>finally</div><div>for</div><div>from</div><div>global</div><div>if</div>
<div>import</div><div>in</div><div>is</div><div>lambda</div><div>nonlocal</div><div>not</div><div>or</div>
<div>pass</div><div>raise</div><div>return</div><div>try</div><div>while</div><div>with</div><div>yield</div>
</div>

<div class="grid grid-cols-3 gap-6 mt-4" style="font-size: 1rem">

<div>
<div class="nl-type nl-type--plain">Values</div>
<code>True False None</code>
</div>

<div>
<div class="nl-type nl-type--plain">Operators</div>
<code>and or not in is</code>
</div>

<div>
<div class="nl-type nl-type--plain">Soft — reserved only in context</div>
<code>match case type _</code>
</div>

</div>

<div class="nl-statement mt-4">
Thirty-five words you cannot use as names — and one line that proves it
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 16 - Keywords
On screen ~45 seconds. Nobody memorises this, so say so first.

"Ne les apprenez pas par cœur. Sachez qu'ils existent, et sachez que votre
éditeur les colore. Si un nom de variable se colore, changez-le."

The soft keywords are worth ten seconds, because they are a real gotcha in
reverse: "match, case, type et l'underscore ne sont réservés qu'en contexte.
Vous POUVEZ appeler une variable match. Ça ne veut pas dire que vous devriez."

Then in the terminal, and this is the habit worth teaching:
import keyword
len(keyword.kwlist)
keyword.iskeyword("match")

"La réponse vient de Python, pas d'une diapositive."

VERIFY BEFORE RECORDING: confirm the count is still 35 on your 3.14. It was
35 on 3.12, and this is exactly the kind of number that moves.
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 03 — CONTROL FLOW</strong>

</div>

<!--
SLIDE 17 - Closing card
On screen ~12 seconds.
Say the next chapter's topic out loud while this is up.
Then: "À mardi." Hold two beats of silence before you stop recording.
-->
