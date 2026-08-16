<!--
  The closing card.

  Mirrors the cover deliberately: same ink-950 surface, same centred
  composition, mark above the words instead of beside them. The video opens
  and closes on the darkest surface in the system, so the deck reads as a
  bracket rather than as a deck that ran out of slides.

  No corner brand mark here — the centred mark is the brand, and two would be
  the cover mistake all over again.

  Styles are colocated and deliberately NOT scoped: they need to reach
  .slidev-layout.end, and keeping them here means this layout is one file to
  drop in, with no edits to layout.css and no extra import.
-->
<template>
  <div class="slidev-layout end">
    <div class="nl-body">
      <span class="nl-end-mark nl-mark-glyph" />
      <slot />
    </div>
  </div>
</template>

<style>
.slidev-layout.end {
  --bg: var(--nl-ink-950);
  --grid-opacity: 0.035;
}

.slidev-layout.end .nl-body {
  align-items: center;
  justify-content: center;
  text-align: center;
}

.slidev-layout.end .nl-end-mark {
  display: block;
  width: 4.4rem;
  height: 4.4rem;
  margin-bottom: 1.6rem;
}

.slidev-layout.end h1 {
  font-size: 3.2rem;
  font-weight: 600;
  letter-spacing: -0.03em;
  margin-bottom: 0.5rem;
}

.slidev-layout.end p {
  color: var(--fg-2);
  font-size: 1.5rem;
  margin: 0;
}

/* The next-video line: a register entry, not a shout. Mono and muted, because
   the accent on this slide is already spent on the mark. */
.slidev-layout.end .nl-next {
  margin-top: 2.4rem;
  padding-top: 1.4rem;
  border-top: 1px solid var(--hair);
  font-family: var(--nl-mono);
  font-size: 1rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--fg-3);
}

.slidev-layout.end .nl-next strong {
  display: block;
  margin-top: 0.6rem;
  font-family: var(--nl-sans);
  font-size: 1.35rem;
  font-weight: 500;
  letter-spacing: -0.01em;
  text-transform: none;
  color: var(--nl-bone);
}
</style>
