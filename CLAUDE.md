# Project Instructions

## Goal
Simple browser game for a child, runs on Samsung S22 via Chrome.

## Constraints
- Single HTML file only (no frameworks, no build tools)
- No external dependencies — inline everything
- Mobile-first: target 360×800px viewport (S22 Chrome)
- Touch events only (no mouse/keyboard logic needed)
- Keep code short and readable — save tokens, avoid over-engineering

## Stack
- Plain HTML + CSS + JavaScript in one file: `index.html`
- No npm, no bundler, no TypeScript

## Code Style
- Short functions, clear names
- Comments only where logic is non-obvious
- No unnecessary abstractions

## Testing
- Open index.html directly in Chrome on S22 to test
- Or use Chrome DevTools → Device toolbar → Galaxy S22 preset

## Token-saving rules for Claude
- Don't explain code unless asked
- Don't add error handling beyond basics
- Don't suggest refactoring unless asked
- Output only the requested change, not the whole file