---
name: design-md
description: >-
  Google Labs DESIGN.md specification and design system skill.
  Provides guidelines, token schemas, linting workflows, and export tools
  to maintain persistent visual identity, WCAG accessibility compliance,
  and token consistency across Web and Mobile UI components.
---

# Google Labs DESIGN.md Skill

This skill equips the agent to create, validate, lint, and enforce `DESIGN.md` files based on the official Google Labs specification (`https://github.com/google-labs-code/design.md`).

## Core Capabilities

1. **Design Token Authoring**: Create `DESIGN.md` containing machine-readable YAML front matter (colors, typography, rounded, spacing, components) and human-readable design rationale prose.
2. **Linting & Validation**: Validate design tokens against the canonical specification, ensuring WCAG AA contrast ratio compliance (>4.5:1 for normal text), checking for broken token references, and enforcing proper section ordering.
3. **Exporting**: Export tokens to Tailwind v3 (`json-tailwind`), Tailwind v4 (`css-tailwind`), and W3C DTCG (`dtcg`) format.
4. **Visual Drift Prevention**: Apply defined design tokens consistently across all Web (React, Vue, HTML/CSS), Mobile (Flutter, React Native), and UI stylesheets.

## Canonical Section Order

When authoring `DESIGN.md`, sections must appear in this order:
1. `## Overview` (or `## Brand & Style`)
2. `## Colors`
3. `## Typography`
4. `## Layout` (or `## Layout & Spacing`)
5. `## Elevation & Depth` (or `## Elevation`)
6. `## Shapes`
7. `## Components`
8. `## Do's and Don'ts`

## Token Schema Reference

```yaml
---
version: alpha
name: ModernDesignSystem
description: Design system specification for modern web applications
colors:
  primary: "#1E3A8A"
  on-primary: "#FFFFFF"
  secondary: "#0F172A"
  surface: "#FFFFFF"
  background: "#F8FAFC"
  accent: "#2563EB"
  text-main: "#0F172A"
  text-muted: "#64748B"
  border: "#E2E8F0"
  danger: "#DC2626"
  warning: "#EAB308"
  success: "#16A34A"
typography:
  h1:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 2.25rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 1.5rem
    fontWeight: 600
    lineHeight: 1.3
  body-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.5
  label-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 0.875rem
    fontWeight: 500
rounded:
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: 10px 18px
  card:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
---
```

## CLI Usage

```bash
# Lint a DESIGN.md file
npx @google/design.md lint DESIGN.md

# Compare two design versions
npx @google/design.md diff DESIGN.md DESIGN-v2.md

# Export to Tailwind CSS
npx @google/design.md export --format css-tailwind DESIGN.md
```

## Best Practices for UI Design

1. **Hierarchy & Intent**: Always write descriptive prose explaining *why* colors and font pairings were selected.
2. **WCAG Compliance**: Ensure contrast ratio between text (`textColor`) and surface (`backgroundColor`) is at least 4.5:1 for standard text and 3:1 for large text.
3. **Consistency**: Use token references (`{colors.primary}`) in component definitions to keep the design system unified.
