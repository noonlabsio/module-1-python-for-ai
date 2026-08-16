---
theme: ../themes/noonlabs
title: Votre premier script Python utile
info: NoonLabs - Module I, vidéo 01
class: text-left
transition: fade
mdc: true
---

<!--
SLIDE 1 - Title card
Appears at 0:25. On screen ~5 seconds, while you say
"Bienvenue sur NoonLabs". Nobody reads this - it is a brand stamp.
-->
# NoonLabs

Le code et l'IA comme on les écrit en production

---
layout: default
---


<!--
SLIDE 2 - What a CSV actually is
Appears ~0:55. On screen ~20 seconds.
This plants "it is just text" so the TypeError lands at 6:00.
Build: table -> equals -> raw text.
-->

# CSV = Comma-Separated Values

<div class="nl-cols mt-8">

<div>

| date | montant | categorie |
|------|---------|-----------|
| 01-01 | 13.16 | Restaurant |
| 01-01 | 5.50 | Courses |
| 01-01 | 23.62 | Abonnements |

<div class="nl-type mt-4">What you see</div>

</div>

<div v-click>

```csv
date,montant,categorie
2026-01-01,13.16,Restaurant
2026-01-01,5.50,Courses
2026-01-01,23.62,Abonnements
```

<div class="nl-type mt-4">What it really is</div>

</div>

</div>

<div v-click class="nl-statement mt-10">
A table, written as plain text
</div>

---
layout: center
---

<!--
SLIDE 3 - String vs Number  *** MOST IMPORTANT SLIDE ***
Appears ~6:15, during the TypeError. On screen ~35 seconds.
The error message says WHAT broke. This slide says WHY.
Build: title -> str side -> float side -> conversion line.
-->

# Why `"47.20" + 12` fails

<div class="nl-cols mt-12">

<div v-click>

<div class="nl-chars">
  <div class="nl-char">4</div>
  <div class="nl-char">7</div>
  <div class="nl-char">.</div>
  <div class="nl-char">2</div>
  <div class="nl-char">0</div>
</div>

<div class="nl-type mt-4">5 characters</div>
<div class="nl-type mt-1"><strong>str</strong></div>

</div>

<div v-click>

<div class="text-center">
  <div class="nl-box">47.20</div>
</div>

<div class="nl-type mt-4">1 number</div>
<div class="nl-type mt-1"><strong>float</strong></div>

</div>

</div>

<div v-click class="nl-statement mt-14">
<code>float("47.20")</code> &nbsp;→&nbsp; 47.20
</div>

---
layout: center
---

<!--
SLIDE 4 - The dictionary
Appears ~10:15, when you type totals = {}. On screen ~25 seconds.
Values are the REAL output of the script - do not invent numbers here.
Build: title -> rows one by one -> bottom line.
-->

# Dictionary: key → value

<div class="nl-kv mt-12">
  <div class="k" v-click>"Logement"</div>
  <div class="arrow" v-click>→</div>
  <div class="v" v-click>1670.03</div>

  <div class="k" v-click>"Courses"</div>
  <div class="arrow" v-click>→</div>
  <div class="v" v-click>955.33</div>

  <div class="k" v-click>"Restaurant"</div>
  <div class="arrow" v-click>→</div>
  <div class="v" v-click>880.41</div>

  <div class="k" v-click>"Transport"</div>
  <div class="arrow" v-click>→</div>
  <div class="v" v-click>659.47</div>
</div>

<div v-click class="nl-statement mt-14">
Look things up by name, not by position
</div>

---
layout: default
---

<!--
SLIDE 5 - Recap
Appears at 15:35. On screen ~45 seconds.
One line revealed per concept as you name it.
This is the most screenshot-able moment in the video.
-->

# What you just used

<div class="nl-recap mt-10">
  <div class="n" v-click>1</div>
  <div v-click><span class="what">Variables</span> &nbsp;<span class="why">store your data</span></div>

  <div class="n" v-click>2</div>
  <div v-click><span class="what">Loops</span> &nbsp;<span class="why">repeat over 247 rows</span></div>

  <div class="n" v-click>3</div>
  <div v-click><span class="what">Conditions</span> &nbsp;<span class="why">filter</span></div>

  <div class="n" v-click>4</div>
  <div v-click><span class="what">Dictionaries</span> &nbsp;<span class="why">group</span></div>

  <div class="n" v-click>5</div>
  <div v-click><span class="what">Type conversion</span> &nbsp;<span class="why">str → float</span></div>

  <div class="n" v-click>6</div>
  <div v-click><span class="what">f-strings</span> &nbsp;<span class="why">format the output</span></div>
</div>

<div v-click class="nl-statement mt-12">
Everything else in Python builds on this
</div>
