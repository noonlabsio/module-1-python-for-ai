<!--
  The corner brand mark, on every teaching slide.

  The glyph itself lives in styles/nl-mark.css as --nl-mark-src, so this
  component holds no asset data and the cover lockup shares the same
  definition. The name comes from --nl-brand-a / --nl-brand-b in layout.css:
  do not type it in here.
-->
<template>
  <div class="nl-brand" aria-hidden="true">
    <span class="nl-mark nl-mark-glyph" />
    <span class="nl-brand-name"><i class="a" /><i class="b" /></span>
  </div>
</template>

<style scoped>
.nl-mark {
  display: block;
  width: 1.9rem;
  height: 1.9rem;
  flex: none;
}
</style>
