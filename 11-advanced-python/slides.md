---
theme: ../themes/noonlabs
title: Advanced Python — Chapter 11
info: NoonLabs - Module I, chapitre 11
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

<div class="nl-eyebrow">Chapter 11</div>

# Advanced Python

<div class="mt-4" style="max-width: 42ch">

The machinery under the language: decorators, the object model, concurrency, and the tools to measure it

</div>

<div class="nl-type mt-6">
  <NlIcon name="layers" /> Object model
  <span class="mx-3">·</span>
  <NlIcon name="split" /> Concurrency
  <span class="mx-3">·</span>
  <NlIcon name="prompt" /> Tooling
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~8 seconds.

"Chapitre onze. Le plus dense du module. Jusqu'ici, on utilisait le langage.
Aujourd'hui, on regarde la machinerie dessous : comment un décorateur, une
propriété ou une boucle asynchrone fonctionnent vraiment."

Restate the format so nobody wonders:
"Les diapositives, c'est pour les concepts. Le code, on l'écrit ensemble
dans VS Code."
-->

---
layout: default
class: nl-deck
---

# Writing a Decorator

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Wrap, then return</div>

```python
def log_calls(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"calling {fn.__name__}{args}")
        return fn(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b): return a + b
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> What the @ line does</div>

`@log_calls` above `def add` means `add = log_calls(add)`. The name `add`
now points at `wrapper`, which calls the original.

<div class="nl-type mt-3"><NlIcon name="check" /> The run</div>

<div style="font-size: 1.05rem">

`add(2, 3)` prints `calling add(2, 3)`, then returns 5. `*args, **kwargs`
let one wrapper fit any function; `@wraps` keeps the name `add`.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A decorator replaces your function with one that wraps it
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 3 - Writing a decorator
On screen ~55 seconds.

Pay off two promises at once:
"Au chapitre huit, on a vu le mécanisme d'un décorateur. Au chapitre dix,
on a revu wraps. J'avais promis qu'au chapitre onze, on les écrirait
nous-mêmes. On y est."

Type it live, then call add(2, 3):
"La ligne arobase log_calls, c'est exactement add égale log_calls de add.
Le nom add pointe maintenant vers wrapper. wrapper affiche l'appel, puis
appelle la vraie fonction."

PAUSE.

Callback to chapter four on *args and **kwargs: c'est ce qui permet au même
wrapper d'envelopper n'importe quelle fonction, quels que soient ses
arguments.

[CLICK]
"Un décorateur remplace votre fonction par une autre qui l'enveloppe."

Then remove @wraps live and print add.__name__: "wrapper". Remettez-le. C'est
le piège du chapitre huit.
-->

---
layout: default
class: nl-deck
---

# Decorators with Arguments

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Three levels</div>

```python
def retry(times):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for n in range(1, times + 1):
                try:
                    return fn(*args, **kwargs)
                except ConnectionError:
                    print(f"attempt {n} failed")
            raise ConnectionError("gave up")
        return wrapper
    return decorator
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> A factory</div>

`retry(times=3)` runs first and returns the real decorator. So
`@retry(times=3)` means `fetch = retry(times=3)(fetch)`.

<div class="nl-type mt-3"><NlIcon name="check" /> The run</div>

<div style="font-size: 1.05rem">

On a function that fails twice: `attempt 1 failed`, `attempt 2 failed`, then
its result.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A decorator with arguments is a function that returns a decorator
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 4 - Decorators with arguments
On screen ~60 seconds.

Callback to chapter seven, the retry slide:
"Au chapitre sept, on écrivait une boucle de nouvelles tentatives à la main,
à chaque fois. Ici, on l'écrit une fois, et on la pose sur n'importe quelle
fonction avec une ligne."

Count the levels out loud, pointing at each def:
"Trois niveaux. retry reçoit le nombre d'essais et renvoie un décorateur. Le
décorateur reçoit la fonction et renvoie wrapper. wrapper fait le travail."

PAUSE.

Run it live on a fetch that fails twice, then succeeds: deux lignes « attempt
failed », puis le résultat.

[CLICK]
"Un décorateur avec arguments, c'est une fonction qui fabrique un décorateur.
Une closure de plus - le chapitre dix."
-->

---
layout: default
class: nl-deck
---

# Class Decorators & the Singleton

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> One instance, ever</div>

```python
def singleton(cls):
    inst = {}
    @wraps(cls)
    def get(*args, **kwargs):
        if cls not in inst:
            inst[cls] = cls(*args, **kwargs)
        return inst[cls]
    return get

@singleton
class Config: ...
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> It receives the class</div>

A class decorator gets the finished class and returns whatever replaces it.
Here, `Config() is Config()` is `True`.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-bad"><code>Config</code> is now a function: <code>isinstance(c, Config)</code> raises <code>TypeError</code></li>
<li class="nl-good">A module is imported once — it is already a singleton</li>
</ul>

</div>

</div>

<div v-click class="nl-statement mt-3">
A class decorator receives the class — and can replace it with anything
</div>

<!--
SLIDE 5 - Class decorators
On screen ~55 seconds. Concept slide, no live coding needed.

Same mechanism, one level up: au lieu d'une fonction, le décorateur reçoit une
classe. @dataclass, au chapitre huit, était un décorateur de classe.

Read the singleton: un dictionnaire caché, et une fonction qui renvoie
toujours la même instance.

PAUSE.

Then the honest part, because the curriculum asks for the pattern and
production code mostly avoids it:
"Problème : Config n'est plus une classe. C'est une fonction. isinstance de
c face à Config lève une TypeError. Vous avez cassé quelque chose pour obtenir
le motif."

"En Python, le singleton le plus simple, c'est un module. Il n'est importé
qu'une fois. Créez l'instance dans le module, et importez-la."

[CLICK]
"Un décorateur de classe reçoit la classe - et peut la remplacer par
n'importe quoi. Y compris par quelque chose qui n'est plus une classe."
-->

---
layout: default
class: nl-deck
---

# Context Managers, Revisited

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Two contextlib tools</div>

```python
from contextlib import suppress, ExitStack

with suppress(FileNotFoundError):
    os.remove("cache.tmp")

with ExitStack() as stack:
    files = [stack.enter_context(open(p))
             for p in paths]
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> __exit__ decides</div>

`__exit__` receives the exception. Return `True` and it is swallowed — that
is all `suppress` does.

<div class="nl-type mt-3"><NlIcon name="check" /> ExitStack</div>

<div style="font-size: 1.05rem">

A number of resources you only know at run time, all closed on the way out,
in reverse order.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>__exit__</code> sees every exception — returning <code>True</code> makes it disappear
</div>

<!--
SLIDE 6 - Context managers revisited
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter six, where both forms were written:
"Au chapitre six, on a écrit un gestionnaire de contexte de deux façons : une
classe avec __enter__ et __exit__, et @contextmanager. Deux détails qu'on
n'avait pas vus."

One: __exit__ reçoit l'exception. S'il renvoie True, elle disparaît.
C'est tout ce que fait suppress : il avale l'exception qu'on lui nomme, et
seulement celle-là.

PAUSE.

Two: ExitStack, pour un nombre de ressources qu'on ne connaît qu'à
l'exécution. Une liste de fichiers à ouvrir : chacun est fermé à la sortie,
dans l'ordre inverse.

[CLICK]
"__exit__ voit passer toutes les exceptions. Renvoyer True les fait
disparaître - utilisez-le exprès, jamais par accident."
-->

---
layout: default
class: nl-deck
---

# Descriptors

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> A reusable rule</div>

```python
class Positive:
    def __set_name__(self, owner, name):
        self.name = "_" + name
    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("must be positive")
        setattr(obj, self.name, value)

class Tx:
    amount = Positive()
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> An object on the class</div>

A descriptor sits on the class and takes over one attribute through
`__get__`, `__set__` and `__delete__`.

<div class="nl-type mt-3"><NlIcon name="check" /> property is one</div>

<div style="font-size: 1.05rem">

`property` has a `__get__` and a `__set__`. `__set_name__` tells a
descriptor its own name, so one class guards any field.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>property</code> is a descriptor — and now you can write your own
</div>

<!--
SLIDE 7 - Descriptors
On screen ~60 seconds. Concept slide, no live coding needed.

Pay off the plant from chapter eight, the property slide:
"Au chapitre huit, je vous ai dit : property est un objet qui fait quelque
chose d'assez malin sous le capot, on verra quoi au chapitre onze. Le voilà.
property est un descripteur."

Read Positive top to bottom:
"__set_name__ apprend le nom de l'attribut. __get__ se déclenche à la lecture,
__set__ à l'écriture. Et si la valeur est négative, ValueError."

PAUSE.

"Tx moins cinq lève une ValueError, sans une ligne de validation dans Tx.
Et la même classe Positive peut protéger amount, quantity, price - autant de
champs que vous voulez."

[CLICK]
"property est un descripteur. Et maintenant, vous savez écrire les vôtres."

Mention it once and move on: les méthodes elles-mêmes sont des descripteurs.
C'est comme ça que self est lié à l'objet.
-->

---
layout: default
class: nl-deck
---

# `__getattr__` vs `__getattribute__`

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> The fallback</div>

```python
class Lazy:
    def __getattr__(self, name):
        return f"computed {name}"

>>> obj = Lazy(); obj.x = 1
>>> obj.x, obj.y
(1, 'computed y')
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> Every lookup</div>

```python
def __getattribute__(self, name):
    return self.__dict__[name]
# RecursionError
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> When each runs</div>

<div class="nl-recap mt-2">
  <div class="n">__getattr__</div><div><span class="why">only when the normal lookup fails</span></div>
  <div class="n">__getattribute__</div><div><span class="why">on every attribute access</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

Inside `__getattribute__`, `self.__dict__` is an attribute access too, so it
calls itself forever. Delegate with `super().__getattribute__(name)`.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>__getattr__</code> is the fallback; <code>__getattribute__</code> is every lookup
</div>

<!--
SLIDE 8 - getattr vs getattribute
On screen ~55 seconds. Concept slide, no live coding needed.

The names are almost identical, so slow down on the difference:
"__getattr__ n'est appelé que si l'attribut est introuvable. obj.x existe,
on le lit normalement : un. obj.y n'existe pas, __getattr__ prend le relais."

PAUSE.

Then the trap:
"__getattribute__, lui, est appelé pour chaque accès, sans exception. Et
dedans, self.__dict__ est aussi un accès à un attribut. Donc il s'appelle
lui-même, à l'infini. RecursionError."

[CLICK]
"__getattr__, c'est le filet. __getattribute__, c'est chaque lecture. Si vous
pensez avoir besoin du second, vous vouliez presque toujours le premier."

The way out, if they really need it: déléguer avec super().__getattribute__.
-->

---
layout: default
class: nl-deck
---

# Metaclasses

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> type builds classes</div>

```python
>>> Point = type("Point", (), {"x": 0})
>>> Point().x
0
>>> type(Point), type(type)
(<class 'type'>, <class 'type'>)
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Usually enough</div>

```python
class Plugin:
    registry = {}
    def __init_subclass__(cls, **kw):
        super().__init_subclass__(**kw)
        Plugin.registry[cls.__name__] = cls
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> A class for classes</div>

A class is an object, built by `type`. A metaclass is a subclass of `type`:
`class Model(metaclass=Meta)` lets `Meta` shape `Model` as it is built.

<div class="nl-type mt-3"><NlIcon name="split" /> Before you write one</div>

<div style="font-size: 1.05rem">

Registering or validating subclasses is `__init_subclass__`: `class Csv(Plugin)`
registers `Csv`, with no metaclass.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Classes are built by <code>type</code> — reach for <code>__init_subclass__</code> before a metaclass
</div>

<!--
SLIDE 9 - Metaclasses
On screen ~60 seconds. Concept slide, no live coding needed.

Start with the line that changes how they see classes:
"type, avec trois arguments, fabrique une classe. Un nom, des parents, des
attributs. C'est exactement ce que fait le mot-clé class, en coulisses."

"Et type de Point, c'est type. Type de type, c'est encore type. Une classe
est un objet, et c'est type qui l'a construite."

PAUSE.

"Une métaclasse, c'est une sous-classe de type. Elle intervient au moment où
la classe est construite. Les ORM et les frameworks s'en servent. Vous, très
rarement."

[CLICK]
"Les classes sont fabriquées par type. Avant d'écrire une métaclasse, essayez
__init_subclass__."

Read the Plugin example as the proof: cinq lignes, et chaque sous-classe
s'enregistre toute seule. C'était le cas d'usage numéro un des métaclasses.
-->

---
layout: default
class: nl-deck
---

# `__slots__`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Fixed attributes</div>

```python
class Point:
    __slots__ = ("x", "y")

>>> p = Point(); p.x = 1
>>> p.z = 3
AttributeError: 'Point' object has no
attribute 'z'
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> No __dict__</div>

Attributes live in fixed slots instead of a per-object dict. Objects get
smaller, and a typo raises instead of quietly creating a new attribute.

<div class="nl-type mt-3"><NlIcon name="box" /> Measured with tracemalloc</div>

<div style="font-size: 1.05rem">

100,000 two-field objects: 8.8 MB plain, 5.6 MB with slots, on CPython 3.12.
`@dataclass(slots=True)` writes `__slots__` for you (3.10+).

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>__slots__</code> trades flexibility for memory — and catches typos for free
</div>

<!--
SLIDE 10 - slots
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter eight, the very first slide: le dictionnaire qui
acceptait « ammount » avec deux M sans rien dire. Avec __slots__, l'objet
refuse : AttributeError.

Then the memory, with the real numbers:
"Cent mille petits objets. Huit virgule huit mégaoctets sans slots. Cinq
virgule six avec. Plus d'un tiers en moins, mesuré avec tracemalloc."

PAUSE.

[CLICK]
"__slots__ échange de la souplesse contre de la mémoire. Et attrape les
fautes de frappe au passage."

Time-sensitive: these figures are CPython 3.12. On 3.13 and 3.14 the plain
version measures 9.6 MB, and the error message adds « and no __dict__ for
setting new attributes ». Run verify-facts.py on the recording machine.

Close on the habit: pour une dataclass, slots égale True, depuis Python 3.10.
-->

---
layout: default
class: nl-deck
---

# Threads & the GIL

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Four threads, pure computation</div>

```python
def work(n):
    s = 0
    for i in range(n):
        s += i

threads = [Thread(target=work,
                  args=(4_000_000,))
           for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> One bytecode at a time</div>

The GIL lets one thread run Python bytecode at a time. Four threads on pure
Python computation take turns, and pay for the switching.

<div class="nl-type mt-3"><NlIcon name="check" /> Where threads help</div>

<div style="font-size: 1.05rem">

Waiting: network, disk, `sleep`. A waiting thread releases the GIL. `Lock`,
`Semaphore` and `Event` coordinate them.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
On the default build, threads overlap waiting — not pure-Python computing
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 11 - Threads and the GIL. This is the chapter's PLANT.
On screen ~65 seconds.

Time it live: work four times in a row, then four threads. Read both numbers
off the screen - on the build machine, CPython 3.12, the threads took about
three times as long as the serial run.

"Quatre threads pour un calcul : plus lent qu'un seul. Pas un peu plus
lent - nettement."

PAUSE.

"La raison s'appelle le GIL, le verrou global de l'interpréteur. Un seul
thread exécute du Python à la fois. Les quatre se relaient, et chaque relais
coûte."

PLANT the payoff and do not explain it:
"Retenez-le : en Python, des threads ne font pas calculer plus vite."

[CLICK]

Then where threads do help: attendre. Réseau, disque, sleep : un thread qui
attend rend le GIL. Lock pour protéger une donnée partagée, Semaphore pour
limiter le nombre de threads simultanés, Event pour qu'un thread en prévienne
un autre.

Time-sensitive, one sentence: depuis Python 3.14, une version sans GIL est
officiellement supportée, mais elle reste optionnelle. Par défaut, le GIL est
toujours là.

And the scope of the rule, said once: tout ça vaut pour du code Python pur.
Une extension en C, comme NumPy, peut libérer le GIL pendant ses calculs -
des threads qui appellent NumPy peuvent vraiment calculer en parallèle.
-->

---
layout: default
class: nl-deck
---

# Processes

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> The same work, four processes</div>

```python
from multiprocessing import Pool

if __name__ == "__main__":
    with Pool(4) as pool:
        pool.map(work, [4_000_000] * 4)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> One interpreter each</div>

Each process has its own interpreter, and its own GIL: four really run at
once. `Pool` is built on `Process` and `Queue`, the lower-level parts.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> The price</div>

<div style="font-size: 1.05rem">

Arguments and results are pickled to cross over, and starting a process
takes time. The `__main__` guard is required.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
CPU-bound work wants processes — one interpreter, one GIL each
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 12 - Processes. This is the chapter's PAYOFF.
On screen ~60 seconds.

Then land the payoff planted on the threads slide. Do this live, same work,
same machine:
"Souvenez-vous des quatre threads, plus lents qu'un seul. Mêmes calculs,
quatre processus."

Read the number. On the build machine, CPython 3.12, about three times faster
than serial; on 3.14, which starts processes differently on Linux, about one
and a half times for a job this small. Say your own number.

PAUSE.

"Chaque processus a son propre interpréteur. Et donc son propre GIL. Cette
fois, les quatre calculent vraiment en même temps."

[CLICK]
"Un calcul lourd, c'est des processus. Un interpréteur, un GIL chacun."

The price, briefly: les arguments et les résultats sont sérialisés avec
pickle - chapitre six - et démarrer un processus coûte du temps. Et le if
__name__ égale __main__ du chapitre quatre devient obligatoire : chaque
processus réimporte votre fichier.

One more name to know: concurrent.futures, avec ProcessPoolExecutor et
ThreadPoolExecutor. La même interface pour les deux.
-->

---
layout: default
class: nl-deck
---

# asyncio: `async` & `await`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Three waits, one thread</div>

```python
async def fetch(i):
    await asyncio.sleep(0.5)
    return i

async def main():
    return await asyncio.gather(
        fetch(1), fetch(2), fetch(3))

asyncio.run(main())  # [1, 2, 3]
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Pause while waiting</div>

Calling an `async def` builds a coroutine; nothing runs until it is awaited.
`await` hands control back to the event loop while it waits.

<div class="nl-type mt-3"><NlIcon name="arrow" /> 0.5 seconds, not 1.5</div>

<div style="font-size: 1.05rem">

`gather` runs the three at once. `create_task` starts one in the background
and lets you carry on.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
asyncio is one thread that never sits idle while it waits
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 13 - asyncio basics
On screen ~60 seconds.

Callback to chapter ten, the generator slide:
"Au chapitre dix, yield mettait une fonction en pause. await, c'est la même
idée : la coroutine se met en pause pendant qu'elle attend, et la boucle
d'événements fait avancer les autres."

Run it live, and time it:
"Trois attentes d'une demi-seconde. Si on les faisait l'une après l'autre :
une seconde et demie. Avec gather : une demi-seconde. Un seul thread."

PAUSE.

The trap to say now, before they hit it: appeler une fonction async ne fait
rien. Ça fabrique une coroutine. Tant que personne ne l'attend, rien ne se
passe.

[CLICK]
"asyncio, c'est un seul thread qui ne reste jamais les bras croisés pendant
qu'il attend."

Fit it with the two previous slides: calcul lourd, des processus. Beaucoup
d'attentes réseau, asyncio. Quelques attentes dans du code existant, des
threads.
-->

---
layout: default
class: nl-deck
---

# asyncio in Practice

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Three modern tools</div>

```python
async with asyncio.TaskGroup() as tg:
    a = tg.create_task(fetch(1))
    b = tg.create_task(fetch(2))

async with asyncio.timeout(2):
    await slow_call()

await asyncio.to_thread(blocking_io)
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> What each guarantees</div>

<div class="nl-recap mt-2">
  <div class="n">TaskGroup</div><div><span class="why">waits for all; one fails, the rest are cancelled</span></div>
  <div class="n">timeout</div><div><span class="why">cancels the block past the deadline</span></div>
  <div class="n">to_thread</div><div><span class="why">blocking code without freezing the loop</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

When several tasks fail, `TaskGroup` raises an `ExceptionGroup`: the
`except*` from chapter 07.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>TaskGroup</code> never leaves a task behind — <code>except*</code> catches what they raised
</div>

<!--
SLIDE 14 - asyncio in practice
On screen ~55 seconds. Concept slide, no live coding needed.

Pay off chapter seven, the ExceptionGroup slide:
"Au chapitre sept, je vous ai dit : vous rencontrerez except étoile avec
asyncio.TaskGroup bien avant de l'écrire vous-même. Le voilà. Deux tâches
échouent, TaskGroup lève un ExceptionGroup, et except étoile trie les
erreurs."

The three tools, one line each. TaskGroup attend toutes les tâches, et si
l'une échoue, il annule les autres - aucune tâche orpheline. timeout annule
un bloc trop long. to_thread envoie du code bloquant dans un thread.

PAUSE.

[CLICK]
"TaskGroup ne laisse jamais une tâche derrière lui. Et except étoile attrape
tout ce qu'elles ont levé."

Time-sensitive: TaskGroup et timeout depuis Python 3.11, to_thread depuis
3.9. Python 3.14 ajoute python -m asyncio ps, qui affiche les tâches d'un
programme en cours d'exécution.
-->

---
layout: default
class: nl-deck
---

# Generics

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> The 3.12 syntax</div>

```python
def first[T](xs: list[T]) -> T:
    return xs[0]

class Stack[T]:
    def __init__(self) -> None:
        self.items: list[T] = []
    def push(self, x: T) -> Self:
        self.items.append(x)
        return self
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Old form, new form</div>

<div class="nl-recap mt-2">
  <div class="n">T = TypeVar("T")</div><div><span class="why">def first[T] — 3.12+</span></div>
  <div class="n">Stack(Generic[T])</div><div><span class="why">class Stack[T] — 3.12+</span></div>
  <div class="n">-> "Stack"</div><div><span class="why">-> Self — 3.11+</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

`T` says: the type that goes in is the type that comes out.
`first([3, 4])` is an `int` to your editor.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
A type variable links what goes in to what comes out
</div>

<!--
SLIDE 15 - Generics
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter four, the type hints translation table:
"Au chapitre quatre, on a traduit List en list et Optional en barre
verticale. Même exercice ici : vous lirez TypeVar et Generic partout dans
le code existant. Depuis Python 3.12, il y a plus court."

Read first: « T » veut dire « un type, n'importe lequel, mais le même des
deux côtés ». Une liste d'entiers entre, un entier sort. Votre éditeur le
sait.

PAUSE.

Self in one line: une méthode qui renvoie l'objet lui-même. Ça permet
d'enchaîner, push puis push.

[CLICK]
"Une variable de type relie ce qui entre à ce qui sort."

Repeat chapter four's rule, because generics make people forget it: rien de
tout ça n'est vérifié à l'exécution. C'est pour l'éditeur et pour mypy.
-->

---
layout: default
class: nl-deck
---

# `Protocol` & `TypedDict`

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Typing a shape</div>

```python
class HasTotal(Protocol):
    def total(self) -> Decimal: ...

def report(x: HasTotal) -> str: ...
```

```python
class Row(TypedDict):
    categorie: str
    montant: float
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="split" /> Protocol: the duck, written down</div>

Any class with a `total()` method matches, with no inheritance.
`isinstance` checks need `@runtime_checkable`.

<div class="nl-type mt-3"><NlIcon name="box" /> TypedDict: keys for the checker</div>

<div style="font-size: 1.05rem">

It describes a dict's keys and value types. At run time it is a plain dict,
and nothing is validated.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>Protocol</code> types the duck; <code>TypedDict</code> types the dict
</div>

<!--
SLIDE 16 - Protocol and TypedDict
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter eight, duck typing:
"Au chapitre huit : Python ne demande pas ce que vous êtes, il demande si
vous répondez. Protocol, c'est cette phrase, écrite pour le vérificateur de
types. N'importe quelle classe qui a une méthode total convient. Sans
hériter de rien."

Then TypedDict, tied to the CSV:
"Les lignes de DictReader, au chapitre six, sont des dictionnaires.
TypedDict décrit leurs clés : categorie est une chaîne, montant un nombre.
Votre éditeur vous corrige si vous écrivez « categori »."

PAUSE.

"Mais à l'exécution, c'est un dict ordinaire. Rien n'est vérifié."

[CLICK]
"Protocol type le canard. TypedDict type le dictionnaire."
-->

---
layout: default
class: nl-deck
---

# Memory: Refcounts, `gc` & `weakref`

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> A cycle</div>

```python
>>> a, b = Node(), Node()
>>> a.other, b.other = b, a
>>> del a, b
>>> gc.collect()   # frees the pair
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Three mechanisms</div>

<div class="nl-recap mt-2">
  <div class="n">refcount</div><div><span class="why">freed when the last reference goes</span></div>
  <div class="n">gc</div><div><span class="why">finds the cycles refcounts cannot</span></div>
  <div class="n">weakref</div><div><span class="why">refers without keeping alive</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

After `del`, each `Node` is still referenced by the other, so its count never
reaches zero. `tracemalloc` shows where memory was allocated, line by line.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Reference counting frees most objects — <code>gc</code> exists for the cycles
</div>

<!--
SLIDE 17 - Memory
On screen ~55 seconds. Concept slide, no live coding needed.

Callback to chapter five, the memory model: des noms qui pointent vers des
objets. Chaque objet compte combien de noms pointent vers lui. Quand le
compte tombe à zéro, il est libéré, immédiatement.

Then the cycle:
"a pointe vers b, b pointe vers a. On supprime les deux noms. Mais chacun
est encore référencé par l'autre. Le compte ne tombe jamais à zéro."

PAUSE.

"C'est pour ça qu'il existe un deuxième mécanisme, le ramasse-miettes du
module gc. Il cherche les cycles que personne ne peut plus atteindre, et
les libère."

[CLICK]
"Le comptage de références libère presque tout. gc existe pour les cycles."

weakref in one line: une référence qui ne garde pas l'objet en vie - pour un
cache qui ne doit pas empêcher la mémoire d'être libérée. Le lru_cache sur
une méthode, au chapitre dix, gardait self en vie : c'est le problème
inverse.
-->

---
layout: default
class: nl-deck
---

# Profiling

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="terminal" /> Where the time goes</div>

```bash
python -m cProfile -s cumulative app.py
```

<div class="nl-type mt-2"><NlIcon name="prompt" /> One snippet, many runs</div>

```python
>>> import timeit
>>> timeit.timeit("sum(range(1000))",
...               number=10_000)
```

</div>

<div>

<div class="nl-type"><NlIcon name="layers" /> Three tools</div>

<div class="nl-recap mt-2">
  <div class="n">timeit</div><div><span class="why">one small snippet, repeated</span></div>
  <div class="n">cProfile</div><div><span class="why">every call, counted and timed</span></div>
  <div class="n">pstats</div><div><span class="why">sorts and filters cProfile's output</span></div>
</div>

<div class="mt-3" style="font-size: 1.05rem">

Python 3.15 adds a sampling profiler, `profiling.sampling`, that attaches to
a running program; `cProfile` stays available.

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
Measure before you optimise — the slow part is rarely where you guess
</div>

<!--
SLIDE 18 - Profiling
On screen ~55 seconds. Concept slide, no live coding needed.

Three tools, three scales:
"timeit, pour comparer deux façons d'écrire une ligne. cProfile, pour savoir
quelle fonction mange le temps dans tout un programme. pstats, pour trier ce
que cProfile a mesuré - par temps cumulé, en général."

Callback to chapter nine, perf_counter: pour chronométrer un bloc,
perf_counter suffit. Pour savoir où le temps passe, il faut un profileur.

PAUSE.

[CLICK]
"Mesurez avant d'optimiser. La partie lente est rarement là où vous
l'imaginez."

Time-sensitive, and check before recording: Python 3.15, dont la sortie est
prévue le 9 octobre 2026, ajoute un module profiling. Un profileur par
échantillonnage, profiling.sampling, qui s'attache à un programme qui tourne
sans le ralentir ; cProfile reste disponible sous son ancien nom. Le module
profile, lui, est déprécié.
-->

---
layout: default
class: nl-deck
---

# Debugging

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> Stop and look</div>

```python
def total(rows):
    breakpoint()   # opens pdb here
    return sum(r["montant"] for r in rows)
```

```bash
PYTHONBREAKPOINT=0 python app.py
python -m pdb app.py
```

</div>

<div>

<div class="nl-type"><NlIcon name="prompt" /> Five pdb commands</div>

<div class="nl-recap mt-2">
  <div class="n">n</div><div><span class="why">next line</span></div>
  <div class="n">s</div><div><span class="why">step into the call</span></div>
  <div class="n">c</div><div><span class="why">continue to the next breakpoint</span></div>
  <div class="n">p x</div><div><span class="why">print x</span></div>
  <div class="n">w</div><div><span class="why">where: the call stack</span></div>
</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>breakpoint()</code> beats <code>print()</code> — you can ask the program questions
</div>

<!--
SLIDE 19 - Debugging
On screen ~55 seconds. Concept slide, no live coding needed.

"Un print, c'est une question que vous avez posée avant de lancer le
programme. breakpoint, c'est un arrêt où vous posez toutes les questions que
vous voulez, au moment où vous en avez besoin."

The five commands, one line each, then the two command lines:
"PYTHONBREAKPOINT égale zéro désactive tous les breakpoint sans toucher au
code. Et python tiret m pdb lance tout le script sous le débogueur : s'il
plante, vous atterrissez à l'endroit du plantage, avec toutes les variables."

PAUSE.

Callback to chapter seven, reading a traceback: la trace dit où ça a cassé.
Le débogueur vous laisse regarder pourquoi.

[CLICK]
"breakpoint vaut mieux que print. Vous pouvez interroger le programme."

VS Code in one sentence: le même principe avec des boutons. Un point rouge
dans la marge, F5. Time-sensitive: depuis Python 3.14, python -m pdb -p
suivi d'un numéro de processus s'attache à un programme déjà en cours.
-->

---
layout: default
class: nl-deck
---

# Advanced Python Pitfalls

<div class="nl-cols mt-4" style="font-size: 1.05rem">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Threads for CPU-bound work</div>

On the default build, pure-Python threads take turns: slower, not faster.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> A wrapper without wraps</div>

`help()` and `__name__` say `wrapper`, and the docstring is gone.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> A blocking call in async def</div>

`time.sleep` inside a coroutine freezes every task on the loop.

</div>

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> Processes, or concurrent.futures</div>

One interpreter and one GIL per worker.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> @wraps(fn) on every wrapper</div>

The name and the docstring survive.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> await asyncio.sleep, or to_thread</div>

The loop keeps serving the other tasks while one waits.

</div>

</div>

<div v-click class="nl-statement mt-3">
None of these crash — they just quietly cost you
</div>

<!--
SLIDE 20 - Pitfalls
On screen ~60 seconds. Close the chapter on the mistakes, not a summary.

Read the left column, then the right, pair by pair. Ten seconds each.

"Des threads pour un calcul : plus lent, on l'a mesuré. Un wrapper sans
wraps : help et __name__ parlent de « wrapper », et la docstring a disparu.
Un time.sleep dans une coroutine : toute la boucle s'arrête, et toutes les
tâches avec."

PAUSE.

[CLICK]
"Aucune de ces erreurs ne plante. Elles vous coûtent, en silence : du temps,
de la lisibilité, des tâches bloquées."

Callback to chapter nine, the pitfalls slide: même famille d'erreurs. Le
code tourne, et c'est précisément pour ça qu'on ne les voit pas.
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 12 — NUMPY</strong>

</div>

<!--
SLIDE 21 - Closing card
On screen ~12 seconds.

One sentence of chapter summary before the sign-off:
"Vous savez maintenant ce qu'il y a sous le capot : les décorateurs, les
descripteurs, et pourquoi un thread ne calcule pas plus vite."

Say the next chapter's topic out loud while this is up: chapitre douze,
NumPy - le premier pas vers le calcul numérique et l'IA.
Then: "À mardi." Hold two beats of silence before you stop recording.
-->
