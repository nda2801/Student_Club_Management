---
version: alpha
name: StudentClubAIDesignSystem
description: Design system specification for Student Club Management System with AI Integration (Google Labs DESIGN.md spec)
colors:
  primary: "#2563EB"
  primary-hover: "#1D4ED8"
  on-primary: "#FFFFFF"
  secondary: "#4F46E5"
  secondary-hover: "#4338CA"
  accent: "#8B5CF6"
  accent-hover: "#7C3AED"
  background: "#F8FAFC"
  background-dark: "#0B0F19"
  surface: "#FFFFFF"
  surface-dark: "#141D2E"
  surface-secondary: "#F1F5F9"
  surface-secondary-dark: "#1E293B"
  text-main: "#0F172A"
  text-main-dark: "#F8FAFC"
  text-secondary: "#334155"
  text-secondary-dark: "#CBD5E1"
  text-muted: "#64748B"
  text-muted-dark: "#94A3B8"
  border: "#E2E8F0"
  border-dark: "#243048"
  border-input: "#CBD5E1"
  border-input-dark: "#334155"
  danger: "#EF4444"
  danger-soft: "#FEF2F2"
  warning: "#F59E0B"
  warning-soft: "#FFFBEB"
  success: "#10B981"
  success-soft: "#ECFDF5"
  info: "#0EA5E9"
  info-soft: "#F0F9FF"
typography:
  font-family: "'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
  display:
    fontSize: "2rem"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "-0.025em"
  h1:
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.02em"
  h2:
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.015em"
  h3:
    fontSize: "1.1rem"
    fontWeight: 600
    lineHeight: 1.4
  body-lg:
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
  body-md:
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.5
  label-sm:
    fontSize: "0.75rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.02em"
rounded:
  xs: "4px"
  sm: "6px"
  md: "10px"
  lg: "14px"
  xl: "20px"
  2xl: "24px"
  full: "9999px"
spacing:
  2xs: "4px"
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "20px"
  xl: "24px"
  2xl: "32px"
  3xl: "48px"
components:
  card:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    shadow: "0 1px 3px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04)"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "9px 18px"
    fontWeight: 600
  button-secondary:
    backgroundColor: "{colors.surface-secondary}"
    textColor: "{colors.text-main}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    padding: "9px 18px"
  badge:
    rounded: "{rounded.full}"
    padding: "3px 10px"
    fontSize: "{typography.label-sm.fontSize}"
    fontWeight: 600
  input:
    rounded: "{rounded.md}"
    padding: "10px 14px"
    borderColor: "{colors.border-input}"
    fontSize: "{typography.body-md.fontSize}"
---

# Student Club AI Design System

The official design system for the **Hệ Thống Quản Lý Câu Lạc Bộ Sinh Viên Tích Hợp AI Agent (Nhóm 28)**, authored according to the **Google Labs `DESIGN.md` specification**.

---

## Overview

### Brand Identity & Intent
The Student Club AI Management System empowers university club executives, committee leaders, and members to coordinate activities with AI-accelerated workflows. The visual identity conveys:
- **Intelligent Modernity**: Clean surfaces with vibrant indigo and electric blue accents, paired with purple-pink gradients for AI features.
- **Clarity & Efficiency**: High contrast, legible typography, purposeful card hierarchy, and minimal visual noise.
- **Adaptive Ergonomics**: Dual-mode operational capability (Light and Dark) respecting WCAG AA standard with zero visual distortion.

---

## Colors

### Palette Archetype
We adopt an **Indigo & Deep Blue Modern Slate** palette:
- **Primary (`#2563EB`)**: High-visibility electric blue for core calls-to-action and active states.
- **Secondary (`#4F46E5`)**: Deep indigo serving as anchoring brand and navigation elements.
- **AI Accent (`#8B5CF6` to `#EC4899`)**: Electric violet and magenta gradient representing generative and predictive AI actions.
- **Surfaces**:
  - Light mode: Pure `#FFFFFF` on `#F8FAFC` slate canvas.
  - Dark mode: Rich obsidian `#141D2E` on deep cosmic `#0B0F19` canvas.
- **Borders**: Subtly contrasting `#E2E8F0` (light) and `#243048` (dark) to delineate elements with spatial discipline.

### Contrast & WCAG Compliance
All primary, secondary, and status text pairings guarantee a contrast ratio greater than **4.5:1** for standard text and **3.0:1** for large headings in both light and dark operational modes.

---

## Typography

### Font Family
- **Plus Jakarta Sans**: Modern geometric grotesque with friendly humanist curves and exceptional legibility on digital screens.
- Fallback stack: `system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`.

### Type Hierarchy
1. **Display (`2rem` / `32px`, 800 Weight)**: Page banners and celebratory hero headers.
2. **Heading 1 (`1.5rem` / `24px`, 700 Weight)**: Main view titles and prominent section labels.
3. **Heading 2 (`1.25rem` / `20px`, 700 Weight)**: Card group titles and modal headings.
4. **Heading 3 (`1.1rem` / `17.6px`, 600 Weight)**: Item headers, Kanban column titles.
5. **Body Large (`1rem` / `16px`, 400 Weight)**: Introductory summaries and announcement text.
6. **Body Medium (`0.875rem` / `14px`, 400 Weight)**: Primary content, inputs, table body text.
7. **Label Small (`0.75rem` / `12px`, 600 Weight)**: Badges, timestamps, secondary captions.

---

## Layout & Spacing

### Spatial Rhythm
An 8-point baseline grid system is utilized across all layouts, with 4px sub-increments for compact utility components:
- `2xs (4px)`: Micro-gaps between icons and label text.
- `xs (8px)`: Chip gaps, compact button paddings.
- `sm (12px)`: Internal card group spacing.
- `md (16px)`: Standard grid gaps and container padding.
- `lg (20px)`: Card padding and view row separations.
- `xl (24px)`: Section padding and page header margins.
- `2xl (32px)`: Major layout block margins.

### Responsive Breakpoints
- Desktop: `> 1024px` (Two-column grids, persistent sidebar).
- Tablet: `768px - 1024px` (Single to dual column transitions).
- Mobile: `< 768px` (Fluid single column, scrollable table containers).

---

## Elevation & Depth

We utilize layered depth planes rather than excessive drop shadows:
- **Level 0 (Canvas)**: `--bg-main` (`#F8FAFC` light / `#0B0F19` dark).
- **Level 1 (Card & Content Surface)**: `--bg-card` (`#FFFFFF` light / `#141D2E` dark) with `shadow-card`.
- **Level 2 (Dropdowns & Popovers)**: `--bg-dropdown` with `shadow-md` and 1px border.
- **Level 3 (Modals & Overlays)**: `--bg-modal` with `shadow-lg` over a `6px` blurred backdrop.
- **AI Glow**: Soft radiant gradient shadows (`rgba(139, 92, 246, 0.25)`) highlighting intelligent outputs.

---

## Shapes

Organic, friendly curvatures aligned to our geometric sans typography:
- **Buttons & Inputs**: `rounded-md (10px)`.
- **Cards & Modals**: `rounded-lg (14px)` to `rounded-xl (20px)`.
- **Badges & Pills**: `rounded-full (9999px)`.
- **Avatars**: Circular `rounded-full`.

---

## Components

### 1. Buttons
- **Primary Button**: Electric blue with subtle hover lift and click feedback.
- **AI Button**: Purple-indigo radiant gradient with sparkle icon.
- **Secondary Button**: Neutral tinted surface with discrete border.
- **Theme Toggle**: Accessible switchable badge with glowing celestial icon.

### 2. Cards & Stat Widgets
- Pure surfaces framed by 1px subtle borders.
- Top-right icon container with tinted role-appropriate backgrounds.
- Quantitative stat numbers with bold, prominent weighting.

### 3. Navigation (Sidebar & Header)
- Sticky top header (`64px` height) with brand emblem, current profile chip, and theme toggle.
- Clean sidebar with distinct active indicator tabs, hover transitions, and pinned bottom metadata.

### 4. Kanban Board
- 3 distinct workflow columns (`To Do`, `In Progress`, `Done`) with colored indicator beacons.
- Task cards featuring skill badges, AI affinity score indicator, and role-guarded status selectors.

### 5. AI Hub Assistant
- Interactive segmented pill controls for switching modes.
- Two-column input/output layouts with instant copy-to-clipboard actions.

---

## Do's and Don'ts

### Do's
- **DO** use CSS custom variables (`var(--...)`) mapped to token definitions for all color, background, and border styling.
- **DO** maintain a white protective padding wrapper around dynamic QR Code SVGs in dark mode to preserve scanner camera readability.
- **DO** provide smooth `0.2s` transitions on hoverable cards and buttons.
- **DO** ensure interactive form elements have clear `:focus` rings.

### Don'ts
- **DON'T** use hardcoded hex values (`#ffffff`, `#000000`, `#0f172a`) in inline element styles.
- **DON'T** use jarring pure black (`#000000`) for dark mode; use refined obsidian slate (`#0B0F19` / `#141D2E`).
- **DON'T** remove text labels from essential action controls.
- **DON'T** nest heavily saturated background panels that compete with the primary data visualizations.
