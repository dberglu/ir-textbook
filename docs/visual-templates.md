# Visual Element Templates - Anthropic Brand

This document provides ready-to-use templates for creating branded visual content in chapters.

---

## Concept Highlight Box

Use this for emphasizing key concepts:

```html
<div class="concept-highlight">
<strong>Key Concept:</strong> [Concept Name]

[Brief explanation of the concept using Lora font, maintaining professional tone for executive audience]
</div>
```

**Example:**
<div class="concept-highlight">
<strong>Key Concept:</strong> Regulation Fair Disclosure (Reg FD)

Reg FD requires public companies to disclose material information to all investors simultaneously, preventing selective disclosure to favored analysts or institutional investors.
</div>

---

## Interactive Element Container

For MicroSims, infographics, or interactive content:

```html
<div class="interactive-element">
<h3>Interactive: [Title]</h3>

[Description of the interactive element]

<details>
    <summary>[Element Type] Specification</summary>
    Type: [MicroSim/Infographic/Chart/etc.]

    [Detailed specification]

    Colors:
    - Primary: Orange (#d97757)
    - Secondary: Blue (#6a9bcc)
    - Background: Light (#faf9f5)

    Implementation: [Technology/approach]
</details>
</div>
```

---

## Dark Card for Callouts

Use for important warnings, executive insights, or special notes:

```html
<div class="card" style="background: #141413; color: #faf9f5; border-radius: 16px; padding: 2rem; margin: 1.5rem 0;">
<h4 style="font-family: 'Poppins', sans-serif; color: #d97757; margin-top: 0;">Executive Insight</h4>

[Content here using Lora font for readability]
</div>
```

**Example:**
<div class="card" style="background: #141413; color: #faf9f5; border-radius: 16px; padding: 2rem; margin: 1.5rem 0;">
<h4 style="font-family: 'Poppins', sans-serif; color: #d97757; margin-top: 0;">Executive Insight</h4>

CDOs implementing AI in IR functions should establish clear governance frameworks before deployment. This includes human-in-the-loop review processes for all AI-generated investor communications to ensure Reg FD compliance.
</div>

---

## Branded Table Template

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data     | Data     | Data     |
| Data     | Data     | Data     |
```

Tables automatically receive:
- Dark header (#141413) with light text (#faf9f5)
- Poppins font for headers
- Light gray hover effect (#e8e6dc)

---

## Color-Coded Admonitions

### Information (Blue)
```markdown
!!! info "Information Title"
    Content using Blue accent (#6a9bcc)
```

### Warning (Orange)
```markdown
!!! warning "Compliance Alert"
    Content using Orange accent (#d97757)
```

### Success (Green)
```markdown
!!! success "Best Practice"
    Content using Green accent (#788c5d)
```

---

## MicroSim Container Template

```html
<div class="microsim-container" style="background: #141413; border-radius: 16px; padding: 2rem; margin: 2rem 0;">

<details>
    <summary>MicroSim: [Simulation Title]</summary>
    Type: p5.js MicroSim

    **Learning Objective:** [What students will learn]

    **Visual Elements:**
    - Canvas size: 800x600
    - Background: Dark (#141413)
    - Primary elements: Orange (#d97757)
    - Interactive elements: Blue (#6a9bcc)
    - Success states: Green (#788c5d)

    **Controls:**
    - [Control 1]: [Description]
    - [Control 2]: [Description]

    **Behavior:**
    [Detailed description of simulation behavior]

    **Typography:**
    - Labels: Poppins 600, 14pt, Light (#faf9f5)
    - Values: Lora 400, 14pt, Light (#faf9f5)

    Implementation: microsim-p5 skill
</details>

</div>
```

---

## Diagram Specification Template

```html
<details>
    <summary>Diagram: [Diagram Title]</summary>
    Type: System Architecture / Flow Diagram / Concept Map

    **Purpose:** [What this diagram illustrates]

    **Elements:**
    1. [Element 1]: Rectangle, Dark (#141413) background, Light (#faf9f5) text
    2. [Element 2]: Rectangle, Orange (#d97757) border
    3. [Connections]: Blue (#6a9bcc) arrows

    **Layout:**
    - Arrangement: [Left-to-right / Top-to-bottom / Hierarchical]
    - Spacing: [Specifications]

    **Labels:**
    - Font: Poppins 600, 14-16pt
    - Color: Dark (#141413)

    **Color Usage:**
    - Background: Light (#faf9f5)
    - Primary boxes: Dark (#141413) fill, Light (#faf9f5) text
    - Highlight boxes: Orange (#d97757) border
    - Arrows/connectors: Blue (#6a9bcc)
    - Success indicators: Green (#788c5d)

    Implementation: [Mermaid / Draw.io / Custom SVG]
</details>
```

---

## Chart Specification Template

```html
<details>
    <summary>Chart: [Chart Title]</summary>
    Type: [Bar / Line / Pie / Scatter]

    **Data:**
    [Description of data being visualized]

    **Series Colors:**
    1. First series: Orange (#d97757)
    2. Second series: Blue (#6a9bcc)
    3. Third series: Green (#788c5d)
    4. Additional: Mid Gray (#b0aea5)

    **Styling:**
    - Background: Light (#faf9f5)
    - Grid lines: Light Gray (#e8e6dc)
    - Axis labels: Dark (#141413), Lora 400, 14pt
    - Legend: Poppins 600, 14pt
    - Title: Poppins 700, 18pt, Dark (#141413)

    **Dimensions:**
    - Width: 800px
    - Height: 500px
    - Responsive: Yes

    Implementation: [Chart.js / Plotly / Custom]
</details>
```

---

## Infographic Specification Template

```html
<details>
    <summary>Infographic: [Title]</summary>
    Type: Interactive Infographic / Static Infographic

    **Learning Objective:** [What this teaches]

    **Sections:**
    1. [Section 1]: [Content]
    2. [Section 2]: [Content]
    3. [Section 3]: [Content]

    **Color Palette:**
    - Primary: Orange (#d97757)
    - Secondary: Blue (#6a9bcc)
    - Tertiary: Green (#788c5d)
    - Background: Light (#faf9f5)
    - Text: Dark (#141413)

    **Typography:**
    - Headings: Poppins 700, 18-24pt
    - Body: Lora 400, 14-16pt
    - Labels: Poppins 600, 14pt

    **Interactions:** (if applicable)
    - Hover effects: Blue (#6a9bcc) highlights
    - Click targets: Orange (#d97757) buttons
    - Active states: Green (#788c5d)

    **Layout:**
    [Description of visual arrangement]

    Implementation: [SVG / HTML+CSS / p5.js]
</details>
```

---

## Best Practices Summary

### When Creating Visual Elements:

1. **Always use the brand color palette** - No custom colors
2. **Apply Poppins for headings** - Maintain hierarchy
3. **Use Lora for body content** - Readability first
4. **Follow accent rotation** - Orange → Blue → Green
5. **Maintain contrast ratios** - WCAG AA minimum (4.5:1)
6. **Round corners consistently** - 8px (small), 12px (medium), 16px (large)
7. **Add adequate padding** - 1rem minimum, 2rem for cards
8. **Test in both modes** - Light and dark themes
9. **Keep it simple** - Executive aesthetic, not decorative
10. **Document thoroughly** - Specifications enable implementation

---

*Use these templates when generating chapter content to ensure consistent Anthropic brand application throughout the textbook.*
