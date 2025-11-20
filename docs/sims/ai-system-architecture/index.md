---
title: AI System Architecture
description: Interactive visualization of modern agentic AI system architecture using the Model Context Protocol (MCP) for secure enterprise AI applications in investor relations.
image: /sims/ai-system-architecture/ai-system-architecture.png
og:image: /sims/ai-system-architecture/ai-system-architecture.png
twitter:image: /sims/ai-system-architecture/ai-system-architecture.png
social:
   cards: false
---

# AI System Architecture: Agentic Systems with MCP

<iframe src="main.html" height="1100px" width="100%" scrolling="no"></iframe>

[Run the AI System Architecture MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## Description

The AI System Architecture MicroSim provides an interactive visualization of how modern agentic AI systems are architected for enterprise use, with specific focus on the **Model Context Protocol (MCP)** introduced by Anthropic. This educational tool helps IR professionals, IT leaders, and students understand the components, data flows, and security layers required for deploying AI systems safely in sensitive business contexts like investor relations.

### How It Works

This MicroSim visualizes a complete agentic AI architecture using **network graph representation** where:

- **Nodes**: System components (LLMs, MCP servers, data sources, tools, security layers)
- **Edges**: Data flows and communication pathways between components
- **Colors**: Component types (Core AI, MCP, Data Sources, Tools, Security)
- **Shapes**: Functional categories (boxes for processing, diamonds for protocols, databases for storage)

**Key Features:**

- **Interactive Architecture**: Click and drag components to explore system structure
- **Multiple Views**: Switch between Full Architecture, MCP Focus, Data Flow, and Security Layers
- **Component Details**: Click any node to see detailed descriptions and technical specifications
- **Real-time Layout**: Network automatically arranges components for optimal visualization
- **Educational Annotations**: Labeled connections show data flow and relationships

### Architecture Components

**1. Core AI Layer** (Red/Orange)

- **LLM (Claude/GPT)**: The foundation model providing natural language understanding and generation
- **Agentic Layer**: Orchestration framework enabling autonomous behavior, tool use, and multi-step reasoning

**2. Model Context Protocol (MCP) Layer** (Teal/Blue)

- **MCP Server**: Standardized protocol server providing controlled access to resources, prompts, and tools
- **MCP Client**: Client-side implementation connecting the AI application to MCP servers

**3. Data Sources** (Green)

- **SEC EDGAR**: Public filings (10-K, 10-Q, 8-K, proxies)
- **IR CRM**: Investor relationship management data
- **Market Data**: Real-time prices, trading data, analyst estimates
- **Internal Databases**: Company financial and operational data

**4. AI Tools** (Orange/Pink)

- **Sentiment Analysis**: Analyzing sentiment in communications
- **Report Generation**: Automated creation of investor materials
- **Q&A Preparation**: Predicting and preparing for analyst questions
- **Compliance Checker**: Automated Reg FD and disclosure review

**5. Security & Governance** (Purple)

- **Authentication**: Identity verification and access control
- **Audit Trail**: Comprehensive logging for compliance and oversight

**6. User Interface** (Yellow)

- **IR Dashboard**: Web application where IR team interacts with AI capabilities

### Understanding the MCP Architecture

The **Model Context Protocol (MCP)** is the key innovation enabling secure, scalable enterprise AI:

**Why MCP Matters:**

- **Standardization**: Single protocol for connecting AI to any data source or tool
- **Security**: Built-in authentication, authorization, and access control
- **Modularity**: Add new data sources without changing core AI application
- **Governance**: Centralized control over what data AI can access
- **Vendor Independence**: Open protocol not tied to specific LLM provider

**How MCP Works in This Architecture:**

1. User makes request through IR Dashboard
2. Agentic layer determines it needs external data
3. Agent calls MCP Client with data request
4. MCP Client connects to MCP Server via standardized protocol
5. MCP Server authenticates, checks permissions, fetches data
6. Data returns through MCP channel to agent
7. Agent uses data to formulate response via LLM
8. All activity logged to audit trail

**MCP vs. Direct Integration:**

- **Without MCP**: Each data source requires custom integration, security model, API handling
- **With MCP**: Single standardized protocol, uniform security, pluggable architecture

### Educational Value

This MicroSim demonstrates several key concepts from Chapter 10 (Agentic AI Systems and MCP):

1. **Agentic Architecture**: How autonomous AI systems are structured with planning, tool use, and iteration
2. **MCP Protocol**: The role of standardized protocols in enterprise AI deployment
3. **Data Governance**: How data access is controlled and audited in AI systems
4. **Security Layers**: Multi-layered approach to securing AI in sensitive business contexts
5. **Tool Integration**: How specialized AI tools extend core LLM capabilities

### Architecture Views

Use the view buttons to explore different perspectives:

**Full Architecture**: See all components and their interconnections

**MCP Focus**: Isolate the MCP protocol layer showing how it mediates between AI and data sources

**Data Flow**: Trace the path from user request through AI processing to data retrieval and response

**Security Layers**: Examine authentication, authorization, and audit trail components

## Lesson Plan

### Learning Objectives

After using this MicroSim, students will be able to:

1. **Understand** the components of a modern agentic AI system architecture (Bloom's: Understand)
2. **Analyze** how the Model Context Protocol enables secure enterprise AI (Bloom's: Analyze)
3. **Evaluate** the security and governance mechanisms required for AI in IR (Bloom's: Evaluate)
4. **Create** architecture diagrams for proposed AI implementations (Bloom's: Create)

### Suggested Activities

#### Activity 1: Architecture Component Discovery (15 minutes)

1. Start with "Full Architecture" view
2. Click each component type (LLM, MCP Server, Data Sources, Tools, Security)
3. Read the description and technical details for each
4. **Reflection Questions**:
   - Which components are essential (cannot be removed)?
   - Which components provide governance and oversight?
   - How many different data sources are integrated?

#### Activity 2: MCP Protocol Deep Dive (20 minutes)

1. Click "MCP Focus" view to isolate MCP components
2. Trace the connections from Agentic Layer → MCP Client → MCP Server → Data Sources
3. Click the MCP Server node and read its description
4. **Discussion Questions**:
   - What problem does MCP solve?
   - How does MCP provide security benefits over direct data access?
   - Why might organizations prefer MCP over building custom integrations?
   - What role does the MCP Server play in governance?

#### Activity 3: Data Flow Tracing (20 minutes)

1. Click "Data Flow" view
2. Start at "IR Dashboard" (user interface)
3. Trace a hypothetical request: "Summarize our last 10-K filing"
4. Follow the path through: UI → Agent → LLM ← → MCP → SEC EDGAR
5. **Exercise**:
   - Document each step in the data flow
   - Identify where security checks occur
   - Note where audit logging happens
   - Explain the role of each component in the chain

#### Activity 4: Security Architecture Analysis (25 minutes)

1. Click "Security Layers" view
2. Identify all security and governance components (Authentication, Audit Trail, Compliance)
3. Trace where security controls are applied
4. **Analysis Tasks**:
   - List all security mechanisms visible in the architecture
   - Explain how Reg FD compliance is enforced
   - Describe the audit trail's role in governance
   - Identify potential security vulnerabilities or gaps

**Advanced Question**: How would you enhance this architecture to meet SOC 2 compliance requirements?

#### Activity 5: Architecture Design Exercise (45 minutes)

**Scenario**: Your company wants to deploy an AI assistant for the IR team that can:
- Answer analyst questions using historical transcripts
- Draft press releases for earnings announcements
- Monitor social media sentiment about the company
- Check all outputs for Reg FD compliance

**Tasks**:
1. Using this MicroSim as a reference, sketch your own architecture diagram
2. Identify which components from this MicroSim you'd reuse
3. Specify additional data sources needed (e.g., social media APIs, transcript database)
4. Add security controls appropriate for this use case
5. **Deliverable**: Present your architecture with justification for each component

### Integration with Chapter 10

This MicroSim connects to these Chapter 10 topics:

- **Section 2**: Agentic AI Systems - visualizes the agent orchestration layer
- **Section 3**: Model Context Protocol - demonstrates MCP architecture and benefits
- **Section 5**: Tool Integration - shows how specialized AI tools extend capabilities
- **Section 7**: Security and Governance - illustrates security layers and audit mechanisms
- **Section 9**: Implementation Patterns - provides reference architecture for deployment

### Prerequisites

- Understanding of basic AI concepts (LLMs, prompts, responses) from Chapter 5
- Awareness of investor relations workflows and data needs (Chapter 1)
- Familiarity with data governance concepts (Chapter 12)
- Basic understanding of system architecture diagrams

### Assessment Opportunities

**Formative Assessment:**
- Can students identify and describe each component type?
- Can they explain the purpose of MCP in this architecture?
- Can they trace data flow from user request to response?

**Summative Assessment:**
- Have students design a complete AI architecture for a specific IR use case
- Ask students to write a 3-page technical specification for implementing this architecture
- Have students present security review findings identifying risks and mitigations
- Create a quiz on component roles and data flow pathways

### Extension Activities

**For Advanced Students:**

1. **Comparative Analysis**: Research alternative agentic AI frameworks (LangChain, AutoGPT, CrewAI) and compare to this architecture
2. **MCP Server Implementation**: Explore the MCP specification and design a custom MCP server for a proprietary data source
3. **Security Hardening**: Propose additional security controls for this architecture to meet financial services regulations
4. **Scalability Analysis**: Analyze bottlenecks and propose scaling strategies for high-volume IR operations
5. **Multi-Agent Systems**: Extend this architecture to support multiple specialized agents collaborating on complex IR tasks

### Educator Notes

**Timing**: Allow 90-120 minutes for a complete lesson using all activities

**Group Size**: Best for small groups (2-4 students) for architecture design exercises

**Technical Background**: Requires some technical literacy but not programming skills

**Common Challenges:**

- Abstract architecture diagrams may be initially confusing
  - Counter: Start with "Data Flow" view showing a single request path
- MCP protocol concept may seem unnecessary
  - Counter: Compare to scenario without MCP (custom integrations for each data source)
- Security components may seem like overhead
  - Counter: Discuss real consequences of AI data leaks or compliance violations

**Discussion Prompts:**

- "Why can't we just connect the LLM directly to all data sources?"
- "What could go wrong if there's no audit trail?"
- "How does this architecture prevent selective disclosure violations?"
- "What happens if the MCP server is compromised?"
- "How would you modify this architecture for a smaller company vs. Fortune 500?"

**Real-World Context:**

This architecture reflects production AI systems deployed at major companies:
- MCP protocol announced by Anthropic (November 2024) and rapidly adopted
- Agentic frameworks like LangChain power thousands of enterprise AI applications
- Audit trails and compliance checks are mandatory for AI in regulated industries
- Multi-layered security essential for AI accessing confidential business data

### Technical Details

**Framework**: vis-network (vis.js)
**Library Version**: Latest from unpkg CDN
**Browser Compatibility**: Chrome, Firefox, Safari, Edge (modern versions)
**Mobile-Friendly**: Partially (best on desktop/tablet due to detail level)
**Accessibility**: Keyboard navigation, descriptive labels, screen reader compatible

**Network Configuration:**

- **Layout**: Force-directed with Barnes-Hut physics
- **Components**: 15 nodes representing system architecture elements
- **Connections**: 23 edges showing data flow and relationships
- **Interactive Views**: 4 pre-configured filtered views plus full architecture

---

## Embedding This MicroSim

You can include this MicroSim on your website using the following `iframe`:

```html
<iframe src="https://[your-domain]/sims/ai-system-architecture/main.html"
        height="1100px"
        width="100%"
        scrolling="no">
</iframe>
```

---

## Additional Resources

- [Chapter 10: Agentic AI Systems and MCP](../../chapters/10-agentic-ai-systems-mcp/index.md) - Full chapter on agentic AI architectures
- [Anthropic: Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) - Official MCP announcement and specification
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction) - Leading agentic AI framework
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Governance framework for AI systems

---

**Reminder**: Create a screenshot named `ai-system-architecture.png` (1400×900px) showing the full MicroSim architecture for optimal social media previews when sharing this resource.
