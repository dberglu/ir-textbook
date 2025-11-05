# Anthropic Brand Guidelines for IR Textbook

This document defines the visual identity and branding standards for the AI for Investor Relations Transformation textbook.

---

## 🎨 Color Palette

### Main Colors

| Color | Hex Code | RGB | Usage |
|-------|----------|-----|-------|
| **Dark** | `#141413` | rgb(20, 20, 19) | Primary text, dark backgrounds, headers |
| **Light** | `#faf9f5` | rgb(250, 249, 245) | Light backgrounds, text on dark |
| **Mid Gray** | `#b0aea5` | rgb(176, 174, 165) | Secondary elements, subtle text |
| **Light Gray** | `#e8e6dc` | rgb(232, 230, 220) | Subtle backgrounds, dividers, borders |

### Accent Colors

| Color | Hex Code | RGB | Usage |
|-------|----------|-----|-------|
| **Orange** | `#d97757` | rgb(217, 119, 87) | Primary accent, links, highlights |
| **Blue** | `#6a9bcc` | rgb(106, 155, 204) | Secondary accent, interactive elements |
| **Green** | `#788c5d` | rgb(120, 140, 93) | Tertiary accent, success states |

### Color Usage Principles

- **Primary Content:** Dark (#141413) text on Light (#faf9f5) background
- **Accent Rotation:** Use Orange → Blue → Green for visual hierarchy
- **Interactive Elements:** Orange for primary actions, Blue for secondary
- **Success/Confirmation:** Use Green for positive feedback
- **Contrast:** Maintain WCAG AA compliance (4.5:1 minimum)

---

## 🖋 Typography

### Font Families

**Headings:** Poppins
- Font: `'Poppins', Arial, sans-serif`
- Weights: 600 (Semi-Bold), 700 (Bold)
- Use: H1-H6, section titles, navigation, emphasis

**Body Text:** Lora
- Font: `'Lora', Georgia, serif`
- Weights: 400 (Regular), 500 (Medium)
- Use: Paragraphs, lists, descriptions, long-form content

**Code:** Roboto Mono
- Font: `'Roboto Mono', monospace`
- Use: Code blocks, technical examples, file paths

### Typography Scale

| Element | Font | Size | Weight | Line Height |
|---------|------|------|--------|-------------|
| H1 | Poppins | 36-48pt | 700 | 1.2 |
| H2 | Poppins | 30-36pt | 600 | 1.3 |
| H3 | Poppins | 24-30pt | 600 | 1.4 |
| H4 | Poppins | 20-24pt | 600 | 1.4 |
| Body | Lora | 16-18pt | 400 | 1.6 |
| Caption | Lora | 14pt | 400 | 1.5 |
| Code | Roboto Mono | 14-16pt | 400 | 1.4 |

---

## 📐 Design Principles

### 1. Simplicity
- Clean, uncluttered layouts
- Generous white space
- Clear visual hierarchy
- Minimal decorative elements

### 2. Hierarchy
- Use typography scale consistently
- Poppins for headings creates clear structure
- Accent colors guide attention
- Visual weight indicates importance

### 3. Consistency
- Apply color palette uniformly
- Use established spacing patterns
- Maintain font usage rules
- Repeat design patterns across chapters

### 4. Readability
- Lora font enhances long-form reading
- Adequate line spacing (1.6 for body)
- Optimal line length (60-80 characters)
- High contrast ratios

### 5. Recognition
- Distinctive Anthropic brand colors
- Consistent header/footer styling
- Recognizable accent color patterns
- Professional executive aesthetic

---

## 🎯 Component Guidelines

### Cards & Containers

**Dark Card** (for callouts, emphasis)
```css
background: #141413
color: #faf9f5
border-radius: 16px
padding: 2rem
```

**Light Card** (for content sections)
```css
background: #faf9f5
color: #141413
border-radius: 8px
padding: 1.5rem
border: 1px solid #e8e6dc
```

### Interactive Elements

**Concept Highlights**
- Background: Light Gray (#e8e6dc)
- Border-left: 4px solid Orange (#d97757)
- Padding: 1rem
- Border-radius: 4px

**Interactive Widgets**
- Border: 2px solid Blue (#6a9bcc)
- Border-radius: 12px
- Background: Light (#faf9f5)
- Padding: 1.5rem

### Tables

- Header background: Dark (#141413)
- Header text: Light (#faf9f5), Poppins 600
- Row hover: Light Gray (#e8e6dc)
- Border: 1px solid Light Gray (#e8e6dc)

### Buttons & Links

- **Primary Button:** Orange background (#d97757)
- **Button Hover:** Blue background (#6a9bcc)
- **Text Links:** Orange (#d97757)
- **Link Hover:** Blue (#6a9bcc)

---

## 🖼 Visual Content Guidelines

### Diagrams & Infographics

**Color Usage:**
- Primary elements: Dark (#141413)
- Backgrounds: Light (#faf9f5) or Light Gray (#e8e6dc)
- Highlights: Orange (#d97757)
- Connections/flows: Blue (#6a9bcc)
- Success/completion: Green (#788c5d)

**Typography:**
- Labels: Poppins 600, 14-16pt
- Descriptions: Lora 400, 14pt
- Titles: Poppins 700, 18-24pt

### MicroSims (p5.js)

**Canvas Styling:**
- Background: Dark (#141413) or Light (#faf9f5)
- Border-radius: 16px
- Container padding: 2rem
- Control panel background: Light Gray (#e8e6dc)

**Interactive Controls:**
- Sliders/buttons: Orange accent (#d97757)
- Hover states: Blue (#6a9bcc)
- Active states: Green (#788c5d)
- Labels: Poppins 600

### Charts & Graphs

**Color Assignment:**
1. First series: Orange (#d97757)
2. Second series: Blue (#6a9bcc)
3. Third series: Green (#788c5d)
4. Additional: Mid Gray (#b0aea5)

**Styling:**
- Axes: Dark (#141413), Lora 400
- Labels: Poppins 600, 14pt
- Grid lines: Light Gray (#e8e6dc)
- Background: Light (#faf9f5)

---

## 📱 Responsive Design

### Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

### Mobile Considerations
- Maintain font hierarchy
- Simplify complex diagrams
- Stack interactive elements vertically
- Ensure touch targets ≥ 44px

---

## ✅ Content Generation Checklist

When generating chapter content, ensure:

- [ ] Headings use Poppins font
- [ ] Body text uses Lora font
- [ ] Color palette adhered to throughout
- [ ] Accent colors used in rotation (Orange → Blue → Green)
- [ ] Tables have branded header styling
- [ ] Interactive elements use Blue borders
- [ ] Concept highlights use Orange left border
- [ ] Code blocks use appropriate monospace font
- [ ] Visual content follows color guidelines
- [ ] Dark/light mode compatibility maintained
- [ ] Consistent spacing and padding
- [ ] Professional executive aesthetic maintained

---

## 🔗 Additional Resources

- **MkDocs Theme:** Material with custom CSS ([anthropic-brand.css](stylesheets/anthropic-brand.css))
- **Font Sources:** Google Fonts (Poppins, Lora)
- **Brand Skill:** `brand-guidelines` skill for reference
- **Design System:** Anthropic official brand guidelines

---

*Last Updated: November 5, 2025*
*Version: 1.0*
