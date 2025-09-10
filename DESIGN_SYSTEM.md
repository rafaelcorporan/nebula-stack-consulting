# 🎨 NebulaStack Design System Tokens

> *Precision-engineered for enterprise IT consulting — clean, deep, authoritative*

---

## 🖌️ Color Palette

### Base
- `slate-50` `#F8FAFC` — Background (Light Mode)
- `slate-900` `#0F172A` — Text / Headings
- `slate-600` `#475569` — Secondary Text
- `slate-300` `#CBD5E1` — Borders / Dividers

### Primary
- `sky-600` `#0284C7` — Primary Actions, CTAs
- `sky-700` `#0369A1` — Hover State
- `sky-500` `#3B82F6` — Accent / Highlights

### Semantic
- `emerald-500` `#10B981` — Success / Positive
- `emerald-50` `#ECFDF5` — Success Background
- `emerald-700` `#047857` — Success Dark

### Neutral
- `white` `#FFFFFF` — Cards, Modals
- `black` `#000000` — (Used sparingly)

---

## 🔤 Typography

### Font Stack
- **Primary**: `Inter` — via `next/font`
- **Code**: `JetBrains Mono` — for technical credibility

### Scale (Mobile → Desktop)

| Token         | Font Size | Line Height | Weight     | Use Case               |
|---------------|-----------|-------------|------------|------------------------|
| `heading-1`   | 2.25rem   | 2.5rem      | 600 (SemiBold) | Hero, Page Titles      |
| `heading-2`   | 1.875rem  | 2.25rem     | 600        | Section Headers        |
| `heading-3`   | 1.5rem    | 2rem        | 600        | Subheaders             |
| `body-lg`     | 1.125rem  | 1.75rem     | 400        | Lead Paragraphs        |
| `body-base`   | 1rem      | 1.5rem      | 400        | Body Text              |
| `body-sm`     | 0.875rem  | 1.25rem     | 400        | Captions, Form Labels  |
| `code-sm`     | 0.875rem  | 1.25rem     | 400        | Inline Code            |

---

## 📐 Spacing Scale (Based on 4pt Grid)

| Token   | Value (px/rem) | Use Case                     |
|---------|----------------|------------------------------|
| `space-1` | 0.25rem (4px)  | Icon padding, micro-gaps     |
| `space-2` | 0.5rem (8px)   | Button padding, small gaps   |
| `space-3` | 0.75rem (12px) | Form element spacing         |
| `space-4` | 1rem (16px)    | Section padding, card gaps   |
| `space-5` | 1.25rem (20px) | Modal padding                |
| `space-6` | 1.5rem (24px)  | Section margins              |
| `space-8` | 2rem (32px)    | Hero vertical rhythm         |
| `space-10`| 2.5rem (40px)  | Major section dividers       |
| `space-12`| 3rem (48px)    | Page section margins         |

---

## 🌀 Radii

| Token        | Value     | Use Case               |
|--------------|-----------|------------------------|
| `radius-sm`  | 0.375rem  | Buttons, Inputs        |
| `radius-md`  | 0.5rem    | Cards, Modals          |
| `radius-lg`  | 0.75rem   | Large CTAs, Hero blobs |
| `radius-full`| 9999px    | Pills, Avatars         |

---

## 🌑 Shadows (Light Mode)

| Token          | Value                                      | Use Case         |
|----------------|--------------------------------------------|------------------|
| `shadow-sm`    | `0 1px 2px 0 rgb(0 0 0 / 0.05)`           | Subtle elevation |
| `shadow-md`    | `0 4px 6px -1px rgb(0 0 0 / 0.1)`         | Cards, Modals    |
| `shadow-lg`    | `0 10px 15px -3px rgb(0 0 0 / 0.1)`       | Dropdowns        |
| `shadow-xl`    | `0 20px 25px -5px rgb(0 0 0 / 0.1)`       | Hero highlights  |

---

## ♿ Accessibility Standards

- ✅ All interactive elements: `:focus-visible` ring + offset
- ✅ Color contrast ≥ 4.5:1 (verified via Tailwind config)
- ✅ Reduced motion respected globally
- ✅ All form fields: associated `<Label>` + `aria-describedby`
- ✅ 3D scenes: fallback images + `role="img"` + `aria-label`

---

## 🧩 Component Status

| Component       | Status     | Notes                     |
|-----------------|------------|---------------------------|
| Button          | ✅ Done    | Variants: default, outline |
| RadioGroup      | ✅ Done    | With semantic icons       |
| Checkbox        | ✅ Done    | Accessible indicator      |
| Slider          | ✅ Done    | Range + thumb styling     |
| Select          | ✅ Done    | Radix UI + custom trigger |
| Label           | ✅ Done    | Peer-disabled states      |
| Quote Estimator | ✅ Done    | Live calc + PDF-ready     |