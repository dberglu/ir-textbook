# Quiz: AI Governance, Ethics, and Risk Management

Test your understanding of AI governance frameworks, ethical principles, algorithmic bias, hallucination detection, model drift management, and compliance monitoring.

---

#### 1. What is the primary purpose of "AI governance models" in investor relations?

<div class="upper-alpha" markdown>
1. Frameworks establishing policies, processes, and oversight mechanisms for responsible AI development and deployment throughout the AI lifecycle
2. AI systems never need governance or oversight
3. Governance models are only for marketing purposes
4. AI governance prevents all use of artificial intelligence
</div>

??? question "Show Answer"
    The correct answer is **A**. AI governance models provide frameworks establishing policies, processes, and oversight mechanisms for responsible AI development, deployment, operation, and evolution. In IR, governance is particularly critical due to regulatory scrutiny, market trust requirements, liability risks, and reputational impacts. Governance addresses the entire AI lifecycle: development (requirements, data sourcing, testing), deployment (approval processes, monitoring), operation (performance tracking, incident response), and evolution (retraining, audit, retirement). Option B is dangerously naive—AI requires careful governance. Option C trivializes governance's purpose. Option D mischaracterizes—governance enables responsible AI use, not prohibition.

    **Concept Tested:** AI Governance Models, Developing AI Policy

    **Bloom's Level:** Understand

    **See:** [Section 1: The Imperative for AI Governance](index.md#1-the-imperative-for-ai-governance-in-investor-relations)

---

#### 2. Which ethical principle requires that investors understand when and how AI influences the information they receive?

<div class="upper-alpha" markdown>
1. Privacy and data protection ensuring secure handling of investor information
2. Transparency and explainability so stakeholders know when AI is used and generally how it works
3. Fairness preventing discrimination against investor groups
4. Human oversight maintaining accountability for decisions
</div>

??? question "Show Answer"
    The correct answer is **B**. Transparency and explainability require that investors and regulators understand when AI is being used and, for material decisions, generally how AI reaches its conclusions. This doesn't require disclosing proprietary algorithms but does require explaining the approach and limitations. For example: "We use NLP to monitor sentiment, informing engagement priorities, but humans draft all material disclosures." Option A addresses data security, not transparency about AI use. Option C addresses fairness in treatment. Option D addresses accountability structure.

    **Concept Tested:** AI Ethics for Finance, Responsible AI Practices

    **Bloom's Level:** Remember

    **See:** [Section 2: Ethical Principles for AI in Finance](index.md#2-ethical-principles-for-ai-in-finance)

---

#### 3. What is "algorithmic bias risk" and why does it matter for IR?

<div class="upper-alpha" markdown>
1. Bias only exists in humans, never in AI systems
2. Algorithmic bias is beneficial and should be maximized
3. Potential for systematic errors in AI leading to unfair or discriminatory outcomes, such as systematically excluding certain investor groups from engagement
4. Bias has no impact on investor relations
</div>

??? question "Show Answer"
    The correct answer is **C**. Algorithmic bias risk represents the potential for systematic errors in AI systems leading to unfair or discriminatory outcomes. In IR, this can manifest as investor targeting systems systematically excluding foreign investors, prioritizing institutional over retail investors, or sentiment analysis performing poorly on non-English content. Bias can stem from training data (historical, sampling, measurement, label bias), model design (feature selection, optimization objectives), or deployment (how humans use AI recommendations). Option A is false—algorithms can encode and amplify human biases. Option B is ethically wrong and potentially illegal. Option D ignores serious fairness and reputation risks.

    **Concept Tested:** Algorithmic Bias Risk, Recognizing AI Bias

    **Bloom's Level:** Understand

    **See:** [Section 3: Algorithmic Bias](index.md#3-algorithmic-bias-recognition-and-mitigation)

---

#### 4. What are "AI hallucinations" in the context of large language models?

<div class="upper-alpha" markdown>
1. Visual illusions created by AI image generators
2. When AI systems generate false or fabricated information presented confidently as fact, such as inventing financial metrics or non-existent regulatory requirements
3. A beneficial feature that should be encouraged
4. Hallucinations only occur in consumer applications, never in enterprise systems
</div>

??? question "Show Answer"
    The correct answer is **B**. AI hallucinations occur when systems generate false or fabricated information presented confidently as fact. In IR contexts, this could include inventing financial metrics ("Q3 revenue grew 47%"—when actual growth was 4.7%), fabricating regulatory requirements, citing non-existent analyst reports, or creating plausible-sounding but incorrect earnings comparisons. Detection techniques include confidence scoring, fact verification against source data, cross-checking with multiple sources, and human expert review. Option A confuses text hallucinations with image generation. Option C is dangerous—hallucinations undermine accuracy and trust. Option D is false—enterprise LLMs hallucinate too, making detection critical.

    **Concept Tested:** Detecting Hallucinations, Recognizing Hallucinations, Reducing Hallucinations

    **Bloom's Level:** Understand

    **See:** [Section 4: Hallucination Detection and Mitigation](index.md#4-ai-hallucinations-detection-and-reduction)

---

#### 5. Which technique helps reduce AI hallucinations in IR applications?

<div class="upper-alpha" markdown>
1. Retrieval-Augmented Generation (RAG) grounding AI responses in verified source documents rather than relying solely on training data
2. Removing all human review from AI outputs
3. Encouraging AI to be more creative with facts
4. Ignoring hallucinations entirely
</div>

??? question "Show Answer"
    The correct answer is **A**. Retrieval-Augmented Generation (RAG) reduces hallucinations by grounding AI responses in verified source documents (SEC filings, earnings transcripts, approved disclosures) rather than relying solely on memorized training data. Other hallucination reduction techniques include confidence thresholds (only displaying high-confidence outputs), fact verification (cross-checking against databases), citation requirements (AI must cite sources), and human-in-the-loop review for material content. Option B removes crucial safety checks. Option C contradicts the goal of factual accuracy. Option D ignores serious risks.

    **Concept Tested:** Reducing Hallucinations

    **Bloom's Level:** Apply

    **See:** [Section 4: Hallucination Detection and Mitigation](index.md#4-ai-hallucinations-detection-and-reduction)

---

#### 6. What is "model drift" and why does it require monitoring?

<div class="upper-alpha" markdown>
1. Physical movement of servers in data centers
2. Models becoming bored with repetitive tasks
3. Models never change once deployed and drift doesn't exist
4. Changes in AI system performance over time as underlying data patterns evolve, requiring detection and management through retraining or feature updates
</div>

??? question "Show Answer"
    The correct answer is **D**. Model drift occurs when AI system performance degrades as underlying data distributions or relationships change over time. In IR, examples include: sentiment models trained pre-pandemic performing poorly on pandemic-era language, investor behavior patterns shifting due to new regulations or market regimes, or feature distributions changing (average engagement frequency declining). Detection involves tracking accuracy metrics, comparing feature distributions, and monitoring prediction calibration. Management requires retraining with recent data, updating features, or collecting new data sources. Option A confuses physical and statistical concepts. Option B anthropomorphizes algorithms. Option C is false—all deployed models drift eventually.

    **Concept Tested:** Detecting Model Drift, Managing Model Drift

    **Bloom's Level:** Understand

    **See:** [Section 5: Model Drift Monitoring and Management](index.md#5-model-drift-monitoring-and-management)

---

#### 7. What does "bias in financial data" refer to?

<div class="upper-alpha" markdown>
1. Financial data is always perfectly accurate with no issues
2. Systematic distortions or inaccuracies in datasets including historical bias, sampling bias, measurement bias, and label bias
3. Any data that disagrees with management's preferred narrative
4. Bias only affects social media data, never financial databases
</div>

??? question "Show Answer"
    The correct answer is **B**. Bias in financial data encompasses systematic distortions including: historical bias (past discriminatory practices reflected in training data), sampling bias (non-representative data collection like English-only media monitoring), measurement bias (Western-centric ESG definitions not translating globally), and label bias (human labelers' subjective judgments in training data). These biases propagate through AI models trained on the data, potentially leading to unfair outcomes. Option A is naive—all real-world data has limitations. Option C conflates bias with disagreement. Option D is false—financial databases contain various biases.

    **Concept Tested:** Bias in Financial Data

    **Bloom's Level:** Remember

    **See:** [Section 3: Algorithmic Bias](index.md#3-algorithmic-bias-recognition-and-mitigation)

---

#### 8. In AI ethics for IR, what is the distinction between identity verification and behavioral analysis using facial recognition?

<div class="upper-alpha" markdown>
1. Both are exactly the same and equally unethical
2. Both are completely ethical with no concerns
3. Neither should ever be used in any context
4. Identity verification for security (confirming participants are who they claim) has clearer ethical grounding than behavioral analysis (emotion detection, gaze tracking) which crosses ethical boundaries in most IR contexts
</div>

??? question "Show Answer"
    The correct answer is **D**. There's a critical ethical distinction: identity verification (using facial recognition to prevent unauthorized access to MNPI) serves security purposes and has clearer ethical grounding with proper consent and data protection. Behavioral analysis (emotion detection from facial expressions, gaze patterns during meetings) raises serious ethical concerns: accuracy problems across demographics, consent issues, manipulation risks, and questionable legitimate business purpose. Best practice prohibits emotion analysis without explicit consent and most organizations avoid it entirely in IR contexts. Option A conflates different use cases. Option B ignores serious ethical concerns. Option C is too absolute—identity verification can be ethical with proper controls.

    **Concept Tested:** Facial Ethics In IR, AI Ethics for Finance

    **Bloom's Level:** Analyze

    **See:** [Section 2: Ethical Principles for AI in Finance](index.md#2-ethical-principles-for-ai-in-finance)

---

#### 9. What is "materiality AI assessment"?

<div class="upper-alpha" markdown>
1. Assessing the physical materials used to build AI hardware
2. Automated evaluation of whether information is significant enough to influence reasonable investor decisions, requiring public disclosure
3. A manual process that can never involve AI
4. Materiality assessment is no longer required under securities law
</div>

??? question "Show Answer"
    The correct answer is **B**. Materiality AI assessment involves automated evaluation of whether information meets the legal standard of materiality—whether a reasonable investor would consider it important in making investment decisions. AI can assist by analyzing historical materiality determinations, comparing to peer disclosures, flagging quantitative thresholds, and identifying potentially material topics. However, final materiality decisions require human legal and business judgment due to their high-stakes nature and context-dependency. Option A confuses financial materiality with physical materials. Option C is too restrictive—AI can assist, though humans must decide. Option D is false—materiality remains fundamental to securities law.

    **Concept Tested:** Materiality AI Assessment

    **Bloom's Level:** Understand

    **See:** [Section 6: Compliance AI Systems](index.md#6-compliance-ai-systems-for-reg-fd-and-disclosure)

---

#### 10. How do "compliance AI monitors" support Reg FD adherence?

<div class="upper-alpha" markdown>
1. By completely replacing legal counsel and compliance officers
2. Compliance monitoring is unnecessary and should be eliminated
3. By continuously surveilling communications, calendar events, and activities to flag potential selective disclosure risks, quiet period violations, and inconsistent information dissemination
4. Monitors only work during business hours on weekdays
</div>

??? question "Show Answer"
    The correct answer is **C**. Compliance AI monitors continuously surveil communications (emails, calendar invites, meeting notes) to flag potential Reg FD violations including: selective disclosure (material nonpublic information shared with specific investors before public release), quiet period breaches (restricted communications before earnings), and disclosure inconsistencies (different information provided to different investors). Systems use NLP to analyze content, integrate with calendars to track quiet periods, and maintain audit trails. These automate mechanical checking, freeing legal teams for complex judgment calls. Option A overstates—AI assists but doesn't replace legal expertise. Option B ignores serious compliance needs. Option D limits monitoring when violations can occur 24/7.

    **Concept Tested:** Compliance AI Monitors, Reg FD Compliance AI

    **Bloom's Level:** Apply

    **See:** [Section 6: Compliance AI Systems](index.md#6-compliance-ai-systems-for-reg-fd-and-disclosure)

---

#### 11. What is a best practice for "mitigating AI bias" in investor targeting systems?

<div class="upper-alpha" markdown>
1. Regular statistical disparity testing comparing engagement recommendations across investor types, geographies, and size categories to detect systematic unfairness
2. Ignoring bias entirely since it's impossible to address
3. Using only one data source to simplify systems
4. Deploying AI without any monitoring or evaluation
</div>

??? question "Show Answer"
    The correct answer is **A**. Mitigating AI bias requires regular statistical disparity testing—analyzing AI system outputs across different groups (institutional vs. retail, domestic vs. international, large vs. small investors) to detect systematic unfairness. Other mitigation strategies include: diverse training data, de-biasing algorithms, regular bias audits, diverse development teams, fairness metrics in model evaluation, and human review of AI-influenced decisions. Proactive bias detection and correction protects both fairness and corporate reputation. Option B is defeatist—bias can be reduced through systematic effort. Option C increases bias risk by limiting data diversity. Option D creates unmanaged risk.

    **Concept Tested:** Mitigating AI Bias, Recognizing AI Bias

    **Bloom's Level:** Apply

    **See:** [Section 3: Algorithmic Bias](index.md#3-algorithmic-bias-recognition-and-mitigation)

---

#### 12. In a hybrid AI governance model for IR, what decisions typically require central governance committee review?

<div class="upper-alpha" markdown>
1. All decisions including trivial scheduling automation
2. No decisions ever require review in hybrid models
3. Only technology purchasing decisions
4. High-risk AI systems that draft material disclosures, make materiality assessments, or could facilitate Reg FD violations
</div>

??? question "Show Answer"
    The correct answer is **D**. In hybrid AI governance, central committees review high-risk AI systems including: those drafting or influencing material disclosures, making materiality assessments, potentially facilitating selective disclosure, or affecting regulatory compliance. Domain teams (IR) manage day-to-day governance for routine applications (meeting scheduling, document retrieval, basic data visualization). This balances consistency with agility—IR teams understand regulatory requirements, while central governance provides expertise and enterprise-wide standards. Clear escalation criteria determine when central review is required. Option A creates bottlenecks for low-risk activities. Option B abandons governance for high-stakes systems. Option C focuses too narrowly on procurement versus risk management.

    **Concept Tested:** AI Governance Models, Developing AI Policy

    **Bloom's Level:** Analyze

    **See:** [Section 1: The Imperative for AI Governance](index.md#1-the-imperative-for-ai-governance-in-investor-relations)

---

## Quiz Statistics

- **Total Questions:** 12
- **Bloom's Taxonomy Distribution:**
    - Remember: 2 questions (17%)
    - Understand: 5 questions (42%)
    - Apply: 3 questions (25%)
    - Analyze: 2 questions (17%)
- **Answer Distribution:**
    - A: 3 questions (25%)
    - B: 3 questions (25%)
    - C: 3 questions (25%)
    - D: 3 questions (25%)
- **Concepts Covered:** 12 of 18 chapter concepts (67%)
- **Estimated Completion Time:** 20-25 minutes

---

## Next Steps

After completing this quiz:

1. Review the [Chapter Summary](index.md#summary) to reinforce AI governance and ethics concepts
2. Work through the [Chapter Exercises](index.md#exercises) for hands-on bias detection and policy development practice
3. Proceed to [Chapter 12: Data Infrastructure and Integration](../12-data-infrastructure-integration/index.md)

For additional practice questions, see the [Quiz Bank](../../learning-graph/quiz-bank.json).
