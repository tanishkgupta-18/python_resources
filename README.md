# devhum — Learn. Build. Share.

[![VitePress](https://img.shields.io/badge/VitePress-1.6.4-2563eb?logo=vite&logoColor=white)](https://vitepress.dev/)
[![Node](https://img.shields.io/badge/Node.js-%3E%3D18.0-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![Deploy Documentation](https://github.com/tanishkgupta-18/python_resources/actions/workflows/deploy.yml/badge.svg)](https://github.com/tanishkgupta-18/python_resources/actions/workflows/deploy.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A developer's knowledge platform solely dedicated to Python programming, language architecture, and clean code.

Built with a lightweight, documentation-first architecture using **VitePress**, **Markdown**, and **TypeScript**, ready for deployment to **GitHub Pages**.

---

## 🌟 Live Preview

- **Live Documentation**: [https://tanishkgupta-18.github.io/python_resources/](https://tanishkgupta-18.github.io/python_resources/)
- **Author**: Tanishk Gupta ([LinkedIn](https://www.linkedin.com/in/tanishk-gupta18/) • [GitHub](https://github.com/tanishkgupta-18))

---

## 📚 Curriculum & Topics

All notes, syntax rules, and runnable examples are organized into 11 structured learning modules:

1. [**Python Essentials**](docs/python/essentials.md): User input (`input()`), escape sequences (`\"`, `\\`, `\t`), formatted printing, variable assignment, and `NoneType`.
2. [**Numbers & Arithmetic**](docs/python/numbers.md): Type casting (`int`, `float`, `complex`), floor division (`//`) vs float division (`/`), exponentiation, `math` and `random` modules, and Banker's rounding.
3. [**Strings & Text Processing**](docs/python/strings.md): String interpolation (f-strings), sequence slicing (`[start:end:step]`), trimming (`strip`), search methods, and input validation.
4. [**Logic & Operators**](docs/python/operators.md): Boolean truthiness, chained comparisons, logical operator precedence, membership (`in`), and identity (`is` vs `==`).
5. [**Conditional Statements**](docs/python/conditionals.md): Indented `if-elif-else` branches, ternary inline expressions, and Python 3.10+ structural pattern matching (`match...case`).
6. [**Loops & Iteration**](docs/python/loops.md): Iterator protocol, configurable `range()` steps, loop control (`break`, `continue`, `pass`), `for...else`, and `while` loops.
7. [**Functions & Scope**](docs/python/functions.md): Functions vs object methods, parameter patterns, positional vs keyword arguments, `*args`, `**kwargs`, and type hints.
8. [**Lists & Comprehensions**](docs/python/lists.md): Sequence unpacking (`*`, `_`), aggregations, in-place sorting vs `sorted()`, memory copy models (shallow vs deepcopy), functional tools (`map`, `filter`), and list comprehensions.
9. [**Tuples & Sets**](docs/python/tuples-and-sets.md): Tuple immutability and indexing vs Set uniqueness, mutations (`add`, `remove` vs `discard`), set mathematics (union, intersection, difference), and subset relations.
10. [**Dictionaries**](docs/python/dictionaries.md): Hash map properties, key immutability rules, safe retrieval with `.get()`, dynamic view objects (`keys`, `values`, `items`), and template initialization via `dict.fromkeys`.
11. [**Object-Oriented Programming (OOP)**](docs/python/oops.md): Classes, instances, `self`, constructor mechanics (`__init__`), constructor overloading simulation, 4 pillars (Encapsulation with `@property`, Abstraction with `ABC`, Inheritance & MRO with C3 linearization, Polymorphism), and magic dunder methods.

> [!NOTE]
> All original Python source files (`01_python_essentials.py` through `11_oops.py`) are organized into the dedicated [`python_scripts/`](./python_scripts) folder as runnable standalone scripts.

---

## 🛠️ Tech Stack & Features

- **Documentation Engine**: VitePress (Vue 3 + Vite)
- **Styling**: Minimalist developer aesthetic with subtle blue accents, clean typography, and full dark-mode support.
- **Search**: Built-in, zero-dependency instant local fuzzy search.
- **Code Highlighting**: Syntax highlighting for Python with one-click copy buttons and clear output blocks.
- **Responsive Layout**: Mobile-first responsive sidebar and navigation drawer.
- **Architecture**: Modular Python learning progression.

---

## 🚀 Local Development

### Prerequisites
- [Node.js](https://nodejs.org/) v18.0.0 or higher
- npm (comes bundled with Node.js)

### 1. Clone the repository
```bash
git clone https://github.com/tanishkgupta-18/python_resources.git
cd python_resources
```

### 2. Install dependencies
```bash
npm install
```

### 3. Start local development server
```bash
npm run dev
```
Open [http://localhost:5173](http://localhost:5173) in your browser with hot module replacement (HMR).

### 4. Build for production
```bash
npm run build
```
The static HTML, CSS, and JS output will be generated into `docs/.vitepress/dist`.

### 5. Preview production build locally
```bash
npm run preview
```

---

## 🚢 Deployment to GitHub Pages

This project is configured with a GitHub Actions workflow in `.github/workflows/deploy.yml` that automatically builds and deploys the site whenever commits are pushed to the `main` branch.

### Enabling GitHub Pages in Repository Settings:
1. Navigate to your repository on GitHub: `https://github.com/tanishkgupta-18/python_resources`.
2. Click **Settings** → **Pages** (in the left sidebar).
3. Under **Build and deployment** → **Source**, select **GitHub Actions**.
4. Push a commit to `main` (or run the workflow manually from the **Actions** tab).
5. Your documentation site will be live at `https://tanishkgupta-18.github.io/python_resources/`!

---

## ⚙️ Customization & Personal Branding

All personal branding and navigation settings are configured in `docs/.vitepress/config.mts`:

- **Site Title & Brand**: `title` and `themeConfig.siteTitle`.
- **Social Links**: `themeConfig.socialLinks` for your GitHub and LinkedIn URLs.
- **Navigation**: `themeConfig.nav` and `themeConfig.sidebar`.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
