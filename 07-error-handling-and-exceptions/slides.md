---
theme: ../themes/noonlabs
title: Error Handling & Exceptions — Chapter 07
info: NoonLabs - Module I, chapitre 07
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

<div class="nl-eyebrow">Chapter 07</div>

# Error Handling &amp; Exceptions

<div class="mt-4" style="max-width: 42ch">

Failing on purpose, failing loudly, and reading what Python already told you

</div>

<div class="nl-type mt-6">
  <NlIcon name="cross" /> Tracebacks
  <span class="mx-3">·</span>
  <NlIcon name="split" /> try / except
  <span class="mx-3">·</span>
  <NlIcon name="box" /> raise
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~8 seconds.

"Chapitre sept. Le chapitre six s'est terminé sur une idée : on essaie, et on
gère l'échec. Maintenant on prend ça au sérieux."

Then the framing that makes the whole chapter land:
"Et on commence par la compétence que personne n'enseigne, alors que c'est la
plus rentable de tout le module : lire un message d'erreur."
-->

---
layout: default
class: nl-deck
---

# Reading a Traceback

<div class="nl-cols mt-4">

<div>

```python
Traceback (most recent call last):
  File "analyse.py", line 14,
    in <module>
    total = total + ligne["montant"]
            ~~~~~~~^~~~~~~~~~~~~~~~~
TypeError: unsupported operand
type(s) for +: 'int' and 'str'
```

</div>

<div style="font-size: 1.05rem">

<div class="nl-type"><NlIcon name="arrow" /> Read it from the bottom up</div>

- **Last line first** — the type of failure and the reason
- **Then the line above** — the file, line number and statement
- **Then upwards** — who called that, and who called them
- The `^^^^` marks the exact expression that failed

<div class="nl-type mt-2 nl-type--plain">
"Most recent call <strong>last</strong>" — your code is usually near the bottom, library code above it.
</div>

</div>

</div>

<div class="nl-statement mt-3">
The traceback is not noise — it is the answer, written before you asked
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 3 - Tracebacks
On screen ~70 seconds. Open the chapter here, deliberately. This is the
single highest-value skill in the module and almost no course teaches it.

Use THE traceback from video one. Reproduce it live if you can.

"Vous avez déjà vu ça. C'était la première vidéo. Notre programme a échoué,
on a lu la dernière ligne, on a corrigé avec float, et on est passé à la
suite. Aujourd'hui on lit tout."

Then walk it, bottom to top, with the cursor:
"La dernière ligne : le type d'erreur et la raison. TypeError, on ne peut pas
additionner un entier et une chaîne. La ligne au-dessus : le fichier, le
numéro de ligne, et l'instruction exacte. Et les petits chapeaux, en dessous,
montrent quelle partie de la ligne a échoué."

PAUSE.

"« Most recent call last ». Le plus récent en dernier. Donc votre code est
souvent en bas, et les bibliothèques au-dessus. Quand une trace fait
quarante lignes, cherchez la dernière ligne qui mentionne VOTRE fichier."

That one sentence saves them hours. Say it twice.
-->

---
layout: default
class: nl-deck
---

# The Exception Hierarchy

<div class="nl-cols mt-4">

<div>

```text
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── OSError
    ├── TypeError
    └── ValueError
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why the split at the top matters</div>

`except Exception` does **not** catch `KeyboardInterrupt` or `SystemExit` —
they sit beside `Exception`, not under it. That is deliberate: Ctrl-C must
always work, even inside a handler.

<div style="font-size: 1.05rem">

Catching a parent catches every child. `except OSError` covers
`FileNotFoundError` and `PermissionError`; `except LookupError` covers both
`KeyError` and `IndexError`.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>except Exception</code> at the top of a program</li>
<li class="nl-bad"><code>except BaseException</code> — you just broke Ctrl-C</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Catching a parent catches every child — so choose the level on purpose
</div>

<!--
SLIDE 4 - Hierarchy
On screen ~60 seconds.

The tree is the slide. Point at the four siblings of Exception and explain
why they are up there:
"SystemExit et KeyboardInterrupt ne sont PAS sous Exception. C'est voulu.
Quand vous faites Contrôle-C, vous voulez que le programme s'arrête - pas
qu'un `except Exception` quelque part l'avale et continue."

Demo it in the terminal: a loop with `except Exception: pass` that you can
still interrupt. Then change it to BaseException and show that Ctrl-C no
longer works. Fifteen seconds, and it is unforgettable.

PAUSE.

Then the inheritance point, which is the practical one:
"Attraper un parent attrape tous les enfants. `except OSError` couvre le
fichier introuvable ET les droits insuffisants. Choisissez le niveau
exprès - ni trop haut, ni trop bas."
-->

---
layout: default
class: nl-deck
---

# try / except: Catch What You Expect

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> Specific</div>

```python
try:
    n = int(raw)
except ValueError:
    n = 0
```

<div class="nl-type mt-2"><NlIcon name="split" /> Several, one clause</div>

```python
except (ValueError, TypeError):
    ...
```

<div class="nl-type mt-2"><NlIcon name="arrow" /> Different handling each</div>

```python
except FileNotFoundError:
    create_default()
except PermissionError:
    ask_for_rights()
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> Keep the try block short</div>

Wrap only the line that can fail. A ten-line `try` catches errors you never
thought about and hands them the wrong handler.

<div style="font-size: 1.05rem">

The first matching clause wins and the rest are skipped, so order from
specific to general — the same rule as `elif` in chapter three.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">One risky call inside the <code>try</code></li>
<li class="nl-bad">Your whole function inside one <code>try</code></li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
A wide <code>try</code> block catches bugs you meant to find
</div>

<!--
SLIDE 5 - try/except
On screen ~60 seconds.

The narrow-try rule is the one that separates working code from
maintainable code, so make it concrete. Show a function with everything
inside one try, then a typo in a variable name three lines down. The
NameError gets caught by `except ValueError`? No - but with
`except Exception` it does, and now your typo silently produces a zero.

"Un try large attrape des erreurs que vous auriez voulu voir. Votre faute de
frappe devient un zéro, et le programme continue tranquillement avec un
résultat faux."

PAUSE.

Then the ordering, with the chapter-three callback:
"Le premier `except` qui correspond gagne. Donc du plus précis au plus
général - exactement comme les elif."
-->

---
layout: default
class: nl-deck
---

# Accessing the Exception: as e

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> An exception is an object</div>

```python
try:
    data = json.loads(raw)
except ValueError as e:
    log.warning("bad json: %s", e)
```

<div class="nl-type mt-2"><NlIcon name="prompt" /> What it carries</div>

```python
e.args          # the arguments
str(e)          # the message
type(e).__name__
e.__traceback__
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Specific types carry more</div>

An `OSError` knows its `errno` and `filename`. A `subprocess.CalledProcessError`
knows the exit code and the output. A `UnicodeDecodeError` knows the byte
position that failed.

<div style="font-size: 1.05rem">

That detail is the difference between "something went wrong" and a message
somebody can act on.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Include the value that caused it in your message</li>
<li class="nl-bad">Discarding <code>e</code> and logging "error occurred"</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Put the offending value in the message — future-you is the one reading it
</div>

<!--
SLIDE 6 - as e
On screen ~55 seconds.

Lead with "an exception is an object" - it reframes the whole thing:
"Une exception n'est pas un message. C'est un objet. Il a un type, des
arguments, une trace, et souvent des attributs spécifiques."

Show it live: catch a FileNotFoundError and print e.filename and e.errno.

"Regardez : il sait QUEL fichier. Vous n'avez pas besoin de le deviner."

Then the message discipline, which is a production habit:
"« Une erreur est survenue » ne sert à personne. Mettez la valeur fautive
dans le message. Le fichier, la clé, le nombre. C'est vous, dans six mois, à
deux heures du matin, qui lirez ce journal."
-->

---
layout: default
class: nl-deck
---

# else and finally: The Full Structure

<div class="nl-cols mt-4">

<div>

```python
try:
    f = open(path)
except FileNotFoundError:
    print("missing")
else:
    data = f.read()
finally:
    print("always runs")
```

</div>

<div style="font-size: 1.05rem">

<div class="nl-recap mt-1">
  <div class="n">try</div><div><span class="why">the code that might fail</span></div>
  <div class="n">except</div><div><span class="why">runs only if it did</span></div>
  <div class="n">else</div><div><span class="why">runs only if it did <strong>not</strong></span></div>
  <div class="n">finally</div><div><span class="why">runs either way, always</span></div>
</div>

<div class="nl-type mt-3"><NlIcon name="check" /> Why <code>else</code> is not decoration</div>

Code in `else` is outside the `try`, so its own exceptions are not caught by
your handler. Moving the success path there keeps the `try` narrow — the rule
from two slides ago, enforced by the syntax.

</div>

</div>

<div class="nl-statement mt-3">
<code>else</code> is the success path — and it is deliberately unprotected
</div>

<!--
SLIDE 7 - else and finally
On screen ~55 seconds.

Most people never use `else` on a try, so justify it rather than listing it:
"Pourquoi un else ? Parce que le code dans le else est HORS du try. Ses
propres erreurs ne sont pas attrapées par votre gestionnaire. C'est la règle
du bloc try étroit, mais imposée par la syntaxe."

The loop callback lands well here:
"Et vous connaissez déjà ce mot-clé dans ce sens. Au chapitre trois, le else
d'une boucle voulait dire « aucun break ». Ici, ça veut dire « aucune
exception ». Même idée : le chemin normal."

`finally` gets ten seconds now - the next slide is entirely about its traps.
-->

---
layout: default
class: nl-deck
---

# The finally Traps

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> A return in finally swallows it</div>

```python
def f():
    try:
        raise ValueError("lost")
    finally:
        return "ok"

f()   # 'ok' — no exception at all
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Prefer a context manager</div>

```python
with open(path) as f:
    data = f.read()
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> <code>finally</code> always wins</div>

A `return` — or a `break`, or a second `raise` — inside `finally` replaces
whatever was happening. The original exception is discarded silently, with no
trace of it anywhere.

<div style="font-size: 1.05rem">

`finally` is for **releasing**, never for deciding. And if the thing you are
releasing has a context manager, use that instead: chapter six's `with` is a
`try/finally` you cannot get wrong.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Close, unlock, roll back, delete the temp file</li>
<li class="nl-bad"><code>return</code> or <code>raise</code> inside <code>finally</code></li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Nothing escapes <code>finally</code> — including the exception you wanted to see
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 8 - finally traps
On screen ~60 seconds. Demo the swallow live - it is genuinely startling.

Write the function, call it, and show that it returns 'ok'.

"On a levé une ValueError. Où est-elle ? Nulle part. Pas de trace, pas de
message, rien. Le return dans le finally l'a remplacée."

PAUSE. Let that sit.

"C'est la pire catégorie de bug : celui qui efface la preuve."

Then the rule, which is short enough to remember:
"Le finally sert à LIBÉRER, jamais à DÉCIDER. Fermer, déverrouiller,
annuler, supprimer le fichier temporaire. Pas return, pas raise."

Then the chapter-six callback: et si l'objet a un gestionnaire de contexte,
utilisez `with`. C'est un try/finally qu'on ne peut pas rater.
-->

---
layout: default
class: nl-deck
---

# raise: Signalling Failure

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="arrow" /> Refuse, with a reason</div>

```python
def withdraw(amount):
    if amount <= 0:
        raise ValueError(
            f"must be > 0, got {amount}")
    ...
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> The alternative people choose</div>

```python
    if amount <= 0:
        return None   # caller ignores it
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Failing loudly is a feature</div>

A returned `None` can be ignored, passed on, and stored — the failure surfaces
three functions away from its cause. An exception stops at the mistake and
names it.

<div style="font-size: 1.05rem">

Pick the type that describes the problem: `ValueError` for a bad value,
`TypeError` for a wrong type, `KeyError` for a missing key, `NotImplementedError`
for a stub.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Validate at the boundary, raise immediately</li>
<li class="nl-bad">Returning a sentinel and hoping someone checks it</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Fail where the mistake is, not three functions later
</div>

<!--
SLIDE 9 - raise
On screen ~55 seconds.

Frame it as a design choice, because that is what it is:
"Votre fonction reçoit une valeur impossible. Vous avez deux options :
renvoyer None, ou lever une exception."

Then make the cost of the first one concrete:
"Un None, ça se range dans une variable. Ça se passe à une autre fonction.
Ça finit dans un fichier. Et le plantage arrive trois fonctions plus loin,
avec une trace qui ne mentionne même pas l'endroit du vrai problème."

PAUSE.

"Une exception s'arrête à l'erreur. Et elle la nomme."

Callback to chapter four: c'est le pendant de « une fonction qui renvoie ».
Elle renvoie un résultat, ou elle refuse. Pas un demi-résultat.
-->

---
layout: default
class: nl-deck
---

# Re-raising and Chaining

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="arrow" /> Keep the cause</div>

```python
try:
    cfg = json.loads(raw)
except ValueError as e:
    raise ConfigError(path) from e
```

<div class="nl-type mt-2 nl-type--plain">
&rarr; "The above exception was the <strong>direct cause</strong> of the following exception"
</div>

<div class="nl-type mt-2"><NlIcon name="split" /> Handle, then pass it on</div>

```python
except OSError:
    log.exception("read failed")
    raise          # same traceback
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Three ways, three meanings</div>

<div class="nl-recap mt-2" style="font-size: 1rem">
  <div class="n">raise</div><div><span class="why">re-raise, traceback intact</span></div>
  <div class="n">raise X from e</div><div><span class="why">X was caused by e</span></div>
  <div class="n">raise X from None</div><div><span class="why">hide the internal cause</span></div>
  <div class="n">raise X</div><div><span class="why">chains anyway, as "during handling"</span></div>
</div>

<div style="font-size: 1.02rem">

A bare `raise X` inside a handler still shows the original, under *"During
handling of the above exception, another exception occurred"* — chaining is
the default, not the favour.

</div>

</div>

</div>

<div class="nl-statement mt-3">
<code>raise</code> alone keeps the whole traceback — <code>raise e</code> would truncate it
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 10 - Chaining
On screen ~70 seconds. This is the chapter's payoff - it pays off slide three.

Do all three live and read the traceback out loud each time. The two English
sentences Python prints are the whole lesson, so let them appear on screen:

  "The above exception was the direct cause of the following exception"
  "During handling of the above exception, another exception occurred"

"Regardez la différence. Avec `from e`, Python dit : la première a CAUSÉ la
seconde. Sans, il dit : la seconde est arrivée PENDANT le traitement de la
première. Ce n'est pas la même histoire, et c'est vous qui la racontez."

PAUSE.

Then the one that saves debugging time:
"Et `raise` tout seul, sans rien après, relève la même exception avec sa
trace complète. Si vous écrivez `raise e`, vous repartez de cette ligne-ci et
vous perdez le chemin."

Close the loop with slide three: on a appris à lire une trace au début du
chapitre. Voilà comment on en écrit une qui se lit.
-->

---
layout: default
class: nl-deck
---

# Custom Exceptions

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> A name, and some context</div>

```python
class ConfigError(Exception):
    """Config could not be loaded."""

    def __init__(self, path, key=None):
        self.path = path
        self.key = key
        super().__init__(
            f"{path}: missing {key}")
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why not just <code>ValueError</code></div>

Because the caller cannot catch *your* failure specifically. A named exception
lets them handle your error and let everything else through — which is the
entire point of having types.

<div style="font-size: 1.05rem">

Store the useful values as **attributes**, not only in the message. A handler
can then read `e.path` instead of parsing text.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Subclass <code>Exception</code>, never <code>BaseException</code></li>
<li class="nl-good">A docstring, and <code>super().__init__(message)</code></li>
<li class="nl-bad">A custom type for something <code>ValueError</code> already says</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Put the data on the exception — a handler should not parse your message
</div>

<!--
SLIDE 11 - Custom exceptions
On screen ~60 seconds.

The attributes point is the one that is actually professional and it is
missing from most tutorials:
"Ne mettez pas l'information uniquement dans le message. Mettez-la en
attribut. Sinon celui qui attrape votre exception devra découper une chaîne
de caractères pour retrouver le chemin du fichier - et le jour où vous
reformulez le message, son code casse."

Chapter four callback: `super().__init__(...)` - on a vu super au chapitre
quatre. Ici il sert à ce que str(e) donne quelque chose de lisible.

And the restraint, which matters as much:
"N'inventez pas un type pour ce que ValueError dit déjà. Une exception
personnalisée, c'est quand l'appelant a besoin de distinguer VOTRE échec."
-->

---
layout: default
class: nl-deck
---

# One Hierarchy per Package

<div class="nl-cols mt-4">

<div>

```python
class NoonLabsError(Exception):
    """Base for everything we raise."""

class ConfigError(NoonLabsError):
    ...

class DataError(NoonLabsError):
    ...

class SchemaError(DataError):
    ...
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> One base class buys two things</div>

Callers who care about detail catch `SchemaError`. Callers who only care that
*your* library failed catch `NoonLabsError` — and neither has to enumerate
every type you might add later.

<div style="font-size: 1.05rem">

It also means you can add a new exception without breaking anyone, as long as
it inherits from the base.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">One base per project, in one <code>exceptions.py</code></li>
<li class="nl-good">Inherit from a builtin too when it fits: <code>class BadRow(DataError, ValueError)</code></li>
<li class="nl-bad">Twenty unrelated exception classes with no common parent</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
A shared base class is a promise your callers can rely on
</div>

<!--
SLIDE 12 - Hierarchy per package
On screen ~50 seconds. Concept slide.

This is a library-design idea, so give them the caller's point of view:
"Imaginez que vous utilisez ma bibliothèque. Vous voulez juste savoir si
c'est elle qui a échoué, pour afficher un message propre. Sans classe de
base, vous devez lister toutes mes exceptions - et le jour où j'en ajoute
une, votre code la laisse passer."

PAUSE.

"Avec une classe de base, vous écrivez `except NoonLabsError` une fois, et
ça reste vrai pour toujours."

The double inheritance line is worth ten seconds: on peut hériter des deux -
de votre base ET de ValueError - pour que le code qui attrape ValueError
fonctionne aussi.
-->

---
layout: default
class: nl-deck
---

# EAFP vs LBYL

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Look before you leap</div>

```python
if "montant" in row:
    total += float(row["montant"])
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Ask forgiveness</div>

```python
try:
    total += float(row["montant"])
except (KeyError, ValueError):
    skipped += 1
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why Python leans one way</div>

The check and the action are two separate moments. Between them a file can
vanish, a dict can change, a network can drop — and the check only tests one
of the things that can go wrong.

<div style="font-size: 1.05rem">

`try` is nearly free when nothing raises, and costly when something does. So
EAFP for the unexpected, a plain `if` for conditions that are simply part of
your logic.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">EAFP for I/O, parsing, anything external</li>
<li class="nl-bad">Exceptions as flow control in a hot loop</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
The check tests one failure. The <code>try</code> catches all of them.
</div>

<!--
SLIDE 13 - EAFP
On screen ~55 seconds. Chapter six planted this on its last slide - name the
callback.

"On l'a dit à la fin du chapitre six : entre la vérification et l'action, il
y a un intervalle. Voilà le nom de cette philosophie."

The nuance is what makes this honest rather than dogmatic:
"Ce n'est pas « toujours try ». Un try ne coûte presque rien quand rien
n'échoue, et cher quand ça échoue. Donc : try pour l'imprévu. Un simple if
pour ce qui fait partie de votre logique normale."

Give the concrete line: `if x in d` quand l'absence est un cas métier normal.
try/except quand l'absence est une anomalie.
-->

---
layout: default
class: nl-deck
---

# Anti-patterns

<div class="nl-cols mt-4" style="font-size: 1.05rem">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> The bare except</div>

`except:` catches `KeyboardInterrupt` and `SystemExit` too. Your Ctrl-C stops
working and nobody knows why.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> The silent swallow</div>

`except Exception: pass` deletes the evidence. The program continues with wrong
data and no trace of when it went wrong.

<div class="nl-type nl-bad mt-3"><NlIcon name="cross" /> The lying handler</div>

Catching `Exception` around ten lines, then reporting "invalid input" — when
the real cause was a typo in a variable name.

</div>

<div>

<div class="nl-type nl-good"><NlIcon name="check" /> Name the type</div>

`except ValueError` — and if you truly need the catch-all, use
`except Exception` and log it.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> If you mean it, say so</div>

`contextlib.suppress(FileNotFoundError)` states in one line that the absence is
expected and intentional.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Narrow, then handle</div>

One risky call per `try`, the specific type, and a message containing the value
that caused it.

</div>

</div>

<div class="nl-statement mt-3">
<code>except: pass</code> does not handle an error — it hides one
</div>

<!--
SLIDE 14 - Anti-patterns
On screen ~60 seconds.

Do the bare-except demo if you did not already on the hierarchy slide: a loop
with `except:` that you cannot interrupt.

The silent swallow deserves the strongest language in the chapter:
"`except Exception: pass`. Deux mots, et vous venez de supprimer la preuve.
Le programme continue avec des données fausses, et vous ne saurez jamais
quand ça a commencé."

PAUSE.

Then the honest exception to the rule, so they do not over-correct:
"Il y a un cas légitime : quand l'absence est NORMALE et VOULUE. Et là, il
existe une façon de le dire à voix haute - `contextlib.suppress`. Une ligne,
et le lecteur sait que c'était intentionnel."

Show suppress in VS Code. It reads better than try/except/pass and it
documents intent.
-->

---
layout: default
class: nl-deck
---

# Logging Errors, Not Printing Them

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Loses the traceback</div>

```python
except OSError as e:
    print("error:", e)
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Keeps everything</div>

```python
import logging
log = logging.getLogger(__name__)

except OSError:
    log.exception("read failed: %s", path)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> What <code>log.exception</code> adds</div>

The full traceback, the logger name, the timestamp, and the level — written
wherever the application decided logs go, not just to whoever happened to be
watching the terminal.

<div style="font-size: 1.05rem">

Call it **inside** the `except` block; it reads the exception currently being
handled.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>log.exception</code> in a handler, <code>%s</code> not f-strings</li>
<li class="nl-good">Library code logs; the application decides where</li>
<li class="nl-bad"><code>print</code> as your error-reporting strategy</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>print</code> tells whoever is watching. A log tells whoever investigates.
</div>

<!--
SLIDE 15 - Logging
On screen ~55 seconds.

The distinction is the statement, so lead with it:
"`print` s'adresse à celui qui regarde l'écran maintenant. Un journal
s'adresse à celui qui enquête dans trois semaines. Ce n'est pas la même
personne."

Show log.exception in VS Code and let the traceback appear in the log output.
That is the difference in one screen: print donne une ligne, log.exception
donne toute la trace.

The %s point needs thirty seconds because it looks like a step backwards:
"Pourquoi `%s` et pas une f-string ? Parce que le formatage n'a lieu que si
le message est effectivement écrit. Sur un log de debug désactivé, vous ne
payez rien."

Chapter nine covers logging properly - say so and move on.
-->

---
layout: default
class: nl-deck
---

# assert Is Not Validation

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Disappears in production</div>

```python
def withdraw(amount):
    assert amount > 0, "must be positive"
```

```bash
$ python -O app.py
# the assert is stripped out entirely
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Always there</div>

```python
    if amount <= 0:
        raise ValueError(amount)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> What <code>assert</code> is for</div>

Stating something you believe is **already true** — an internal invariant, a
sanity check inside your own code, a condition in a test.

<div style="font-size: 1.05rem">

Run with `-O` and every `assert` vanishes. If it was your only check on user
input, you shipped a program with no validation at all.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Tests, and invariants you control</li>
<li class="nl-bad">Anything that came from a user, a file, or a network</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>assert</code> is a note to yourself — <code>raise</code> is a contract with your caller
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 16 - assert
On screen ~50 seconds. Demo the stripping, it takes ten seconds and it is
the whole slide.

python3 app.py       -> AssertionError
python3 -O app.py    -> no error, the function runs with a negative amount

"La même ligne. Un drapeau en plus. Et votre validation a disparu."

PAUSE.

"Ce n'est pas un bug de Python. C'est la définition d'`assert` : une
affirmation que vous croyez déjà vraie, qu'on peut retirer en production
sans changer le comportement. Si la retirer change le comportement, ce
n'était pas un assert."

Where it IS right: dans les tests, et pour vos invariants internes. On en
reparlera au chapitre seize avec pytest, où assert est justement l'outil
principal.
-->

---
layout: default
class: nl-deck
---

# ExceptionGroup and except* (3.11+)

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="split" /> Several failures at once</div>

```python
raise ExceptionGroup("batch", [
    ValueError("row 3"),
    KeyError("row 7"),
])
```

<div class="nl-type mt-2"><NlIcon name="check" /> Handle each kind</div>

```python
try:
    run_all(tasks)
except* ValueError as eg:
    log.warning("bad values: %s", eg)
except* OSError as eg:
    retry(eg)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why a new syntax was needed</div>

`except` handles **one** exception. When twenty tasks run concurrently and
three fail differently, one of the three used to win and the others were lost.

<div style="font-size: 1.05rem">

`except*` runs **every** matching clause, each receiving the subgroup that
matched it. You will meet this with `asyncio.TaskGroup` long before you write
it yourself.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Concurrent work, batch validation</li>
<li class="nl-bad">Ordinary sequential code — plain <code>except</code> is right</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>except</code> picks one winner. <code>except*</code> lets every failure be handled.
</div>

<!--
SLIDE 17 - ExceptionGroup
On screen ~45 seconds. Keep it short: recognition, not mastery.

Frame the problem first, or the syntax looks gratuitous:
"Vingt tâches en parallèle. Trois échouent, chacune pour une raison
différente. Avec un `except` classique, une seule gagne - les deux autres
disparaissent."

PAUSE.

"`except` étoile exécute TOUS les blocs qui correspondent, chacun avec son
sous-groupe."

Then set expectations honestly:
"Vous ne l'écrirez probablement pas cette année. Mais vous le RENCONTREREZ
dès que vous toucherez à asyncio. Sachez le reconnaître."

Note it needs 3.11 or newer - which their environment from chapter one has.
-->

---
layout: default
class: nl-deck
---

# Retrying, and Knowing When to Stop

<div class="nl-cols mt-4">

<div>

```python
for attempt in range(1, 4):
    try:
        return fetch(url)
    except TimeoutError:
        if attempt == 3:
            raise
        time.sleep(2 ** attempt)
```

<div class="nl-type mt-2 nl-type--plain">
1s, 2s, 4s — then give up and let the caller decide.
</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Retry only what might succeed</div>

A timeout, a dropped connection, a rate limit: worth another try. A
`ValueError` on your own data will fail identically forever — retrying it just
wastes time and hides the bug.

<div style="font-size: 1.05rem">

Always bound the attempts, back off between them, and re-raise at the end. An
unbounded retry loop is an outage that never reports itself.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Transient network and I/O failures</li>
<li class="nl-good">A cap, a backoff, and a final <code>raise</code></li>
<li class="nl-bad">Retrying a bug and calling it resilience</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Retry what is transient. Everything else, you are just hiding.
</div>

<!--
SLIDE 18 - Retry
On screen ~55 seconds. Close the chapter on the production pattern.

The distinction is the lesson, so make it sharp:
"Un délai dépassé, une connexion coupée, une limite de débit : ça vaut le
coup de réessayer. Une ValueError sur vos propres données échouera
exactement pareil, mille fois de suite."

PAUSE.

"Réessayer un bug, ce n'est pas de la robustesse. C'est de la dissimulation
avec une boucle autour."

The three requirements are worth naming as a checklist: une limite, une
attente croissante, et un raise à la fin. Sans le raise final, votre
programme échoue en silence - et on revient à l'anti-patron du swallow.

Mention that in real projects you use `tenacity` or your framework's retry
rather than writing this - but you should be able to write it.
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 08 — OBJECT-ORIENTED PYTHON</strong>

</div>

<!--
SLIDE 19 - Closing card
On screen ~12 seconds.
Say the next chapter's topic out loud while this is up.
Then: "À mardi." Hold two beats of silence before you stop recording.
-->
