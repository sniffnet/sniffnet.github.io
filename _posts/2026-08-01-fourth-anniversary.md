---
layout: post
title: "4 years of Sniffnet: the temptation that made it possible"
share-title: "4 years of Sniffnet: the temptation that made it possible"
nav-title: News
thumbnail-img: /assets/img/post/fourth-anniversary/cover.png
tags: [anniversary]
github-discussion: XXX
---

**4 years ago** on this day, I made the very first commit to Sniffnet GitHub repository and,
as it's tradition, today I'd like to celebrate the project's anniversary with a blog post.<br><br>
Usually, the anniversary post is somewhat deep, reflective, and personal: the past years I've talked about how being a maintainer changed my life,
how important is to balance Sniffnet development with a full-time job, and how sustainable open source is crucial to ensure a project's longevity.<br><br>
I love discussing such topics because they help pulling the curtain back and showing the human that's behind the code, but this year it'll be slightly different.<br>
I think that delicate arguments must come out naturally without forcing them, so rather than repeating myself
with another tear-jerking essay, or letting AI prose fake sentiments in my place,
this time I was genuinely curious to visually see how Sniffnet has evolved over all this time as a reminder of the journey I've been through.

<hr>

### <i>"The temptation to make a GUI is strong"</i>

As many of you know, Sniffnet was originally a simple program that could only run from command line to collect network traffic and print some rudimental statistics.<br>
At the time I was a student, I had just followed a Rust course... and I wasn't able to just stop there and move on with the following semester.<br>
I don't know why, it's probably that the Rust language hit me differently or that I was getting into the magic world of network programming, but I felt like there was a huge potential in making something way more complete and useful out of this.<br>
Fact is that on the 20th of October 2022, I wrote this message to the friend I worked with on the first version of Sniffnet CLI:

<div align="center">
<img width="50%" alt="" src="{{ 'assets/img/post/fourth-anniversary/chat.jpeg' | relative_url }}">
</div>

Translated from Italian, it just says: "The temptation to make a GUI is strong".<br>
And well... you know the rest of the story: I started neglecting lectures and sleep (_without any apparent consequence_) to work on what was becoming my new favorite hobby.<br>
What you surely don't know though, is that attached to that message there was a short video that I've never shared publicly so far.

<div align="center">
    <video class="myShadow" controls muted width="100%" height="auto">
        <source type="video/mp4" src="{{ 'assets/img/post/fourth-anniversary/gui_experiment.mp4' | relative_url }}">
    </video>
</div>

The video shows a very early prototype of the graphical interface, which was just a simple counter of the network packets that were being captured.<br>
I remember very well the excitement I felt when I saw a window appear for the first time: in retrospective it was a small step, but it was a huge leap for me at the time.<br>
In fact, initially I didn't even know if it was possible to make a graphical interface in Rust at all.

After some research I found out different frameworks that could help me with this, and ultimately I decided to go with Iced.
I remember very well my first steps with Iced, and I'd have never imagined that 4 years later Sniffnet would be prominently featured on their website landing page as one of the most popular tools built with it.

From there things escalated quickly and just a month later, on the 21st of November, I released the first graphical interface as version 1.0.

After all of this time, I was interested in reviewing the evolution of the interface in a handy way, so I made a simple widget that allows to travel through Sniffnet's main pages and releases.

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

You can use the scrubber to see how the app has become more complete and polished over time.

<hr>

## The past 12 months

Shifting to the recent history, the past year saw the release of a new major version, which among the other things finally brought the long-awaited **process identification** feature.<br>
Implementing it was quite a challenge, but now I can say it was worth it: version 1.5.0 has
been the most successful release of the project so far, with more than 100k downloads in the first 2 months after its launch.<br>

In addition to 1.5.0, three minor releases were published to introduce more features like BPF filtering, remote notifications, pausable packet captures, custom IP blacklists support, connections latency measurements, and signed packages for Windows.<br>

This year brought the total number of downloads to 530k, with a daily average of 650 downloads that is considerably higher than the previous year's 400 per day.

The GitHub repository has also gained 10k new stars, which is lower than the previous year (14k), but still a very good result considering that the project is more mature and has been around for a while.<br>
This further growth today places Sniffnet in the top xx% of all GitHub public repositories (xx out of yy): something astonishing to even think about.

Recently we also met new contributors who helped packaging Sniffnet as AppImage, fixed various bugs, and added 4 new languages (bringing the total to 26 different translations by native speakers).<br>

Last but not least, the project also has a new domain and custom email addresses as announced not long ago.

<hr>

## What's next

If during the past couple years I found the energies and motivation to keep working on Sniffnet until late at night,
it was also thanks to the substantial support I received from European Commission's Next Generation Internet program. <br>
However, their support is now coming to an end.<br>
I'll keep maintaining Sniffnet after the funding period, even if probably not at the pace of the past months:
in these cases long term consistency beats speed and intensity, keeps away from burning out, and allows to enjoy life as much as development.

The next major release will be version 1.6.0. and will finally make it possible to inspect network traffic from remote machines and routers.<br>
You can already give a look at `sniffnet-agent`, a new companion program that will soon allow you to capture traffic from remote devices and send it to Sniffnet for inspection.

The complete set of planned features is already defined and available for consultation in the usual Roadmap.

Until the next blog post, I wish Sniffnet a happy birthday!

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
