---
theme: ../themes/noonlabs
title: Object-Oriented Programming — Chapter 08
info: NoonLabs - Module I, chapitre 08
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

<div class="nl-eyebrow">Chapter 08</div>

# Object-Oriented Programming

<div class="mt-4" style="max-width: 42ch">

Bundling state with the code that guards it, and teaching your objects to speak the language

</div>

<div class="nl-type mt-6">
  <NlIcon name="box" /> Classes
  <span class="mx-3">·</span>
  <NlIcon name="layers" /> Inheritance
  <span class="mx-3">·</span>
  <NlIcon name="prompt" /> Magic Methods
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~10 seconds.

"Chapitre huit. Le plus long du module, et celui qui change la façon dont
vous écrivez le reste. Jusqu'ici, nos données étaient dans des variables et
des dictionnaires, et le code qui les manipule était ailleurs. À partir de
maintenant, les deux voyagent ensemble."

Restate the format:
"Les diapositives, c'est pour les concepts. Le code, on l'écrit ensemble
dans VS Code."

Warn them about the length, it buys goodwill:
"C'est une vidéo longue. Les chapitres sont dans la description si vous
voulez y revenir par morceaux."
-->

---
layout: default
class: nl-deck
---

# Why a Class?

<div class="nl-cols mt-4">

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="arrow" /> How it always goes</div>

- **Day one** — one `dict` per transaction, three helper functions
- **Month six** — forty call sites read `t["amount"]`
- One of them writes `t["ammount"]`, and nothing raises

<div class="nl-type mt-3"><NlIcon name="layers" /> Why the dict cannot help</div>

A `dict` accepts any key you hand it. That is the entire point of a `dict`, and
it is the entire problem.

</div>

<div>

<div class="nl-type"><NlIcon name="check" /> What a class adds</div>

<ul style="font-size: 1.05rem">
<li class="nl-good">One place where the field names are written down</li>
<li class="nl-good">Your editor and <code>mypy</code> can both see that place</li>
<li class="nl-good">Validation gets somewhere to live</li>
<li class="nl-good">Behaviour travels with the data it acts on</li>
</ul>

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> What it costs</div>

<div style="font-size: 1.05rem">

Four lines of ceremony you genuinely did not need on day one. The dict was the
right call then. It stopped being one.

</div>

</div>

</div>

<div class="nl-statement mt-4">
A class is the moment the shape of your data needs a name
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 3 - Motivation
On screen ~60 seconds.

Do not open with the four pillars. Open with the pain, or the pillars sound
like vocabulary homework.

"Jour un : une transaction, c'est un dictionnaire. Trois fonctions autour.
Ça marche, c'est rapide, et honnêtement c'est le bon choix ce jour-là."

PAUSE.

"Mois six : quarante endroits lisent la clé « amount ». Un seul écrit
« ammount », avec deux M. Et Python ne dit rien, parce qu'un dictionnaire
accepte n'importe quelle clé. C'est sa raison d'être. C'est aussi le
problème."

Demo it in VS Code - the dict version, then the typo, then show that the
KeyError only fires on the branch that runs in production. Ninety seconds
maximum.

Be fair to the dict on the way out, it keeps you honest:
"Le dictionnaire n'était pas une erreur. Il a cessé d'être le bon outil."
-->

---
layout: default
class: nl-deck
---

# The Four Pillars

<div class="nl-cols mt-4" style="font-size: 1.1rem">

<div>

<div class="nl-type"><NlIcon name="box" /> Encapsulation</div>

State, and the code that guards it, living in one place.

<div class="nl-type mt-3"><NlIcon name="layers" /> Inheritance</div>

A subclass reuses a parent and narrows it.

</div>

<div>

<div class="nl-type"><NlIcon name="split" /> Polymorphism</div>

The same call, a different object, different behaviour.

<div class="nl-type mt-3"><NlIcon name="prompt" /> Abstraction</div>

The caller sees an interface and never the wiring.

</div>

</div>

<ul class="mt-4" style="font-size: 1.05rem">
<li class="nl-good">Encapsulation and polymorphism — you will use these every week</li>
<li class="nl-bad">Multiple inheritance and formal abstraction — twice a year, if that</li>
</ul>

<div class="nl-statement mt-3">
Two of these you will use every week. Two you will use twice a year.
</div>

<!--
SLIDE 4 - The pillars
On screen ~50 seconds. Concept slide, nothing to demo.

Name them quickly, one line each, and do not linger. They are a map, not a
lesson.

Then spend the remaining thirty seconds on the honest part, because nobody
else will tell them:
"Ces quatre mots sont dans tous les cours. Deux vous serviront chaque
semaine sans que vous y pensiez : l'encapsulation et le polymorphisme.
L'héritage multiple et l'abstraction formelle, deux fois par an."

PAUSE.

"Je vais quand même vous les enseigner. Pas pour que vous en écriviez - pour
que vous sachiez les lire le jour où vous tombez dessus dans le code de
quelqu'un d'autre."
-->

---
layout: default
class: nl-deck
---

# class, `__init__`, self

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> The shape</div>

```python
class Transaction:
    def __init__(self, label, amount):
        self.label = label
        self.amount = amount

t = Transaction("Carrefour", 47.20)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> <code>__init__</code> is not a constructor</div>

The object already exists when `__init__` runs — which is exactly why
`__init__` never returns anything. It fills a blank object; it does not make
one.

<div class="nl-type mt-3"><NlIcon name="check" /> self is a parameter</div>

Python passes the new object in as the first argument. `self` is that
argument. Rename it and the code still runs.

</div>

</div>

<div class="nl-statement mt-4">
<code>self</code> is a parameter name. That is the whole mystery.
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 5 - Syntax
On screen ~65 seconds.

The constructor point contradicts almost every other course, so say it
deliberately rather than in passing:
"On appelle __init__ un constructeur, par habitude. Ce n'en est pas un.
L'objet existe déjà quand __init__ tourne - il a été créé avant, par une
autre méthode. __init__ ne construit rien : il remplit un objet vide."

Then the consequence, which makes it stick:
"Et c'est pour ça qu'__init__ ne renvoie jamais rien. Il n'a rien à
renvoyer. L'objet est déjà là."

PAUSE.

Now demystify self, live. In VS Code, rename self to `this` throughout the
class and run it. It works.

"Regardez. Ça tourne. Parce que self n'est pas un mot-clé - c'est un nom de
paramètre, et Python remplit le premier paramètre avec l'objet."

Then rename it back and say why: PEP 8, et tous les relecteurs du monde.
-->

---
layout: default
class: nl-deck
---

# Instance vs Class Attributes

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Two kinds</div>

```python
class Account:
    history = []             # one, ever

    def __init__(self, owner):
        self.owner = owner   # one each
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> What that means</div>

```python
>>> a = Account("Amina")
>>> b = Account("Bruno")
>>> a.history.append("open")
>>> b.history
['open']
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> One object, not two</div>

`a.history is b.history` is `True`. These are not two lists that happen to
match. There is one list, and it belongs to the class, not to either instance.

<div class="nl-type mt-3"><NlIcon name="check" /> Where a class attribute belongs</div>

<ul style="font-size: 1.05rem">
<li class="nl-good">A constant, a version string, a default number</li>
<li class="nl-bad">Any container — list, dict, set</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
You met this shape in chapter 04 — it is the same bug, one level up
</div>

<!--
SLIDE 6 - Class attributes. This is the chapter's PLANT.
On screen ~60 seconds.

Set up the distinction cleanly first: owner est sur self, donc un par
instance. history est dans le corps de la classe, donc un seul, pour tout le
monde, pour toute la durée du programme.

Then read the REPL out loud, slowly, and let the last line land:
"On crée deux comptes. On ajoute une entrée à l'historique d'Amina. Et
l'historique de Bruno la contient aussi."

PAUSE.

"Ce ne sont pas deux listes qui se ressemblent. C'est une seule liste."

Now the callback, which is the point of the slide:
"Vous avez déjà vu cette forme. Chapitre quatre, l'argument par défaut
mutable. C'est le même bug, remonté d'un niveau - d'un paramètre de fonction
à un attribut de classe. Un nom, un objet. Encore."

Do NOT give the fix. Say only "retenez cette erreur" and move on. It is
resolved on the dataclasses slide, where the language now refuses it
outright.
-->

---
layout: default
class: nl-deck
---

# Encapsulation: `_` and `__`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="indent" /> Three levels, one of them real</div>

<div class="nl-recap mt-2">
  <div class="n">pin</div><div><span class="why">public — part of your API</span></div>
  <div class="n">_pin</div><div><span class="why">a promise, enforced by nothing</span></div>
  <div class="n">__pin</div><div><span class="why">renamed by the interpreter</span></div>
</div>

<div class="nl-type mt-3"><NlIcon name="file" /> Name mangling</div>

```python
>>> a.__pin
AttributeError
>>> a._Account__pin
1234
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> Not security</div>

The attribute moved; it did not disappear. Anyone who wants it can still read
it, and now they know you did not want them to.

<div class="nl-type mt-3"><NlIcon name="check" /> What <code>__</code> is actually for</div>

<div style="font-size: 1.05rem">

Stopping a subclass from clobbering a parent's internals by accident. That is
the whole use case. It is a collision guard, not a lock.

</div>

</div>

</div>

<div class="nl-statement mt-3">
Python has no private — <code>_</code> is a promise, <code>__</code> is a rename
</div>

<!--
SLIDE 7 - Encapsulation
On screen ~55 seconds.

Walk the recap top to bottom. The first two are conventions; only the third
does anything.

"Un underscore, ça veut dire « n'y touche pas, ça peut changer ». Rien ne
l'empêche. C'est un contrat entre développeurs."

Then the mangling, and read the number out loud - it is what makes the point
land:
"Deux underscores, et l'interpréteur renomme l'attribut en
underscore-Account-underscore-underscore-pin. a.__pin lève une
AttributeError. Mais a._Account__pin renvoie mille deux cent trente-quatre,
tranquillement."

PAUSE.

"Donc ce n'est pas de la sécurité. Si vous cherchez à protéger un secret,
ce n'est pas ici que ça se passe. Le vrai usage, c'est d'éviter qu'une
sous-classe écrase par accident un attribut interne du parent."
-->

---
layout: default
class: nl-deck
---

# `@property`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="check" /> A rule added later</div>

```python
@amount.setter
def amount(self, v):
    if v < 0:
        raise ValueError("negative")
    self._amount = v
```

<div class="nl-type mt-2"><NlIcon name="box" /> Computed, never stored</div>

```python
@property
def total(self):
    return self.qty * self.amount
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why it matters</div>

Yesterday `amount` was a plain attribute and forty callers wrote to it. Today
it validates on every write. Not one call site changed.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> No setter means read-only</div>

<div style="font-size: 1.05rem">

`r.total = 10` raises `AttributeError: property 'total' of 'Row' object has no
setter`. You wrote no check for that. A computed value also cannot go stale —
there is nothing stored to fall out of sync.

</div>

</div>

</div>

<div class="nl-statement mt-3">
A property is how you add a rule to code that already shipped
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 8 - property
On screen ~70 seconds. Two distinct uses on one slide, so signpost them.

Use one, validation. The syntax is thirty seconds; the argument is the rest:
"Hier, amount était un attribut ordinaire. Quarante appelants écrivaient
t.amount égale quelque chose. Aujourd'hui il valide. Et pas un seul appelant
n'a changé d'une ligne."

Demo exactly that in VS Code: run the old caller unchanged, then run
t.amount = -5 and read the ValueError out loud.

"C'est pour ça qu'en Python on n'écrit pas de getters et de setters dès le
départ, contrairement à Java. On expose l'attribut, et le jour où il faut
une règle, on la glisse dessous."

PAUSE.

Use two, computed. Different purpose entirely - rien à valider, rien à
stocker:
"total n'est pas rangé quelque part. Il est calculé à chaque lecture. Donc
il ne peut pas se désynchroniser - il n'y a rien à tenir cohérent."

And the free consequence: pas de setter, donc lecture seule, et le message
d'erreur est explicite. Vous n'avez écrit aucune vérification.

PLANT for chapter 11, and do not explain it: "property est un objet qui fait
quelque chose d'assez malin sous le capot. On verra quoi au chapitre onze."
-->

---
layout: default
class: nl-deck
---

# Instance, Class & Static Methods

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> The alternative constructor</div>

```python
@classmethod
def from_csv_row(cls, row):
    return cls(row[0], float(row[1]))
```

<div class="nl-type mt-3"><NlIcon name="prompt" /> Three signatures</div>

<div class="nl-recap mt-2">
  <div class="n">def m(self)</div><div><span class="why">needs the object</span></div>
  <div class="n">def m(cls)</div><div><span class="why">needs the class</span></div>
  <div class="n">def m()</div><div><span class="why">needs neither</span></div>
</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why <code>cls</code>, not the class name</div>

Hard-code `Transaction(...)` and a subclass gets a `Transaction`. Write
`cls(...)` and it gets itself. One word, and inheritance keeps working.

<div class="nl-type mt-3"><NlIcon name="split" /> The <code>float()</code> is not decoration</div>

<ul style="font-size: 1.05rem">
<li class="nl-good">A CSV row is strings — chapter 06, a file has no types</li>
<li class="nl-bad">A <code>@staticmethod</code> needing nothing from the class — that is a module function</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
The alternative constructor is the one that earns its keep
</div>

<!--
SLIDE 9 - classmethod and staticmethod
On screen ~60 seconds.

The three signatures are the frame: la différence tient entièrement au
premier paramètre. self, l'objet. cls, la classe. Rien, ni l'un ni l'autre.

Then the one use that justifies classmethod:
"Le constructeur alternatif. Une ligne de CSV entre, une Transaction sort.
C'est le seul usage de classmethod que vous écrirez souvent."

Point at float(row[1]) and take the callback:
"Et le float, ce n'est pas de la décoration. Une ligne de CSV, ce sont des
chaînes. Toujours. Chapitre six : un fichier n'a pas de types. On convertit
une fois, à la frontière."

PAUSE.

The cls-versus-hardcoding point is worth ten slow seconds, because it is
invisible until it bites:
"Si vous écriviez Transaction en dur, une sous-classe recevrait une
Transaction. Avec cls, elle se reçoit elle-même."

Close on staticmethod, briefly and dismissively - c'est une fonction rangée
dans une classe. Si elle n'a besoin de rien de la classe, elle est mieux au
niveau du module. Python a déjà des espaces de noms : les fichiers.
-->

---
layout: default
class: nl-deck
---

# Inheritance and `super()`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> A subclass</div>

```python
class Refund(Transaction):
    def __init__(self, label, amt, ref):
        super().__init__(label, -amt)
        self.ref = ref
```

<div class="nl-type mt-3"><NlIcon name="prompt" /> Three shapes</div>

<div class="nl-recap mt-2">
  <div class="n">single</div><div><span class="why">class B(A)</span></div>
  <div class="n">multilevel</div><div><span class="why">C(B), and B(A)</span></div>
  <div class="n">multiple</div><div><span class="why">class C(A, B)</span></div>
</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="arrow" /> What <code>super()</code> does</div>

It walks up the chain and runs the parent's `__init__`. That one line is what
gives a `Refund` a label and an amount at all.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> Forget it and nothing complains</div>

<div style="font-size: 1.05rem">

The object is built. No error. Three functions later somebody reads
`self.label` and gets an `AttributeError` — pointing at the line that reads,
not the line that forgot.

</div>

</div>

</div>

<div class="nl-statement mt-3">
Skip <code>super().__init__()</code> and your object is half-built, silently
</div>

<!--
SLIDE 10 - Inheritance
On screen ~60 seconds.

Read the code line by line. Refund est une Transaction, plus une référence.

The minus sign is worth pointing at, because it shows what inheritance is
for:
"Regardez le moins devant amt. Un remboursement, c'est un montant négatif.
La sous-classe ne réécrit pas la logique du parent - elle lui passe une
valeur différente."

The three shapes are vocabulary, twenty seconds, no more. Multiple gets its
own slide in a moment.

PAUSE.

Then the failure, and give it the weight it deserves:
"Vous oubliez la ligne super(). Le code tourne. L'objet se crée. Rien ne
râle. Et trois fonctions plus loin, quelqu'un lit self.label et reçoit une
AttributeError sur un attribut jamais assigné."

Callback to chapter seven: "La trace vous pointera l'endroit qui lit, pas
l'endroit qui a oublié. Lire une trace, c'est remonter du symptôme à la
cause - et ici la distance est longue."
-->

---
layout: default
class: nl-deck
---

# Overriding: Replace or Extend

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="check" /> Extend the parent</div>

```python
class Refund(Transaction):
    def describe(self):
        base = super().describe()
        return f"{base} · refund"
```

<div class="nl-type mt-2"><NlIcon name="layers" /> Two choices</div>

<div style="font-size: 1.05rem">

Replace the parent's work outright, or call it and wrap the result. Wrapping is
usually what you want — and it is exactly what `__init__` has been doing.

</div>

</div>

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> An override may</div>

<ul style="font-size: 1.05rem">
<li class="nl-good">Do the work differently, or accept more than the parent did</li>
<li class="nl-good">Return something more specific</li>
</ul>

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> An override may not</div>

<ul style="font-size: 1.05rem">
<li class="nl-bad">Demand an argument the parent did not</li>
<li class="nl-bad">Return a different kind of thing, or raise what the caller cannot expect</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
An override the caller has to know about is a special case, not polymorphism
</div>

<!--
SLIDE 11 - Overriding
On screen ~60 seconds.

Technically trivial - même nom dans la sous-classe, et c'est la vôtre qui
gagne. Say that in five seconds and move to the part that matters.

The replace-or-extend distinction is almost never taught explicitly:
"Vous avez deux options. Remplacer : vous ignorez le parent. Ou étendre :
vous appelez super().describe(), vous récupérez son résultat, et vous
l'enrichissez. Le parent garde la responsabilité de sa partie."

Then close the loop with the previous slide:
"Et remarquez que c'est exactement ce que fait super().__init__ depuis dix
minutes. Ce n'était pas un cas spécial. N'importe quelle méthode peut
appeler celle qu'elle remplace."

PAUSE.

The contract, right column, as a rule they can apply without judgement:
"Élargir, jamais restreindre. Parce que tout l'intérêt de l'héritage, c'est
qu'un appelant qui manipule une Transaction fonctionne avec un Refund sans
le savoir. Le jour où il doit le savoir, vous avez perdu ce que l'héritage
devait vous donner."

If someone comments the name Liskov, confirm it. Do not put it on the slide.
-->

---
layout: default
class: nl-deck
---

# Multiple Inheritance & the MRO

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Ask, do not guess</div>

```python
>>> class D(B, C): pass
>>> D.__mro__
(D, B, C, A, object)
```

<div class="nl-type mt-3"><NlIcon name="prompt" /> C3 linearization</div>

<div style="font-size: 1.05rem">

Left to right, children before parents, each class exactly once. An impossible
order is refused when the class is created, not at the first call.

</div>

</div>

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> It is cooperative</div>

```python
class Mixin:
    def __init__(self):
        self.mixed = True   # no super()
```

<div style="font-size: 1.05rem">

Break the chain and the next class in the MRO never runs. `vars()` on the
instance shows `mixed` — and no `base`. The parent was never initialised, and
nothing said so.

</div>

<ul class="mt-2" style="font-size: 1.05rem">
<li class="nl-good">A mixin with no <code>__init__</code> cannot break the chain</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
When you cannot say what <code>super()</code> calls, read <code>__mro__</code>
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 12 - MRO
On screen ~65 seconds.

Draw the diamond verbally - D hérite de B et C, qui héritent tous les deux
de A - then go straight to the answer:
"Vous n'avez pas à devider. Chaque classe a un attribut __mro__, et il vous
donne l'ordre exact."

Print D.__mro__ live. Two lines, and it removes an entire category of
guesswork.

Mention that an impossible order is refused at class creation. Do not demo
it: CPython puts a hard line break inside that error message, so it wraps
differently than anything you would put on a slide.

PAUSE.

The cooperative trap is the expensive part, so slow down:
"L'héritage multiple est coopératif. Chaque classe de la chaîne doit appeler
super(). Ce mixin ne le fait pas. Résultat : il pose son attribut, et la
classe qui vient après lui dans le MRO ne tourne jamais."

"vars() sur l'instance montre mixed. Et pas base. Le parent n'a jamais été
initialisé, et rien n'a protesté."

Close with the production rule:
"Le seul héritage multiple qui passe en revue de code, ce sont les mixins.
Une classe, un comportement, pas d'état, pas d'__init__ du tout. Un mixin
sans __init__ ne peut pas casser la chaîne."
-->

---
layout: default
class: nl-deck
---

# Composition, or No Class at All

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="split" /> Is a, or has a</div>

<ul style="font-size: 1.05rem">
<li class="nl-bad"><code>class FraudModel(Scaler, Logger)</code> — inherits a parent that changes for someone else's reasons</li>
<li class="nl-good"><code>self.scaler = Scaler()</code> — holds a collaborator you can swap in a test</li>
</ul>

<div style="font-size: 1.05rem">

A `Refund` **is a** `Transaction`. A model **has a** scaler. If you hesitate,
it is composition.

</div>

</div>

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> When not to write one at all</div>

<div class="nl-recap mt-2">
  <div class="n">one method</div><div><span class="why">no state — that is a function</span></div>
  <div class="n">built once</div><div><span class="why">that is a module</span></div>
  <div class="n">only data</div><div><span class="why">that is a dataclass</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

Most classes named `Manager`, `Helper` or `Handler` are a function with a
lease.

</div>

</div>

</div>

<div class="nl-statement mt-3">
Inheritance couples you to a class. Composition couples you to a method name.
</div>

<!--
SLIDE 13 - Composition
On screen ~60 seconds. Two production rules that no introductory course gives
you, so this slide earns its place.

Left side first:
"À gauche, un modèle de fraude qui hérite d'un Scaler et d'un Logger. Ça
paraît économique. Le problème, c'est que le parent va changer - pour les
besoins de quelqu'un d'autre, dans une autre équipe, dans six mois. Et votre
classe changera avec lui."

"À droite, le modèle contient un Scaler. Il ne l'est pas, il en a un. Et du
coup, dans un test, vous en injectez un faux en une ligne."

Give them the deciding question, not a principle:
"« Est-ce que c'en est un », ou « est-ce que ça en a un ». Si vous hésitez,
c'est de la composition."

PAUSE.

Right side, and be blun:
"On vient de passer une demi-heure sur les classes, alors disons quand il ne
faut pas en écrire. Une classe avec une seule méthode et aucun état, c'est
une fonction. Une classe que vous instanciez une fois, c'est un module."

Land the last line dry. It gets a laugh if you do not push it.
-->

---
layout: default
class: nl-deck
---

# isinstance & Duck Typing

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Asking the type</div>

```python
>>> isinstance(dog, Animal)
True
>>> isinstance(True, int)
True
>>> type(True) is int
False
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> Never <code>type(x) == C</code></div>

<div style="font-size: 1.05rem">

It excludes subclasses — precisely the objects polymorphism exists to accept.

</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Or do not ask at all</div>

- `len(x)` calls `x.__len__()`
- `for i in x` calls `x.__iter__()`
- `with x:` calls `x.__enter__()`
- `x + y` calls `x.__add__(y)`

<div style="font-size: 1.05rem">

Not one of these checks a type or a base class. Your object joins the language
by implementing a method, not by inheriting from anything.

</div>

</div>

</div>

<div class="nl-statement mt-3">
Python does not ask what you are — it asks whether you answer
</div>

<!--
SLIDE 14 - isinstance and duck typing
On screen ~60 seconds.

Left first, and use bool as the demonstration because it surprises people:
"isinstance respecte l'héritage. Un chien est un chien, et il est aussi un
animal. Regardez le bas : isinstance de True face à int renvoie True, parce
qu'en Python, bool hérite de int. Mais type(True) is int renvoie False."

"Donc n'écrivez jamais type(x) égale égale quelque chose. Vous croyez
vérifier un type ; vous excluez toutes les sous-classes. C'est-à-dire
exactement les objets que le polymorphisme devait vous laisser accepter."

PAUSE.

Then the pivot, and slow right down - this is the part of the language worth
being enthusiastic about:
"Mais la vraie question n'est pas laquelle des deux fonctions utiliser.
C'est de savoir s'il faut poser la question du tout."

Read the four lines out loud, one at a time. len appelle __len__. Le for du
chapitre trois appelle __iter__. Le with du chapitre six appelle __enter__.
Le plus appelle __add__.

"Aucun de ces mécanismes ne regarde votre type. Ils demandent une méthode.
Si votre objet répond, il fonctionne partout."

Everything after this slide is writing those answers.
-->

---
layout: default
class: nl-deck
---

# Abstract Base Classes

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> An interface that refuses</div>

```python
from abc import ABC, abstractmethod

class Detector(ABC):
    @abstractmethod
    def score(self, tx): ...
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> The message</div>

```python
TypeError: Can't instantiate
abstract class Passthrough without
an implementation for abstract
method 'score'
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="arrow" /> The failure moves</div>

Without an ABC, a subclass that forgets `score` is built happily and fails at
the first call — three hours into a pipeline. With one, it fails the moment
somebody tries to build it.

<div class="nl-type mt-3"><NlIcon name="check" /> Where it earns its place</div>

<ul style="font-size: 1.05rem">
<li class="nl-good">Several people implementing one interface</li>
<li class="nl-bad">A base class with exactly one subclass</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
An ABC moves the failure from call time to construction time
</div>

<!--
SLIDE 15 - ABCs
On screen ~60 seconds.

The mechanism is thirty seconds: hériter d'ABC, décorer avec
@abstractmethod, et la classe ne s'instancie plus.

The value is the rest, and it is entirely about when the error arrives:
"Sans ABC, une sous-classe qui oublie score se crée sans problème. Le
plantage arrive au premier appel - souvent au milieu d'un traitement,
souvent en production. Avec ABC, l'erreur tombe à la construction."

Read the message out loud; it names both the class and the missing method.

PAUSE.

"Le déplacement est minuscule à l'écrit et énorme en pratique. Vous passez
d'une erreur à la troisième heure d'un pipeline à une erreur au démarrage."

Then be honest about scope, so nobody goes and puts an ABC on everything:
"Où je m'en sers vraiment : quand plusieurs personnes vont écrire des
implémentations de la même interface. Un détecteur de fraude, un chargeur de
données. Une classe de base avec une seule sous-classe, ça ne sert à rien."

One connection worth saying but not showing: collections.abc contient des
ABC qui répondent structurellement - isinstance d'un objet avec un __len__
face à Sized renvoie True, sans qu'il en hérite. Mention it, do not demo it;
Iterable tests __iter__ specifically, and the exceptions open a longer
conversation than this chapter has room for.
-->

---
layout: default
class: nl-deck
---

# `__str__` and `__repr__`

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> The default</div>

```python
>>> t
<Transaction object at 0x7f10b3d4>
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> One line of work</div>

```python
def __repr__(self):
    return f"Transaction({self.label!r})"
```

</div>

<div>

<div class="nl-type"><NlIcon name="split" /> Which one, and for whom</div>

<div class="nl-recap mt-2">
  <div class="n">__repr__</div><div><span class="why">for you, in a traceback</span></div>
  <div class="n">__str__</div><div><span class="why">for the user, readable</span></div>
</div>

<div class="nl-type mt-3"><NlIcon name="layers" /> The fallback is one-way</div>

<div style="font-size: 1.05rem">

`str()` falls back to `__repr__`. `repr()` never falls back to `__str__`. So
if you only write one, write `__repr__`.

</div>

</div>

</div>

<div class="nl-statement mt-3">
A log line reading <code>&lt;Transaction object at 0x…&gt;</code> is a dead end you wrote yourself
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 16 - str and repr
On screen ~60 seconds. The highest return-on-effort method in the chapter,
and nobody teaches it as such.

Open with the failure, not the feature:
"Par défaut, quand vous affichez un objet, Python vous donne le nom de la
classe et une adresse mémoire. C'est exact. Et c'est inutilisable."

Make it concrete, because that is what sells it:
"Le jour où votre pipeline plante à trois heures du matin et que la ligne de
log dit « Transaction object at 0x7f10 », vous n'avez rien. Vous ne savez
même pas de quelle transaction il s'agit."

PAUSE.

Demo in VS Code, three steps, and the third one is the one that convinces:
print an object, add __repr__, print again - then raise an exception carrying
the object and show the traceback with the good repr in it.

Then the fallback direction, stated as a rule:
"Si vous n'écrivez que __repr__, str() l'utilise. Si vous n'écrivez que
__str__, repr() ne l'utilise pas et vous récupérez l'adresse mémoire. Donc
si vous n'en écrivez qu'une seule : __repr__."
-->

---
layout: default
class: nl-deck
---

# Equality, Ordering & the `__hash__` Trap

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Define two, get six</div>

```python
def __eq__(self, other):
    return self.total == other.total

def __lt__(self, other):
    return self.total < other.total
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> The rest for free</div>

<div style="font-size: 1.05rem">

`__eq__` gives you `!=`. `__lt__` alone is enough for `sorted()`.
`@functools.total_ordering` derives the other four.

</div>

</div>

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> The price of <code>__eq__</code></div>

```python
>>> Money.__hash__
None
>>> {Money(1)}
TypeError: unhashable type: 'Money'
```

<div style="font-size: 1.05rem">

Equal objects must hash alike. You redefined equality, so Python cannot guess
the matching hash — and rather than leave a silent inconsistency, it removes
your object from every `set` and every dict key in the codebase.

</div>

</div>

</div>

<div class="nl-statement mt-3">
Defining <code>__eq__</code> silently sets <code>__hash__</code> to <code>None</code>
</div>

<!--
SLIDE 17 - Comparison
On screen ~65 seconds.

Left is the good news, and it is genuinely economical:
"Vous définissez __eq__, et le double égal marche - et le différent aussi,
Python le déduit. Vous définissez __lt__, et sorted() sait trier vos objets.
La fonction de tri n'a besoin de rien d'autre."

"Il reste quatre opérateurs. Vous pouvez les écrire à la main - quatre
méthodes qui se ressemblent, quatre occasions de se tromper de sens. Ou vous
posez @functools.total_ordering sur la classe, et il les dérive."

PAUSE.

Right is the trap, and it fails far from its cause, so give it room:
"Et voilà le prix. Quand vous définissez __eq__, Python met __hash__ à None.
Automatiquement. Silencieusement. Votre objet ne peut plus entrer dans un
set, ni servir de clé de dictionnaire."

Explain the reason, because it makes the behaviour reasonable rather than
arbitrary: deux objets égaux doivent avoir le même hash. Python ne peut pas
deviner le vôtre. Plutôt que de vous laisser deux objets égaux dans deux
cases différentes d'un dictionnaire, il retire l'objet du jeu.

"Le jour où quelqu'un écrit set(transactions) pour dédupliquer, il reçoit
une TypeError, et il n'a aucune idée que la cause est un __eq__ écrit trois
mois plus tôt."

PLANT: say only "une dataclass gelée règle ça" and move on. It is resolved on
the dataclass options slide.
-->

---
layout: default
class: nl-deck
---

# Operator Overloading

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Return a new object</div>

```python
def __add__(self, other):
    if not isinstance(other, Vector):
        return NotImplemented
    return Vector(self.x + other.x,
                  self.y + other.y)
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Let Python write the error</div>

<div style="font-size: 1.05rem">

`NotImplemented` is *returned*, not raised. Python tries the reverse operation,
then raises `unsupported operand type(s) for +` naming both types itself.

</div>

</div>

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> In-place must return self</div>

```python
def __iadd__(self, other):
    self.value += other   # no return
```

```python
>>> c = Counter(5)
>>> c += 3
>>> c
None
```

<div style="font-size: 1.05rem">

`+=` rebinds the name to whatever `__iadd__` returned. Your object is fine; the
name that pointed at it is gone.

</div>

</div>

</div>

<div class="nl-statement mt-3">
An operator returns a new object — except the in-place ones, which must return <code>self</code>
</div>

<!--
SLIDE 18 - Operators
On screen ~70 seconds. Two traps, one slide. Signpost the switch.

Left, and insist on "new":
"__add__ ne modifie pas self. Il renvoie un Vector neuf. Comme pour les
entiers et les chaînes du chapitre deux : a plus b ne change ni a ni b."

Then the detail that separates amateur code from library code:
"Que faire si l'autre opérande n'est pas du bon type ? La tentation, c'est
de lever une TypeError vous-même. Ne le faites pas. Renvoyez la constante
NotImplemented."

"Parce que Python, en la recevant, essaie l'opération dans l'autre sens -
peut-être que l'autre objet sait additionner un Vector - et si ça échoue
aussi, il lève lui-même une TypeError en nommant les deux types. Vous
n'auriez pas écrit mieux."

Worth one line: NotImplemented n'est pas NotImplementedError. L'un est une
valeur qu'on renvoie, l'autre une exception qu'on lève.

PAUSE.

Right. Type this one live if you type anything on this slide - the reveal
does not work read aloud:
"La méthode fait son travail. self.value passe bien à huit. Puis on regarde
c... et c vaut None."

PAUSE. Let it sit.

"Parce que c plus égal trois, ce n'est pas seulement un appel de méthode.
C'est un appel suivi d'une réaffectation. La méthode n'a rien renvoyé, donc
elle a renvoyé None, donc c vaut None. Votre objet existe toujours en
mémoire - plus personne n'a son adresse."

One reassurance to end on: si vous ne définissez pas __iadd__ du tout, plus
égal retombe sur __add__ et réaffecte le nouvel objet. Ça marche. Ne
définissez __iadd__ que si vous avez une vraie raison de modifier sur place.
-->

---
layout: default
class: nl-deck
---

# The Container Protocol

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> Four operations, four methods</div>

<div class="nl-recap mt-2">
  <div class="n">len(deck)</div><div><span class="why">__len__</span></div>
  <div class="n">deck[0]</div><div><span class="why">__getitem__</span></div>
  <div class="n">"A" in deck</div><div><span class="why">__contains__</span></div>
  <div class="n">for c in deck</div><div><span class="why">__iter__</span></div>
</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Python falls back</div>

Write `__len__` and `__getitem__` and you also get `in` and iteration. No
`__contains__`? It scans using `__iter__`. No `__iter__` either? It calls
`__getitem__` with 0, 1, 2 until `IndexError`.

<div class="nl-type mt-3"><NlIcon name="check" /> When to add <code>__contains__</code></div>

<div style="font-size: 1.05rem">

Only when you can beat a scan — a `set` held inside the object answers in
constant time where the fallback is linear.

</div>

</div>

</div>

<div class="nl-statement mt-3">
Two methods, and your class behaves like a list everywhere a list is accepted
</div>

<!--
SLIDE 19 - Container protocol
On screen ~55 seconds.

Read the recap left to right, four beats. Quatre opérations que vous faites
tous les jours sur des listes, et la méthode que chacune appelle.

Then the gift, which is the actual content of the slide:
"Écrivez seulement __len__ et __getitem__ - deux méthodes de deux lignes -
et vous obtenez aussi le in et l'itération. Gratuitement."

"Parce que quand une opération ne trouve pas sa méthode dédiée, Python ne
renonce pas : il redescend dans le protocole. Pas de __contains__ ? Il
parcourt avec __iter__. Pas d'__iter__ non plus ? Il appelle __getitem__
avec zéro, un, deux, jusqu'à l'IndexError."

PAUSE.

Answer the question they will have:
"Alors quand ajouter __contains__ ? Uniquement quand vous pouvez faire mieux
qu'un parcours. Si vos éléments sont dans un set en interne, votre
__contains__ répond en temps constant là où le parcours est linéaire."

Close the loop with duck typing, ten slides earlier:
"Et votre classe n'a hérité de rien. Elle a écrit deux méthodes, et elle se
comporte comme une liste partout où une liste est acceptée."
-->

---
layout: default
class: nl-deck
---

# Dataclasses

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Python refuses</div>

```python
@dataclass
class Account:
    owner: str
    history: list = []
```

```python
ValueError: mutable default
<class 'list'> for field history
is not allowed: use default_factory
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Written from the annotations</div>

<div style="font-size: 1.05rem">

`__init__`, `__repr__` and `__eq__`, generated from the type hints alone. The
hints are not decoration here — without one, the field does not exist.

</div>

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> The fix</div>

```python
history: list = field(
    default_factory=list
)
```

</div>

</div>

<div class="nl-statement mt-3">
Chapter 04's bug is now a language error — Python refuses before you can ship it
</div>

<!--
SLIDE 20 - Dataclasses. This is the chapter's PAYOFF. Do not rush it.
On screen ~80 seconds.

Start with what it removes, because that is the sales pitch:
"Vous déclarez des champs avec leurs types, et Python vous écrit __init__,
__repr__ et __eq__. Le __repr__ dont on parlait il y a quatre slides. Le
__eq__ d'il y a trois. Tout ça, à partir des annotations."

One precision worth making: les annotations sont obligatoires ici. Sans
annotation, la dataclass ne voit pas le champ du tout.

PAUSE.

Now the payoff. Point at the history line and say nothing for a beat.

"Une liste comme valeur par défaut. Exactement ce qu'on avait tout à
l'heure, sur la diapositive des attributs de classe. Exactement ce qu'on
avait au chapitre quatre avec l'argument par défaut mutable."

PAUSE. Two full seconds.

"Et Python refuse. ValueError. « mutable default list for field history is
not allowed : use default_factory. » Pas un avertissement. Pas un
comportement bizarre à débusquer dans six mois. Un refus, au moment où la
classe est créée."

PAUSE.

Land it:
"Ce bug nous a coûté deux chapitres à expliquer. Les concepteurs du langage
l'ont vu aussi souvent que nous, et ils ont fait la seule chose sensée : ils
l'ont rendu impossible."

Then the fix, calmly: field, avec default_factory égale list. Une usine
appelée une fois par instance, au lieu d'une liste unique sur la classe.
-->

---
layout: default
class: nl-deck
---

# Dataclass & Field Options

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> On the class</div>

<div class="nl-recap mt-2">
  <div class="n">frozen=True</div><div><span class="why">no reassignment; hashable again</span></div>
  <div class="n">order=True</div><div><span class="why">the four comparisons</span></div>
  <div class="n">unsafe_hash</div><div><span class="why">the name is the warning</span></div>
</div>

</div>

<div>

<div class="nl-type"><NlIcon name="box" /> On the field</div>

<div class="nl-recap mt-2">
  <div class="n">default_factory</div><div><span class="why">a fresh object each time</span></div>
  <div class="n">repr=False</div><div><span class="why">keep a token out of your logs</span></div>
  <div class="n">compare=False</div><div><span class="why">keep a timestamp out of ==</span></div>
</div>

</div>

</div>

<div class="mt-4" style="font-size: 1.05rem">

A plain `@dataclass` generates `__eq__`, so its `__hash__` is `None`.
`frozen=True` buys the hash back, if every field is hashable: a list field can
still be mutated, and makes `hash()` fail.

</div>

<div class="nl-statement mt-3">
The free <code>__eq__</code> cost you <code>__hash__</code> — <code>frozen=True</code> buys it back
</div>

<!--
SLIDE 21 - Options
On screen ~65 seconds.

Two recaps, then the paragraph underneath, which is the reason this slide
exists.

frozen first: l'objet devient immuable, toute affectation après la
construction lève une FrozenInstanceError. Et le __hash__ revient.

The caveat, in one breath, because frozen sounds stronger than it is:
« gelé » interdit de réaffecter un champ, pas de modifier ce qu'il contient.
Un champ liste peut toujours recevoir append, et hash échoue alors avec
« unhashable type: 'list' ».

Then take the payoff from slide 17:
"Souvenez-vous du piège du hash. Une dataclass ordinaire génère __eq__ pour
vous. Donc une dataclass ordinaire a exactement le même problème : son
__hash__ vaut None, et elle ne peut pas entrer dans un set. Le cadeau avait
un prix, et personne ne vous l'avait dit."

PAUSE.

"Avec frozen, Python sait que les champs ne changeront plus. Donc un hash
stable est calculable, donc il le génère. Immuable et hachable, d'un seul
mot-clé."

order égale True génère les quatre comparaisons - le total_ordering d'il y a
quatre slides, mais intégré. unsafe_hash, le nom vous dit tout : ne le
touchez pas sans raison.

Field options, thirty seconds, and make them concrete:
"repr égale False, le champ disparaît du __repr__ - c'est comme ça qu'un
jeton d'authentification n'atterrit pas dans vos logs. compare égale False,
le champ est exclu de l'égalité - typiquement un horodatage de création, qui
ne devrait pas empêcher deux enregistrements d'être identiques."
-->

---
layout: default
class: nl-deck
---

# One Mechanism: the Decorator

<div class="nl-cols mt-4">

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> You have used four</div>

`@property` · `@classmethod` · `@staticmethod` · `@dataclass`

<div style="font-size: 1.05rem">

All the same shape: a function that takes your function or your class, and
hands back a replacement.

</div>

</div>

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> What the replacement forgets</div>

```python
>>> alpha.__name__
'wrapper'
>>> beta.__name__
'beta'
```

<div style="font-size: 1.05rem">

`wraps` copies `__name__` and `__doc__`, and sets `__wrapped__`. A traceback
shows a `wrapper` frame either way: frames come from the code, not the name.

</div>

</div>

</div>

<div class="nl-statement mt-3">
A decorator is a function that takes your function and returns a different one
</div>

<!--
SLIDE 22 - Decorators
On screen ~50 seconds. A synthesis slide - it names something they have been
using all chapter without noticing.

"@property. @classmethod. @staticmethod. @dataclass. Quatre décorateurs,
dans une seule vidéo. Et c'est un seul mécanisme : une fonction qui prend
votre fonction, ou votre classe, et renvoie autre chose à la place."

The consequence is the useful part, and it is a chapter-07 callback:
"Ce qui veut dire que ce que vous décorez n'est plus tout à fait ce que vous
avez écrit. Regardez à droite. alpha a perdu son nom : elle s'appelle
« wrapper », parce que c'est le nom de la fonction que le décorateur a
renvoyée. beta a gardé le sien, parce que son décorateur utilise
functools.wraps."

"Pourquoi ça compte ? Parce que help, la documentation, et tous les outils
qui inspectent une fonction lisent __name__ et __doc__. Sans wraps, ils
voient « wrapper », et la docstring a disparu."

Be precise about tracebacks, because it is a common misconception: dans une
trace d'erreur, une ligne « wrapper » apparaît dans les deux cas, avec ou sans
wraps. La trace lit le code, pas le nom. Et la fonction d'origine y apparaît
aussi, juste en dessous.

PAUSE.

Stop here deliberately, and say so:
"Écrire ses propres décorateurs, les décorateurs à arguments, les
décorateurs de classe et le motif Singleton : c'est le chapitre onze. Vous
avez le mécanisme. Vous aurez la fabrication."

SCOPE NOTE - ds-ml-ai-content.md puts decorators in chapter 11. This slide
gives the mechanism and the wraps trap only. Expanding it here leaves 11 with
nothing.
-->

---
layout: default
class: nl-deck
---

# The Errors You Will Actually Read

<div class="grid grid-cols-3 gap-6 mt-4" style="font-size: 0.98rem">

<div class="nl-card">

<div class="nl-type"><NlIcon name="cross" /> TypeError</div>

```python
Transaction.__init__()
missing 1 required
positional argument:
'amount'
```

You forgot an argument.

</div>

<div class="nl-card">

<div class="nl-type"><NlIcon name="cross" /> AttributeError</div>

```python
'Refund' object has no
attribute 'label'.
Did you mean: 'ref'?
```

You forgot `super().__init__()`.

</div>

<div class="nl-card">

<div class="nl-type"><NlIcon name="cross" /> TypeError</div>

```python
Can't instantiate
abstract class Loader
without an implementation
for abstract method 'load'
```

An abstract method is missing.

</div>

</div>

<div class="nl-cols mt-3" style="font-size: 1.05rem">

<div>

<div class="nl-type"><NlIcon name="check" /> Read the qualified name</div>

Python names the class and the method it failed in. That is usually enough to
find the line without a debugger.

</div>

<div>

<div class="nl-type"><NlIcon name="box" /> The suggestion is free</div>

`Did you mean` appears in the printed traceback, not in the exception message
itself.

</div>

</div>

<div class="nl-statement mt-3">
Three messages cover most of the OOP mistakes you will make this year
</div>

<!--
SLIDE 23 - Errors
On screen ~60 seconds. Close on the mistakes, like chapter three did.

The three cards are thirty seconds. Point at each as you read it.

Un : missing one required positional argument, 'amount'. Vous avez oublié un
argument à la construction. Et notez le nom qualifié - Transaction point
__init__ - Python vous dit dans quelle classe.

Deux : 'Refund' object has no attribute 'label'. Neuf fois sur dix, c'est le
super().__init__ oublié.

Trois : can't instantiate abstract class. Une méthode abstraite manque, et
le message vous dit laquelle.

PAUSE.

The two notes underneath are the lesson:
"« Did you mean » n'apparaît que dans la trace affichée. Pas dans le message
de l'exception. Si vous attrapez l'erreur et que vous loguez str(e), vous
perdez la suggestion."

Then the closing habit:
"Apprenez ces trois messages à la reconnaissance, pas à la compréhension.
Dès que vous les voyez, vous savez où aller."
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 09 — THE STANDARD LIBRARY</strong>

</div>

<!--
SLIDE 24 - Closing card
On screen ~14 seconds.

One sentence of chapter summary before the sign-off:
"Une classe n'est pas là pour ranger votre code. Elle est là pour qu'un
attribut ne puisse pas être mal orthographié, et qu'un état ne puisse pas
être partagé par accident."

Then the next chapter out loud: chapitre neuf, la bibliothèque standard -
tout ce que Python sait déjà faire et que vous êtes en train de réécrire.

Then: "À mardi." Hold two beats of silence before you stop recording.
-->
