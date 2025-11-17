#!/usr/bin/env python3
"""
Generate 15-chapter structure with all 298 concepts properly assigned
"""

import json
from pathlib import Path
from collections import defaultdict

def load_learning_graph(path):
    with open(path, 'r') as f:
        return json.load(f)

def analyze_dependencies(lg):
    """Build dependency mappings"""
    prereqs = defaultdict(list)
    for edge in lg['edges']:
        prereqs[edge['to']].append(edge['from'])
    return prereqs

def get_concept_by_label(nodes, label):
    """Find concept by label (case-insensitive partial match)"""
    label_lower = label.lower()
    for node in nodes:
        if label_lower in node['label'].lower():
            return node
    return None

def assign_concepts_to_chapters(lg):
    """Assign all 298 concepts to 15 chapters"""
    nodes = lg['nodes']
    prereqs = analyze_dependencies(lg)

    # Create lookup by taxonomy and label
    by_taxonomy = defaultdict(list)
    for node in nodes:
        by_taxonomy[node.get('group', 'OTHER')].append(node)

    # Sort each taxonomy by label
    for tax in by_taxonomy:
        by_taxonomy[tax].sort(key=lambda n: n['label'])

    # Manual chapter assignments based on revised structure
    chapters = []

    # Chapter 1: Foundations of Modern IR (18 concepts)
    ch1 = [n for n in nodes if n['label'] in [
        'Investor Relations Function', 'Corporate Valuation Strategy', 'Market Communication Strategy',
        'Shareholder Engagement', 'Key Performance Indicators', 'IR Engagement Metrics',
        'Tracking Investor Outreach', 'Meeting Effectiveness', 'Response Time Analytics',
        'Earnings Reporting Process', 'Investor Targeting Methods', 'Q&A Preparation Techniques',
        'Annual General Meetings', 'Investor Presentations', 'Roadshow Planning',
        'Earnings Call Scripts', 'Press Release Drafting', 'Proxy Season Management'
    ]]
    chapters.append(('Foundations of Modern Investor Relations', ch1))

    # Chapter 2: Regulatory Frameworks (28 concepts - all REG-COMP)
    ch2 = by_taxonomy['REG-COMP']
    chapters.append(('Regulatory Frameworks and Compliance', ch2))

    # Chapter 3: Investor Types (14 concepts)
    ch3 = [n for n in nodes if n['label'] in [
        'Institutional Investors', 'Retail Investors', 'Hedge Funds', 'Mutual Funds',
        'Pension Funds', 'Sovereign Wealth Funds', 'Buy-Side Analysts', 'Sell-Side Analysts',
        'Investment Bank Relations', 'Analyst Coverage Review', 'Consensus Estimates',
        'Earnings Guidance Strategy', 'Guidance Withdrawal Risks', 'Setting Guidance Ranges',
        'Beat-and-Raise Tactics'
    ]]
    chapters.append(('Investor Types and Market Dynamics', ch3))

    # Chapter 4: Valuation Metrics (26 concepts - all VALMET)
    ch4 = by_taxonomy['VALMET']
    chapters.append(('Valuation Metrics and Performance Indicators', ch4))

    # Chapter 5: AI/ML Fundamentals (12 concepts - AI-TECH + some AGENTIC intro)
    ch5 = by_taxonomy['AI-TECH'].copy()
    # Add basic agent concepts (intro only)
    ch5.extend([n for n in nodes if n['label'] in [
        'Agentic AI Systems', 'Autonomous AI Agents'
    ]])
    chapters.append(('AI and Machine Learning Fundamentals', ch5))

    # Chapter 6: AI Content Creation (10 concepts - all AI-CONT)
    ch6 = by_taxonomy['AI-CONT']
    chapters.append(('AI-Powered Content Creation', ch6))

    # Chapter 7: Sentiment Analysis Methods (24 concepts - ANLYT subset)
    sentiment_keywords = ['Sentiment', 'NLP', 'Text Mining', 'Natural Language',
                          'News', 'Social', 'Media', 'Analyst Report', 'Feedback',
                          'Voice Tone', 'Monitoring']
    ch7 = [n for n in by_taxonomy['ANLYT'] if any(kw in n['label'] for kw in sentiment_keywords)]
    chapters.append(('Sentiment Analysis: Signals and Methods', ch7))

    # Chapter 8: Predictive Analytics (remaining ANLYT)
    ch8 = [n for n in by_taxonomy['ANLYT'] if n not in ch7]
    chapters.append(('Predictive Analytics and Market Intelligence', ch8))

    # Chapter 9: Personalized Engagement (NEW - cross-taxonomy)
    # Mix of AGENTIC, ANLYT, TRANSFORM related to personalization
    ch9 = [n for n in nodes if any(kw in n['label'] for kw in [
        'Targeting AI', 'Dashboard', 'Real-Time', 'Chatbot', 'Briefing',
        'Live Data', 'Designing Dashboards', 'Integrating Live Data',
        'Agents for Data Retrieval', 'Personali', 'Engagement'
    ]) and n not in ch1 and n not in ch7 and n not in ch8]
    # Ensure we have ~18 concepts
    if len(ch9) < 18:
        # Add some IR-OPS and analytics concepts
        ch9.extend([n for n in nodes if n['label'] in [
            'Earnings Guidance Strategy', 'IR Engagement Metrics'
        ] and n not in ch1 and n not in ch3])
    chapters.append(('Personalized and Real-Time Investor Engagement', ch9[:18]))

    # Chapter 10: Agentic AI (27 concepts - remaining AGENTIC)
    ch10 = [n for n in by_taxonomy['AGENTIC'] if n not in ch5 and n not in ch9]
    # Add MCP concepts
    ch10.extend([n for n in nodes if 'MCP' in n['label'] or 'Model Context Protocol' in n['label']])
    chapters.append(('Agentic AI Systems and Model Context Protocol', ch10))

    # Chapter 11: AI Governance (24 concepts - AI-GOV)
    ch11 = by_taxonomy['AI-GOV']
    chapters.append(('AI Governance, Ethics, and Risk Management', ch11))

    # Chapter 12: Data Governance (24 concepts - DATA-GOV)
    ch12 = by_taxonomy['DATA-GOV']
    chapters.append(('Data Governance and Security', ch12))

    # Chapter 13: IR Platforms & Tools (23 concepts - TRANSFORM subset + case studies)
    platform_keywords = ['Platform', 'Bloomberg', 'FactSet', 'Nasdaq', 'Q4', 'AlphaSense',
                         'Salesforce', 'Tableau', 'Power BI', 'Ipreo', 'Broadridge',
                         'Computershare', 'Intralinks', 'DealCloud', 'Thomson Reuters',
                         'Case Study', 'Tesla', 'Apple', 'Amazon', 'Berkshire', 'Enron',
                         'Theranos', 'WeWork', 'GameStop', 'VW', 'Bitcoin']
    ch13 = [n for n in by_taxonomy['TRANSFORM'] if any(kw in n['label'] for kw in platform_keywords)]
    # Add IR-FOUND case studies
    ch13.extend([n for n in by_taxonomy['IR-FOUND'] if 'Case' in n['label'] or any(comp in n['label'] for comp in ['Tesla', 'Apple', 'Amazon', 'Berkshire', 'WeWork'])])
    # Add IR-OPS case studies
    ch13.extend([n for n in by_taxonomy['IR-OPS'] if any(comp in n['label'] for comp in ['Apple', 'Berkshire'])])
    chapters.append(('IR Platforms, Tools, and Case Studies', ch13))

    # Chapter 14: Transformation & Change (remaining TRANSFORM)
    ch14 = [n for n in by_taxonomy['TRANSFORM'] if n not in ch9 and n not in ch13]
    chapters.append(('Transformation Strategy and Change Management', ch14))

    # Chapter 15: Future Outlook (NEW - forward-looking concepts)
    future_keywords = ['Neural Net', 'Deep Learning', 'Reinforcement', 'Feature Engineering',
                       'Model Training', 'Unsupervised', 'Supervised', 'Advanced',
                       'Future', 'Next-Gen', 'Emerging']
    ch15 = [n for n in nodes if any(kw in n['label'] for kw in future_keywords)
            and n not in [c for _, concepts in chapters for c in concepts]]
    # If we need more concepts, add some advanced TRANSFORM concepts
    if len(ch15) < 10:
        advanced_transform = [n for n in by_taxonomy['TRANSFORM']
                             if n not in [c for _, concepts in chapters for c in concepts]][:12-len(ch15)]
        ch15.extend(advanced_transform)
    chapters.append(('Future Outlook: Agentic Ecosystems and Next-Gen IR', ch15))

    return chapters

def validate_assignments(chapters, total_expected=298):
    """Validate chapter assignments"""
    assigned_ids = set()
    duplicates = []

    for title, concepts in chapters:
        for concept in concepts:
            if concept['id'] in assigned_ids:
                duplicates.append((concept['label'], title))
            assigned_ids.add(concept['id'])

    print(f"\n{'='*80}")
    print(f"VALIDATION REPORT")
    print(f"{'='*80}")
    print(f"Total concepts assigned: {len(assigned_ids)}")
    print(f"Expected: {total_expected}")
    print(f"Missing: {total_expected - len(assigned_ids)}")

    if duplicates:
        print(f"\n⚠️  WARNING: {len(duplicates)} duplicate assignments:")
        for label, chapter in duplicates[:5]:
            print(f"   - {label} in {chapter}")
    else:
        print("✅ No duplicates found")

    print(f"\nChapter sizes:")
    for i, (title, concepts) in enumerate(chapters, 1):
        print(f"  Ch {i:2d}: {len(concepts):2d} concepts - {title}")

    return len(assigned_ids) == total_expected and len(duplicates) == 0

def print_chapter_summary(chapters):
    """Print detailed chapter summary"""
    print(f"\n{'='*80}")
    print(f"15-CHAPTER STRUCTURE - DETAILED BREAKDOWN")
    print(f"{'='*80}\n")

    for i, (title, concepts) in enumerate(chapters, 1):
        print(f"\nChapter {i}: {title}")
        print(f"{'-'*80}")
        print(f"Total Concepts: {len(concepts)}")

        # Show taxonomy distribution
        tax_dist = defaultdict(int)
        for c in concepts:
            tax_dist[c.get('group', 'OTHER')] += 1
        print(f"Taxonomies: {dict(tax_dist)}")

        # Show all concepts
        print(f"\nConcepts:")
        for j, c in enumerate(sorted(concepts, key=lambda x: x['label']), 1):
            print(f"  {j:2d}. {c['label']}")

def save_chapter_data(chapters, output_path):
    """Save chapter assignments to JSON for later use"""
    data = {
        'total_chapters': len(chapters),
        'total_concepts': sum(len(concepts) for _, concepts in chapters),
        'chapters': [
            {
                'number': i,
                'title': title,
                'concept_count': len(concepts),
                'concepts': [
                    {
                        'id': c['id'],
                        'label': c['label'],
                        'group': c.get('group', 'OTHER')
                    }
                    for c in concepts
                ]
            }
            for i, (title, concepts) in enumerate(chapters, 1)
        ]
    }

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\n✅ Chapter assignments saved to: {output_path}")

if __name__ == '__main__':
    lg_path = Path('/Users/davidberglund/ir-textbook/docs/learning-graph/learning-graph.json')
    output_path = Path('/Users/davidberglund/ir-textbook/chapter-assignments.json')

    print("Loading learning graph...")
    lg = load_learning_graph(lg_path)

    print(f"Total concepts in graph: {len(lg['nodes'])}")

    print("\nAssigning concepts to 15 chapters...")
    chapters = assign_concepts_to_chapters(lg)

    # Validate
    is_valid = validate_assignments(chapters, len(lg['nodes']))

    # Print summary
    print_chapter_summary(chapters)

    # Save for later use
    save_chapter_data(chapters, output_path)

    if is_valid:
        print("\n✅ All concepts successfully assigned to chapters!")
    else:
        print("\n⚠️  Some concepts missing or duplicated. Review assignments.")
