---
title: Sentiment Scoring Engine
description: An interactive MicroSim demonstrating how sentiment analysis works on financial text using lexicon-based scoring methods inspired by the Loughran-McDonald dictionary.
image: /sims/sentiment-scoring-engine/sentiment-scoring-engine.png
og:image: /sims/sentiment-scoring-engine/sentiment-scoring-engine.png
twitter:image: /sims/sentiment-scoring-engine/sentiment-scoring-engine.png
social:
   cards: false
---

# Sentiment Scoring Engine

<iframe src="main.html" height="682px" width="100%" scrolling="no"></iframe>

[Run the Sentiment Scoring Engine MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## Description

The Sentiment Scoring Engine MicroSim provides an interactive demonstration of how lexicon-based sentiment analysis works on financial communications text. This educational tool helps students and IR professionals understand the mechanics of sentiment scoring—a critical component of modern AI-powered investor relations analytics.

### How It Works

The MicroSim uses a simplified financial sentiment lexicon inspired by the **Loughran-McDonald (LM) Dictionary**, which is specifically designed for financial text analysis. Unlike general-purpose sentiment dictionaries, financial lexicons account for domain-specific word meanings (e.g., "liability" is neutral in finance but negative in general language).

**Key Features:**

- **Real-time Analysis**: Type or paste financial text and see instant sentiment scoring
- **Visual Sentiment Gauge**: Color-coded meter showing sentiment from very negative (-1.0) to very positive (+1.0)
- **Word-Level Breakdown**: See counts of positive and negative words detected
- **Sample Texts**: Pre-loaded examples of positive, negative, neutral, and mixed sentiment communications
- **Interactive Learning**: Experiment with different phrases to understand how word choice affects sentiment scores

### Educational Value

This MicroSim demonstrates several key concepts from Chapter 7 (Sentiment Analysis Methods):

1. **Lexicon-Based Approaches**: How dictionaries of positive and negative words are used to score text
2. **Financial Domain Specificity**: Why generic sentiment tools can misinterpret financial language
3. **Scoring Methodology**: How individual word counts translate to overall sentiment scores
4. **Real-World Application**: How IR teams can use sentiment analysis to review communications before release

### Technical Implementation

The MicroSim implements a simplified version of the lexicon-based sentiment analysis approach:

```
Sentiment Score = (Positive Words - Negative Words) / (Total Words × 0.3)
```

The score is normalized to range from -1.0 (very negative) to +1.0 (very positive), with values near 0 indicating neutral sentiment.

**Financial Lexicon Sample:**

- **Positive Words**: growth, profit, strong, excellent, innovation, momentum, confidence, leadership
- **Negative Words**: loss, decline, weak, concerns, risks, uncertainty, volatility, crisis, litigation

**Note**: This is a simplified educational model. Production sentiment analysis systems use much larger lexicons (Loughran-McDonald contains 2,000+ negative words), contextual analysis, negation detection, and often combine lexicon-based and machine learning approaches.

## Lesson Plan

### Learning Objectives

After using this MicroSim, students will be able to:

1. **Understand** how lexicon-based sentiment analysis calculates scores from text (Bloom's: Understand)
2. **Apply** sentiment analysis concepts to evaluate investor communications (Bloom's: Apply)
3. **Analyze** how specific word choices impact overall sentiment scores (Bloom's: Analyze)
4. **Evaluate** the strengths and limitations of lexicon-based sentiment methods (Bloom's: Evaluate)

### Suggested Activities

#### Activity 1: Explore Sample Texts (5 minutes)

1. Click each of the four sample text buttons (Positive, Negative, Neutral, Mixed)
2. Observe how the sentiment gauge responds to each example
3. Note the word counts and which specific words were detected
4. **Discussion Question**: Why does the "Mixed" example show the sentiment score it does?

#### Activity 2: Word Impact Experiment (10 minutes)

1. Start with the neutral example text
2. Add one positive word (e.g., "growth") and observe the score change
3. Add one negative word (e.g., "concerns") and observe again
4. Experiment with adding multiple positive or negative words
5. **Discussion Question**: How many negative words does it take to shift a positive message to negative?

#### Activity 3: Real-World Application (15 minutes)

1. Find a real earnings call transcript excerpt or press release (from your company or a public example)
2. Paste a 2-3 sentence excerpt into the MicroSim
3. Analyze the sentiment score
4. **Reflection Questions**:
   - Does the score match your intuitive reading of the text?
   - What words drove the score?
   - How might you revise the text to shift sentiment while maintaining accuracy?

#### Activity 4: Limitations Analysis (10 minutes)

Test these challenging cases to understand limitations:

1. **Negation**: "Not a bad quarter" vs. "Bad quarter"
2. **Context**: "We address concerns" (proactive) vs. "Concerns remain" (reactive)
3. **Sarcasm**: "Clearly our best quarter ever" (when results are poor)
4. **Domain Specificity**: "Aggressive growth strategy" (positive in business, sounds negative)

**Discussion Question**: What are the limitations of simple word-counting sentiment analysis? How do modern AI approaches (like FinBERT discussed in Chapter 7) address these limitations?

### Integration with Chapter 7

This MicroSim connects to these Chapter 7 topics:

- **Section 2**: Lexicon-Based Sentiment Analysis - demonstrates the core methodology
- **Section 3**: Financial-Specific Dictionaries - shows why domain dictionaries matter
- **Section 4**: Sentiment Scoring Approaches - illustrates score calculation methods
- **Section 7**: Practical Applications - shows how IR teams might use sentiment tools

### Prerequisites

- Basic understanding of investor relations communications (Chapter 1)
- Familiarity with earnings calls and press releases (Chapter 1)
- Awareness that AI can analyze text for patterns (Chapter 5)

### Assessment Opportunities

**Formative Assessment:**
- Can students explain why certain texts score as positive/negative?
- Can they predict the approximate score before analyzing new text?

**Summative Assessment:**
- Have students draft two versions of an earnings announcement paragraph (one emphasizing positive sentiment, one neutral) and explain word choices
- Ask students to write a 1-page analysis of sentiment analysis limitations based on their experiments

### Extension Activities

**For Advanced Students:**

1. Research the full Loughran-McDonald dictionary and compare it to this simplified version
2. Investigate how FinBERT or other transformer models improve on lexicon-based approaches
3. Explore how sentiment analysis integrates with other IR analytics (covered in Chapter 8)
4. Design a governance process for reviewing AI-generated sentiment scores before communications release (connecting to Chapter 11)

### Educator Notes

**Timing**: Allow 30-40 minutes for a complete lesson using all activities

**Group Size**: Works well for individual exploration or pairs discussing observations

**Discussion Prompts**:
- "Why might a neutral sentiment score actually be desirable for certain IR communications?"
- "How could biased or incomplete sentiment lexicons create problems for IR teams?"
- "What role should human judgment play alongside automated sentiment analysis?"

**Common Misconceptions to Address**:
- More words always mean higher accuracy (quality > quantity in lexicons)
- Sentiment analysis is "objective" (it reflects the lexicon designer's choices)
- Negative sentiment is always bad (sometimes transparency about challenges builds credibility)

### Technical Details

**Framework**: p5.js 1.11.10
**Canvas Dimensions**: 800×682 (responsive width)
**Accessibility**: Includes ARIA labels for screen readers
**Browser Compatibility**: Chrome, Firefox, Safari, Edge (modern versions)
**Mobile-Friendly**: Yes (though text input easier on desktop)

---

## Embedding This MicroSim

You can include this MicroSim on your website using the following `iframe`:

```html
<iframe src="https://[your-domain]/sims/sentiment-scoring-engine/main.html"
        height="682px"
        width="100%"
        scrolling="no">
</iframe>
```

---

## Additional Resources

- [Loughran-McDonald Sentiment Word Lists](https://sraf.nd.edu/loughranmcdonald-master-dictionary/) - The academic research behind financial sentiment dictionaries
- [Chapter 7: Sentiment Analysis Methods](../../chapters/07-sentiment-analysis-methods/index.md) - Full chapter covering sentiment analysis in detail
- [FinBERT Model](https://huggingface.co/ProsusAI/finbert) - Modern transformer-based financial sentiment analysis

---

**Reminder**: Create a screenshot named `sentiment-scoring-engine.png` (800×682px) showing the MicroSim in action for optimal social media previews when sharing this resource.
