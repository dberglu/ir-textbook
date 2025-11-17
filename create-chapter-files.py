#!/usr/bin/env python3
"""
Generate index.md files for all 15 chapters based on chapter-assignments.json
"""

import json
from pathlib import Path

# Chapter URL mappings
CHAPTER_URLS = {
    1: '01-foundations-of-modern-ir',
    2: '02-regulatory-frameworks-compliance',
    3: '03-investor-types-market-dynamics',
    4: '04-valuation-metrics-performance',
    5: '05-ai-ml-fundamentals',
    6: '06-ai-powered-content-creation',
    7: '07-sentiment-analysis-methods',
    8: '08-predictive-analytics-intelligence',
    9: '09-personalized-realtime-engagement',
    10: '10-agentic-ai-systems-mcp',
    11: '11-ai-governance-ethics-risk',
    12: '12-data-governance-security',
    13: '13-ir-platforms-tools-case-studies',
    14: '14-transformation-strategy-change',
    15: '15-future-agentic-ecosystems'
}

# One-sentence summaries for each chapter
CHAPTER_SUMMARIES = {
    1: "This chapter introduces the strategic role of investor relations in capital markets, covering core IR functions, essential workflows, and fundamental stakeholder engagement practices that establish the context for AI transformation.",
    2: "This chapter examines the regulatory environment—particularly Regulation Fair Disclosure and Sarbanes-Oxley—governing all IR activities and shaping how AI tools must be designed and deployed to ensure compliance.",
    3: "This chapter explores the diverse landscape of institutional and retail investors, analyst types, and market engagement strategies that IR professionals must navigate to effectively communicate corporate value.",
    4: "This chapter covers financial metrics, valuation multiples, market indicators, and performance measurement techniques that IR professionals use to communicate corporate value to the investment community.",
    5: "This chapter provides foundational knowledge of artificial intelligence and machine learning, including LLMs, RAG, model quality assessment, and the basic concepts of agentic systems that enable AI-powered IR.",
    6: "This chapter explores how generative AI can enhance IR content creation through prompt engineering, structured templates, tone analysis, and compliance-aware workflows while maintaining narrative consistency.",
    7: "This chapter examines sentiment analysis methodologies, NLP techniques for processing transcripts and news, feature engineering strategies, and dataset selection for converting market signals into actionable IR intelligence.",
    8: "This chapter covers predictive analytics applications including forecasting investor behavior, scenario modeling, early-warning indicators, and linking analytical insights to strategic IR actions like roadshows and briefings.",
    9: "This chapter introduces next-generation IR approaches including investor digital twins, real-time monitoring, multimodal analysis of calls and presentations, and personalized engagement strategies that deliver right-time outreach.",
    10: "This chapter details autonomous AI agents, Model Context Protocol architecture for secure AI integration, agent orchestration patterns, and practical applications of agentic systems in IR workflows and automation.",
    11: "This chapter establishes governance frameworks for responsible AI use in IR, covering bias mitigation, hallucination detection, ethical considerations, and risk management practices essential for maintaining market trust.",
    12: "This chapter addresses data quality, security standards, privacy compliance, audit trails, and risk management frameworks necessary for building trustworthy data foundations that support AI-powered IR.",
    13: "This chapter surveys leading IR platforms (Q4, Bloomberg, FactSet, Nasdaq), analytical tools (Python, R, Tableau), and real-world case studies demonstrating successful and cautionary tales in IR strategy and execution.",
    14: "This chapter provides strategic frameworks for AI transformation including business case development, vendor selection, proof-of-concept design, change management models, and stakeholder alignment for successful AI adoption in IR.",
    15: "This chapter explores emerging trends including multi-agent ecosystems, multimodal reasoning, synthetic data, real-time investor copilots, autonomy boundaries, and advanced computing impacts on the future of IR."
}

def load_assignments(path):
    with open(path, 'r') as f:
        return json.load(f)

def generate_chapter_index(chapter_num, title, summary, concepts):
    """Generate index.md content for a chapter"""

    # Determine prerequisites
    if chapter_num == 1:
        prereq_text = """This chapter assumes only the prerequisites listed in the [course description](../../course-description.md):

- Working knowledge of corporate financial statements and capital markets
- Basic understanding of investor relations roles and disclosures
- Executive-level experience in digital, data, or innovation functions"""
    else:
        prereq_text = f"""This chapter builds on concepts from previous chapters. We recommend completing:

- [Chapter 1: Foundations of Modern Investor Relations](../01-foundations-of-modern-ir/index.md)"""

        # Add specific prerequisites for certain chapters
        if chapter_num >= 5:
            prereq_text += f"\n- Chapters 2-4 for regulatory and market context"
        if chapter_num >= 7:
            prereq_text += f"\n- [Chapter 5: AI and Machine Learning Fundamentals](../05-ai-ml-fundamentals/index.md)"

    # Build concept list
    concept_list = "\n".join([f"   {i}. {c['label']}" for i, c in enumerate(concepts, 1)])

    content = f"""# {title}

## Summary

{summary}

## Prerequisites

{prereq_text}

## Concepts Covered

This chapter covers the following {len(concepts)} concepts from the learning graph:

{concept_list}

---

**Status**: Chapter structure created. Content generation pending.

*Use the chapter-content-generator skill to populate this chapter with detailed educational content, diagrams, examples, and exercises.*
"""

    return content

def create_all_chapter_files(assignments, base_path):
    """Create index.md files for all chapters"""

    chapters = assignments['chapters']

    for ch in chapters:
        ch_num = ch['number']
        title = ch['title']
        concepts = ch['concepts']

        # Get URL path
        url_path = CHAPTER_URLS[ch_num]
        chapter_dir = base_path / url_path

        # Create directory if it doesn't exist
        chapter_dir.mkdir(parents=True, exist_ok=True)

        # Generate content
        summary = CHAPTER_SUMMARIES.get(ch_num, f"This chapter covers {len(concepts)} concepts related to {title.lower()}.")
        content = generate_chapter_index(ch_num, title, summary, concepts)

        # Write file
        index_file = chapter_dir / 'index.md'
        with open(index_file, 'w') as f:
            f.write(content)

        print(f"✅ Created: {index_file}")

def update_chapters_index(assignments, base_path):
    """Update the main chapters/index.md file"""

    chapters = assignments['chapters']

    chapter_links = []
    for ch in chapters:
        ch_num = ch['number']
        title = ch['title']
        url_path = CHAPTER_URLS[ch_num]
        summary = CHAPTER_SUMMARIES.get(ch_num, "")
        # Get first sentence only
        summary_short = summary.split('.')[0] + '.'

        chapter_links.append(f"{ch_num}. [{title}]({url_path}/index.md) - {summary_short}")

    content = f"""# Chapters

This textbook is organized into **15 chapters** covering **298 concepts** across investor relations fundamentals, AI technologies, analytics, governance, and strategic transformation.

## Chapter Overview

{chr(10).join(chapter_links)}

## How to Use This Textbook

This course follows a carefully designed learning progression:

1. **Chapters 1-4** establish IR fundamentals, regulatory frameworks, investor types, and valuation metrics
2. **Chapters 5-6** introduce AI/ML foundations and content creation applications
3. **Chapters 7-9** cover analytics, predictions, and personalized engagement
4. **Chapters 10-12** explore autonomous systems, AI governance, and data security
5. **Chapters 13-14** provide practical guidance on platforms, tools, and transformation strategy
6. **Chapter 15** looks ahead to emerging trends and future IR ecosystems

Each chapter builds on previous concepts, so we recommend following the sequence. However, experienced practitioners may skip foundational chapters based on their background.

## Chapter Structure

Each chapter includes:
- **Summary**: Overview of topics and learning objectives
- **Prerequisites**: Recommended prior knowledge
- **Concepts Covered**: Complete list of concepts from the learning graph
- **Content**: Detailed explanations, examples, diagrams, and case studies
- **Exercises**: Hands-on activities and reflection prompts
- **Quiz**: Assessment questions aligned with Bloom's taxonomy

---

**Note:** All chapters reference the [learning graph](../learning-graph/index.md) for concept dependencies and the [glossary](../glossary.md) for term definitions.
"""

    index_file = base_path / 'index.md'
    with open(index_file, 'w') as f:
        f.write(content)

    print(f"\n✅ Updated: {index_file}")

if __name__ == '__main__':
    assignments_path = Path('/Users/davidberglund/ir-textbook/chapter-assignments.json')
    chapters_base = Path('/Users/davidberglund/ir-textbook/docs/chapters')

    print("Loading chapter assignments...")
    assignments = load_assignments(assignments_path)

    print(f"\nCreating index.md files for {assignments['total_chapters']} chapters...\n")
    create_all_chapter_files(assignments, chapters_base)

    print("\nUpdating main chapters/index.md...")
    update_chapters_index(assignments, chapters_base)

    print(f"\n{'='*80}")
    print("✅ ALL CHAPTER FILES CREATED SUCCESSFULLY!")
    print(f"{'='*80}")
    print(f"\nTotal chapters: {assignments['total_chapters']}")
    print(f"Total concepts: {assignments['total_concepts']}")
    print("\nNext step: Update mkdocs.yml navigation")
