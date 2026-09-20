# Google Labs DESIGN.md Specification

Source: https://github.com/google-labs-code/design.md

DESIGN.md is a self-contained, plain-text representation of a design system. It defines the visual identity of a brand and product, ensuring stylistic choices are consistently followed across design sessions and AI coding agents.

## Structure

1. **YAML Front Matter**: Machine-readable design tokens.
2. **Markdown Body**: Human-readable design rationale and guidance.

## Canonical Section Order

1. **Overview** (or "Brand & Style")
2. **Colors**
3. **Typography**
4. **Layout** (or "Layout & Spacing")
5. **Elevation & Depth** (or "Elevation")
6. **Shapes**
7. **Components**
8. **Do's and Don'ts**

## Token Groups

- `colors`: Key-value pairs of CSS color strings (`#hex`, `rgb()`, `oklch()`, etc.)
- `typography`: Objects with `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`, `fontFeature`, `fontVariation`.
- `rounded`: Scale levels (`sm`, `md`, `lg`, `full`) mapped to dimensions.
- `spacing`: Scale levels mapped to dimensions or numbers.
- `components`: Component tokens with properties like `backgroundColor`, `textColor`, `rounded`, `padding`, `size`, `height`, `width`.
- `omitted`: Sections intentionally skipped to silence linter warnings.
