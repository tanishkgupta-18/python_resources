---
layout: home

hero:
  name: "HumDev"
  text: "Learn. Build. Share."
  tagline: "A developer's knowledge space for exploring technology, understanding engineering concepts and sharing what I build."
  actions:
    - theme: brand
      text: Explore Python Series →
      link: /python/
    - theme: alt
      text: About HumDev
      link: /about

features:
  - icon: 🧠
    title: Learn Fundamental Concepts
    details: Deconstruct language mechanics, execution models, and algorithmic fundamentals through crisp, concept-first notes.
  - icon: ⚙️
    title: Build with Real Code
    details: Every concept is paired with tested, executable code snippets, expected outputs, and common engineering trade-offs.
  - icon: 🚀
    title: Share in Public
    details: Curated as a living engineering repository and digital garden, designed for fast reference and continuous learning.
---

<div class="vp-doc" style="max-width: 1152px; margin: 0 auto; padding: 1.5rem 1.5rem 3rem 1.5rem;">

<div class="pub-section-header">
  <div>
    <span class="track-active">● Active Knowledge Series</span>
    <h2 style="margin-top: 0.5rem !important;">Python Language Architecture</h2>
  </div>
  <span>10 Comprehensive Modules • From Essentials to Internals</span>
</div>

<p style="color: var(--vp-c-text-2); font-size: 1.05rem; margin-top: 0.25rem;">
  A structured, modular learning path exploring Python's syntax, memory model, functional constructs, and standard data structures.
</p>

<div class="topics-grid">

  <a class="topic-card" href="./python/essentials">
    <div>
      <div class="topic-card-header">
        <span class="topic-badge">Module 01</span>
        <span style="font-size: 0.75rem; color: var(--vp-c-text-3);">Basics</span>
      </div>
      <h3>Python Essentials</h3>
      <p>Terminal I/O, string formatting, escape sequences (<code>\"</code>, <code>\t</code>), multi-argument printing, and <code>NoneType</code> semantics.</p>
    </div>
    <div class="topic-card-footer">Read Module →</div>
  </a>

  <a class="topic-card" href="./python/numbers">
    <div>
      <div class="topic-card-header">
        <span class="topic-badge">Module 02</span>
        <span style="font-size: 0.75rem; color: var(--vp-c-text-3);">Numeric</span>
      </div>
      <h3>Numbers & Arithmetic</h3>
      <p>Explicit type casting, true division (<code>/</code>) vs floor division (<code>//</code>), exponentiation, <code>math</code>, and Banker's rounding.</p>
    </div>
    <div class="topic-card-footer">Read Module →</div>
  </a>

  <a class="topic-card" href="./python/strings">
    <div>
      <div class="topic-card-header">
        <span class="topic-badge">Module 03</span>
        <span style="font-size: 0.75rem; color: var(--vp-c-text-3);">Sequences</span>
      </div>
      <h3>Strings & Text Processing</h3>
      <p>Modern f-strings, stride slicing (<code>[start:end:step]</code>), whitespace stripping, substring search, and character validation.</p>
    </div>
    <div class="topic-card-footer">Read Module →</div>
  </a>

  <a class="topic-card" href="./python/operators">
    <div>
      <div class="topic-card-header">
        <span class="topic-badge">Module 04</span>
        <span style="font-size: 0.75rem; color: var(--vp-c-text-3);">Logic</span>
      </div>
      <h3>Logic & Operators</h3>
      <p>Truthiness, chained comparisons (<code>1 &lt; x &lt; 5</code>), operator precedence, membership (<code>in</code>), and identity (<code>is</code> vs <code>==</code>).</p>
    </div>
    <div class="topic-card-footer">Read Module →</div>
  </a>

  <a class="topic-card" href="./python/conditionals">
    <div>
      <div class="topic-card-header">
        <span class="topic-badge">Module 05</span>
        <span style="font-size: 0.75rem; color: var(--vp-c-text-3);">Branching</span>
      </div>
      <h3>Conditional Statements</h3>
      <p>Structured <code>if-elif-else</code> branching, inline ternary expressions, and Python 3.10+ structural pattern matching (<code>match...case</code>).</p>
    </div>
    <div class="topic-card-footer">Read Module →</div>
  </a>

  <a class="topic-card" href="./python/loops">
    <div>
      <div class="topic-card-header">
        <span class="topic-badge">Module 06</span>
        <span style="font-size: 0.75rem; color: var(--vp-c-text-3);">Iteration</span>
      </div>
      <h3>Loops & Iteration</h3>
      <p>Sequence traversal, step-configured <code>range()</code>, loop control (<code>break</code>, <code>continue</code>, <code>pass</code>), <code>for...else</code>, and <code>while</code> loops.</p>
    </div>
    <div class="topic-card-footer">Read Module →</div>
  </a>

  <a class="topic-card" href="./python/functions">
    <div>
      <div class="topic-card-header">
        <span class="topic-badge">Module 07</span>
        <span style="font-size: 0.75rem; color: var(--vp-c-text-3);">Architecture</span>
      </div>
      <h3>Functions & Scope</h3>
      <p>Built-ins vs methods, parameter patterns, positional vs keyword arguments, <code>*args</code>, <code>**kwargs</code>, and modern type hints.</p>
    </div>
    <div class="topic-card-footer">Read Module →</div>
  </a>

  <a class="topic-card" href="./python/lists">
    <div>
      <div class="topic-card-header">
        <span class="topic-badge">Module 08</span>
        <span style="font-size: 0.75rem; color: var(--vp-c-text-3);">Data Structure</span>
      </div>
      <h3>Lists & Comprehensions</h3>
      <p>Dynamic array memory model, unpacking, in-place sort vs <code>sorted()</code>, shallow vs deep copy, iterators, and list comprehensions.</p>
    </div>
    <div class="topic-card-footer">Read Module →</div>
  </a>

  <a class="topic-card" href="./python/tuples-and-sets">
    <div>
      <div class="topic-card-header">
        <span class="topic-badge">Module 09</span>
        <span style="font-size: 0.75rem; color: var(--vp-c-text-3);">Data Structure</span>
      </div>
      <h3>Tuples & Sets</h3>
      <p>Tuple immutability & indexing, set uniqueness, mutations (<code>remove</code> vs <code>discard</code>), set mathematics, and relational operators.</p>
    </div>
    <div class="topic-card-footer">Read Module →</div>
  </a>

  <a class="topic-card" href="./python/dictionaries">
    <div>
      <div class="topic-card-header">
        <span class="topic-badge">Module 10</span>
        <span style="font-size: 0.75rem; color: var(--vp-c-text-3);">Data Structure</span>
      </div>
      <h3>Dictionaries</h3>
      <p>Hash map key immutability, safe access via <code>.get()</code>, view objects (<code>keys</code>, <code>values</code>, <code>items</code>), mutations, and <code>fromkeys</code> initialization.</p>
    </div>
    <div class="topic-card-footer">Read Module →</div>
  </a>

</div>

<!-- Author & Platform Section -->
<hr style="margin: 3.5rem 0 2.5rem 0; border: none; border-top: 1px solid var(--vp-c-divider);" />

<div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 2rem;">
  <div style="flex: 1; min-width: 280px;">
    <h3 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; font-weight: 700;">About the Platform</h3>
    <p style="color: var(--vp-c-text-2); font-size: 0.95rem; line-height: 1.6; margin: 0 0 1rem 0;">
      <strong>HumDev</strong> is authored by <strong>Tanishk Gupta</strong> as an open developer knowledge base. It documents programming fundamentals, system patterns, and practical software engineering experiments.
    </p>
    <a href="./about" style="font-weight: 600; color: var(--vp-c-brand-1);">Read more about HumDev & the author →</a>
  </div>

  <div style="flex: 1; min-width: 280px;">
    <h3 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; font-weight: 700;">Connect & Follow</h3>
    <p style="color: var(--vp-c-text-2); font-size: 0.95rem; line-height: 1.6; margin: 0 0 0.75rem 0;">
      Follow along for regular technical notes, software design patterns, and engineering insights:
    </p>
    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
      <a href="https://www.linkedin.com/in/tanishk-gupta18/" target="_blank" rel="noopener noreferrer" style="font-weight: 600; color: var(--vp-c-brand-1);">
        💼 LinkedIn Profile
      </a>
      <span style="color: var(--vp-c-divider);">•</span>
      <a href="https://github.com/tanishkgupta-18" target="_blank" rel="noopener noreferrer" style="font-weight: 600; color: var(--vp-c-text-1);">
        🐙 GitHub
      </a>
    </div>
  </div>
</div>

</div>
