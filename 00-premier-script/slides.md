---
theme: ../themes/noonlabs
title: Votre premier script Python utile
info: NoonLabs - Module I, vidéo 01
layout: cover
transition: fade
mdc: true
---


# NoonLabs

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { duration: 800, ease: 'easeOut' } }"
  class="text-3xl font-semibold mt-16"
>
  Think deeply. Code practically. Build for production.
</div>

<div
  v-motion
  :initial="{ y: 40, opacity: 0 }"
  :enter="{ y: 0, opacity: 0.7, transition: { duration: 800, delay: 400, ease: 'easeOut' } }"
  class="text-xl mt-8 text-center"
>
  From mathematical foundations<br>
  to modern AI systems.
</div>

<!--
SLIDE 1 - Brand stamp
On screen ~4 seconds.
Two animated lines, in this order: Philosophy (the first v-motion block),
then Subtitle (the second). Those two labels were comments in the slide body.

Draft cover, kept verbatim from a commented-out block at the top of this slide:

# NoonLabs

Learn fundamentals, Build or work with modern AI
    Code and AI as written in production


---
layout: default
---
-->
---
layout: default
---



# CSV = Comma-Separated Values

<div class="nl-cols mt-8">

<div>

| date       | description         | montant | categorie   |
|------------|---------------------|---------|-------------|
| 2026-01-01 | La Fontaine         | 13.16   | Restaurant  |
| 2026-01-01 | Carrefour Market    | 5.50    | Courses     |
| 2026-01-01 | Amazon Prime        | 23.62   | Abonnements |
| 2026-01-01 | Brasserie du Nord   | 23.58   | Restaurant  |

<div class="nl-type mt-4">What you see</div>

</div>

<div v-click>

```csv
date,description,montant,categorie
2026-01-01,La Fontaine,13.16,Restaurant
2026-01-01,Carrefour Market,5.50,Courses
2026-01-01,Amazon Prime,23.62,Abonnements
2026-01-01,Brasserie du Nord,23.58,Restaurant
```

<div class="nl-type mt-4">What it really is</div>

</div>

</div>

<div v-click class="nl-statement mt-10">
A table, written as plain text
</div>
<style> .nl-cols > div:first-child table { font-size: 0.5em; } .nl-cols > div:first-child th, .nl-cols > div:first-child td { padding: 0.35em 0.6em; } </style>

<!--
SLIDE 2 - String vs Number  *** MOST IMPORTANT SLIDE ***
On screen ~35 seconds. Appears ~6:15, during the TypeError.
The error message says WHAT broke. This slide says WHY.
Build: title -> str side -> float side -> conversion line.
-->

---
layout: default
---

# Dictionary: key → value

<div class="text-lg opacity-80 mt-4" v-click="1">
A dictionary stores information as pairs: <strong>key → value</strong>
</div>

<div class="nl-cols mt-8" v-click="2">

<div>

```python
{
    'date': '2026-01-01',
    'description': 'La Fontaine',
    'montant': '13.16',
    'categorie': 'Restaurant'
}
```

<div class="nl-type mt-2" v-click="2">Python</div>

</div>


<div v-click>

<div class="nl-kv mt-2" v-click="3">
  <div class="k">'date'</div>
  <div class="arrow">→</div>
  <div class="v">'2026-01-01'</div>

  <div class="k">'description'</div>
  <div class="arrow">→</div>
  <div class="v">'La Fontaine'</div>

  <div class="k">'montant'</div>
  <div class="arrow">→</div>
  <div class="v">'13.16'</div>

  <div class="k">'categorie'</div>
  <div class="arrow">→</div>
  <div class="v">'Restaurant'</div>
</div>

</div>

</div>

<div class="nl-statement mt-10" v-click="4">
Look things up by name (key), not by position
</div>

<style>
.nl-cols > div:nth-child(2) .nl-kv {
  font-size: 0.8em;

  display: grid;
  grid-template-columns: auto 24px auto;

  column-gap: 0.35em;
  row-gap: 0.6em;

  justify-content: start;
  align-items: center;
}

.nl-cols > div:nth-child(2) .nl-kv .k,
.nl-cols > div:nth-child(2) .nl-kv .v {
  font-size: 1em;
}

.nl-cols > div:nth-child(2) .nl-kv .arrow {
  font-size: 0.9em;
  text-align: center;
}
</style>

<!--
SLIDE 3 - What a CSV actually is
On screen ~20 seconds. Appears ~0:55.
This plants "it is just text" so the TypeError lands at 6:00.
Build: table -> equals -> raw text.
-->

---
layout: center
---


# Why `"13.16" + 0`  fails

<div class="nl-cols mt-12">

<div v-click>

<div class="nl-chars">
  <div class="nl-char">1</div>
  <div class="nl-char">3</div>
  <div class="nl-char">.</div>
  <div class="nl-char">1</div>
  <div class="nl-char">6</div>
</div>

<div class="nl-type mt-4">5 characters</div>
<div class="nl-type mt-1"><strong>str</strong></div>

</div>

<div v-click>

<div class="text-center">
  <div class="nl-box">13.16</div>
</div>

<div class="nl-type mt-4">1 number</div>
<div class="nl-type mt-1"><strong>float</strong></div>

</div>

</div>

<div v-click class="nl-statement mt-14">
<code>float("13.16")</code> &nbsp;→&nbsp; 13.16
</div>

<!--
SLIDE 4 - The dictionary
On screen ~25 seconds. Appears ~10:15, when you type totals = {}.
Values are the REAL output of the script - do not invent numbers here.
Build: title -> rows one by one -> bottom line.
-->
---
layout: default
---

# Sorting by Amount

<div class="nl-cols mt-6">

<div>

<div class="nl-type">One pair</div>

<div class="nl-kv mt-3" style="font-size: 1.3rem">
  <div class="k">x[0]</div>
  <div class="arrow">→</div>
  <div class="v">'Logement'</div>

  <div class="k">x[1]</div>
  <div class="arrow">→</div>
  <div class="v">1670.03</div>
</div>

<div class="nl-type mt-6">Biggest first</div>

<div class="nl-recap mt-3" style="font-size: 1.05rem">
  <div class="n">1</div>
  <div><span class="what">Logement</span> &nbsp;<span class="why">1670.03</span></div>

  <div class="n">2</div>
  <div><span class="what">Courses</span> &nbsp;<span class="why">955.33</span></div>

  <div class="n">3</div>
  <div><span class="what">Restaurant</span> &nbsp;<span class="why">880.41</span></div>
</div>

</div>

<div>

<div class="nl-type">The plan</div>

<div class="nl-recap mt-3" style="font-size: 1.05rem">
  <div class="n">1</div>
  <div><span class="what">Pairs</span> &nbsp;<span class="why"><code>.items()</code> turns the dictionary into (name, amount) pairs</span></div>

  <div class="n">2</div>
  <div><span class="what">Compare</span> &nbsp;<span class="why">a <code>lambda</code> picks the amount, <code>x[1]</code></span></div>

  <div class="n">3</div>
  <div><span class="what">Flip</span> &nbsp;<span class="why"><code>reverse=True</code> puts the biggest first</span></div>

  <div class="n">4</div>
  <div><span class="what">Unpack</span> &nbsp;<span class="why">one variable for the name, one for the amount</span></div>
</div>

</div>

</div>

<div v-click class="nl-statement mt-4">
Sort by the amount, not by the name
</div>

<!--
SLIDE 5 - Sorting by amount
On screen ~45 seconds. Concept slide: show it just before you type the sorted() loop in VS Code.
Values are the REAL output of the script - do not invent numbers here.
Point at the pair on the left first, then walk the plan on the right top to bottom.
"Notre dictionnaire est dans l'ordre où les catégories sont apparues. Nous, on veut la plus grosse dépense en premier."
"`.items()` transforme le dictionnaire en paires : le nom de la catégorie, et son total."
"Dans une paire, `x[0]` c'est le nom, `x[1]` c'est le montant."
"Une `lambda`, c'est une mini-fonction : on lui donne une paire, elle rend le montant. C'est ça que `sorted` va comparer."
"`reverse=True` : du plus grand au plus petit."
"Et dans la boucle, on découpe chaque paire en deux variables : `categorie` et `montant`."
Point at the left column: Logement comes first, at 1670.03.
PAUSE.
[CLICK]
"On trie par le montant, pas par le nom. Maintenant, on l'écrit."
-->

---
layout: default
---


# What you just used

<div class="nl-recap mt-10">
  <div class="n" v-click="1">1</div>
  <div v-click="1"><span class="what">Variables</span> &nbsp;<span class="why">store your data</span></div>

  <div class="n" v-click="2">2</div>
  <div v-click="2"><span class="what">Loops</span> &nbsp;<span class="why">repeat over 247 rows</span></div>

  <div class="n" v-click="3">3</div>
  <div v-click="3"><span class="what">Conditions</span> &nbsp;<span class="why">filter</span></div>

  <div class="n" v-click="4">4</div>
  <div v-click="4"><span class="what">Dictionaries</span> &nbsp;<span class="why">group</span></div>

  <div class="n" v-click="5">5</div>
  <div v-click="5"><span class="what">Type conversion</span> &nbsp;<span class="why">str → float</span></div>

  <div class="n" v-click="6">6</div>
  <div v-click="6"><span class="what">f-strings</span> &nbsp;<span class="why">format the output</span></div>
</div>

<div v-click="7" class="nl-statement mt-12">
Everything else in Python builds on this
</div>

<!--
SLIDE 6 - Recap
On screen ~45 seconds. Appears at 15:35.
One line revealed per concept as you name it.
This is the most screenshot-able moment in the video.
-->

---
layout: end
---

# Thanks for watching

The full code is in the description

<div class="nl-recap mt-12">


  <strong>  See you in the next video</strong>
</div>
 
<div class="nl-recap mt-12">
 <strong> Set up a python project like a pro</strong>

</div>

<!--
SLIDE 7 - Closing card
On screen ~12 seconds. Appears at ~17:30.
Say the next video's topic out loud while this is up - the line on screen
is the reminder, your voice is the reason they come back.
Then: "À mardi." Hold two beats of silence before you stop recording,
so the editor has room to fade.
-->
