<!--
  Stroke pictograms, drawn rather than borrowed.

  Two reasons they are not icon-font glyphs: JetBrains Mono has no coverage
  for symbols like ✉ or ☎, so those fall back to the system emoji font and
  render full-colour and off-weight at 1080p. And these are drawn at the same
  1.4 stroke weight as NlBrand, so the mark and the pictograms read as one set.

  Colour comes from currentColor, so an icon inside .nl-type is bronze and an
  icon inside body text is body-coloured, with no per-use styling.

  Usage:  <NlIcon name="terminal" />   <NlIcon name="mail" :size="14" />
-->
<template>
  <svg
    class="nl-icon"
    :width="size" :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    stroke-width="1.4"
    stroke-linecap="round"
    stroke-linejoin="round"
    aria-hidden="true"
    v-html="path"
  />
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  name: { type: String, required: true },
  size: { type: [Number, String], default: 17 },
})

const PATHS = {
  // structure and flow
  file:      '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/>',
  terminal:  '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9l2.5 2.5L7 14"/><path d="M12.5 14h4.5"/>',
  prompt:    '<path d="M3 7l4 5-4 5"/><path d="M10 7l4 5-4 5"/><path d="M17 7l4 5-4 5"/>',
  arrow:     '<path d="M4 12h15"/><path d="M13 6l6 6-6 6"/>',
  check:     '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.5 2.5L16 9.5"/>',
  download:  '<path d="M12 3v12"/><path d="M7.5 10.5L12 15l4.5-4.5"/><path d="M4 20h16"/>',
  box:       '<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M12 12l8-4.5M12 12v9M12 12L4 7.5"/>',
  layers:    '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
  indent:    '<path d="M4 6h16"/><path d="M9 11h11"/><path d="M13 16h7"/><path d="M4 11v5"/>',
  server:    '<rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="14" width="18" height="6" rx="2"/><path d="M7 7.5h.01M7 17h.01"/>',
  cloud:     '<path d="M7 18h10a4 4 0 0 0 .4-7.98A6 6 0 0 0 5.6 11.2A3.4 3.4 0 0 0 7 18z"/>',
  cells:     '<rect x="3" y="4" width="18" height="6" rx="1.5"/><rect x="3" y="14" width="18" height="6" rx="1.5"/>',
  lock:      '<rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
  split:     '<circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="12" r="2.5"/><path d="M8.5 6.8L15.6 11M8.5 17.2L15.6 13"/>',
  // contact
  play:      '<circle cx="12" cy="12" r="9"/><path d="M10 8.5l6 3.5-6 3.5z"/>',
  mail:      '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5L12 13l8.5-6.5"/>',
  phone:     '<path d="M6 3h3l2 5-2.5 1.5a11 11 0 0 0 5 5L15 12l5 2v3a2 2 0 0 1-2.2 2A16 16 0 0 1 4 5.2A2 2 0 0 1 6 3z"/>',
  branch:    '<circle cx="7" cy="5" r="2.4"/><circle cx="7" cy="19" r="2.4"/><circle cx="17" cy="9" r="2.4"/><path d="M7 7.4v9.2"/><path d="M17 11.4c0 3.2-2.6 4.6-7 4.6"/>',
}

const path = computed(() => PATHS[props.name] ?? PATHS.box)
</script>

<style scoped>
.nl-icon { flex: none; display: inline-block; vertical-align: -0.16em; }
</style>
