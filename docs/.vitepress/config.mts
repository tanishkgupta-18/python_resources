import { defineConfig } from 'vitepress'

// Determine base path for deployment: default to repository name on GitHub Pages
const base = process.env.BASE_PATH || (process.env.GITHUB_ACTIONS ? '/python_resources/' : '/')

export default defineConfig({
  title: "devhum",
  titleTemplate: ":title | devhum",
  description: "A developer's knowledge platform solely dedicated to Python programming, language architecture, and clean code.",
  base: base,
  lang: 'en-US',
  cleanUrls: true,
  lastUpdated: true,

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: `${base}favicon.svg` }],
    ['link', { rel: 'alternate icon', type: 'image/svg+xml', href: `${base}logo.svg` }],
    ['meta', { name: 'theme-color', content: '#2563eb' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:site_name', content: 'devhum' }],
    ['meta', { property: 'og:title', content: 'devhum | Learn. Build. Share.' }],
    ['meta', { property: 'og:description', content: "A developer's knowledge platform solely dedicated to Python programming, language architecture, and clean code." }],
    ['meta', { property: 'og:image', content: `https://tanishkgupta-18.github.io/python_resources/og-image.png` }],
    ['meta', { property: 'og:image:width', content: '1200' }],
    ['meta', { property: 'og:image:height', content: '630' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: 'devhum | Learn. Build. Share.' }],
    ['meta', { name: 'twitter:description', content: "A developer's knowledge platform solely dedicated to Python programming, language architecture, and clean code." }],
    ['meta', { name: 'twitter:image', content: `https://tanishkgupta-18.github.io/python_resources/og-image.png` }],
  ],

  themeConfig: {
    siteTitle: 'devhum',
    logo: '/logo.svg',

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Python Series', link: '/python/' },
      {
        text: 'Topics',
        items: [
          {
            text: 'Fundamentals',
            items: [
              { text: 'Python Essentials', link: '/python/essentials' },
              { text: 'Numbers & Math', link: '/python/numbers' },
              { text: 'Strings', link: '/python/strings' },
              { text: 'Logic & Operators', link: '/python/operators' },
            ]
          },
          {
            text: 'Control Flow & Functions',
            items: [
              { text: 'Conditional Statements', link: '/python/conditionals' },
              { text: 'Loops & Iteration', link: '/python/loops' },
              { text: 'Functions & Scope', link: '/python/functions' },
            ]
          },
          {
            text: 'Data Structures',
            items: [
              { text: 'Lists & Comprehensions', link: '/python/lists' },
              { text: 'Tuples & Sets', link: '/python/tuples-and-sets' },
              { text: 'Dictionaries', link: '/python/dictionaries' },
            ]
          },
          {
            text: 'Object-Oriented Programming',
            items: [
              { text: 'OOP in Python', link: '/python/oops' },
            ]
          }
        ]
      },
      { text: 'About', link: '/about' }
    ],

    sidebar: {
      '/python/': [
        {
          text: 'Getting Started',
          collapsed: false,
          items: [
            { text: 'Overview & Roadmap', link: '/python/' },
            { text: 'Python Essentials', link: '/python/essentials' },
          ]
        },
        {
          text: 'Core Data Types & Logic',
          collapsed: false,
          items: [
            { text: 'Numbers & Arithmetic', link: '/python/numbers' },
            { text: 'Strings & Text Processing', link: '/python/strings' },
            { text: 'Logic & Operators', link: '/python/operators' },
            { text: 'Conditional Statements', link: '/python/conditionals' },
          ]
        },
        {
          text: 'Control Flow & Functions',
          collapsed: false,
          items: [
            { text: 'Loops & Iteration', link: '/python/loops' },
            { text: 'Functions & Scope', link: '/python/functions' },
          ]
        },
        {
          text: 'Data Structures',
          collapsed: false,
          items: [
            { text: 'Lists & Comprehensions', link: '/python/lists' },
            { text: 'Tuples & Sets', link: '/python/tuples-and-sets' },
            { text: 'Dictionaries', link: '/python/dictionaries' },
          ]
        },
        {
          text: 'Object-Oriented Python',
          collapsed: false,
          items: [
            { text: 'Object-Oriented Programming (OOP)', link: '/python/oops' },
          ]
        }
      ]
    },

    socialLinks: [
      {
        icon: {
          svg: '<svg role="img" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><title>LinkedIn</title><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>'
        },
        link: 'https://www.linkedin.com/in/tanishk-gupta18/'
      }
    ],

    search: {
      provider: 'local'
    },

    footer: {
      message: 'devhum — The Python Developer Knowledge Base.',
      copyright: 'Copyright © 2026 Tanishk Gupta. All rights reserved.'
    },

    docFooter: {
      prev: 'Previous topic',
      next: 'Next topic'
    },

    outline: {
      level: [2, 3],
      label: 'On this page'
    }
  }
})
