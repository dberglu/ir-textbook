#!/usr/bin/env python3
"""
Generate 15-chapter structure with all 298 concepts - FIXED VERSION
"""

import json
from pathlib import Path
from collections import defaultdict

def load_learning_graph(path):
    with open(path, 'r') as f:
        return json.load(f)

def assign_concepts_to_chapters_fixed(lg):
    """Assign all 298 concepts to 15 chapters - properly balanced"""
    nodes = lg['nodes']

    # Create lookup by taxonomy
    by_taxonomy = defaultdict(list)
    for node in nodes:
        by_taxonomy[node.get('group', 'OTHER')].append(node)

    # Sort each by label
    for tax in by_taxonomy:
        by_taxonomy[tax].sort(key=lambda n: n['label'])

    # Track assigned concepts to avoid duplicates
    assigned = set()
    chapters = []

    def add_concepts(concept_list):
        """Helper to add concepts and track assignments"""
        result = []
        for c in concept_list:
            if c['id'] not in assigned:
                result.append(c)
                assigned.add(c['id'])
        return result

    # Chapter 1: IR Foundations (18 concepts)
    ch1_labels = [
        'Investor Relations Function', 'Corporate Valuation Strategy', 'Market Communication Strategy',
        'Shareholder Engagement', 'Key Performance Indicators', 'IR Engagement Metrics',
        'Tracking Investor Outreach', 'Meeting Effectiveness', 'Response Time Analytics',
        'Earnings Reporting Process', 'Investor Targeting Methods', 'Q&A Preparation Techniques',
        'Annual General Meetings', 'Investor Presentations', 'Roadshow Planning',
        'Earnings Call Scripts', 'Press Release Drafting', 'Proxy Season Management'
    ]
    ch1 = add_concepts([n for n in nodes if n['label'] in ch1_labels])
    chapters.append(('Foundations of Modern Investor Relations', ch1))

    # Chapter 2: Regulatory (28 concepts - all REG-COMP)
    ch2 = add_concepts(by_taxonomy['REG-COMP'])
    chapters.append(('Regulatory Frameworks and Compliance', ch2))

    # Chapter 3: Investor Types (15 concepts)
    ch3_labels = [
        'Institutional Investors', 'Retail Investors', 'Hedge Funds', 'Mutual Funds',
        'Pension Funds', 'Sovereign Wealth Funds', 'Buy-Side Analysts', 'Sell-Side Analysts',
        'Investment Bank Relations', 'Analyst Coverage Review', 'Consensus Estimates',
        'Earnings Guidance Strategy', 'Guidance Withdrawal Risks', 'Setting Guidance Ranges',
        'Beat-and-Raise Tactics'
    ]
    ch3 = add_concepts([n for n in nodes if n['label'] in ch3_labels])
    chapters.append(('Investor Types and Market Dynamics', ch3))

    # Chapter 4: Valuation (26 concepts - all VALMET)
    ch4 = add_concepts(by_taxonomy['VALMET'])
    chapters.append(('Valuation Metrics and Performance Indicators', ch4))

    # Chapter 5: AI/ML Fundamentals (12 concepts - all AI-TECH + intro agent concepts)
    ch5 = add_concepts(by_taxonomy['AI-TECH'])
    # Add intro agentic concepts
    ch5.extend(add_concepts([n for n in nodes if n['label'] in ['Agentic AI Systems', 'Autonomous AI Agents']]))
    chapters.append(('AI and Machine Learning Fundamentals', ch5))

    # Chapter 6: AI Content (8 concepts - all AI-CONT)
    ch6 = add_concepts(by_taxonomy['AI-CONT'])
    chapters.append(('AI-Powered Content Creation', ch6))

    # Chapter 7: Sentiment Analysis (20 concepts - ANLYT sentiment subset)
    sentiment_keywords = ['Sentiment', 'NLP', 'Text', 'Natural Language', 'News',
                          'Social', 'Media', 'Analyst Report', 'Feedback', 'Voice', 'Tone']
    ch7 = add_concepts([n for n in by_taxonomy['ANLYT']
                       if any(kw in n['label'] for kw in sentiment_keywords)])
    chapters.append(('Sentiment Analysis: Signals and Methods', ch7))

    # Chapter 8: Predictive Analytics (24 concepts - remaining ANLYT)
    ch8 = add_concepts([n for n in by_taxonomy['ANLYT'] if n['id'] not in assigned])
    chapters.append(('Predictive Analytics and Market Intelligence', ch8))

    # Chapter 9: Personalized Engagement (18 concepts)
    # Dashboard, real-time, targeting concepts
    ch9_keywords = ['Dashboard', 'Real-Time', 'Targeting AI', 'Chatbot', 'Briefing',
                    'Live Data', 'Query Handling', 'Alerts', 'Monitoring']
    ch9 = add_concepts([n for n in nodes if any(kw in n['label'] for kw in ch9_keywords)])
    # Add some IR-OPS engagement concepts if needed
    if len(ch9) < 15:
        ch9.extend(add_concepts([n for n in by_taxonomy['IR-OPS'] if n['id'] not in assigned])[:18-len(ch9)])
    chapters.append(('Personalized and Real-Time Investor Engagement', ch9))

    # Chapter 10: Agentic AI (25 concepts - remaining AGENTIC)
    ch10 = add_concepts([n for n in by_taxonomy['AGENTIC'] if n['id'] not in assigned])
    chapters.append(('Agentic AI Systems and Model Context Protocol', ch10))

    # Chapter 11: AI Governance (20 concepts - all AI-GOV)
    ch11 = add_concepts(by_taxonomy['AI-GOV'])
    chapters.append(('AI Governance, Ethics, and Risk Management', ch11))

    # Chapter 12: Data Governance (24 concepts - all DATA-GOV)
    ch12 = add_concepts(by_taxonomy['DATA-GOV'])
    chapters.append(('Data Governance and Security', ch12))

    # Chapter 13: Platforms & Tools (25 concepts)
    platform_keywords = ['Platform', 'Bloomberg', 'FactSet', 'Nasdaq', 'Q4', 'AlphaSense',
                         'Salesforce', 'Tableau', 'Power BI', 'Ipreo', 'Broadridge',
                         'Computershare', 'Intralinks', 'DealCloud', 'Thomson Reuters',
                         'Python', 'R Statistical', 'Tools']
    ch13 = add_concepts([n for n in by_taxonomy['TRANSFORM']
                        if any(kw in n['label'] for kw in platform_keywords)])
    # Add case studies
    case_labels = ['Tesla IR Case Study', 'Apple Earnings Strategy', 'Amazon Letter Insights',
                   'Berkshire AGM Lessons', 'Enron Detection Failures', 'VW Scandal Response',
                   'Theranos IR Ethics', 'WeWork IPO Analysis', 'GameStop Squeeze AI', 'Bitcoin ETF Monitoring']
    ch13.extend(add_concepts([n for n in nodes if n['label'] in case_labels]))
    chapters.append(('IR Platforms, Tools, and Case Studies', ch13))

    # Chapter 14: Transformation (24 concepts - TRANSFORM subset)
    strategy_keywords = ['Strategy', 'Roadmap', 'Business Case', 'ROI', 'Pilot',
                         'Change Management', 'Stakeholder', 'C-Suite', 'Vendor',
                         'Build vs Buy', 'PoC', 'Success Metrics']
    ch14 = add_concepts([n for n in by_taxonomy['TRANSFORM']
                        if any(kw in n['label'] for kw in strategy_keywords)
                        and n['id'] not in assigned])
    chapters.append(('Transformation Strategy and Change Management', ch14[:24]))

    # Chapter 15: Future Outlook (remaining concepts)
    ch15 = add_concepts([n for n in by_taxonomy['TRANSFORM'] if n['id'] not in assigned])
    # Add any remaining IR-FOUND or IR-OPS
    ch15.extend(add_concepts([n for n in by_taxonomy['IR-FOUND'] if n['id'] not in assigned]))
    ch15.extend(add_concepts([n for n in by_taxonomy['IR-OPS'] if n['id'] not in assigned]))
    # Add any remaining INVEST
    ch15.extend(add_concepts([n for n in by_taxonomy['INVEST'] if n['id'] not in assigned]))
    chapters.append(('Future Outlook: Agentic Ecosystems and Next-Gen IR', ch15))

    return chapters, assigned

def print_summary(chapters, assigned, total=298):
    """Print concise summary"""
    print(f"\n{'='*80}")
    print(f"CHAPTER ASSIGNMENT SUMMARY")
    print(f"{'='*80}")
    print(f"\nTotal concepts assigned: {len(assigned)} of {total}")
    print(f"Status: {'✅ COMPLETE' if len(assigned) == total else '⚠️ MISSING ' + str(total - len(assigned))}")

    print(f"\n{'Chapter':<50} {'Concepts':>10}")
    print('-' * 80)
    for i, (title, concepts) in enumerate(chapters, 1):
        print(f"{i:2d}. {title:<45} {len(concepts):>10}")

    print('-' * 80)
    print(f"{'TOTAL':<50} {sum(len(c) for _, c in chapters):>10}")

def save_to_json(chapters, output_path):
    """Save chapter assignments"""
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
                    for c in sorted(concepts, key=lambda x: x['label'])
                ]
            }
            for i, (title, concepts) in enumerate(chapters, 1)
        ]
    }

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\n✅ Saved to: {output_path}")

if __name__ == '__main__':
    lg_path = Path('/Users/davidberglund/ir-textbook/docs/learning-graph/learning-graph.json')
    output_path = Path('/Users/davidberglund/ir-textbook/chapter-assignments.json')

    lg = load_learning_graph(lg_path)
    chapters, assigned = assign_concepts_to_chapters_fixed(lg)

    print_summary(chapters, assigned, len(lg['nodes']))
    save_to_json(chapters, output_path)

    if len(assigned) == len(lg['nodes']):
        print("\n✅ SUCCESS: All 298 concepts assigned with no duplicates!")
    else:
        print(f"\n⚠️  WARNING: {len(lg['nodes']) - len(assigned)} concepts not assigned")
