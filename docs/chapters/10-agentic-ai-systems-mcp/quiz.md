# Quiz: Agentic AI Systems and Model Context Protocol

Test your understanding of autonomous agentic AI, Model Context Protocol architecture, agent orchestration, security standards, and practical IR applications.

---

#### 1. What distinguishes "agentic AI" from traditional task-specific AI systems?

<div class="upper-alpha" markdown>
1. Agentic AI is goal-oriented, can plan multi-step workflows, use external tools, and adapt plans based on intermediate results
2. Traditional AI is always superior to agentic systems
3. Agentic AI requires no human oversight whatsoever
4. Agentic AI and traditional AI are exactly identical
</div>

??? question "Show Answer"
    The correct answer is **A**. Agentic AI represents a paradigm shift from reactive task automation to autonomous goal-oriented systems. Key characteristics include: planning and reasoning (decomposing goals into sub-tasks), tool use (invoking APIs, databases, search engines), adaptive behavior (adjusting plans based on results), contextual memory (maintaining context across interactions), and multi-agent collaboration. Unlike traditional AI that responds to single prompts, agentic AI can execute complex multi-step workflows autonomously. Option B is incorrect—neither is universally superior; they serve different purposes. Option C is dangerous—human oversight remains essential for high-stakes actions. Option D is false.

    **Concept Tested:** Agentic AI Systems, Agent-Based IR Workflows

    **Bloom's Level:** Understand

    **See:** [Section 1: From Task Automation to Autonomous Agents](index.md#1-from-task-automation-to-autonomous-agents)

---

#### 2. What is the Model Context Protocol (MCP)?

<div class="upper-alpha" markdown>
1. A type of machine learning algorithm for sentiment analysis
2. An open standard enabling secure, auditable AI access to enterprise data systems and tools with authentication, authorization, and encryption
3. A programming language for writing AI applications
4. A social media platform for investor communications
</div>

??? question "Show Answer"
    The correct answer is **B**. The Model Context Protocol (MCP) is an emerging open standard (developed by Anthropic and adopted industry-wide) for connecting AI systems with enterprise data sources and tools securely and auditablly. MCP provides standardized integration (common protocol for any AI and any data system), security and access control (authentication, authorization, encryption, audit logging), tool discovery and invocation, and context management. This eliminates custom integrations for each AI-data combination. Option A misidentifies MCP as an algorithm rather than a protocol. Option C confuses protocols with programming languages. Option D is completely unrelated.

    **Concept Tested:** Model Context Protocol, MCP Architecture Overview

    **Bloom's Level:** Remember

    **See:** [Section 2: Model Context Protocol](index.md#2-model-context-protocol-secure-ai-integration-architecture)

---

#### 3. In MCP security architecture, what does the "Principle of Least Privilege Access" mean?

<div class="upper-alpha" markdown>
1. Agents should have access to all company data without restrictions
2. No security measures are needed for AI agents
3. Agents receive only the minimum permissions necessary for their specific function—earnings agents don't need write access, chatbots don't access board materials
4. Only executives can use AI systems
</div>

??? question "Show Answer"
    The correct answer is **C**. The Principle of Least Privilege Access grants AI agents only the minimum permissions required for their specific function. For example: an earnings report generator needs read access to financial databases and market data but no write access to financial systems; a chatbot needs access to public investor materials but not board-level strategic documents. This security principle minimizes damage from compromised agents or programming errors. Option A violates the principle—unrestricted access creates massive risk. Option B abandons security entirely (dangerous). Option D unnecessarily restricts legitimate use.

    **Concept Tested:** MCP Security Standards

    **Bloom's Level:** Understand

    **See:** [Section 2: MCP Security Standards](index.md#2-model-context-protocol-secure-ai-integration-architecture)

---

#### 4. What is "agent orchestration" in multi-agent systems?

<div class="upper-alpha" markdown>
1. A type of musical performance by AI systems
2. Agents working independently without any coordination
3. All agents must be identical with no specialization
4. Coordinating multiple specialized agents through patterns like sequential, parallel, hierarchical, or autonomous collaboration to accomplish complex objectives
</div>

??? question "Show Answer"
    The correct answer is **D**. Agent orchestration coordinates multiple specialized agents working toward complex IR objectives through various patterns: sequential (agents execute in order, passing results forward), parallel (agents work simultaneously on independent sub-tasks), hierarchical (supervisor agent delegates to worker agents and aggregates results), or autonomous collaboration (agents negotiate and coordinate dynamically). This enables complex workflows beyond single-agent capabilities. Option A misinterprets the technical term metaphorically. Option B describes the absence of orchestration. Option C eliminates the value of specialization.

    **Concept Tested:** Agent Orchestration, Multi-Agent Coordination

    **Bloom's Level:** Understand

    **See:** [Section 3: Agent Orchestration Patterns](index.md#3-agent-orchestration-patterns-coordinating-specialized-agents)

---

#### 5. Which agentic application generates daily, weekly, or event-driven briefings autonomously?

<div class="upper-alpha" markdown>
1. Automated IR Reports that compile market data, investor activity, sentiment analysis, and competitive intelligence into stakeholder briefings
2. Manual spreadsheet creation requiring full human effort
3. Systems that only generate reports once per decade
4. Non-automated processes with no AI involvement
</div>

??? question "Show Answer"
    The correct answer is **A**. Automated IR Reports use agentic systems to autonomously generate daily briefings (market activity, overnight news, scheduled events), weekly summaries (investor meetings, sentiment trends, analyst activity), or event-driven reports (triggered by earnings announcements, M&A news, activist filings). Agents retrieve data from multiple sources, perform analysis, identify anomalies, and generate structured briefings distributed to IR teams and executives. This eliminates manual report compilation. Option B describes traditional manual processes. Options C and D don't characterize automated reporting frequency or capabilities.

    **Concept Tested:** Automated IR Reports, Automated Report Tools

    **Bloom's Level:** Remember

    **See:** [Section 4: Practical Agentic Applications](index.md#4-practical-agentic-applications-in-investor-relations)

---

#### 6. What is the primary function of "crisis AI assistance" in investor relations?

<div class="upper-alpha" markdown>
1. Creating crises to generate media attention
2. Rapid situation assessment, draft communication generation, and stakeholder analysis during unexpected negative events like earnings misses, executive departures, or regulatory investigations
3. Preventing all crises from ever occurring
4. Ignoring crises entirely and hoping they resolve themselves
</div>

??? question "Show Answer"
    The correct answer is **B**. Crisis AI assistance provides rapid situation assessment (analyzing immediate impact, sentiment, media coverage), draft communication generation (preparing holding statements, investor FAQs, analyst talking points), stakeholder analysis (identifying most affected investors, predicting questions), and timeline management (coordinating disclosure requirements, communication sequencing). Agents accelerate crisis response from hours to minutes, though human judgment remains essential for final decisions. Option A confuses crisis response with crisis creation. Option C overstates—some crises are unpreventable. Option D represents dangerous negligence.

    **Concept Tested:** Crisis AI Assistance

    **Bloom's Level:** Apply

    **See:** [Section 4: Practical Agentic Applications](index.md#4-practical-agentic-applications-in-investor-relations)

---

#### 7. How do "earnings prep simulators" help executives prepare for earnings calls?

<div class="upper-alpha" markdown>
1. By guaranteeing that no difficult questions will be asked
2. By canceling all earnings calls to avoid preparation
3. AI agents simulate realistic analyst questioning based on recent reports, historical patterns, and company performance to prepare executives through practice Q&A sessions
4. By providing generic questions unrelated to the company
</div>

??? question "Show Answer"
    The correct answer is **C**. Earnings prep simulators use AI agents to generate realistic analyst questions based on recent analyst reports, historical questioning patterns, company performance versus expectations, competitive developments, and sector trends. Agents simulate actual earnings call Q&A, allowing executives to practice responses, identify gaps in prepared answers, and develop messaging strategies. This preparation improves call performance and reduces unforced errors. Option A is unrealistic—simulators prepare for difficult questions, don't prevent them. Option B defeats the purpose of investor communication. Option D provides no value—questions must be company-specific.

    **Concept Tested:** Earnings Prep Simulators

    **Bloom's Level:** Apply

    **See:** [Section 4: Practical Agentic Applications](index.md#4-practical-agentic-applications-in-investor-relations)

---

#### 8. What do "proxy firm simulations" predict?

<div class="upper-alpha" markdown>
1. Future stock prices with perfect accuracy
2. The weather during annual meetings
3. Next quarter's revenue for all companies
4. ISS and Glass Lewis voting recommendations for governance proposals based on their published methodologies and company governance characteristics
</div>

??? question "Show Answer"
    The correct answer is **D**. Proxy firm simulations use predictive models to forecast how influential proxy advisory firms (Institutional Shareholder Services and Glass Lewis) will vote on governance proposals (executive compensation, board elections, shareholder proposals) based on their published methodologies, historical voting patterns, company governance characteristics, and peer comparisons. This allows companies to anticipate opposition, adjust proposals, or prepare counterarguments before proxy season. Option A overstates prediction capability—prices aren't perfectly predictable. Options B and C are unrelated to proxy advisory forecasting.

    **Concept Tested:** Proxy Firm Simulations

    **Bloom's Level:** Remember

    **See:** [Section 4: Practical Agentic Applications](index.md#4-practical-agentic-applications-in-investor-relations)

---

#### 9. In MCP architecture, what is the purpose of comprehensive audit trails?

<div class="upper-alpha" markdown>
1. Recording every agent action (which agent, which tool, which parameters, timestamp, result) for compliance, debugging, and accountability
2. Preventing any AI usage within the organization
3. Making systems slower and less efficient
4. Audit trails serve no purpose and should be eliminated
</div>

??? question "Show Answer"
    The correct answer is **A**. Comprehensive audit trails record every agent action: which agent accessed what data, which tools were invoked, which parameters were used, timestamps, and results. These immutable logs serve multiple purposes: regulatory compliance (demonstrating proper access controls), debugging (diagnosing errors or unexpected behavior), accountability (tracking who approved what actions), and security (detecting unauthorized access or anomalous behavior). Audit trails are foundational for enterprise AI deployment with material nonpublic information. Option B confuses auditing with prohibition. Option C mischaracterizes—well-designed logging has minimal performance impact. Option D is dangerous and non-compliant.

    **Concept Tested:** MCP Security Standards, MCP Architecture Overview

    **Bloom's Level:** Understand

    **See:** [Section 2: MCP Security Standards](index.md#2-model-context-protocol-secure-ai-integration-architecture)

---

#### 10. What are "vote solicitation bots" designed to accomplish?

<div class="upper-alpha" markdown>
1. Automatically changing shareholder votes without permission
2. Increasing proxy voting participation through personalized outreach, voting reminders, and simplified voting processes for retail and institutional shareholders
3. Preventing shareholders from voting on any proposals
4. Generating fake votes to manipulate outcomes
</div>

??? question "Show Answer"
    The correct answer is **B**. Vote solicitation bots use automated systems to increase proxy voting participation through personalized outreach (customized emails to different shareholder types), voting reminders (multi-channel nudges before deadlines), simplified voting processes (one-click voting links, mobile-friendly interfaces), and follow-up (contacting non-voters). Higher participation improves governance legitimacy and reduces activist vulnerability. These systems operate within regulatory requirements for proxy solicitation. Option A describes illegal vote manipulation. Option C is the opposite of the goal. Option D describes fraud.

    **Concept Tested:** Vote Solicitation Bots

    **Bloom's Level:** Apply

    **See:** [Section 4: Practical Agentic Applications](index.md#4-practical-agentic-applications-in-investor-relations)

---

#### 11. What is a key advantage of "news aggregation AI" for IR teams?

<div class="upper-alpha" markdown>
1. News aggregation AI eliminates the need to ever read news
2. AI-generated fake news to mislead investors
3. Autonomous systems collecting, categorizing, and summarizing news relevant to IR from diverse sources (company mentions, competitors, sector, regulatory) saving hours of manual monitoring
4. Aggregation has no benefits for IR workflows
</div>

??? question "Show Answer"
    The correct answer is **C**. News aggregation AI autonomously collects news from diverse sources (financial media, industry publications, regulatory feeds, social media), categorizes by relevance (company mentions, competitor news, sector trends, regulatory developments), filters noise (removing irrelevant content), summarizes key articles (extracting main points), and delivers structured briefings. This saves IR teams hours of manual monitoring while ensuring comprehensive coverage. Agents flag breaking news requiring immediate attention. Option A overstates—human judgment remains important for strategic interpretation. Option B describes misinformation (opposite of the tool's purpose). Option D ignores obvious efficiency benefits.

    **Concept Tested:** News Aggregation AI, Agents for Data Retrieval

    **Bloom's Level:** Analyze

    **See:** [Section 4: Practical Agentic Applications](index.md#4-practical-agentic-applications-in-investor-relations)

---

#### 12. Why must agentic systems include "human-in-the-loop checkpoints" for high-stakes actions?

<div class="upper-alpha" markdown>
1. Humans are completely unnecessary and should be removed from all processes
2. Checkpoints slow down systems with no benefits
3. Agents can query and analyze autonomously, but only humans should make final decisions
4. High-stakes actions (publishing investor communications, filing SEC documents, material disclosures) require explicit human approval to ensure accountability, compliance, and strategic alignment
</div>

??? question "Show Answer"
    The correct answer is **D**. Despite agentic autonomy for analysis and drafting, high-stakes actions require explicit human approval because: compliance and legal liability (humans remain accountable for regulatory violations), strategic judgment (nuanced decisions about disclosure level, timing, messaging tone), error prevention (catching agent mistakes before public distribution), stakeholder relationships (preserving trust through responsible communication), and materiality assessment (determining what constitutes material information). Agents accelerate preparation but humans make final decisions on sensitive matters. Option A is reckless—human oversight is essential. Option B ignores risk management value. Option C is incomplete—doesn't explain why checkpoints matter.

    **Concept Tested:** Agent-Based IR Workflows, MCP Security Standards

    **Bloom's Level:** Analyze

    **See:** [Section 1: Characteristics of Agentic AI](index.md#1-from-task-automation-to-autonomous-agents)

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
- **Concepts Covered:** 12 of 18 chapter concepts (67%)
- **Estimated Completion Time:** 20-25 minutes

---

## Next Steps

After completing this quiz:

1. Review the [Chapter Summary](index.md#summary) to reinforce agentic AI and MCP concepts
2. Work through the [Chapter Exercises](index.md#exercises) for hands-on agent design practice
3. Proceed to [Chapter 11: AI Governance, Ethics, and Risk Management](../11-ai-governance-ethics-risk/index.md)

For additional practice questions, see the [Quiz Bank](../../learning-graph/quiz-bank.json).
