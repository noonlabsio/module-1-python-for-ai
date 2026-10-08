---
theme: ../themes/noonlabs
title: File I/O & Data Formats — Chapter 06
info: NoonLabs - Module I, chapitre 06
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

<div class="nl-eyebrow">Chapter 06</div>

# File I/O &amp; Data Formats

<div class="mt-4" style="max-width: 42ch">

Getting data in and out — and the encoding question nobody warns you about

</div>

<div class="nl-type mt-6">
  <NlIcon name="file" /> Files
  <span class="mx-3">·</span>
  <NlIcon name="box" /> CSV &amp; JSON
  <span class="mx-3">·</span>
  <NlIcon name="layers" /> Paths
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~8 seconds.

"Chapitre six. Jusqu'ici, nos données étaient dans le programme. Maintenant
elles viennent de l'extérieur - et l'extérieur est plus hostile qu'on
l'imagine."

Then set the hook for the whole chapter:
"Et on va répondre définitivement à la question de la première vidéo :
pourquoi est-ce que lire un fichier vous donne toujours du texte."
-->

---
layout: default
class: nl-deck
---

# File Opening Modes

<div class="nl-cols mt-4" style="font-size: 1.02rem">

<div>

<div class="nl-recap mt-1">
  <div class="n">r</div><div><span class="why">read — the file must exist</span></div>
  <div class="n">w</div><div><span class="why">write — creates, or <strong>truncates</strong></span></div>
  <div class="n">a</div><div><span class="why">append — writes at the end</span></div>
  <div class="n">x</div><div><span class="why">exclusive create — fails if it exists</span></div>
  <div class="n">b</div><div><span class="why">binary, added to any of the above</span></div>
  <div class="n">+</div><div><span class="why">read and write on the same handle</span></div>
</div>

<div class="nl-type mt-2 nl-type--plain">
Combine them: <code>rb</code>, <code>w+</code>, <code>ab</code>, <code>r+b</code>. Default is <code>rt</code>.
</div>

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> The mode that destroys data</div>

`"w"` truncates the file to zero bytes **the moment it opens** — before you
write anything, and whether or not your write succeeds.

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Pick the narrowest mode</div>

<ul style="font-size: 1.05rem">
<li class="nl-good"><code>a</code> for logs — never loses what came before</li>
<li class="nl-good"><code>x</code> when overwriting would be a bug</li>
<li class="nl-bad"><code>w</code> on a path you have not checked</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>"w"</code> empties the file before your first write — not after
</div>

<!--
SLIDE 3 - Modes
On screen ~55 seconds.

The table is reference. The right column is the lesson.

Demonstrate the truncation, because reading about it does not land:
create a file with content, open it with "w", then crash the program before
writing anything. The file is empty. The data is gone.

"Le mode w ne remplace pas le contenu à la fin. Il vide le fichier à
l'ouverture. Si votre programme plante entre les deux, vous n'avez plus
rien."

PAUSE.

Then the habit:
"Choisissez le mode le plus étroit qui fait le travail. Pour un journal, a.
Pour un fichier qui ne doit pas exister encore, x. Et w seulement quand vous
êtes sûr."
-->

---
layout: default
class: nl-deck
---

# Text, Bytes, and Encoding

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="split" /> Two different types come back</div>

```python
open(p).read()          # -> str
open(p, "rb").read()    # -> bytes
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> A real French CSV</div>

```python
open("clients.csv",
     encoding="utf-8").read()
# UnicodeDecodeError: 0xe9 in
# position 15
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Excel wrote cp1252</div>

```python
open("clients.csv",
     encoding="cp1252").read()
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Text mode is binary plus a decoder</div>

A file on disk is always bytes. Text mode hands you `str` by running those
bytes through a codec — and if you name the wrong codec, you get an exception
or, worse, silent mojibake.

<div style="font-size: 1.05rem">

The default depends on your platform's locale, so the same code can work on
your machine and fail on a colleague's.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Always pass <code>encoding=</code> explicitly</li>
<li class="nl-good"><code>errors="replace"</code> when a log must not crash</li>
<li class="nl-bad">Trusting the default on a file you did not write</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Text is bytes plus a decoder — and the decoder is your decision
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 4 - Encoding
On screen ~75 seconds. This is the most useful slide in the chapter for a
French-speaking audience and it is in almost no tutorial. Do it live.

Make the file yourself, in cp1252, with an accent in it. Then read it as
utf-8 and let the UnicodeDecodeError appear.

"Un fichier exporté depuis Excel en France. Il y a un « café » dedans. Et
Python refuse de le lire."

PAUSE.

"Ce n'est pas Python qui a tort. Un fichier sur le disque, ce sont des
octets. Toujours. Le mode texte vous rend une chaîne en faisant passer ces
octets par un codec. Si vous vous trompez de codec, ça explose - ou pire, ça
marche et vous avez des caractères abîmés."

Show the mojibake version too - open the utf-8 file as latin-1 and get
"cafÃ©". Silent corruption is worse than an exception.

Then the rule, and it applies for the rest of their career:
"Précisez toujours l'encodage. Toujours. Le défaut dépend de la machine, donc
votre code peut marcher chez vous et casser chez un collègue."

VERIFY BEFORE RECORDING: run locale.getpreferredencoding(False) on your own
3.14 and say what YOUR default is - it differs by platform.
-->

---
layout: default
class: nl-deck
---

# Context Managers: with

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Risky</div>

```python
f = open("file.txt")
data = f.read()
f.close()   # may never run
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Safe</div>

```python
with open("file.txt") as f:
    data = f.read()
# closed, even if read() raised
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why it is not just tidier</div>

If `read()` raises, the `close()` line is never reached. The handle stays open
until the garbage collector happens to notice — which on some interpreters is
never.

<div style="font-size: 1.05rem">

An unflushed write is worse: your data is in a buffer, not on disk, and the
process exits without it.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Files, locks, connections, transactions</li>
<li class="nl-good">Several at once: <code>with open(a) as f, open(b) as g:</code></li>
<li class="nl-bad">A bare <code>open()</code> anywhere in production code</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>with</code> guarantees the cleanup runs — an exception does not skip it
</div>

<!--
SLIDE 5 - with
On screen ~55 seconds.

Do not sell `with` as "cleaner". Sell it as correctness:
"Si `read` lève une exception, la ligne `close` n'est jamais atteinte. Le
fichier reste ouvert."

PAUSE.

Then the version that actually costs money:
"Et en écriture, c'est pire. Vos données sont dans un tampon, pas sur le
disque. Le processus s'arrête, et le fichier est vide ou tronqué."

The multiple-context form is worth ten seconds - they will need it for
read-one-file-write-another, which is most real scripts.

Mention that `with` is not only for files: verrous, connexions, transactions.
Anything that must be released.
-->

---
layout: default
class: nl-deck
---

# Writing Your Own Context Manager

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> The protocol</div>

```python
class Timer:
    def __enter__(self):
        self.t = time.monotonic()
        return self

    def __exit__(self, *exc):
        print(time.monotonic() - self.t)
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> The short way</div>

```python
@contextmanager
def timer():
    t = time.monotonic()
    try:
        yield
    finally:
        print(time.monotonic() - t)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Two methods, one guarantee</div>

`__enter__` runs on the way in and its return value is what `as` binds.
`__exit__` runs on the way out — **always**, exception or not.

<div style="font-size: 1.05rem">

`@contextmanager` from `contextlib` turns a generator into the same thing:
everything before `yield` is entry, everything in the `finally` is exit.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Any acquire-then-release pair</li>
<li class="nl-good">The <code>finally</code> is what makes it safe</li>
<li class="nl-bad">Doing cleanup after the <code>yield</code> with no <code>try</code></li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
If you always release it, it wants to be a context manager
</div>

<!--
SLIDE 6 - Custom context managers
On screen ~60 seconds.

Use a timer rather than a database connection - they can run it immediately
and see the result.

The `finally` is the whole point and the source material omits it:
"Sans le try/finally, si le code dans le bloc lève une exception, votre
nettoyage ne s'exécute pas. Vous avez réécrit le bug que `with` était censé
supprimer."

PAUSE.

The chapter-four callback: `@contextmanager` is a décorateur, and a décorateur
c'est une fonction qui prend une fonction. On les verra proprement au chapitre
onze - pour l'instant, sachez que ça marche.

Show the generator version running in VS Code. `yield` will feel strange; say
that chapter ten explains it and move on.
-->

---
layout: default
class: nl-deck
---

# Reading Files

<div class="nl-cols mt-4" style="font-size: 1.02rem">

<div>

<div class="nl-recap mt-1">
  <div class="n">read()</div><div><span class="why">the whole file, as one string</span></div>
  <div class="n">read(n)</div><div><span class="why">at most n characters</span></div>
  <div class="n">readline()</div><div><span class="why">one line, newline included</span></div>
  <div class="n">readlines()</div><div><span class="why">every line, as a list</span></div>
  <div class="n">for line in f</div><div><span class="why">one line at a time, lazily</span></div>
</div>

<div class="nl-type mt-2"><NlIcon name="prompt" /> With line numbers</div>

```python
for i, line in enumerate(f, 1):
    print(i, line.rstrip())
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> The file is an iterator</div>

Iterating a file yields one line at a time and holds one line in memory.
`read()` and `readlines()` hold the **entire file** — fine for a config,
fatal for a 4 GB log.

<div style="font-size: 1.05rem">

Same protocol as chapter three: a file is consumed as you walk it. Read it
twice without `f.seek(0)` and the second pass is empty.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>for line in f</code> as the default</li>
<li class="nl-bad"><code>readlines()</code> on a file you did not size</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Iterate by default — <code>read()</code> is the exception, not the habit
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 7 - Reading
On screen ~60 seconds.

The iterator callback is the payoff from chapter three, so name it:
"Un fichier ouvert est un itérateur. Vous vous souvenez de zip qui se vidait ?
Pareil. Lisez-le deux fois sans revenir au début, et la deuxième fois vous
n'avez rien."

Demo it: read the file, print the length, read again, print zero. Then
f.seek(0) and read again.

The memory point is the production one:
"`read` charge tout. Sur un fichier de configuration, aucun problème. Sur un
journal de quatre gigaoctets, votre programme meurt."

`enumerate(f, 1)` is a chapter-three callback too - line numbers that start
at one, like every editor.
-->

---
layout: default
class: nl-deck
---

# Writing Files

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="arrow" /> Three ways out</div>

```python
f.write("one line\n")
f.writelines(["a\n", "b\n"])
print("one line", file=f)
```

<div class="nl-type mt-2"><NlIcon name="file" /> Appending to a log</div>

```python
with open("app.log", "a",
          encoding="utf-8") as f:
    f.write(f"{now}: started\n")
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> Two things that surprise people</div>

`write()` adds **no newline** — you supply every one yourself. And despite the
name, `writelines()` adds none either; it is just a loop over `write()`.

<div style="font-size: 1.05rem">

`print(..., file=f)` does add one, which is why it is often the friendlier
choice.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Build the text, then write once: <code>"\n".join(lines)</code></li>
<li class="nl-good"><code>a</code> mode for anything append-only</li>
<li class="nl-bad">Assuming the data is on disk before the block ends</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
<code>writelines()</code> does not write lines — it writes strings
</div>

<!--
SLIDE 8 - Writing
On screen ~50 seconds.

The writelines naming is a genuine trap and worth the demo. Pass it a list
without newlines and show everything on one line.

"Le nom est mensonger. `writelines` n'ajoute aucun saut de ligne. C'est une
boucle sur `write`, rien de plus."

PAUSE.

Then the alternative that behaves as expected:
"`print` avec `file=`, lui, ajoute le saut de ligne. Pour du texte simple,
c'est souvent plus sûr."

And the flush point, which connects back to `with`:
"Et jusqu'à la fin du bloc `with`, vos données sont peut-être encore dans un
tampon. Ce n'est pas sur le disque parce que vous avez appelé write."
-->

---
layout: default
class: nl-deck
---

# CSV: Reading

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> By position, or by name</div>

```python
import csv

with open(p, newline="",
          encoding="utf-8") as f:
    for row in csv.reader(f):
        print(row[0])

    for row in csv.DictReader(f):
        print(row["montant"])
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> Every value is a string</div>

`csv.reader` gives you `["47.20", "12"]` — two strings. A file has no types,
because a file is text.

<div style="font-size: 1.05rem">

That is exactly why `"47.20" + 12` failed in the very first video. The `csv`
module was not being unhelpful; it had nothing else to give.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>float()</code> or <code>int()</code> at the boundary, once</li>
<li class="nl-good"><code>newline=""</code> — the module handles line endings</li>
<li class="nl-bad">French Excel: the delimiter is <code>;</code></li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
A file has no types — every field arrives as a string
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 9 - CSV reading
On screen ~70 seconds. THIS IS THE CHAPTER'S PAYOFF. Take the time.

Print a row from csv.reader and then print the types.

"Deux chaînes. Pas un nombre en vue."

PAUSE.

Then close the loop that opened the channel:
"Dans la toute première vidéo, notre programme a échoué sur « quarante-sept
virgule vingt » plus douze. On a corrigé avec float, et au chapitre deux on a
expliqué pourquoi Python refuse de deviner. Voilà la dernière pièce : le
module csv ne pouvait rien donner d'autre. Un fichier, c'est du texte. Le
texte n'a pas de type."

Let that sit.

Then the two practical points. newline="" with its reason - le module csv gère
lui-même les fins de ligne, et sans ça vous aurez des lignes vides sous
Windows. And the French Excel delimiter, which will affect half the audience:
"Excel en français écrit des points-virgules. `delimiter=';'`."
-->

---
layout: default
class: nl-deck
---

# CSV: Writing

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="arrow" /> Rows, or dictionaries</div>

```python
with open(p, "w", newline="",
          encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["nom", "montant"])
    w.writerows(rows)

    d = csv.DictWriter(f,
        fieldnames=["nom", "montant"])
    d.writeheader()
    d.writerow({"nom": "Alice"})
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why not just write commas</div>

Because a field can contain a comma, a quote, or a newline. The `csv` module
quotes and escapes for you; a hand-rolled `",".join(...)` produces a file that
looks right and parses wrong.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>DictWriter</code> when the column order must be explicit</li>
<li class="nl-good"><code>delimiter</code>, <code>quotechar</code>, <code>quoting</code> for other dialects</li>
<li class="nl-bad"><code>",".join(values)</code> to produce CSV</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Never build CSV by joining commas — one field will contain one
</div>

<!--
SLIDE 10 - CSV writing
On screen ~55 seconds.

Lead with the failure that justifies the module. In VS Code, write a row by
hand with ",".join, where one value is "Dupont, Marie". Then read it back and
show three fields where there should be two.

"Le fichier a l'air correct. Il se relit faux. Et personne ne s'en aperçoit
avant que ce soit en production."

PAUSE.

Then csv.writer doing it properly - guillemets automatiques.

DictWriter gets thirty seconds: quand les colonnes doivent être dans un ordre
précis, ou quand vos données sont déjà des dictionnaires - ce qui arrive dès
qu'elles viennent d'une API.
-->

---
layout: default
class: nl-deck
---

# JSON: load and dump

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> File, or string</div>

```python
import json

with open(p, encoding="utf-8") as f:
    data = json.load(f)

data = json.loads('{"a": 1}')

with open(p, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

s = json.dumps(data, indent=2)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> The <code>s</code> means string</div>

`load` and `dump` take a **file**. `loads` and `dumps` take and return a
**string**. That single letter is the whole API.

<div class="nl-type mt-3"><NlIcon name="check" /> Options worth knowing</div>

<ul style="font-size: 1.05rem">
<li class="nl-good"><code>indent=2</code> so a human, and git, can read the diff</li>
<li class="nl-good"><code>ensure_ascii=False</code> to keep accents readable</li>
<li class="nl-good"><code>sort_keys=True</code> for stable output</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Unlike CSV, JSON keeps types — numbers come back as numbers
</div>

<!--
SLIDE 11 - JSON basics
On screen ~55 seconds.

The s-for-string mnemonic saves them looking it up forever:
"`load` prend un fichier. `loads` prend une chaîne. Le s, c'est string. Une
lettre, et vous n'avez plus jamais besoin de chercher."

Then the contrast with the previous slide, which is the reason JSON exists:
"Et contrairement au CSV, JSON garde les types. Un nombre revient nombre, un
booléen revient booléen. C'est pour ça qu'on préfère JSON pour échanger des
données structurées."

ensure_ascii=False matters for this audience specifically: sans ça, « café »
devient une séquence d'échappement illisible dans le fichier.
-->

---
layout: default
class: nl-deck
---

# JSON: Where the Types Stop

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Silent, and loud</div>

```python
json.dumps({1: "a"})
# '{"1": "a"}'   int key -> string

json.dumps({"t": (1, 2)})
# '{"t": [1, 2]}'  tuple -> list

json.dumps({"s": {1, 2}})
# TypeError: not serializable
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> JSON has six types</div>

Object, array, string, number, boolean, null. Everything else has to be
converted — and some conversions happen **without telling you**.

<div style="font-size: 1.05rem">

A `datetime`, a `set`, a `Decimal`, a dataclass: all `TypeError`. Pass
`default=str`, or write an encoder.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>json.dumps(d, default=str)</code> for a quick log</li>
<li class="nl-good">A <code>JSONEncoder</code> subclass when the shape matters</li>
<li class="nl-bad">Assuming a round trip returns what you put in</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
JSON round trips are not lossless — tuples come back as lists
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 12 - JSON type gap
On screen ~65 seconds. Do all three live, in order.

The int key is the dangerous one because it is silent:
json.dumps({1: "a"})  ->  '{"1": "a"}'

"Vous avez mis un entier comme clé. Vous récupérez une chaîne. Aucune
erreur, aucun avertissement. Votre dictionnaire n'est plus le même."

PAUSE.

The tuple is the same category: tuple à l'aller, liste au retour. Callback to
chapter five - un tuple est hachable, une liste non. Donc si vous utilisiez
ce tuple comme clé quelque part, ça casse.

The set raises, which is the honest behaviour - and mention that raising is
BETTER than converting silently.

Then the fix: default=str pour un log rapide, un encodeur pour du sérieux. Show
the JSONEncoder subclass with datetime.isoformat().
-->

---
layout: default
class: nl-deck
---

# Binary Files &amp; struct

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> Bytes in, bytes out</div>

```python
with open("image.png", "rb") as f:
    data = f.read()      # bytes

with open("out.bin", "wb") as f:
    f.write(data)
```

<div class="nl-type mt-2"><NlIcon name="layers" /> Fixed-width records</div>

```python
import struct
blob = struct.pack("ifi", 42, 3.14, 7)
a, b, c = struct.unpack("ifi", blob)
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="split" /> No decoder, no newline translation</div>

In binary mode nothing is interpreted. You get the exact bytes, which is the
only correct way to handle an image, an audio file, or anything compressed.

<div style="font-size: 1.05rem">

`struct` maps bytes to fixed-width numbers: `i` is a 4-byte int, `f` a 4-byte
float, `d` an 8-byte double. Sizes and byte order are the whole game.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Images, audio, archives, network frames</li>
<li class="nl-bad">Opening a PNG in text mode — it will corrupt</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Binary mode gives you the bytes that are actually on disk
</div>

<!--
SLIDE 13 - Binary
On screen ~50 seconds.

Keep this tight - most of them will not write struct code for years, but they
need to recognise it and they need binary mode for images.

The demonstration worth doing: open a PNG in text mode and watch it fail or
mangle. That makes "no decoder" concrete.

"En mode binaire, rien n'est interprété. Pas de décodage, pas de traduction
des fins de ligne. Vous avez les octets exacts."

struct in thirty seconds: c'est la traduction entre des octets et des nombres
de taille fixe. Vous en aurez besoin le jour où vous lirez un format binaire
ou une trame réseau. Sachez que ça existe.
-->

---
layout: default
class: nl-deck
---

# pickle, and When Not To

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> Any Python object, saved</div>

```python
import pickle

with open("cache.pkl", "wb") as f:
    pickle.dump(obj, f)

with open("cache.pkl", "rb") as f:
    obj = pickle.load(f)
```

<div class="nl-type nl-bad mt-2"><NlIcon name="cross" /> What load() really does</div>

```python
# pickle.load can execute
# arbitrary code. Loading a
# hostile file is running it.
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> Three reasons to avoid it</div>

- Loading untrusted data is **remote code execution**
- The format is tied to your classes: rename one and old files stop loading
- Nothing outside Python can read it

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> Where it is fine</div>

<div style="font-size: 1.05rem">

A cache your own program wrote, on your own machine, that you can safely
delete and rebuild.

</div>

</div>

</div>

<div class="nl-statement mt-3">
Unpickling a file you did not write is running code you did not read
</div>

<!--
SLIDE 14 - pickle
On screen ~55 seconds. Be direct. This is a security slide.

"pickle sauvegarde n'importe quel objet Python. C'est très pratique. Et c'est
la fonctionnalité la plus dangereuse du chapitre."

PAUSE.

"`pickle.load` peut exécuter du code arbitraire. Ce n'est pas un bug, c'est
son fonctionnement. Charger un fichier pickle hostile, c'est exécuter le
programme de l'attaquant, avec vos droits."

Say where they will meet the trap: un fichier .pkl téléchargé, un modèle
d'apprentissage automatique partagé sur un forum. C'est un vecteur réel.

Then the two non-security reasons, which matter just as much day to day: le
format est couplé à vos classes, et rien d'autre que Python ne peut le lire.

Close on the legitimate use, so they are not left thinking it is forbidden:
un cache que votre programme a écrit, sur votre machine, que vous pouvez
supprimer sans rien perdre.
-->

---
layout: default
class: nl-deck
---

# os.path vs pathlib

<div class="nl-cols mt-4">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> os.path — strings</div>

```python
import os
p = os.path.join("data", "raw.csv")
os.path.exists(p)
os.path.splitext(p)[1]
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> pathlib — objects</div>

```python
from pathlib import Path
p = Path("data") / "raw.csv"
p.exists()
p.suffix
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> A path is not a string</div>

`os.path` treats paths as text, so you get separator bugs, and every operation
is a function call on a string. `pathlib` makes the path an object that knows
what it is.

<div class="nl-recap mt-2" style="font-size: 1.02rem">
  <div class="n">p.parent</div><div><span class="why">the directory above</span></div>
  <div class="n">p.name</div><div><span class="why">filename with extension</span></div>
  <div class="n">p.stem</div><div><span class="why">filename without it</span></div>
  <div class="n">p.suffix</div><div><span class="why">the extension</span></div>
</div>

</div>

</div>

<div class="nl-statement mt-3">
The <code>/</code> operator builds paths correctly on every platform
</div>

<!--
SLIDE 15 - paths
On screen ~55 seconds.

The slash operator always gets a reaction, so lead with it:
"Regardez ça. On divise un chemin par une chaîne. Et ça produit le bon
chemin, avec le bon séparateur, sur Windows comme sur Linux."

The reason os.path still matters: vous le lirez partout dans du code
existant. Il n'est pas cassé, il est juste verbeux.

Then the four properties. Point at stem versus name - c'est la distinction
qu'on cherche toujours et qu'on n'arrive jamais à retenir.

Callback to chapter one: le chemin de votre projet, ce n'est pas une chaîne
que vous concaténez. C'est un objet.
-->

---
layout: default
class: nl-deck
---

# pathlib in Practice

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="prompt" /> Small files, one line</div>

```python
Path("notes.md").write_text(
    text, encoding="utf-8")

text = Path("notes.md").read_text(
    encoding="utf-8")
```

<div class="nl-type mt-2"><NlIcon name="split" /> Finding things</div>

```python
for p in Path("data").glob("*.csv"):
    ...
for p in Path("data").rglob("*.csv"):
    ...
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="check" /> The methods you will actually use</div>

<div class="nl-recap mt-2" style="font-size: 1.02rem">
  <div class="n">mkdir()</div><div><span class="why"><code>parents=True, exist_ok=True</code></span></div>
  <div class="n">glob()</div><div><span class="why">one level; <code>rglob()</code> recurses</span></div>
  <div class="n">iterdir()</div><div><span class="why">everything in a directory</span></div>
  <div class="n">unlink()</div><div><span class="why">delete a file</span></div>
</div>

<div style="font-size: 1.02rem">

`read_text` and `write_text` open, act and close in one call — perfect for a
config, wrong for anything large.

</div>

</div>

</div>

<div class="nl-statement mt-3">
<code>mkdir(parents=True, exist_ok=True)</code> is the line you will write a hundred times
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 16 - pathlib in practice
On screen ~60 seconds. All live - this is immediately useful.

read_text and write_text first: pour un fichier de configuration, une ligne
suffit. Pas de with, pas de read. Mais notez qu'on précise l'encodage - la
règle du début du chapitre ne change pas.

Then glob and rglob, on their own project directory. Show the difference:
glob descend d'un niveau, rglob descend partout.

The mkdir line deserves the statement because everyone gets it wrong once:
"`parents=True` crée les dossiers intermédiaires. `exist_ok=True` ne plante
pas si le dossier existe déjà. Sans les deux, votre script marche la première
fois et casse la deuxième."
-->

---
layout: default
class: nl-deck
---

# Temporary Files &amp; Atomic Writes

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> Scratch space that cleans itself</div>

```python
from tempfile import TemporaryDirectory

with TemporaryDirectory() as d:
    p = Path(d) / "work.csv"
    p.write_text(data)
# the whole directory is gone
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Writing without risk</div>

```python
tmp = path.with_suffix(".tmp")
tmp.write_text(new_data)
os.replace(tmp, path)   # atomic
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type nl-bad"><NlIcon name="cross" /> The half-written file</div>

Open a file with `"w"` and crash halfway through, and you have neither the old
version nor the new one. The original is already gone.

<div style="font-size: 1.05rem">

Write to a temporary file, then `os.replace()` — a rename on the same
filesystem is atomic, so a reader sees either the whole old file or the whole
new one, never a fragment.

</div>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>TemporaryDirectory</code> for tests and scratch work</li>
<li class="nl-good"><code>os.replace</code> for any file that matters</li>
<li class="nl-bad">Overwriting a good file in place</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Write beside the file, then rename over it — never write through it
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 17 - Temp files and atomic writes
On screen ~70 seconds. The atomic write is the most production-grade idea in
the chapter and it is in no beginner tutorial. Give it room.

Start with TemporaryDirectory - obvious value, thirty seconds. Tests,
traitement de fichiers, données sensibles.

Then set up the failure properly. In VS Code: a script that opens an important
file with "w", writes half the lines, and raises. Show the file afterwards.

"L'ancienne version a disparu à l'ouverture. La nouvelle n'est pas finie.
Vous n'avez plus rien."

PAUSE.

Then the fix, and explain WHY it works:
"On écrit à côté. Puis on renomme par-dessus. Un renommage sur le même
système de fichiers est atomique - il réussit ou il n'a pas lieu. Un lecteur
voit soit tout l'ancien fichier, soit tout le nouveau. Jamais un morceau."

"Trois lignes. C'est la différence entre un script et un outil."
-->

---
layout: default
class: nl-deck
---

# Environment Variables &amp; Secrets

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> Reading configuration</div>

```python
import os

os.getenv("API_KEY")          # None
os.getenv("PORT", "8000")     # default
os.environ["API_KEY"]         # KeyError
```

<div class="nl-type mt-2"><NlIcon name="file" /> A .env for local work</div>

```python
from dotenv import load_dotenv
load_dotenv()          # reads ./.env
key = os.getenv("API_KEY")
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> Why config lives outside the code</div>

The same program must run on your laptop, in CI, and in production with
different values — and a secret in a repository is a secret that has leaked,
permanently, even after you delete it.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>.env</code> in <code>.gitignore</code>, <code>.env.example</code> committed</li>
<li class="nl-good"><code>os.environ[...]</code> when a missing value must stop the program</li>
<li class="nl-bad">A key, token or password anywhere in a <code>.py</code> file</li>
</ul>

</div>

</div>

<div class="nl-statement mt-3">
Every environment variable is a string — convert it, and validate it
</div>

<!--
SLIDE 18 - Environment variables
On screen ~60 seconds. Security slide, so be concrete.

getenv versus environ is a real design choice, not a style one:
"`getenv` renvoie None si la variable n'existe pas. `environ` avec des
crochets lève une erreur. Choisissez selon votre intention : est-ce que
l'absence est acceptable, ou est-ce que le programme ne doit pas démarrer ?"

For a database password, the answer is: il ne doit pas démarrer. Mieux vaut
planter au lancement que tourner à moitié.

Then the git point, said plainly:
"Un secret dans un dépôt est un secret perdu. Même si vous le supprimez, il
reste dans l'historique. Et si le dépôt est public, considérez qu'il a été
lu."

.env in .gitignore, .env.example committed - callback to chapter one, where
we put .venv in .gitignore for the same reason.

Close on the statement: toute variable d'environnement est une chaîne. PORT
n'est pas un entier. int(os.getenv("PORT", "8000")).
-->

---
layout: default
class: nl-deck
---

# Failing Well

<div class="nl-cols mt-4" style="font-size: 1.05rem">

<div>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Check, then open</div>

```python
if path.exists():
    data = path.read_text()
```

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Just open, and handle it</div>

```python
try:
    data = path.read_text()
except FileNotFoundError:
    data = ""
```

</div>

<div style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> The gap between the two lines</div>

Between `exists()` and the read, the file can be deleted, renamed, or have its
permissions changed. The check does not protect you — it just moves the crash
somewhere less obvious.

<div class="nl-recap mt-2" style="font-size: 1.02rem">
  <div class="n">FileNotFoundError</div><div><span class="why">no such path</span></div>
  <div class="n">PermissionError</div><div><span class="why">not allowed</span></div>
  <div class="n">IsADirectoryError</div><div><span class="why">you meant a file</span></div>
  <div class="n">UnicodeDecodeError</div><div><span class="why">wrong encoding</span></div>
</div>

</div>

</div>

<div class="nl-statement mt-3">
Ask forgiveness, not permission — the file can change between the two lines
</div>

<!--
SLIDE 19 - Failing well
On screen ~55 seconds. Chapter eight goes deep on exceptions; here we only
cover what is specific to files.

The race condition is the concept, and it is a genuinely professional idea:
"Entre `exists` et la lecture, il y a un intervalle. Le fichier peut
disparaître, changer de nom, changer de droits. Votre vérification ne protège
rien - elle déplace juste le plantage à un endroit moins clair."

PAUSE.

"En Python, on demande pardon, pas la permission. On essaie, et on gère
l'échec."

The four exception names are worth naming out loud - ils sont explicites, et
savoir lequel attraper vous évite d'écrire `except Exception`, qui masque tout.

Say clearly: on approfondit au chapitre huit. Ici, on retient les quatre noms
et le réflexe try.
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 07 — ERRORS &amp; EXCEPTIONS</strong>

</div>

<!--
SLIDE 20 - Closing card
On screen ~12 seconds.
Say the next chapter's topic out loud while this is up.
Then: "À mardi." Hold two beats of silence before you stop recording.
-->
