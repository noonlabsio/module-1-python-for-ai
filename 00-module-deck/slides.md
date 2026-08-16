---
theme: ../themes/noonlabs
title: Python Fundamentals — Module I
info: NoonLabs - Module I, deck maître
layout: cover
transition: fade
mdc: true
---

# NoonLabs
Code and AI as written in production
<!--
SLIDE 1 - Brand stamp
On screen ~4 seconds. Nobody reads this. Say "Bienvenue sur NoonLabs"
over it and move on. If a video needs to reach content faster, skip
straight to slide 2 - this one is disposable.
-->

---
layout: default
class: nl-deck
---

# <span class="nl-logo nl-logo--python" /> Python Fundamentals

## From Beginner to Industry-Ready

<div class="mt-4" style="max-width: 46ch">

A comprehensive guide to mastering Python for data science, AI, and software development

</div>

<div class="nl-type mt-6">
  <NlIcon name="layers" /> 150+ Slides
  <span class="mx-3">·</span>
  <NlIcon name="box" /> 18 Chapters
  <span class="mx-3">·</span>
  <NlIcon name="check" /> Industry-ready
</div>

<div class="nl-footer">
  <span><NlIcon name="play" :size="14" /> @noonlabsio</span>
  <span><NlIcon name="branch" :size="14" /> github.com/noonlabsio</span>
  <span><NlIcon name="mail" :size="14" /> noonlabs@gmail.com</span>
  <span><NlIcon name="phone" :size="14" /> +4915228517569</span>
</div>

<!--
SLIDE 2 - Course card
On screen ~8 seconds. Say the promise rather than reading the slide:
"Ce module couvre Python du premier script jusqu'au code qu'on met en
production. Dix-huit chapitres. Chacun se termine par quelque chose qui
tourne."
Point at the eighteen-chapter mark, then move on. Do NOT read the footer
aloud - it is there for the screenshot, not for the ear.
-->

---
layout: default
class: nl-deck
---

# What is a Programming Language?

<div class="nl-cols mt-4">

<div>

- A precise way to write instructions a machine can execute
- And that a person can still read six months later
- Source code is **plain text** — nothing more
- A **translator** turns that text into machine instructions
- Python's is an **interpreter**: it reads and runs, line by line

</div>

<div>

<div class="nl-type"><NlIcon name="file" /> What you write</div>

```python
# hello.py — a text file
print("Hello, NoonLabs!")
```

<div class="nl-type mt-2"><NlIcon name="terminal" /> What the machine does</div>

```bash
$ python hello.py
Hello, NoonLabs!
```

</div>

</div>

<div class="nl-statement mt-4">
The machine does exactly what you wrote — not what you meant
</div>

<!--
SLIDE 3 - What a language actually is
On screen ~50 seconds. The conceptual floor of the whole module.

"Avant d'écrire une ligne de Python, il faut comprendre ce qu'est un
langage de programmation. Ce n'est pas magique."

Walk the bullets. Slow down on the third:
"Le code source, c'est du texte. Rien d'autre. Vous pouvez l'ouvrir dans
n'importe quel éditeur."

PAUSE - this sentence pays off twice later: at the TypeError on a CSV, and
at the prompt a few slides from now. Same idea: c'est du texte.

Then the right column: "Vous écrivez ça. La machine fait ça."

Land on the statement, two beats, no explanation.
-->

---
layout: default
class: nl-deck
---

# Why Python? The Language of Modern Tech

<div class="grid grid-cols-2 gap-5 mt-4" style="font-size: 1.05rem">

<div class="nl-card">

<div class="nl-type"><NlIcon name="layers" /> One language, many domains</div>

Web, data, machine learning, automation, scientific computing — one syntax.

</div>

<div class="nl-card">

<div class="nl-type"><NlIcon name="box" /> An ecosystem to lean on</div>

Over 750,000 packages on PyPI. Someone has already met your problem.

</div>

<div class="nl-card">

<div class="nl-type"><NlIcon name="indent" /> Readable by design</div>

Indentation is syntax, not style. The structure is not optional.

</div>

<div class="nl-card">

<div class="nl-type"><NlIcon name="server" /> It runs real systems</div>

Production services under load, not only notebooks.

</div>

</div>

<div class="nl-statement mt-4">
Readable code is how a system outlives its author
</div>

<!--
SLIDE 4 - Why Python
On screen ~45 seconds. One sentence per card. Do not read them - they are
already on screen. Add what is NOT on screen:

"Le troisième point est celui qu'on sous-estime. L'indentation
obligatoire, ça agace au début. En production, sur du code écrit par
quelqu'un d'autre il y a deux ans, c'est ce qui vous sauve."

That is the channel's whole angle in one sentence. Say it slowly.

Then: "C'est pour ça qu'on commence par Python - pas parce que c'est
facile, parce que ça se relit."
-->

---
layout: default
class: nl-deck
---

# Your Python Learning Path

<div class="grid grid-cols-3 gap-8 mt-4">

<div class="nl-recap">
  <div class="n">01</div><div><span class="what">Getting Started</span></div>
  <div class="n">02</div><div><span class="what">Syntax &amp; Types</span></div>
  <div class="n">03</div><div><span class="what">Control Flow</span></div>
  <div class="n">04</div><div><span class="what">Functions</span></div>
  <div class="n">05</div><div><span class="what">Data Structures</span></div>
  <div class="n">06</div><div><span class="what">OOP</span></div>
</div>

<div class="nl-recap">
  <div class="n">07</div><div><span class="what">File I/O</span></div>
  <div class="n">08</div><div><span class="what">Error Handling</span></div>
  <div class="n">09</div><div><span class="what">Standard Library</span></div>
  <div class="n">10</div><div><span class="what">Functional</span></div>
  <div class="n">11</div><div><span class="what">Advanced</span></div>
  <div class="n">12</div><div><span class="what">NumPy</span></div>
</div>

<div class="nl-recap">
  <div class="n">13</div><div><span class="what">Pandas</span></div>
  <div class="n">14</div><div><span class="what">Visualization</span></div>
  <div class="n">15</div><div><span class="what">APIs</span></div>
  <div class="n">16</div><div><span class="what">Testing</span></div>
  <div class="n">17</div><div><span class="what">Best Practices</span></div>
  <div class="n">18</div><div><span class="what">Projects</span></div>
</div>

</div>

<div class="nl-statement mt-6">
Each chapter ends with something that runs
</div>

<!--
SLIDE 5 - The path
On screen ~35 seconds. The most screenshot-able slide in the module -
people save it as a roadmap. Give it room.

Sweep the three columns rather than naming eighteen things:
"Les six premiers, c'est le langage. Les six suivants, c'est ce qu'on en
fait. Les six derniers, c'est ce qui sépare un script d'un vrai projet."

Then point at 16 and 17:
"Testing et Best Practices ne sont pas en option. C'est là que la plupart
des cours s'arrêtent, et c'est là que le travail commence."
-->

---
layout: section
class: nl-deck
---

<div class="nl-eyebrow">Chapter 01</div>

# Getting Started with Python

<div class="mt-4" style="max-width: 40ch">

Setting up your environment, and understanding why Python ended up everywhere

</div>

<div class="nl-type mt-6">
  <NlIcon name="download" /> Installation
  <span class="mx-3">·</span>
  <NlIcon name="lock" /> Setup
  <span class="mx-3">·</span>
  <NlIcon name="prompt" /> First Program
</div>

<!--
SLIDE 6 - Chapter divider
On screen ~6 seconds. A breath, not a lesson.

"Chapitre un. On installe, on isole, on vérifie. Et on écrit notre
première ligne."

The three marks at the bottom are the chapter's shape - point at them once
as you say it, then cut.
-->

---
layout: default
class: nl-deck
---

# Python Installation & Setup

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="download" /> 1 · Install</div>

```bash
# macOS
brew install python

# Windows
python.org/downloads
✓ Check "Add to PATH"

# Debian / Ubuntu
apt install python3
```

<div class="nl-type mt-2"><NlIcon name="lock" /> 2 · Isolate</div>

```bash
uv venv
source .venv/bin/activate
```

</div>

<div>

<div class="nl-type"><NlIcon name="check" /> 3 · Verify</div>

```bash
$ python3 --version
Python 3.14.7
```

<div class="nl-type mt-2"><NlIcon name="prompt" /> 4 · Meet the prompt</div>

```python
>>> print("Hello, NoonLabs!")
Hello, NoonLabs!
>>> exit()
```

</div>

</div>

<div class="nl-statement mt-4">
A verified install and an isolated environment, before the first real line
</div>

<!--
SLIDE 7 - Installation
On screen ~70 seconds, most of it live in the terminal.

Say why step 2 exists, because every beginner skips it:
"On n'installe jamais des paquets dans le Python du système. Un projet,
un environnement. Ça vous évitera la phrase la plus coûteuse du métier :
« ça marche sur ma machine »."

Then step 4 - the payoff from slide 3, landed explicitly:
"Et voilà les trois chevrons. C'est Python qui lit votre texte et qui
répond immédiatement. Souvenez-vous : du texte, un interprète, un
résultat."

VERIFY BEFORE RECORDING: the version on screen must match what your
terminal prints.
-->

---
layout: default
class: nl-deck
---

# Virtual Environments: venv & uv

<div class="nl-cols mt-4">

<div style="font-size: 1.15rem">

<div class="nl-type"><NlIcon name="split" /> Without one</div>

- Two projects need different library versions
- Upgrading for one silently breaks the other

<div class="nl-type mt-2"><NlIcon name="lock" /> With one per project</div>

- Dependencies isolated, and pinned in a file
- Broken? Delete the folder and rebuild

</div>

<div>

<div class="nl-type"><span class="nl-logo nl-logo--python" /> Standard library</div>

```bash
python3 -m venv .venv
source .venv/bin/activate
deactivate
```

<div class="nl-type mt-2"><span class="nl-logo nl-logo--uv" /> uv — what we use here</div>

```bash
uv venv
uv add pandas
uv sync --frozen
```

</div>

</div>

<div class="nl-statement mt-4">
One project, one environment — that is the entire fix
</div>

<!--
SLIDE 8 - Virtual environments
On screen ~60 seconds. Left column from memory, right column live.

Open with the failure, not the feature:
"Vous installez pandas pour un projet. Six mois plus tard, un autre
projet a besoin d'une version différente. Vous mettez à jour. Le premier
projet ne démarre plus. Personne ne vous a prévenu."

PAUSE. Then: "Un projet, un environnement. C'est tout."

Point at `uv sync --frozen` - the line that separates a tutorial from
production: "Cette commande installe exactement les versions du fichier de
verrouillage. Pas « à peu près ». Exactement."

Why teach venv at all if we use uv: "venv est dans la bibliothèque
standard, il est sur toutes les machines. Il faut savoir le faire à la
main avant de laisser un outil le faire pour vous."
-->

---
layout: default
class: nl-deck
---

# Development Tools: Jupyter, VS Code & Google Colab

<div class="grid grid-cols-3 gap-6 mt-4" style="font-size: 1rem">

<div class="nl-card">

<div class="nl-type"><span class="nl-logo nl-logo--jupyter" /> Jupyter</div>

Cell-by-cell execution with plots inline. Excellent for exploring data, poor
at telling you what ran in which order.

<div class="nl-type mt-2"><NlIcon name="cells" :size="14" /> Explore</div>

</div>

<div class="nl-card">

<div class="nl-type"><span class="nl-logo nl-logo--vscode" /> VS Code</div>

Debugger, git, type checking, tests. Everything on this channel is written
here.

<div class="nl-type mt-2"><NlIcon name="server" :size="14" /> Build and ship</div>

</div>

<div class="nl-card">

<div class="nl-type"><NlIcon name="cloud" /> Google Colab</div>

A notebook in the browser with a GPU attached. Nothing to install, so it is
the fastest way to try something on a borrowed machine.

<div class="nl-type mt-2"><NlIcon name="arrow" :size="14" /> Try quickly</div>

</div>

</div>

<div class="nl-statement mt-4">
Explore in a notebook if you like — but ship from an editor
</div>

<!--
SLIDE 9 - Tools
On screen ~45 seconds. Have all three open in tabs and switch to them as
you name them.

The honest version, which most courses will not give:
"Jupyter est excellent pour explorer. Il est mauvais pour construire,
parce qu'il vous cache l'ordre d'exécution. Vous avez une cellule qui
marche, vous relancez le notebook depuis le début, et plus rien ne
marche."

PAUSE.

"C'est exactement pour ça que ce cours se fait dans VS Code. On explore
dans un carnet, on livre depuis un éditeur."

Colab is an escape hatch, not a home.

VERIFY BEFORE RECORDING: Colab's free tier terms change. Say "avec un
GPU" only if it is still true on the day.
-->

---
layout: default
class: nl-deck
---

# Your First Python Program

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="file" /> hello.py</div>

```python
# my first program
print("Hello, World!")
print("Welcome to Python!")
```

<div class="nl-type mt-2"><NlIcon name="terminal" /> Run it</div>

```bash
$ python hello.py
Hello, World!
Welcome to Python!
```

</div>

<div>

<div class="nl-type"><NlIcon name="prompt" /> Or ask directly</div>

```python
>>> 2 + 3
5
>>> "Hello, " + "World!"
'Hello, World!'
```

<div class="nl-recap mt-3">
  <div class="n">print()</div><div><span class="why">displays a value</span></div>
  <div class="n">#</div><div><span class="why">a comment — Python ignores it</span></div>
  <div class="n">.py</div><div><span class="why">the extension that marks source</span></div>
</div>

</div>

</div>

<div class="nl-statement mt-4">
The prompt is for asking. The file is for keeping.
</div>

<!--
SLIDE 10 - Hello, World
On screen ~70 seconds, most of it live in VS Code and the terminal.

Type the file by hand. Do not paste. Say the parts as you type:
"print, parenthèse, guillemet. Le texte entre guillemets, c'est une chaîne
de caractères. Retenez ce mot, on y revient dans la vidéo sur les types."

Run it. Two lines of output for two appels à print - point at the
correspondence, it is not obvious to a beginner.

Then the prompt, landing the payoff from slide 3:
"Là, je ne garde rien. Je demande. Deux plus trois, il répond cinq."

PAUSE on "Hello, " + "World!" and plant the hook WITHOUT explaining it:
"Notez le plus entre deux chaînes : il les colle. Gardez ça en tête. Dans
la prochaine vidéo, le même plus entre du texte et un nombre va faire
échouer notre programme, et c'est là que tout devient clair."

Close: "L'invite, c'est pour demander. Le fichier, c'est pour garder."
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>VIDEO 2 TITLE</strong>

</div>

<!--
SLIDE 11 - Closing card
On screen ~12 seconds.
Say the next video's topic out loud while this is up - the line on screen
is the reminder, your voice is the reason they come back.
Then: "À mardi." Hold two beats of silence before you stop recording, so
the editor has room to fade.
-->
