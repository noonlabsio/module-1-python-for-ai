---
theme: ../themes/noonlabs
title: Getting Started — Chapter 01
info: NoonLabs - Module I, chapitre 01
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

<div class="nl-eyebrow">Chapter 01</div>

# Getting Started

<div class="mt-4" style="max-width: 42ch">

From an empty machine to a Python project you can rebuild

</div>

<div class="nl-type mt-6">
  <NlIcon name="download" /> Install
  <span class="mx-3">·</span>
  <NlIcon name="lock" /> Isolate
  <span class="mx-3">·</span>
  <NlIcon name="play" /> Run
</div>

<!--
SLIDE 2 - Chapter divider
On screen ~8 seconds.

"Chapitre un. Avant d'écrire du Python, on prépare l'atelier : un
éditeur, un outil, une version de Python, et un projet qu'on peut
reconstruire avec les mêmes paquets."

Restate the format so nobody wonders:
"Les diapositives, c'est pour les concepts. Le code, on l'écrit ensemble
dans Visual Studio Code, qu'on appellera VS Code."
-->

---
layout: default
class: nl-deck
---

# Welcome to Python for Modern AI

<div class="nl-cols mt-4">

<div v-click style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="server" /> What you will build</div>

- A **CSV expense analyzer**: validated, summarised, tested
- A **public-data reporter**: fetch, clean, chart, report
- A **personal expense platform**: a CLI, a FastAPI backend, SQLite, charts, tests, deployed

</div>

<div style="font-size: 1.1rem">

<div v-click>

<div class="nl-type"><NlIcon name="layers" /> What you will be able to do</div>

- Read and write idiomatic Python
- Clean and analyse data with NumPy, pandas and Polars
- Test, lint and ship code someone else can run

</div>

<div v-click>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Fundamentals first, then models</li>
<li>No model training in this module</li>
</ul>

</div>

</div>

</div>

<div v-click class="nl-statement mt-4">
Every chapter ends with something that runs on your machine
</div>

<!--
SLIDE 3 - Welcome
On screen ~55 seconds. Concept slide, no live coding.

[CLICK 1]
Walk the three projects top to bottom, one sentence each. Do not list the
stack: "Le dernier projet, c'est une vraie application : une ligne de
commande, une API, une base de données, des graphiques, des tests. Et elle
est en ligne."

[CLICK 2]
"Et ce que vous saurez faire : lire et écrire du Python propre, analyser
des données avec NumPy, pandas et Polars, et livrer du code que quelqu'un d'autre
peut lancer."

PAUSE.

[CLICK 3]
Then the honest line about the scope:
"Ici, on n'entraîne pas de modèle. On construit la fondation sur laquelle
les modèles reposent. Les modules suivants : les mathématiques, puis le
machine learning."

[CLICK 4]
"Chaque chapitre se termine par quelque chose qui tourne."
-->

---
layout: default
class: nl-deck
---

# Your Learning Path

<div class="grid grid-cols-3 gap-6 mt-4">

<div v-click>

<div class="nl-type"><NlIcon name="indent" /> The language</div>

<div class="nl-recap mt-2">
  <div class="n">01</div><div><span class="why">Getting Started</span></div>
  <div class="n">02</div><div><span class="why">Syntax &amp; Types</span></div>
  <div class="n">03</div><div><span class="why">Control Flow</span></div>
  <div class="n">04</div><div><span class="why">Functions</span></div>
  <div class="n">05</div><div><span class="why">Data Structures</span></div>
  <div class="n">06</div><div><span class="why">Files &amp; Formats</span></div>
</div>

</div>

<div v-click>

<div class="nl-type"><NlIcon name="box" /> Structure</div>

<div class="nl-recap mt-2">
  <div class="n">07</div><div><span class="why">Errors</span></div>
  <div class="n">08</div><div><span class="why">Classes &amp; OOP</span></div>
  <div class="n">09</div><div><span class="why">Standard Library</span></div>
  <div class="n">10</div><div><span class="why">Functional</span></div>
  <div class="n">11</div><div><span class="why">Advanced Python</span></div>
  <div class="n">12</div><div><span class="why">NumPy</span></div>
</div>

</div>

<div v-click>

<div class="nl-type"><NlIcon name="server" /> Data &amp; production</div>

<div class="nl-recap mt-2">
  <div class="n">13</div><div><span class="why">pandas &amp; Polars</span></div>
  <div class="n">14</div><div><span class="why">Visualization</span></div>
  <div class="n">15</div><div><span class="why">APIs</span></div>
  <div class="n">16</div><div><span class="why">Testing</span></div>
  <div class="n">17</div><div><span class="why">Tooling</span></div>
  <div class="n">18</div><div><span class="why">Projects</span></div>
</div>

</div>

</div>

<div v-click class="nl-statement mt-4">
Each chapter builds on the last
</div>

<!--
SLIDE 4 - The path
On screen ~40 seconds. People screenshot this one as a roadmap. Give it
room.

One column per click, one sentence each.

[CLICK 1]
"Les six premiers, c'est le langage."

[CLICK 2]
"Les six suivants : organiser un vrai programme, puis les premiers outils
pour les données, avec NumPy."

[CLICK 3]
"Les six derniers, c'est les données, et ce qui sépare un script d'un
projet."

Point at 16 and 17:
"Les tests et l'outillage ne sont pas en option. C'est là que beaucoup de
cours s'arrêtent, et c'est là que le travail commence."

[CLICK 4]
"Chaque chapitre s'appuie sur le précédent."

Hold the fully revealed slide for two seconds before you move on.
-->

---
layout: default
class: nl-deck
---

# What Is a Programming Language?

<div class="nl-cols mt-4">

<div style="font-size: 1.1rem">

<div v-click>

<div class="nl-type"><NlIcon name="file" /> Source code is text</div>

A language is a strict format for instructions. You write them in a plain
text file. Any editor can open it.

</div>

<div v-click>

<div class="nl-type mt-3"><NlIcon name="terminal" /> An interpreter runs it</div>

The **interpreter** is a program that reads your file and executes it.
CPython, the standard one, first compiles it to bytecode, then runs that
bytecode. You never see this step.

</div>

</div>

<div>

<div v-click>

<div class="nl-type"><NlIcon name="file" /> What you write</div>

```python
# hello.py is a text file
print("Hello, World!")
```

</div>

<div v-click>

<div class="nl-type mt-2"><NlIcon name="terminal" /> What the interpreter does</div>

```bash
$ python hello.py
Hello, World!
```

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">It does exactly what the text says</li>
<li class="nl-bad">It does not guess what you meant</li>
</ul>

</div>

</div>

</div>

<div v-click class="nl-statement mt-4">
Your program is text. The interpreter gives it meaning.
</div>

<!--
SLIDE 5 - What a language is
On screen ~55 seconds. Concept slide, no live coding needed.

"Avant d'installer quoi que ce soit, une idée simple : un programme, c'est
du texte. Rien de magique."

[CLICK 1]
"Vous écrivez des instructions dans un fichier texte. N'importe quel
éditeur peut l'ouvrir."

[CLICK 2]
"Un autre programme, l'interpréteur, lit ce fichier et l'exécute. Pour
Python, cet interpréteur s'appelle CPython."

[CLICK 3]
Point at the file: "Vous écrivez ça."

[CLICK 4]
Point at the terminal: "L'interpréteur fait ça." Then, slowly:
"Il fait exactement ce que le texte dit. Pas ce que vous vouliez dire. Une
faute de frappe, et il s'arrête."

"Plus tard, on ne tapera plus python directement : on passera par uv run.
On verra pourquoi."

PAUSE.

[CLICK 5]
"Tout ce qu'on va installer aujourd'hui sert à une chose : donner à
l'interpréteur le bon texte, avec les bons outils autour."
-->

---
layout: default
class: nl-deck
---

# Why Python?

<div class="grid grid-cols-2 gap-6 mt-4" style="font-size: 1.05rem">

<div v-click class="nl-card">

<div class="nl-type"><NlIcon name="indent" /> Readable by design</div>

The syntax is short and the indentation is enforced. Code written by
someone else two years ago still reads.

</div>

<div v-click class="nl-card">

<div class="nl-type"><NlIcon name="cells" /> The language of data and AI</div>

NumPy, pandas, scikit-learn and PyTorch are all driven from Python.

</div>

<div v-click class="nl-card">

<div class="nl-type"><NlIcon name="layers" /> One language, many jobs</div>

Scripts, web backends, data pipelines, automation and tests all use the
same syntax.

</div>

<div v-click class="nl-card">

<div class="nl-type"><NlIcon name="server" /> Fast where it matters</div>

The heavy work runs in compiled C, C++ or Rust. Python is the readable
layer on top.

</div>

</div>

<div v-click class="nl-statement mt-4">
Python is slow to run and fast to write, and the libraries do the heavy lifting
</div>

<!--
SLIDE 6 - Why Python
On screen ~60 seconds. No market figures, no rankings. The reasons only.

One card per click. Do not read them; add what is not on screen.

[CLICK 1]
"Le premier point, on le sous-estime. Le code, on le lit beaucoup plus
souvent qu'on ne l'écrit."

[CLICK 2]
"Les grandes bibliothèques de données et d'IA se pilotent en Python."

[CLICK 3]
"Un script, un serveur web, un pipeline de données, des tests : la même
syntaxe."

[CLICK 4]
The honest card:
"Python, en soi, n'est pas rapide. Mais quand vous faites un calcul avec
NumPy, ce n'est pas Python qui calcule. C'est du code compilé, en dessous.
Python, c'est la couche qu'on lit."

PAUSE.

[CLICK 5]
"C'est pour ça que l'IA parle Python : on écrit vite, et les
bibliothèques font le travail lourd."
-->

---
layout: default
class: nl-deck
---

# "It Works on My Machine"

<div class="nl-cols mt-4">

<div>

<div v-click>

<div class="nl-type"><NlIcon name="split" /> Same code, two machines</div>

<div class="nl-recap mt-2">
  <div class="n">yours</div><div><span class="why">Python 3.14, pandas 3.0, runs</span></div>
  <div class="n">a colleague's</div><div><span class="why">Python 3.12, pandas 2.2, may fail</span></div>
  <div class="n">the server</div><div><span class="why">no pandas at all, may fail</span></div>
</div>

</div>

<div v-click>

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-bad">Packages installed globally, for every project at once</li>
<li class="nl-bad">Upgrading for one project breaks another</li>
</ul>

</div>

</div>

<div v-click style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="lock" /> What an environment fixes</div>

- **Isolation**: each project gets its own Python and its own packages
- **A record**: the versions are written in a file, not remembered
- **Rebuildable**: the same package versions, recreated from that file

</div>

</div>

<div v-click class="nl-statement mt-4">
The code is not the only thing that runs. Its environment runs too.
</div>

<!--
SLIDE 7 - The problem environments solve
On screen ~55 seconds. Concept slide.

[CLICK 1]
Tell the table as a story, one row per sentence:
"Votre script marche. Vous l'envoyez à un collègue. Chez lui, il peut
planter : il n'a pas la même version de Python, pas la même version de
pandas. Sur le serveur, pandas n'est même pas installé."

"Et vous dites la phrase la plus chère du métier : « ça marche sur ma
machine »."

PLANT the payoff and do not explain it:
"Retenez cette phrase. Avant la fin de ce chapitre, on va y répondre."

[CLICK 2]
"Le fond du problème : tout est installé au même endroit, pour tous les
projets. Mettre à jour pour l'un casse l'autre."

PAUSE.

[CLICK 3]
Then the right column, three words: isolation, une trace écrite, et on
reconstruit les mêmes versions.

[CLICK 4]
"Le code n'est pas la seule chose qui tourne : son environnement aussi."
-->

---
layout: default
class: nl-deck
---

# Visual Studio Code: Why an IDE

<div class="nl-cols mt-4">

<div v-click style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="layers" /> One window for the whole job</div>

A plain editor only edits text. An **IDE** also understands the code. It
completes names, shows errors before you run, and has a terminal, a
debugger and Git built in.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">macOS: <code>Cmd</code> for <code>Ctrl</code>, except the terminal: <code>Ctrl+&#96;</code></li>
<li class="nl-good">Or the menu: <strong>Terminal &gt; New Terminal</strong></li>
</ul>

</div>

<div v-click>

<div class="nl-type"><NlIcon name="file" /> The four areas you use daily</div>

<div class="nl-recap mt-2" style="font-size: 1.05rem">
  <div class="n">Explorer</div><div><span class="why">project files · Ctrl+Shift+E</span></div>
  <div class="n">Editor</div><div><span class="why">your code · open a file: Ctrl+P</span></div>
  <div class="n">Terminal</div><div><span class="why">uv and python · Ctrl+&#96;</span></div>
  <div class="n">Palette</div><div><span class="why">every command · Ctrl+Shift+P</span></div>
</div>

</div>

</div>

<div v-click class="nl-statement mt-4">
If you remember one shortcut, make it <code>Ctrl+Shift+P</code>
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 8 - VS Code tour
On screen ~60 seconds, most of it live in VS Code.

[CLICK 1]
"Un éditeur de texte, ça édite du texte. Un IDE comprend ce que vous
écrivez. Il vous montre l'erreur avant que vous lanciez le programme."

"Seul, VS Code ne comprend pas encore Python. Ce sont les extensions de la
diapositive suivante qui le lui apprennent."

Point at the two bullets:
"Sur Mac, Cmd à la place de Ctrl, sauf pour le terminal : Ctrl+backtick
partout."

[CLICK 2]
Point at the table: the four areas, in the order you will show them.

[LIVE]
Switch to VS Code with an empty folder open (File > Open Folder). Tour the
four areas in the order of the table and press each shortcut as you name
it:
- Ctrl+Shift+E: "l'explorateur, les fichiers du projet."
- Ctrl+P: "ouvrir un fichier par son nom."
- Ctrl+backtick: "le terminal intégré. On va y passer beaucoup de temps."
  No shortcut? Show the menu once: Terminal, New Terminal.
- Ctrl+Shift+P: type « theme » to show that every setting is a command.

[BACK]

PAUSE.

[CLICK 3]
"Vous ne savez pas où est une option ? Ctrl+Shift+P, et vous tapez ce que
vous cherchez."
-->

---
layout: default
class: nl-deck
---

# Essential Extensions

<div class="nl-cols mt-4">

<div v-click>

<div class="nl-type"><NlIcon name="box" /> Install these four</div>

<div class="nl-recap mt-2" style="font-size: 1.05rem">
  <div class="n">Python</div><div><span class="why">run, debug, pick the interpreter</span></div>
  <div class="n">Pylance</div><div><span class="why">completion, types, errors as you type</span></div>
  <div class="n">Error Lens</div><div><span class="why">the error printed on its own line</span></div>
  <div class="n">Jupyter</div><div><span class="why">notebooks inside the editor</span></div>
</div>

</div>

<div v-click style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="download" /> How</div>

Open the Extensions view with `Ctrl+Shift+X` and search by name.
Installing **Python** (Microsoft) also installs Pylance, the Python
Debugger and Python Environments.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good">Check the publisher before you install</li>
<li class="nl-bad">Twenty extensions you cannot explain</li>
</ul>

</div>

</div>

<div v-click class="nl-statement mt-4">
Pylance finds the mistake. Error Lens puts it where you are looking.
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 9 - Extensions
On screen ~50 seconds, live in VS Code.

[CLICK 1]
"Quatre extensions. Chacune a une raison d'être là."

[CLICK 2]
"Une installation, et vous avez Pylance, le débogueur, et la gestion des
environnements."

Point at the last bullet:
"Méfiez-vous des listes de vingt extensions indispensables."

[LIVE]
Ctrl+Shift+X. Search « Python », install the one published by Microsoft.
Point at the extensions that come with it.

Then search « Error Lens » (publisher: Alexander, id usernamehw.errorlens)
and « Jupyter » (Microsoft). Install both.

[BACK]

PAUSE.

[CLICK 3]
"Pylance comprend votre code. Error Lens affiche le message directement sur
la ligne. Sans lui, l'erreur est soulignée en rouge, et il faut aller
chercher le message."
-->

---
layout: default
class: nl-deck
---

# Conda, Anaconda and Mamba

<div v-click class="grid grid-cols-3 gap-6 mt-4" style="font-size: 0.98rem">

<div class="nl-card">

<div class="nl-type"><NlIcon name="box" /> conda</div>

A package and environment manager for **any** language: Python, R, C
libraries, CUDA.

</div>

<div class="nl-card">

<div class="nl-type"><NlIcon name="layers" /> Anaconda</div>

A distribution: conda, Python and hundreds of data-science packages in
one installer.

</div>

<div class="nl-card">

<div class="nl-type"><NlIcon name="arrow" /> Mamba</div>

A fast C++ reimplementation of conda. Its solver is now conda's default.

</div>

</div>

<div class="nl-cols mt-3">

<div v-click>

<div class="nl-type nl-good"><NlIcon name="check" /> Why people use them</div>

<ul class="mt-2" style="font-size: 1.05rem">
<li class="nl-good">Non-Python dependencies: GPU stacks, geospatial, compilers</li>
<li class="nl-good">A standard in many research labs</li>
</ul>

</div>

<div v-click>

<div class="nl-type"><span class="nl-logo nl-logo--uv" /> Why we start with uv</div>

<ul class="mt-2" style="font-size: 1.05rem">
<li class="nl-good">Our dependencies install as ready-made packages from PyPI</li>
<li class="nl-good">Standard <code>pyproject.toml</code>, a lock file by default</li>
</ul>

</div>

</div>

<div v-click class="nl-statement mt-3">
conda manages a software stack. uv manages a Python project.
</div>

<!--
SLIDE 10 - Conda, Anaconda, Mamba
On screen ~65 seconds. Concept slide, nothing to install.

[CLICK 1]
You will meet these names in every tutorial, so say what each one is:
"conda, c'est l'outil. Il installe des paquets et crée des environnements,
et pas seulement pour Python : du R, des bibliothèques C, CUDA pour les
cartes graphiques."

"Anaconda, c'est une distribution : conda, Python, et des centaines de
paquets déjà installés, en un seul installateur. Pratique, mais lourd."

"Mamba, c'est conda réécrit en C++, beaucoup plus rapide. Son moteur de
résolution est même devenu celui de conda par défaut."

PAUSE.

[CLICK 2]
Be fair about when conda is the right tool:
"Si votre projet dépend de choses qui ne sont pas du Python, comme une pile
GPU ou des bibliothèques géospatiales, conda est souvent le bon choix."

"Si un jour vous choisissez conda, passez par Miniforge : il utilise
conda-forge, qui reste gratuit."

[CLICK 3]
Then why this course does not use it:
"Nos dépendances s'installent depuis PyPI en paquets déjà compilés, des
« wheels » : rien à compiler chez vous. uv suit les standards de Python, il
crée un fichier de verrouillage tout seul, et il est très rapide."

Mention once, without dwelling, that Anaconda's own package channel has
paid terms for organisations above 200 people, while conda-forge stays
free. VERIFY BEFORE RECORDING: Anaconda's terms change.

[CLICK 4]
"conda gère une pile logicielle. uv gère un projet Python."
-->

---
layout: default
class: nl-deck
---

# Installing uv and Python 3.14

<div class="nl-cols mt-4">

<div v-click style="font-size: 1.1rem">

<div class="nl-type"><span class="nl-logo nl-logo--uv" /> What uv is</div>

One tool for Python, environments and packages.

<ul class="mt-3" style="font-size: 1.05rem">
<li class="nl-good"><code>uv</code> not found? Open a new terminal</li>
<li class="nl-good">Use 3.14 to follow along exactly</li>
</ul>

</div>

<div v-click>

<div class="nl-type"><NlIcon name="terminal" /> In the VS Code terminal (Ctrl+&#96;): macOS, Linux</div>

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

</div>

</div>

<div v-click>

<div class="nl-type mt-2"><NlIcon name="terminal" /> Windows (PowerShell)</div>

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

</div>

<div class="nl-cols mt-3">

<div v-click>

<div class="nl-type"><NlIcon name="download" /> Then Python itself</div>

```bash
uv --version
uv python install 3.14
uv python list
```

</div>

</div>

<div v-click class="nl-statement mt-3">
uv installs Python too: no installer, no PATH checkbox
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 11 - Installing uv and Python
On screen ~60 seconds, live in the VS Code terminal.

[CLICK 1]
"Un seul outil. Il installe Python, il crée les environnements, il gère les
paquets. Avant, il en fallait trois ou quatre."

Point at the second bullet:
"Pourquoi 3.14 ? C'est la version de tout ce cours. Utilisez-la pour
suivre exactement : avec une autre version, certains messages d'erreur ne
seront pas les mêmes."

[CLICK 2]
Point at the curl line: "Sur macOS et Linux, cette ligne."
"Cette ligne télécharge un script et l'exécute. Vous pouvez le lire avant :
remplacez « | sh » par « | less »."

[CLICK 3]
"Sous Windows, celle-ci, dans PowerShell."

[CLICK 4]
"Ensuite, Python lui-même : trois commandes."

[LIVE]
Open the terminal with Ctrl+backtick and paste the line for your system.
The installer adds uv to your PATH; if `uv` is not found afterwards, open a
new terminal (the trash icon, then Ctrl+backtick again).

Type: uv --version
Expected: a line starting with "uv 0." and the version number.

Type: uv python install 3.14
"Pas besoin d'aller sur python.org. uv télécharge Python et le range à
part, sans toucher au Python de votre système."

Type: uv python list
Point at the 3.14 line marked as installed.

[BACK]

PAUSE.

[CLICK 5]
"uv installe aussi Python : pas d'installateur, pas de case PATH à cocher."

VERIFY BEFORE RECORDING: Python 3.15 is out since October 2026. Keep 3.14
on screen only if every chapter is recorded on 3.14.
-->

---
layout: default
class: nl-deck
---

# Virtual Environments

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="box" /> One .venv per project</div>

<svg viewBox="0 0 400 178" width="100%" role="img" aria-label="System Python at the top, with no project packages. Below it, two projects, each with its own .venv: hello-ai with Python 3.14 and pandas 3.0.6, old-report with Python 3.12 and pandas 2.2.3">
<g v-click>
<rect x="0.5" y="0.5" width="399" height="33" rx="8" fill="var(--nl-ink-950)" stroke="var(--nl-line)" stroke-dasharray="4 4"/>
<text x="16" y="21" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--fg-3)">system Python</text>
<text x="384" y="21" text-anchor="end" font-family="var(--nl-sans)" font-size="11.2px" fill="var(--fg-3)">no project packages here</text>
</g>
<g v-click font-family="var(--nl-mono)" font-size="11.2px">
<rect x="0.5" y="48.5" width="189" height="128" rx="8" fill="var(--nl-ink-950)" stroke="var(--nl-line)"/>
<text x="14" y="70" fill="var(--nl-bone)">hello-ai/</text>
<rect x="14.5" y="82.5" width="161" height="82" rx="6" fill="none" stroke="var(--accent)"/>
<text x="28" y="104" fill="var(--accent)">.venv/</text>
<text x="28" y="128" fill="var(--nl-c-plain)">python 3.14</text>
<text x="28" y="150" fill="var(--nl-c-plain)">pandas 3.0.6</text>
</g>
<g v-click font-family="var(--nl-mono)" font-size="11.2px">
<rect x="210.5" y="48.5" width="189" height="128" rx="8" fill="var(--nl-ink-950)" stroke="var(--nl-line)"/>
<text x="224" y="70" fill="var(--nl-bone)">old-report/</text>
<rect x="224.5" y="82.5" width="161" height="82" rx="6" fill="none" stroke="var(--accent)"/>
<text x="238" y="104" fill="var(--accent)">.venv/</text>
<text x="238" y="128" fill="var(--nl-c-plain)">python 3.12</text>
<text x="238" y="150" fill="var(--nl-c-plain)">pandas 2.2.3</text>
</g>
</svg>

</div>

<div>

<div v-click>

<div class="nl-type"><span class="nl-logo nl-logo--uv" /> Create one with uv</div>

```bash
uv init --no-package --python 3.14 hello-ai
cd hello-ai
uv venv
```

</div>

<div v-click>

<div class="nl-type mt-2"><span class="nl-logo nl-logo--vscode" /> Tell VS Code to use it</div>

<ul class="mt-2" style="font-size: 1.05rem">
<li class="nl-good"><code>Ctrl+Shift+P</code>, then <strong>Python: Select Interpreter</strong></li>
<li class="nl-good">Pick <code>.venv</code> and check the status bar</li>
</ul>

</div>

</div>

</div>

<div v-click class="nl-statement mt-4">
One project, one environment, one folder you can throw away
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 12 - Virtual environments
On screen ~75 seconds, live in the VS Code terminal.

"Un environnement virtuel, c'est un dossier. Dedans : un Python, et les
paquets de ce projet. Rien d'autre."

Build the diagram, one group per click.

[CLICK 1]
Point at the dashed box, system Python:
"Le Python du système, on n'y installe rien."

[CLICK 2]
Trace the hello-ai .venv box with your finger:
"hello-ai a son propre Python, 3.14, et pandas 3.0."

[CLICK 3]
Trace the old-report .venv box:
"old-report a Python 3.12 et pandas 2.2. Deux versions côte à côte, sur
la même machine, sans conflit."

[CLICK 4]
"Pour créer le vôtre : trois commandes."

[CLICK 5]
"Puis on dit à VS Code d'utiliser ce Python-là."

[LIVE]
Type: uv init --no-package --python 3.14 hello-ai
Explain the flags once: « no-package » parce qu'on écrit des scripts, pas
une bibliothèque ; sans ce drapeau, les versions récentes de uv créent un
dossier src. « python 3.14 » fixe la version du projet.

Type: cd hello-ai, then code -r . to reopen VS Code on the project.
"Si la commande code n'est pas reconnue : File, Open Folder. Sur macOS,
installez-la une fois depuis la palette : « Shell Command: Install 'code'
command in PATH ». La fenêtre se recharge : rouvrez un terminal."

Type: uv venv
Expected: "Using CPython 3.14.x" then "Creating virtual environment at:
.venv". Show the folder in the Explorer.

"uv venv, c'est pour le voir une fois. Ensuite, vous n'en aurez plus
besoin : uv add, uv run et uv sync créent .venv tout seuls s'il manque."

Then the interpreter. Ctrl+Shift+P, « Python: Select Interpreter », choose
the one in .venv. Point at the status bar: it now shows the project's
environment.

[BACK]

"Si VS Code utilise le mauvais Python, rien ne marchera comme prévu. C'est
la première chose à vérifier."

PAUSE.

[CLICK 6]

"Ce dossier, on peut le jeter. Gardez ça en tête."
-->

---
layout: default
class: nl-deck
---

# Hello, World!

<div class="nl-cols mt-4">

<div>

<div v-click>

<div class="nl-type"><NlIcon name="file" /> hello.py</div>

```python
# My first program
print("Hello, World!")
print("Python is ready.")
```

</div>

<div v-click>

<div class="nl-type mt-2"><NlIcon name="terminal" /> Run it</div>

```bash
$ uv run hello.py
Hello, World!
Python is ready.
```

</div>

</div>

<div>

<div v-click>

<div class="nl-recap" style="font-size: 1.05rem">
  <div class="n">print()</div><div><span class="why">displays a value</span></div>
  <div class="n">#</div><div><span class="why">a comment, ignored by Python</span></div>
  <div class="n">.py</div><div><span class="why">marks a Python source file</span></div>
</div>

</div>

<div v-click>

<div class="nl-type mt-3"><NlIcon name="check" /> The setup works if</div>

<ul class="mt-2" style="font-size: 1.05rem">
<li class="nl-good">Both lines print, from <code>.venv</code>'s Python</li>
<li class="nl-good">The status bar shows <code>.venv</code></li>
<li class="nl-good">Error Lens flags a typo like <code>prnt</code></li>
</ul>

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
One file, two lines, and every tool in the chain has been tested
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 13 - Hello, World
On screen ~65 seconds, live in VS Code.

[CLICK 1]
"Notre premier programme : un commentaire et deux print."

[CLICK 2]
"On le lance avec uv run."

[LIVE]
Create hello.py in the Explorer. Type it by hand, do not paste. Say the
parts as you type:
"Dièse : un commentaire. Python l'ignore, il est là pour les humains.
print, parenthèse, guillemets. Le texte entre guillemets, c'est une chaîne
de caractères."

Type: uv run hello.py
Expected:
Hello, World!
Python is ready.
"Deux appels à print, deux lignes." Point at the correspondence, it is
not obvious to a beginner.

PAUSE.

Now test the chain, one link at a time:
Type: uv run python -c "import sys; print(sys.prefix)"
Expected: a path ending in hello-ai/.venv. "C'est bien le Python du
projet."

Point at the status bar: .venv. Then change print to prnt on line 2. Error
Lens shows the problem on the line before you run anything. Run it anyway:
Expected last line: NameError: name 'prnt' is not defined. Did you mean: 'print'?
Fix it back.

[BACK]

[CLICK 3]
"print affiche une valeur. Le dièse, un commentaire. Et .py, c'est ce qui
dit : ceci est un fichier source Python."

[CLICK 4]
"Les trois vérifications qu'on vient de faire. Si elles passent, votre
installation est bonne."

[CLICK 5]
"uv, Python 3.14, l'environnement, VS Code, les extensions. Tout est
vérifié."
-->

---
layout: default
class: nl-deck
---

# pyproject.toml and the Lock File

<div class="nl-cols mt-4">

<div>

<div v-click>

<div class="nl-type"><NlIcon name="terminal" /> uv add pandas</div>

```toml
[project]
name = "hello-ai"
requires-python = ">=3.14"
dependencies = [
    "pandas>=3.0.6",
]
```

</div>

<div class="mt-3">

<svg viewBox="0 0 400 80" width="100%" role="img" aria-label="pyproject.toml, then an arrow labelled uv lock to uv.lock, then an arrow labelled uv sync to .venv">
<g v-click>
<rect x="0.5" y="20.5" width="111" height="35" rx="8" fill="var(--nl-ink-950)" stroke="var(--nl-line)"/>
<text x="56" y="42" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--nl-c-plain)" text-anchor="middle">pyproject.toml</text>
<text x="56" y="74" font-family="var(--nl-sans)" font-size="11.2px" fill="var(--fg-3)" text-anchor="middle">what you ask for</text>
</g>
<g v-click>
<g stroke="var(--fg-3)" fill="var(--fg-3)">
<line x1="114" y1="38" x2="136" y2="38"/>
<path d="M136 34 L142 38 L136 42 Z"/>
</g>
<text x="128" y="12" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--fg-3)" text-anchor="middle">uv lock</text>
<rect x="144.5" y="20.5" width="111" height="35" rx="8" fill="var(--nl-ink-950)" stroke="var(--accent)"/>
<text x="200" y="42" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--nl-c-plain)" text-anchor="middle">uv.lock</text>
<text x="200" y="74" font-family="var(--nl-sans)" font-size="11.2px" fill="var(--fg-3)" text-anchor="middle">exact versions</text>
</g>
<g v-click>
<g stroke="var(--fg-3)" fill="var(--fg-3)">
<line x1="258" y1="38" x2="280" y2="38"/>
<path d="M280 34 L286 38 L280 42 Z"/>
</g>
<text x="272" y="12" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--fg-3)" text-anchor="middle">uv sync</text>
<rect x="288.5" y="20.5" width="111" height="35" rx="8" fill="var(--nl-ink-950)" stroke="var(--nl-line)"/>
<text x="344" y="42" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--nl-c-plain)" text-anchor="middle">.venv/</text>
<text x="344" y="74" font-family="var(--nl-sans)" font-size="11.2px" fill="var(--fg-3)" text-anchor="middle">installed here</text>
</g>
</svg>

</div>

</div>

<div style="font-size: 1.1rem">

<div v-click>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Why not requirements.txt</div>

<ul class="mt-2" style="font-size: 1.05rem">
<li class="nl-bad">A list of things to install, not a project</li>
<li class="nl-bad"><code>pip freeze</code>: a one-machine snapshot, mixing what you chose with what came along</li>
<li class="nl-bad"><code>tzdata</code> is Windows-only for pandas, so a Linux-made file does not pin it</li>
<li class="nl-good"><code>uv.lock</code> pins every platform</li>
</ul>

</div>

<div v-click>

<div class="nl-type nl-good mt-3"><NlIcon name="check" /> The rule</div>

<ul class="mt-2" style="font-size: 1.05rem">
<li class="nl-good">Change dependencies with <code>uv add</code>, <code>uv remove</code></li>
<li class="nl-bad">Never edit <code>uv.lock</code> by hand</li>
</ul>

</div>

</div>

</div>

<div v-click class="nl-statement mt-3">
<code>pyproject.toml</code> says what you want. <code>uv.lock</code> says exactly what you got.
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 14 - Project files
On screen ~80 seconds, live in VS Code.

[CLICK 1]
"On ajoute pandas au projet. Une commande : uv add pandas."

[LIVE]
Type: uv add pandas
Then open pyproject.toml in the editor. The slide trims the description and
readme lines; say so if anyone squints.

"Une seule ligne a changé : pandas, version minimum. C'est ce que vous avez
demandé."

Open uv.lock and scroll:
"Ici, il y a pandas, mais aussi numpy, dateutil, six, tzdata. Tout ce qui
vient avec, à la version exacte. Ce fichier, c'est uv qui l'écrit. Vous ne
le modifiez jamais à la main."

[BACK]

Build the diagram left to right, one box per click.

[CLICK 2]
Point at pyproject.toml: "pyproject.toml, ce que vous demandez."

[CLICK 3]
Point at the uv lock arrow, then the bronze box:
"uv lock en tire uv.lock, les versions exactes."

[CLICK 4]
Point at the uv sync arrow, then .venv:
"uv sync installe ces versions dans .venv." Then: "uv add fait les trois
d'un coup."

PAUSE.

[CLICK 5]
Then requirements.txt, with the concrete proof:
"Un requirements.txt, c'est une liste de choses à installer. Si je le
génère avec pip freeze, c'est une photo d'une seule machine : ce que j'ai
choisi et ce qui est venu avec, mélangés."

"pandas n'a besoin de tzdata que sous Windows. Sur ma machine Linux, pip
freeze ne l'écrit donc pas. Mon collègue sous Windows l'aura quand même,
mais dans la version du jour, pas une version épinglée. uv.lock, lui,
épingle les versions pour toutes les plateformes."

[CLICK 6]
"La règle : on change les dépendances avec uv add et uv remove. uv.lock,
on n'y touche jamais à la main."

If a tool insists on a requirements.txt: uv export can write one from the
lock file. Say it once, do not demo it.

VERIFY BEFORE RECORDING: the pandas version uv writes. Update the slide to
what your uv add prints.

[CLICK 7]
"pyproject.toml dit ce que vous voulez. uv.lock dit exactement ce que vous
avez obtenu."
-->

---
layout: default
class: nl-deck
---

# Three Ways to Run Python

<div class="grid grid-cols-3 gap-6 mt-4" style="font-size: 0.98rem">

<div v-click class="nl-card">

<div class="nl-type"><NlIcon name="file" /> Script</div>

A `.py` file, run top to bottom.

`uv run hello.py`

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Code you keep</div>

</div>

<div v-click class="nl-card">

<div class="nl-type"><NlIcon name="prompt" /> REPL</div>

The `>>>` prompt. One line, one answer.

`uv run python`

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> A quick question</div>

</div>

<div v-click class="nl-card">

<div class="nl-type"><NlIcon name="cells" /> Notebook</div>

A `.ipynb` file of cells, with output inline.

`Ctrl+Shift+P`, New Jupyter Notebook

<div class="nl-type nl-good mt-2"><NlIcon name="check" /> Exploring data</div>

</div>

</div>

<div v-click class="nl-cols mt-3">

<div>

```python
>>> 2 + 3
5
>>> "Hello, " + "World!"
'Hello, World!'
```

</div>

<div style="font-size: 1.1rem">

REPL means Read, Eval, Print, Loop. It forgets everything when you type
`exit()`.

</div>

</div>

<div v-click class="nl-statement mt-3">
Ask in the REPL, explore in a notebook, keep in a script
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 15 - Ways to run Python
On screen ~55 seconds, the REPL part live.

"Trois façons de lancer Python. Elles ne se font pas concurrence. Chacune a
son usage."

[CLICK 1]
"Un script : un fichier .py, lancé du début à la fin. Le code qu'on garde."

[CLICK 2]
"La console : une ligne, une réponse."

[CLICK 3]
"Le carnet : des cellules, avec le résultat juste en dessous."

"Essayons la console."

[LIVE]
Type: uv run python
"Les trois chevrons : Python attend votre question."

Type: 2 + 3
Expected: 5

Type: "Hello, " + "World!"
Expected: 'Hello, World!'

PAUSE on the plus between two strings, and plant the hook for the types
chapter WITHOUT explaining it:
"Notez le plus entre deux chaînes : il les colle. Gardez ça en tête. Au
chapitre sur les types, le même plus, entre du texte et un nombre, va
faire échouer notre programme."

Type: exit()

[BACK]

[CLICK 4]
"REPL : lire, évaluer, afficher, recommencer. Et tout est oublié quand vous
tapez exit()."

[CLICK 5]
"La console, c'est pour demander. Le carnet, c'est pour explorer. Le
fichier, c'est pour garder."
-->

---
layout: default
class: nl-deck
---

# Jupyter Notebooks in VS Code

<div class="nl-cols mt-4">

<div v-click style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="cells" /> Cells and the kernel</div>

A notebook is a list of **cells**: code or text. The **kernel** is a
Python process that runs them and keeps every variable in memory.

</div>

<div v-click>

<div class="nl-type"><span class="nl-logo nl-logo--vscode" /> In VS Code</div>

```bash
uv add --dev ipykernel
```

<ul class="mt-2" style="font-size: 1.05rem">
<li class="nl-good"><strong>Select Kernel</strong>, then the project's <code>.venv</code></li>
</ul>

</div>

</div>

<div class="nl-cols mt-3">

<div v-click>

<ul style="font-size: 1.05rem">
<li class="nl-good">The number <code>[3]</code> shows the run order</li>
<li class="nl-bad">Cells run out of order hide bugs</li>
<li class="nl-good">Restart and Run All before you trust a result</li>
</ul>

</div>

<div v-click>

<div class="nl-type"><span class="nl-logo nl-logo--jupyter" /> JupyterLab in the browser</div>

```bash
uv run --with jupyter jupyter lab
```

</div>

</div>

<div v-click class="nl-statement mt-4">
The kernel remembers what you ran, not what you see on the page
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 16 - Jupyter
On screen ~65 seconds, live in VS Code.

[CLICK 1]
"Un carnet, c'est des cellules. Le noyau, c'est le Python qui les exécute,
et il garde tout en mémoire."

[CLICK 2]
"Pour VS Code : ipykernel dans le projet, puis Select Kernel, et le .venv
du projet."

[LIVE]
Type: uv add --dev ipykernel
"ipykernel, c'est ce qui permet à un carnet de parler à notre
environnement. --dev, parce que le programme final n'en a pas besoin. Seul
le développeur en a besoin."

Ctrl+Shift+P, « Create: New Jupyter Notebook ». Click Select Kernel, then
Python Environments, then .venv.

Live demo of the trap, three cells:
cell 1: x = 1
cell 2: print(x)
Run cell 1, run cell 2: it prints 1. Change cell 1 to x = 10 and do NOT run
it. Run cell 2: it still prints 1.

"La page dit dix. Le noyau dit un."

Then the fix: Restart the kernel, then Run All. Cell 2 now prints 10.

Then JupyterLab, briefly: uv run --with jupyter jupyter lab opens the
browser on localhost port 8888. Ctrl+C in the terminal to stop it.

[BACK]

[CLICK 3]
"Le numéro entre crochets, c'est l'ordre d'exécution. Des cellules lancées
dans le désordre cachent des bugs."

PAUSE.

"Avant de faire confiance à un résultat : Restart, puis Run All."

[CLICK 4]
"JupyterLab, dans le navigateur. Jupyter n'est pas ajouté au projet : uv
le met dans un environnement à part, en cache. pyproject.toml et .venv ne
changent pas."

[CLICK 5]
"Le noyau se souvient de ce que vous avez exécuté, pas de ce que vous
voyez."
-->

---
layout: default
class: nl-deck
---

# Google Colab

<div class="nl-cols mt-4">

<div style="font-size: 1.1rem">

<div v-click>

<div class="nl-type"><NlIcon name="cloud" /> What it is</div>

A Jupyter notebook hosted by Google. It runs in the browser on a Google
machine, with free access to GPUs when they are available. Notebooks are
saved to Google Drive.

</div>

<div v-click>

<div class="nl-type mt-3"><NlIcon name="cross" /> What it is not</div>

A permanent machine. The runtime resets, and installed packages go with
it.

</div>

</div>

<div>

<div v-click>

<div class="nl-type"><NlIcon name="check" /> When to use it</div>

<ul class="mt-2" style="font-size: 1.05rem">
<li class="nl-good">A machine where you cannot install anything</li>
<li class="nl-good">A GPU for a short experiment</li>
<li class="nl-good">Sharing a notebook that runs in one click</li>
</ul>

</div>

<div v-click>

<div class="nl-type mt-3"><NlIcon name="cross" /> When not to</div>

<ul class="mt-2" style="font-size: 1.05rem">
<li class="nl-bad">Data that must not leave your machine</li>
<li class="nl-bad">Long jobs: runtimes have time limits</li>
</ul>

</div>

</div>

</div>

<div v-click class="nl-statement mt-4">
Colab is a borrowed machine: try things there, keep them in your project
</div>

<!--
SLIDE 17 - Google Colab
On screen ~55 seconds. Have colab.research.google.com open in a tab.

[CLICK 1]
"Colab, c'est un carnet Jupyter dans le navigateur, sur une machine de
Google. Rien à installer, et une carte graphique gratuite, quand il y en a."

PAUSE.

[CLICK 2]
"Mais la machine ne vous appartient pas. Fermez l'onglet trop longtemps,
et elle est effacée, avec tout ce que vous y avez installé."

[CLICK 3]
"Quand l'utiliser ? Sur une machine où vous ne pouvez rien installer, pour
une courte expérience sur GPU, ou pour partager un carnet qui tourne en un
clic."

[CLICK 4]
"Et votre code tourne chez Google : des données qui ne doivent pas quitter
votre machine n'ont rien à faire là. Les longs calculs non plus : une
session a une durée limitée, et elle s'arrête si vous êtes inactif. Google
ne publie pas ces limites, elles changent."

Optional, one sentence: Google's « Google Colab » extension lets a VS Code
notebook run on a Colab runtime, so you can keep your editor and borrow
their GPU.

[CLICK 5]
"Colab, c'est une machine empruntée : on essaie là-bas, on garde dans son
projet."

VERIFY BEFORE RECORDING: free-tier GPU access and session limits change
without notice. Say "quand il y en a" about GPUs.
-->

---
layout: default
class: nl-deck
---

# Reproducibility

<div class="nl-cols mt-4">

<div>

<div class="nl-type"><NlIcon name="lock" /> Delete it, rebuild it</div>

<svg viewBox="0 0 400 144" width="100%" role="img" aria-label="The project files diagram, pyproject.toml to uv.lock to .venv. Then .venv is crossed out as deleted, and a green arrow labelled uv sync --locked runs from uv.lock to a new .venv, rebuilt">
<g v-click>
<rect x="0.5" y="20.5" width="111" height="35" rx="8" fill="var(--nl-ink-950)" stroke="var(--nl-line)"/>
<text x="56" y="42" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--nl-c-plain)" text-anchor="middle">pyproject.toml</text>
<g stroke="var(--fg-3)" fill="var(--fg-3)">
<line x1="114" y1="38" x2="136" y2="38"/>
<path d="M136 34 L142 38 L136 42 Z"/>
</g>
<text x="128" y="12" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--fg-3)" text-anchor="middle">uv lock</text>
<rect x="144.5" y="20.5" width="111" height="35" rx="8" fill="var(--nl-ink-950)" stroke="var(--accent)"/>
<text x="200" y="42" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--nl-c-plain)" text-anchor="middle">uv.lock</text>
<g stroke="var(--fg-3)" fill="var(--fg-3)">
<line x1="258" y1="38" x2="280" y2="38"/>
<path d="M280 34 L286 38 L280 42 Z"/>
</g>
<text x="272" y="12" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--fg-3)" text-anchor="middle">uv sync</text>
<rect x="288.5" y="20.5" width="111" height="35" rx="8" fill="var(--nl-ink-950)" stroke="var(--nl-line)"/>
<text x="344" y="42" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--nl-c-plain)" text-anchor="middle">.venv/</text>
</g>
<g v-click>
<rect x="288.5" y="20.5" width="111" height="35" rx="8" fill="var(--nl-ink-950)" stroke="var(--nl-error)" stroke-dasharray="4 4"/>
<text x="344" y="42" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--fg-3)" text-anchor="middle">.venv/</text>
<g stroke="var(--nl-error)" stroke-width="2">
<line x1="300" y1="26" x2="388" y2="50"/>
<line x1="300" y1="50" x2="388" y2="26"/>
</g>
<text x="344" y="72" font-family="var(--nl-sans)" font-size="11.2px" fill="var(--nl-error)" text-anchor="middle">deleted</text>
</g>
<g v-click>
<polyline points="200,56 200,104 280,104" fill="none" stroke="var(--nl-verify)"/>
<path d="M280 100 L286 104 L280 108 Z" fill="var(--nl-verify)"/>
<text x="192" y="108" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--nl-verify)" text-anchor="end">uv sync --locked</text>
<rect x="288.5" y="86.5" width="111" height="35" rx="8" fill="var(--nl-ink-950)" stroke="var(--nl-verify)"/>
<text x="344" y="108" font-family="var(--nl-mono)" font-size="11.2px" fill="var(--nl-c-plain)" text-anchor="middle">.venv/</text>
<text x="344" y="138" font-family="var(--nl-sans)" font-size="11.2px" fill="var(--nl-verify)" text-anchor="middle">rebuilt</text>
</g>
</svg>

</div>

<div v-click style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="branch" /> What goes into Git</div>

<ul class="mt-2" style="font-size: 1.05rem">
<li class="nl-good"><code>pyproject.toml</code> and <code>uv.lock</code></li>
<li class="nl-good"><code>.python-version</code> and your code</li>
<li class="nl-bad"><code>.venv</code>: already in <code>.gitignore</code></li>
</ul>

<code>&#45;&#45;locked</code> refuses to run if <code>uv.lock</code> no longer
matches <code>pyproject.toml</code>.

</div>

</div>

<div class="grid grid-cols-3 gap-6 mt-3">

<div v-click class="col-span-2">

<div class="nl-type"><NlIcon name="terminal" /> macOS, Linux</div>

```bash
uv run python -c "import pandas; print(pandas.__version__)"
rm -rf .venv
uv sync --locked
uv run python -c "import pandas; print(pandas.__version__)"
```

</div>

<div v-click>

<div class="nl-type"><NlIcon name="terminal" /> Windows: instead of rm</div>

```powershell
Remove-Item -Recurse -Force .venv
```

</div>

</div>

<div v-click class="nl-statement mt-3">
Share the recipe: <code>uv.lock</code> rebuilds the same packages
</div>

<div class="nl-live"><span><span class="nl-logo nl-logo--vscode" /> Live in VS Code</span></div>

<!--
SLIDE 18 - Reproducibility
On screen ~70 seconds, live in the VS Code terminal. This slide carries the
chapter's payoff. Do not rush. Demo first: the slide shows only its title
until you come back.

Before you start: stop the notebook kernel and JupyterLab (Ctrl+C in its
terminal). A running kernel uses the Python inside .venv, and on Windows it
locks those files, so the delete fails.

"Je vous avais dit que ce dossier, on pouvait le jeter. On le jette."

[LIVE]
Type: uv run python -c "import pandas; print(pandas.__version__)"
Expected: 3.0.6. "Notez ce numéro."

Type: rm -rf .venv (Windows: Remove-Item -Recurse -Force .venv)
The folder disappears from the Explorer.

Type: uv sync --locked
Expected: uv recreates .venv and reinstalls pandas and its dependencies,
in a second or two.

Type: uv run python -c "import pandas; print(pandas.__version__)"
Expected: 3.0.6 again. "Le même numéro. pandas n'est pas dans la
bibliothèque standard : s'il s'importe, c'est que .venv a vraiment été
reconstruit."

[BACK]

[CLICK 1]
"Ce qu'on vient de faire, en image : pyproject.toml, uv.lock, .venv."

[CLICK 2]
Point at the crossed-out .venv:
"Le dossier a disparu. pyproject.toml et uv.lock, eux, n'ont pas bougé."

[CLICK 3]
Follow the green arrow from uv.lock down to the new box:
"uv sync --locked reconstruit .venv à partir du fichier de verrouillage."

PAUSE.

Then land the payoff planted on the "It works on my machine" slide:
"Vous vous souvenez de la phrase ? « Ça marche sur ma machine. » Votre
collègue clone le projet, tape uv sync, et il obtient les mêmes versions de
paquets que vous. Son système peut encore être différent ; les paquets,
eux, sont les mêmes."

[CLICK 4]
"On partage la recette : pyproject.toml et uv.lock. Jamais le dossier
.venv ; uv init l'a déjà mis dans le .gitignore."

[CLICK 5]
"Les commandes, pour les retrouver."

[CLICK 6]
"Sous Windows, Remove-Item à la place de rm."

[CLICK 7]
"On partage la recette : uv.lock reconstruit les mêmes paquets."
-->

---
layout: default
class: nl-deck
---

# Setup Pitfalls

<div class="nl-cols mt-4">

<div v-click>

<div class="nl-type nl-bad"><NlIcon name="cross" /> Symptom</div>

<div class="nl-recap mt-2" style="font-size: 1.05rem">
  <div class="n">1</div><div><span class="why"><code>No module named 'pandas'</code></span></div>
  <div class="n">2</div><div><span class="why"><code>externally-managed-environment</code></span></div>
  <div class="n">3</div><div><span class="why">A 100+ MB <code>.venv</code> pushed to GitHub</span></div>
  <div class="n">4</div><div><span class="why">Windows: <code>python</code> opens the Store</span></div>
</div>

</div>

<div v-click>

<div class="nl-type nl-good"><NlIcon name="check" /> Fix</div>

<div class="nl-recap mt-2" style="font-size: 1.05rem">
  <div class="n">1</div><div><span class="why">select <code>.venv</code>, use <code>uv run</code>, or <code>uv add pandas</code></span></div>
  <div class="n">2</div><div><span class="why"><code>uv add</code>, not <code>pip install</code></span></div>
  <div class="n">3</div><div><span class="why">commit <code>uv.lock</code>, ignore <code>.venv</code></span></div>
  <div class="n">4</div><div><span class="why">use <code>uv run python</code></span></div>
</div>

</div>

</div>

<div v-click class="nl-statement mt-4">
When something breaks, first ask: which Python is running?
</div>

<!--
SLIDE 19 - Setup pitfalls
On screen ~55 seconds. Concept slide.

[CLICK 1]
Read the four symptoms as the viewer will meet them, one line each:
"« No module named pandas ». « externally-managed-environment ». Un
dossier .venv énorme sur GitHub. Et sous Windows, python qui ouvre le
Microsoft Store."

PAUSE.

[CLICK 2]
Then the fixes, row by row:

1: "Souvent, pandas est bien installé, mais VS Code ou le terminal utilise
un autre Python que celui du projet. Et si pandas manque vraiment : uv add
pandas. Il l'installe, et il l'inscrit dans pyproject.toml et uv.lock, pour
que le projet s'en souvienne."

2: "Sur Ubuntu ou Debian récents, pip install refuse de toucher au Python
du système. C'est une protection, pas un bug. Utilisez uv add."

3: "Le dossier .venv sur GitHub : une centaine de mégaoctets avec pandas,
et inutile sur une autre machine. On partage uv.lock."

4: "Sous Windows, taper python peut ouvrir le Microsoft Store. C'est un
raccourci de Windows. Passez par uv run python."

[CLICK 3]
"Quand quelque chose casse, la première question, c'est : quel Python est
en train de tourner ?"
-->

---
layout: default
class: nl-deck
---

# Your Turn

<div class="nl-cols mt-4">

<div v-click>

<div class="nl-type"><NlIcon name="terminal" /> Four steps, on your own</div>

<div class="nl-recap mt-2" style="font-size: 1.05rem">
  <div class="n">1</div><div><span class="why">create a project with <code>uv init</code></span></div>
  <div class="n">2</div><div><span class="why">write a script, run it with <code>uv run</code></span></div>
  <div class="n">3</div><div><span class="why">add a package with <code>uv add</code></span></div>
  <div class="n">4</div><div><span class="why">delete <code>.venv</code>, then <code>uv sync --locked</code></span></div>
</div>

</div>

<div v-click style="font-size: 1.1rem">

<div class="nl-type"><NlIcon name="check" /> Done when</div>

<ul class="mt-2" style="font-size: 1.05rem">
<li class="nl-good">The script runs with <code>.venv</code>'s Python</li>
<li class="nl-good">The package is in <code>pyproject.toml</code> and <code>uv.lock</code></li>
<li class="nl-good">After the rebuild, the package still imports</li>
</ul>

</div>

</div>

<div v-click class="nl-statement mt-4">
Rebuild it once yourself before you share it
</div>

<!--
SLIDE 20 - Challenge
On screen ~40 seconds. No live coding: this one is for the viewer.

"Avant la prochaine vidéo, un défi. Mettez sur pause et faites-le seul."

[CLICK 1]
Walk the four steps, one sentence each:
"Un projet avec uv init. Un script, lancé avec uv run. Un paquet de votre
choix avec uv add, par exemple rich. Puis vous supprimez .venv, et vous le
reconstruisez avec uv sync --locked."

PAUSE.

[CLICK 2]
Point at the last line:
"Le vrai test, c'est celui-là : après la reconstruction, l'import du
paquet marche encore. Un script qui affiche du texte ne prouve pas que
l'environnement est revenu."

[CLICK 3]
"Reconstruisez-le une fois vous-même avant de le partager."
-->

---
layout: end
class: nl-deck
---

# Thanks for watching

The full code is in the description

<div class="nl-next">

Next video · Tuesday
<strong>CHAPTER 02 — SYNTAX &amp; DATA TYPES</strong>

</div>

<!--
SLIDE 21 - Closing card
On screen ~12 seconds.
Say the next chapter's topic out loud while this is up. Then: "À mardi."
Hold two beats of silence before you stop recording.
-->
