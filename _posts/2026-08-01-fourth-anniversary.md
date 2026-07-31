---
layout: post
title: "4 years of Sniffnet: the temptation that made it possible"
share-title: "4 years of Sniffnet: the temptation that made it possible"
nav-title: News
thumbnail-img: /assets/img/post/fourth-anniversary/cover.png
tags: [anniversary]
github-discussion: 1262
---

**4 years ago** on this day, I made the very first commit to the Sniffnet GitHub repository and,
as is tradition, today I'd like to celebrate the project's anniversary with a blog post.<br><br>
Usually, the anniversary post is somewhat deep, reflective, and personal: over the past years I've talked about how being a maintainer changed my life,
how important it is to balance Sniffnet development with a full-time job, and how sustainable open source is crucial to ensure a project's longevity.<br><br>
I love discussing such topics because they pull the curtain back and show _the human that's behind the code_, but this year it'll be slightly different.<br>
I think that delicate subjects must come out naturally without forcing them, so rather than repeating myself
with another tear-jerking essay, or letting AI prose fake sentiments in my place,
this time I'd like to take a more lighthearted route, sharing some fun facts and Sniffnet's visual evolution over the years.

<hr>

### <i>"The temptation to make a GUI is strong"</i>

As many of you know, Sniffnet was <a href="{{ 'news/announcing-sniffnet' | relative_url }}">originally</a>
a simple program that could only run from the command line to collect network traffic and print some rudimentary statistics.

At the time I was a student, and I had just taken a Rust course.<br>
I don't know why, it's probably that the Rust language hit me differently or that I was getting into the magic world of networking,
but I felt like there was huge potential to make something way more complete and useful than a primitive terminal interface.

The fact is that on the 20th of October 2022, I wrote this message to the friend I worked with on the first version of Sniffnet CLI:

<div align="center">
<img width="50%" alt="" src="{{ 'assets/img/post/fourth-anniversary/chat.jpeg' | relative_url }}">
</div>

Translated from Italian, the message just says: _"The temptation to make a GUI is strong"_.

Attached to that message there was a short video showing a very early prototype of the graphical interface: a simple counter of the network packets being captured.<br>
It was the first time I saw a window with Sniffnet's name on it, and I'm only sharing the video publicly today.

<div align="center">
    <video class="myShadow" controls muted width="100%" height="auto">
        <source type="video/mp4" src="{{ 'assets/img/post/fourth-anniversary/gui_experiment.mp4' | relative_url }}">
    </video>
</div>

I still remember the excitement I felt when I saw the window appear: in retrospect it was a small step, but at the time it felt like a huge leap.<br>
In fact, initially I didn't even know if it was possible to make a graphical interface in Rust at all.

After some research I found several frameworks that could help me with this, and ultimately I decided to go with <a target="_blank" rel="noopener" href="https://iced.rs">Iced</a>.<br>
My first steps with Iced are still vivid, and I'd never have imagined that 4 years later Sniffnet would be prominently featured on their landing page as one of the most popular tools built with it.

From there things moved quickly, and just a month later, on the 21st of November 2022, I released the first graphical interface as version 1.0.

After all of this time, I was curious to look back at how the interface evolved, so I made a minimal widget that lets you travel through Sniffnet's main pages and releases.

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

### The past 12 months

Let's now shift to recent history.

The past year saw the release of a <a href="{{ 'news/v1.5' | relative_url }}">new major version</a>, which finally brought the long-awaited process identification feature.<br>
Implementing it was quite a <a href="{{ 'news/process-identification' | relative_url }}">challenge</a>, but I can say it was worth it: version 1.5.0 has
been the most successful release of the project so far, with more than 100k downloads in the first two months after its launch.

In addition to 1.5.0, three minor releases were published to introduce more features such as <a href="{{ 'news/remote-notifications' | relative_url }}">remote notifications</a>,
BPF filtering, pausable packet captures, custom IP blacklist support, connection latency measurements,
and signed installers for Windows (shoutout to <a target="_blank" rel="noopener" href="https://signpath.org">SignPath</a> for providing free code signing to Sniffnet).

This year brought the total number of downloads to 530k, with a daily average of 657 downloads that is considerably higher than the previous year's 397 per day.

<div align="center">
<img alt="Downloads over the years" title="Downloads over the years" style="border-radius: 15px" src="{{ 'assets/img/post/fourth-anniversary/downloads.png' | relative_url }}" width="70%"/>
</div>

The GitHub repository has also gained 10k new stars, fewer than last year's 14k, but still a very good result considering that the project is more mature and has been around for a while.<br>
This growth places Sniffnet in the top 0.0002% of all GitHub public repositories (678th<sup><a target="_blank" rel="noopener" title="Source: top1000repos.com" href="https://top1000repos.com/#GyulyVGC/sniffnet">[↗]</a></sup> out of 395 million<sup><a target="_blank" rel="noopener" title="Source: GitHub Octoverse 2025" href="https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/">[↗]</a></sup>): something astonishing to even think about.

<div align="center">
<img alt="GitHub Stars over the years" title="GitHub Stars over the years" style="border-radius: 15px" src="{{ 'assets/img/post/fourth-anniversary/stars.png' | relative_url }}" width="70%"/>
</div>

Along the way I met new contributors who helped package Sniffnet as an AppImage, fixed various bugs, and added four new languages (bringing the total to 26 different translations by native speakers).

Lately I've also had the pleasure of being contacted by <a target="_blank" rel="noopener" href="https://www.recall.ai/?ashby_jid=7b02811e-bc91-4ef2-925d-f56a5acac13b&utm_source=github&utm_medium=sponsorship&utm_campaign=sniffnet">recall.ai</a> and <a target="_blank" rel="noopener" href="https://www.coderabbit.ai">CodeRabbit</a>, two companies that started sponsoring Sniffnet with a recurring monthly donation.

Last but not least, the project also has a new domain and custom email addresses, as <a href="{{ 'news/new-domain' | relative_url }}">announced</a> not long ago.

<hr>

### What's next

If during the past couple of years I found the energy and motivation to keep working on Sniffnet until late at night,
it was largely thanks to the substantial support I received from the European Commission's <a href="{{ 'news/ngi-program' | relative_url }}">Next Generation Internet</a> program.<br>
Unfortunately, nothing lasts forever, and their funding is now coming to an end.

I'll keep maintaining Sniffnet after the funding period, albeit probably not at the pace of the past months:
in these cases _long-term consistency_ beats speed and intensity, keeps burnout at bay, and leaves room to enjoy life as much as development.

The next major release will be version 1.6.0 and will finally make it possible to inspect network traffic from remote machines, firewalls, and routers.<br>
You can already have a look at <a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet-agent"><code>sniffnet-agent</code></a>,
a new companion program that will soon allow you to capture traffic from headless devices and send it to Sniffnet for inspection.

<div align="center">
<a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet-agent"><img width="100%" alt="" title="sniffnet-agent" src="{{ 'assets/img/post/fourth-anniversary/sniffnet-agent.png' | relative_url }}"></a>
</div>

Other exciting features are already in the pipeline, so make sure to
check the complete set of planned items in the usual <a target="_blank" rel="noopener" href="https://whimsical.com/Damodrdfx22V9jGnpHSCGo">Roadmap</a>.

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
