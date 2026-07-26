---
layout: post
title: "4 years of Sniffnet"
share-title: "4 years of Sniffnet"
nav-title: News
thumbnail-img: /assets/img/post/fourth-anniversary/cover.png
tags: [anniversary]
github-discussion: XXX
---

<!-- ═══════════════════ INTRO ═══════════════════ -->
<!-- Opening paragraphs: mark the 4-year milestone, set the tone, invite the reader in. -->

_Placeholder: write the intro here — a warm opening about reaching 4 years of Sniffnet, what the project has become, and what this post covers._

<!-- (the interactive scrubber below — leave the widget markup intact) -->
<style>
.evo * { box-sizing: border-box; }
.evo { margin: 2.2em 0; }
/* shared 16:10 frame */
.evo-frame {
  /* padding-bottom hack keeps the 16:10 box in EVERY browser (no aspect-ratio dependency) */
  position:relative; width:100%; height:0; padding-bottom:62.5%; background:#13141a;
  border-radius:14px; overflow:hidden; box-shadow:0 6px 24px rgba(0,0,0,.28);
}
.evo-frame img { position:absolute; top:0; right:0; bottom:0; left:0; width:100%; height:100%; object-fit:contain; display:block; }

/* ---- continuous scrubber ---- */
/* track + labels are narrower than the frame and centered, so it's a short drag end-to-end */
.evo-ticks { display:flex; justify-content:space-between; font-size:.72em; opacity:.6;
  padding:0 2px; margin:.1em auto 0; width:70%; max-width:440px; }
.cscrub-stage .cs-layer { will-change:opacity; } /* opacity set by JS; DOM order stacks top layer above */
.cscrub-track { position:relative; height:34px; margin:1.1em auto 0; width:70%; max-width:440px;
  cursor:pointer; touch-action:none; }
.cscrub-rail { position:absolute; top:50%; left:0; right:0; height:6px; transform:translateY(-50%);
  background:rgba(128,128,128,.3); border-radius:3px; }
.cscrub-fill { position:absolute; top:50%; left:0; height:6px; transform:translateY(-50%);
  background:#6c5ce7; border-radius:3px; width:0; }
.cscrub-ticks { position:absolute; top:0; right:0; bottom:0; left:0; }
.cscrub-ticks span { position:absolute; top:50%; width:2px; height:12px; transform:translate(-50%,-50%);
  background:rgba(128,128,128,.6); border-radius:1px; }
.cscrub-handle { position:absolute; top:50%; left:0; width:26px; height:26px; transform:translate(-50%,-50%);
  background:#fff; border:3px solid #6c5ce7; border-radius:50%; box-shadow:0 2px 8px rgba(0,0,0,.4);
  cursor:grab; z-index:2; }
.cscrub-handle:active { cursor:grabbing; }
.cscrub-track:focus-visible { outline:none; }
.cscrub-track:focus-visible .cscrub-handle { box-shadow:0 0 0 4px rgba(108,92,231,.4); }

/* ---- tabs ---- */
.evo-tabs { display:flex; flex-wrap:wrap; align-items:center; margin-bottom:1em; }
.evo-tabs-label { margin:0 .5em .5em 0; font-size:.9em; font-weight:600; opacity:.7; }
.evo-tab {
  border:1px solid rgba(128,128,128,.35); background:transparent; color:inherit;
  padding:.45em 1em; border-radius:20px; cursor:pointer; font-size:.9em; font-weight:600;
  margin:0 .5em .5em 0; /* child margins instead of flex gap → spacing works in every browser */
}
.evo-tab.active { background:#6c5ce7; color:#fff; border-color:#6c5ce7; }
</style>

<p>Drag the handle to travel through Sniffnet's releases, and switch tabs to follow how each part of the app has evolved.</p>

<div class="evo" id="evo-tabbed">
  <div class="evo-tabs">
    <span class="evo-tabs-label">Page:</span>
    <button type="button" class="evo-tab active" data-view="initial">Initial</button>
    <button type="button" class="evo-tab" data-view="overview">Overview</button>
    <button type="button" class="evo-tab" data-view="inspect">Inspect</button>
    <button type="button" class="evo-tab" data-view="notifications">Notifications</button>
  </div>
  <div class="evo-frame cscrub-stage"></div>
  <div class="cscrub-track" tabindex="0" role="slider" aria-label="Version scrubber">
    <div class="cscrub-rail"></div>
    <div class="cscrub-fill"></div>
    <div class="cscrub-ticks"></div>
    <div class="cscrub-handle"></div>
  </div>
  <div class="evo-ticks"></div>
</div>

<hr>

<!-- ═══════════════════ MAIN BODY ═══════════════════ -->
<!-- Write your article below in plain Markdown. Reorder, rename, add, or drop -->
<!-- any of these sections freely — they're just scaffolding to fill in.       -->

## A look back

_Placeholder: the story of the past year (or the whole 4 years) — key milestones, releases, turning points. Reference the scrubber above to tie the visuals to the narrative._

## What's new in the latest release

_Placeholder: highlight the headline features/changes of the newest version (v1.5). Screenshots, before/after, why it matters to users._

## By the numbers

_Placeholder: stats worth celebrating — downloads, GitHub stars, commits, contributors, releases. (These mirror the video end card: 500k+ downloads, 40k+ stars, 3k+ commits, 70+ contributors, 18 releases.)_

## Thank you

_Placeholder: thank contributors, sponsors, translators, and the community. Link the repo, sponsor page, and discussions._

## What's next

_Placeholder: a look ahead — roadmap, upcoming features, how people can get involved._

<hr>

<script>
(function(){
  var BASE = "{{ '/assets/img/post/fourth-anniversary/' | relative_url }}";
  var VIEWS = {
    initial:       { label:'Initial',        versions:['v1.0','v1.1','v1.2','v1.3','v1.4','v1.5'] },
    overview:      { label:'Overview',       versions:['v1.0','v1.1','v1.2','v1.3','v1.4','v1.5'] },
    inspect:       { label:'Inspect',        versions:['v1.2','v1.3','v1.4','v1.5'] },
    notifications: { label:'Notifications',  versions:['v1.1','v1.2','v1.3','v1.4','v1.5'] }
  };
  var src = function(view, v){ return BASE + view + '-' + v + '.png'; };

  /* ---- continuous crossfade scrubber (shared component) ---- */
  function buildScrubber(root){
    var stage  = root.querySelector('.cscrub-stage');
    var track  = root.querySelector('.cscrub-track');
    var fill   = root.querySelector('.cscrub-fill');
    var handle = root.querySelector('.cscrub-handle');
    var ticksT = root.querySelector('.cscrub-ticks');
    var ticksL = root.querySelector('.evo-ticks');
    var view, vers, t = 0, dragging = false, raf = 0, preloaded = {};

    // Two persistent layers: bottom always shows the "from" frame fully opaque,
    // top fades in the "to" frame. The stage is never emptied, so no dark ever shows.
    var bottom = document.createElement('img'); bottom.className = 'cs-layer';
    var top    = document.createElement('img'); top.className = 'cs-layer';
    stage.appendChild(bottom); stage.appendChild(top); // top last => stacks above
    var botIdx = -1, topIdx = -1;
    function setLayer(layer, curIdx, wantIdx){
      if(curIdx !== wantIdx) layer.src = src(view, vers[wantIdx]);
      return wantIdx;
    }

    var FADE_MARGIN = 0.3; // dead zone near each point: frame stays crisp, fade only in the middle gap
    function render(){
      var max = vers.length - 1;
      var base = Math.max(0, Math.min(Math.floor(t), max)), frac = t - base;
      var next = Math.min(base + 1, max);
      // hold at the current frame for FADE_MARGIN on each side, crossfade only in between
      var blend = frac <= FADE_MARGIN ? 0
                : frac >= 1 - FADE_MARGIN ? 1
                : (frac - FADE_MARGIN) / (1 - 2 * FADE_MARGIN);
      botIdx = setLayer(bottom, botIdx, base); bottom.style.opacity = 1;
      topIdx = setLayer(top, topIdx, next);    top.style.opacity = (next === base ? 0 : blend);
      var p = max > 0 ? t / max * 100 : 0;
      fill.style.width = p + '%';
      handle.style.left = p + '%';
      track.setAttribute('aria-valuenow', Math.round(t));
      track.setAttribute('aria-valuetext', vers[Math.round(t)]);
    }
    function animateTo(target){
      cancelAnimationFrame(raf);
      var start = t, t0 = null;
      raf = requestAnimationFrame(function loop(ts){
        if(t0 === null) t0 = ts;
        var k = Math.min(1, (ts - t0) / 260);
        k = k < .5 ? 2*k*k : 1 - Math.pow(-2*k + 2, 2) / 2; // easeInOutQuad
        t = start + (target - start) * k;
        render();
        if(k < 1) raf = requestAnimationFrame(loop);
      });
    }
    function posFromClientX(clientX){
      var r = track.getBoundingClientRect();
      var x = clientX - r.left;
      return Math.max(0, Math.min(1, x / r.width)) * (vers.length - 1);
    }
    function onDrag(clientX){ t = posFromClientX(clientX); render(); }
    // Mouse + touch instead of Pointer Events: works in every browser/OS, no feature gaps.
    // move/up bind to document so a drag keeps tracking even when the cursor leaves the track.
    track.addEventListener('mousedown', function(e){ dragging = true; cancelAnimationFrame(raf); onDrag(e.clientX); e.preventDefault(); track.focus(); });
    document.addEventListener('mousemove', function(e){ if(dragging) onDrag(e.clientX); });
    document.addEventListener('mouseup',   function(){ dragging = false; });
    // touch: preventDefault stops the page from scrolling while dragging the handle
    track.addEventListener('touchstart', function(e){ dragging = true; cancelAnimationFrame(raf); onDrag(e.touches[0].clientX); e.preventDefault(); }, {passive:false});
    track.addEventListener('touchmove',  function(e){ if(dragging){ onDrag(e.touches[0].clientX); e.preventDefault(); } }, {passive:false});
    document.addEventListener('touchend',    function(){ dragging = false; });
    document.addEventListener('touchcancel', function(){ dragging = false; });
    track.addEventListener('keydown', function(e){
      if(e.key === 'ArrowRight' || e.key === 'ArrowUp'){ e.preventDefault(); animateTo(Math.min(vers.length-1, Math.round(t)+1)); }
      else if(e.key === 'ArrowLeft' || e.key === 'ArrowDown'){ e.preventDefault(); animateTo(Math.max(0, Math.round(t)-1)); }
    });

    function load(v){
      cancelAnimationFrame(raf); // stop any in-flight arrow-key animation from the previous view
      view = v; vers = VIEWS[v].versions;
      // preload every frame for this view so src swaps during a drag are instant (no flash)
      vers.forEach(function(ver){
        var key = view + ver;
        if(!preloaded[key]){ var im = new Image(); im.src = src(view, ver); preloaded[key] = im; }
      });
      botIdx = -1; topIdx = -1; // force both layers to re-point at the new view
      bottom.alt = VIEWS[v].label;
      top.alt = VIEWS[v].label;
      ticksT.innerHTML = vers.map(function(_, i){
        var p = vers.length > 1 ? i / (vers.length - 1) * 100 : 0;
        return '<span style="left:' + p + '%"></span>';
      }).join('');
      ticksL.innerHTML = vers.map(function(ver){ return '<span>' + ver + '</span>'; }).join('');
      track.setAttribute('aria-valuemin', 0);
      track.setAttribute('aria-valuemax', vers.length - 1);
      t = 0; render();
    }
    return { load: load };
  }

  /* ---- tabbed continuous scrubber ---- */
  (function(){
    var root = document.getElementById('evo-tabbed');
    if(!root) return;
    var sc = buildScrubber(root);
    root.querySelectorAll('.evo-tab').forEach(function(btn){
      btn.addEventListener('click', function(){
        root.querySelectorAll('.evo-tab').forEach(function(b){ b.classList.remove('active'); });
        btn.classList.add('active');
        sc.load(btn.dataset.view);
      });
    });
    sc.load('initial');
  })();
})();
</script>