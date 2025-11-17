# Quiz: Sentiment Analysis - Signals and Methods

Test your understanding of sentiment analysis methodologies, NLP techniques, data sources, and model evaluation for investor relations intelligence.

---

#### 1. What is the primary value proposition of Natural Language Processing (NLP) for investor relations?

<div class="upper-alpha" markdown>
1. NLP eliminates the need for any human analysis of communications
2. NLP enables automated processing of massive text volumes at scale and speed, providing comprehensive rather than sample-based analysis
3. NLP guarantees 100% accuracy in sentiment classification
4. NLP only works for social media monitoring, not professional communications
</div>

??? question "Show Answer"
    The correct answer is **B**. NLP's strategic value centers on scale (processing 100% of content vs. 10-20% manual sampling) and speed (minutes rather than days for analysis), enabling comprehensive coverage while maintaining consistency and objectivity. A mid-cap company might generate thousands of documents monthly that NLP can systematically analyze. Option A overstates—human judgment remains essential for strategic interpretation. Option C is unrealistic—typical accuracy is 75-90%, not perfect. Option D is incorrect—NLP works across all text types including transcripts, reports, and filings.

    **Concept Tested:** Natural Language Processing

    **Bloom's Level:** Understand

    **See:** [Section 1: Natural Language Processing Foundations](index.md#1-natural-language-processing-foundations-for-ir)

---

#### 2. Which internal IR dataset provides the most direct stakeholder feedback for sentiment analysis?

<div class="upper-alpha" markdown>
1. Public SEC filings available to all investors
2. Historical stock price movements and trading volumes
3. Press releases distributed through newswires
4. Investor email corpus containing questions, concerns, and compliments from shareholders
</div>

??? question "Show Answer"
    The correct answer is **D**. The investor email corpus (50-500+ monthly emails from institutional investors, analysts, and retail shareholders) provides direct stakeholder feedback revealing emerging concerns before they become public, tracking response effectiveness, and enabling sentiment segmentation by investor type. This internal dataset offers unfiltered insights into stakeholder thinking. Option A describes public documents, not direct feedback. Option B reflects market behavior but not explicit sentiment. Option C represents company-originated communications, not stakeholder feedback.

    **Concept Tested:** Sentiment Data Sources (Internal Datasets)

    **Bloom's Level:** Remember

    **See:** [Section 2: Sentiment Data Sources](index.md#2-sentiment-data-sources-internal-and-external-datasets)

---

#### 3. In the NLP pipeline for sentiment analysis, what happens during the "feature extraction" stage?

<div class="upper-alpha" markdown>
1. Transform preprocessed text into numerical representations that machine learning models can process
2. Collect raw text from APIs, web scraping, and document uploads
3. Remove HTML tags, special characters, and extra whitespace
4. Generate final sentiment scores and actionable insights
</div>

??? question "Show Answer"
    The correct answer is **A**. Feature extraction transforms preprocessed text into numerical representations using techniques like TF-IDF (weighting words by importance), word embeddings (dense vectors capturing semantic meaning), or contextual embeddings (transformer models understanding context). This conversion enables machine learning on text data. Option B describes data collection (Stage 1). Option C describes preprocessing/cleaning (also Stage 1). Option D describes aggregation and analysis (Stage 4), which occurs after sentiment classification.

    **Concept Tested:** Text Mining Methods, NLP Pipeline

    **Bloom's Level:** Understand

    **See:** [Section 1: Natural Language Processing Foundations](index.md#1-natural-language-processing-foundations-for-ir)

---

#### 4. When analyzing analyst reports, what does tracking "theme frequency" reveal about market sentiment?

<div class="upper-alpha" markdown>
1. The exact future stock price movements
2. Whether the company should change its strategy immediately
3. What topics dominate analyst attention and how emphasis shifts over time
4. The personal opinions of individual retail investors
</div>

??? question "Show Answer"
    The correct answer is **C**. Theme frequency analysis (e.g., "AI Strategy discussed in 78% of reports, up 15pp from prior quarter") reveals what topics dominate analyst attention and how emphasis evolves, informing IR messaging priorities and identifying emerging areas of focus or concern. This provides strategic intelligence on market priorities. Option A overstates—sentiment analysis informs but doesn't predict prices precisely. Option B conflates analysis inputs with strategy decisions. Option D misidentifies the source—this analyzes professional analyst reports, not retail sentiment.

    **Concept Tested:** Analyst Report Insights

    **Bloom's Level:** Analyze

    **See:** [Section 2: Sentiment Data Sources](index.md#2-sentiment-data-sources-internal-and-external-datasets)

---

#### 5. What is "voice tone analysis" in the context of earnings calls?

<div class="upper-alpha" markdown>
1. Counting how many times executives speak during the call
2. Evaluating emotional characteristics, confidence, and sentiment through speech patterns and vocal features like pitch, pace, and pauses
3. Measuring the volume level of the audio recording
4. Translating spoken words into written transcripts
</div>

??? question "Show Answer"
    The correct answer is **B**. Voice tone analysis evaluates emotional characteristics, confidence, and sentiment conveyed through speech patterns and vocal features including pitch (stress/uncertainty indicators), pace (speaking speed), volume (emphasis patterns), pauses (hesitation), and vocal quality. This provides insights beyond words themselves for executive coaching and question difficulty assessment. Option A is a simple count, not tone analysis. Option C measures technical audio quality, not emotional tone. Option D describes speech-to-text transcription, a prerequisite but not tone analysis itself.

    **Concept Tested:** Voice Tone Analysis

    **Bloom's Level:** Remember

    **See:** [Section 3: NLP for Earnings Transcripts](index.md#3-nlp-for-earnings-transcripts-and-investor-communications)

---

#### 6. Your sentiment model achieves 90% accuracy but performs poorly in practice. What is the most likely explanation?

<div class="upper-alpha" markdown>
1. The model is too complex and needs simplification
2. Accuracy is the only metric that matters for sentiment analysis
3. The model uses outdated NLP techniques from the 1990s
4. Class imbalance—if 90% of samples are neutral, always predicting neutral achieves 90% accuracy but provides no value
</div>

??? question "Show Answer"
    The correct answer is **D**. High accuracy can be misleading with class imbalance. If 90% of training samples are neutral, a model that always predicts "neutral" achieves 90% accuracy while identifying zero positive or negative signals. This is why F1 score (balancing precision and recall) is a better metric than raw accuracy for imbalanced sentiment data. Option A doesn't explain the accuracy-performance gap. Option B is wrong—accuracy alone is insufficient, especially with imbalance. Option C is irrelevant to the accuracy-performance disconnect described.

    **Concept Tested:** Model Evaluation for Sentiment

    **Bloom's Level:** Apply

    **See:** [Section 5: Model Evaluation](index.md#5-model-evaluation-and-continuous-improvement)

---

#### 7. Which feature engineering category captures the MEANING and context of words rather than just their frequency?

<div class="upper-alpha" markdown>
1. Semantic features using contextual embeddings like BERT that understand word meaning in context
2. Lexical features counting positive and negative words from dictionaries
3. Syntactic features measuring sentence length and complexity
4. Metadata features tracking document source and publication timing
</div>

??? question "Show Answer"
    The correct answer is **A**. Semantic features use techniques like topic models, entity recognition, and contextual embeddings (BERT-based representations) that capture word meaning in context rather than just counting occurrences. For example, "bank" means something different in "river bank" vs. "investment bank"—semantic features distinguish these. Option B describes lexical features (word-level counting). Option C describes syntactic features (structural patterns). Option D describes metadata features (document characteristics).

    **Concept Tested:** Feature Engineering for NLP

    **Bloom's Level:** Understand

    **See:** [Section 4: Feature Engineering](index.md#4-feature-engineering-and-model-development)

---

#### 8. When monitoring social media sentiment, what is a critical challenge that IR teams must address?

<div class="upper-alpha" markdown>
1. Social media never contains any useful investor sentiment information
2. All social media content is automatically accurate and representative
3. High noise ratio—much content is irrelevant, sarcastic, bot-generated, or represents coordinated manipulation rather than genuine sentiment
4. Social media monitoring is prohibited by SEC regulations
</div>

??? question "Show Answer"
    The correct answer is **C**. Social media sentiment faces critical challenges including high noise ratio (irrelevant content, sarcasm, bots), representativeness issues (skews younger, retail, tech-savvy vs. institutional investors), manipulation risk (coordinated campaigns, pump-and-dump schemes), and volume overwhelm (thousands of daily mentions for popular stocks). Best practices include filtering for credible accounts, weighting by engagement, and cross-referencing with other sources. Option A is too extreme—social media provides valuable early signals despite challenges. Option B ignores serious quality issues. Option D is incorrect—monitoring public social media is permissible.

    **Concept Tested:** Social Media Analytics, Monitoring Social Media

    **Bloom's Level:** Apply

    **See:** [Section 2: Sentiment Data Sources](index.md#2-sentiment-data-sources-internal-and-external-datasets)

---

#### 9. What is the primary purpose of the Loughran-McDonald financial sentiment lexicon?

<div class="upper-alpha" markdown>
1. To translate financial documents into multiple languages
2. To provide a dictionary of 6,000+ words with positive/negative sentiment labels specific to financial texts rather than general language
3. To automatically generate earnings releases and press statements
4. To replace all human financial analysts with AI systems
</div>

??? question "Show Answer"
    The correct answer is **B**. The Loughran-McDonald lexicon provides a financial domain-specific sentiment dictionary with 2,000+ positive words and 4,000+ negative words tailored to financial texts. This matters because words like "liability" or "outstanding" have different connotations in finance than general language. Domain-specific lexicons outperform general sentiment dictionaries for financial text. Option A describes translation tools, not sentiment lexicons. Option C describes content generation, not sentiment analysis. Option D overstates—lexicons support but don't replace human judgment.

    **Concept Tested:** Feature Engineering for NLP, Text Mining Methods

    **Bloom's Level:** Remember

    **See:** [Section 4: Feature Engineering](index.md#4-feature-engineering-and-model-development)

---

#### 10. In a real-time sentiment monitoring system, what should trigger a "critical" alert requiring immediate IR team notification?

<div class="upper-alpha" markdown>
1. Any mention of the company name on any social media platform
2. A single retail investor posting a question on a discussion forum
3. Normal fluctuations in daily sentiment scores within expected ranges
4. Tier 1 analyst downgrade, multiple negative news articles within an hour, or sentiment dropping 30+ points in 2 hours
</div>

??? question "Show Answer"
    The correct answer is **D**. Critical alerts should trigger on significant, actionable events: Tier 1 analyst downgrades (high-authority sources), concentrated negative news (3+ articles within 1 hour indicating developing narrative), or sharp sentiment drops (>30 points in 2 hours suggesting material shift). Alert calibration is crucial—too sensitive creates fatigue and system abandonment. Option A would generate thousands of false alarms. Option B lacks materiality for immediate escalation. Option C describes normal variation, not alert-worthy events.

    **Concept Tested:** Real-Time Sentiment Data, AI Sentiment Tracking

    **Bloom's Level:** Apply

    **See:** [Section 6: Real-Time Sentiment Monitoring](index.md#6-real-time-sentiment-monitoring-and-actionable-intelligence)

---

#### 11. What does "NLP for transcripts" analysis of earnings call Q&A reveal about investor concerns?

<div class="upper-alpha" markdown>
1. Question topic clustering showing what themes dominate analyst attention and how emphasis shifts across quarters
2. The personal phone numbers of analysts asking questions
3. Guaranteed predictions of next quarter's financial results
4. Legal compliance with all SEC disclosure requirements
</div>

??? question "Show Answer"
    The correct answer is **A**. NLP analysis of earnings call Q&A performs question topic clustering revealing themes dominating analyst attention (e.g., "AI Strategy: 35% of questions, ↑15pp vs Q2"), question sentiment (challenging vs. supportive), response quality (direct vs. deflecting), and uncertainty language. This identifies emerging concerns and helps prepare for future calls. Option B confuses sentiment analysis with contact information extraction. Option C overstates—analysis informs but doesn't predict results. Option D confuses sentiment analysis with compliance checking (different function).

    **Concept Tested:** NLP For Transcripts

    **Bloom's Level:** Understand

    **See:** [Section 3: NLP for Earnings Transcripts](index.md#3-nlp-for-earnings-transcripts-and-investor-communications)

---

#### 12. Why is continuous model evaluation and retraining necessary for sentiment analysis systems?

<div class="upper-alpha" markdown>
1. Sentiment models never require updates once initially deployed
2. Regulatory requirements mandate monthly model retraining
3. Language evolves, business context changes, and sentiment toward topics shifts over time (e.g., "AI investment" more positive in 2024 than 2020), causing model drift
4. Continuous retraining allows models to predict stock prices with perfect accuracy
</div>

??? question "Show Answer"
    The correct answer is **C**. Continuous evaluation and retraining are essential because language evolves, business context changes, and sentiment toward specific topics shifts over time. For example, sentiment toward "AI investment" became more positive from 2020 to 2024 as capabilities matured. Without retraining, models drift and accuracy degrades. Systematic feedback loops and regular retraining on recent labeled data maintain performance. Option A is incorrect—all deployed models require maintenance. Option B mischaracterizes—no such regulatory mandate exists. Option D is unrealistic—retraining improves accuracy but doesn't enable perfect price prediction.

    **Concept Tested:** Model Evaluation for Sentiment, Analyzing Feedback

    **Bloom's Level:** Analyze

    **See:** [Section 5: Model Evaluation](index.md#5-model-evaluation-and-continuous-improvement)

---

## Quiz Statistics

- **Total Questions:** 12
- **Bloom's Taxonomy Distribution:**
    - Remember: 3 questions (25%)
    - Understand: 4 questions (33%)
    - Apply: 3 questions (25%)
    - Analyze: 2 questions (17%)
- **Answer Distribution:**
    - A: 3 questions (25%)
    - B: 3 questions (25%)
    - C: 3 questions (25%)
    - D: 3 questions (25%)
- **Concepts Covered:** 14 of 14 chapter concepts (100%)
- **Estimated Completion Time:** 20-25 minutes

---

## Next Steps

After completing this quiz:

1. Review the [Chapter Summary](index.md#summary) to reinforce sentiment analysis concepts
2. Work through the [Chapter Exercises](index.md#exercises) for hands-on feature engineering practice
3. Proceed to [Chapter 8: Predictive Analytics and Market Intelligence](../08-predictive-analytics-intelligence/index.md)

For additional practice questions, see the [Quiz Bank](../../learning-graph/quiz-bank.json).
