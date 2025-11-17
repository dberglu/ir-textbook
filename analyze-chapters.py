#!/usr/bin/env python3
"""
Analyze learning graph and design optimal chapter structure for 298 concepts
"""

import json
from collections import defaultdict
from pathlib import Path

def load_learning_graph(path):
    with open(path, 'r') as f:
        return json.load(f)

def analyze_dependencies(lg):
    """Analyze concept dependencies"""
    deps = defaultdict(list)  # concept_id -> [dependent_ids]
    prereqs = defaultdict(list)  # concept_id -> [prerequisite_ids]

    for edge in lg['edges']:
        prereqs[edge['to']].append(edge['from'])
        deps[edge['from']].append(edge['to'])

    return deps, prereqs

def get_depth_level(node_id, prereqs, memo=None):
    """Calculate depth level (longest path from a foundational concept)"""
    if memo is None:
        memo = {}
    if node_id in memo:
        return memo[node_id]

    if not prereqs[node_id]:  # Foundational
        memo[node_id] = 0
        return 0

    max_depth = max(get_depth_level(p, prereqs, memo) for p in prereqs[node_id])
    memo[node_id] = max_depth + 1
    return max_depth + 1

def design_chapters(lg):
    """Design optimal chapter structure"""
    nodes = lg['nodes']
    deps, prereqs = analyze_dependencies(lg)

    # Calculate depth for each concept
    depths = {}
    for node in nodes:
        depths[node['id']] = get_depth_level(node['id'], prereqs)

    # Group concepts by taxonomy and depth
    taxonomy_groups = defaultdict(list)
    for node in nodes:
        taxonomy_groups[node.get('group', 'OTHER')].append(node)

    # Sort each taxonomy group by depth
    for tax in taxonomy_groups:
        taxonomy_groups[tax].sort(key=lambda n: (depths[n['id']], n['label']))

    # Design 14 chapters (298 concepts / 14 ≈ 21 per chapter)
    chapters = []

    # Chapter 1: IR Foundations (IR-FOUND + IR-OPS basics)
    ch1 = []
    ch1.extend([n for n in taxonomy_groups['IR-FOUND'] if depths[n['id']] == 0])
    ch1.extend([n for n in taxonomy_groups['IR-OPS'] if depths[n['id']] <= 1][:8])
    ch1.extend([n for n in taxonomy_groups['INVEST'] if depths[n['id']] == 0])
    chapters.append(('Foundations of Modern Investor Relations', ch1))

    # Chapter 2: Regulatory Compliance (REG-COMP)
    ch2 = [n for n in taxonomy_groups['REG-COMP'] if depths[n['id']] <= 2]
    chapters.append(('Regulatory Frameworks and Compliance', ch2))

    # Chapter 3: Investor Types (INVEST + IR-OPS)
    ch3 = []
    ch3.extend([n for n in taxonomy_groups['INVEST'] if depths[n['id']] > 0])
    ch3.extend([n for n in taxonomy_groups['IR-OPS'] if n not in ch1 and depths[n['id']] <= 2])
    chapters.append(('Investor Types and Market Engagement', ch3))

    # Chapter 4: Valuation Metrics (VALMET)
    ch4 = [n for n in taxonomy_groups['VALMET']]
    chapters.append(('Valuation Metrics and Market Performance', ch4))

    # Chapter 5: AI Fundamentals (AI-TECH)
    ch5 = [n for n in taxonomy_groups['AI-TECH']]
    chapters.append(('AI and Machine Learning Fundamentals', ch5))

    # Chapter 6: AI Content Creation (AI-CONT)
    ch6 = [n for n in taxonomy_groups['AI-CONT']]
    chapters.append(('AI-Powered Content Creation for IR', ch6))

    # Chapter 7: Sentiment & Analytics Part 1 (ANLYT - first half)
    anlyt_nodes = sorted(taxonomy_groups['ANLYT'], key=lambda n: depths[n['id']])
    ch7 = anlyt_nodes[:26]  # First half
    chapters.append(('Sentiment Analysis and Predictive Analytics I', ch7))

    # Chapter 8: Sentiment & Analytics Part 2 (ANLYT - second half)
    ch8 = anlyt_nodes[26:]  # Second half
    chapters.append(('Advanced Analytics and Market Intelligence', ch8))

    # Chapter 9: Agentic AI (AGENTIC)
    ch9 = [n for n in taxonomy_groups['AGENTIC']]
    chapters.append(('Agentic AI Systems and Model Context Protocol', ch9))

    # Chapter 10: AI Governance (AI-GOV + REG-COMP advanced)
    ch10 = []
    ch10.extend([n for n in taxonomy_groups['AI-GOV']])
    ch10.extend([n for n in taxonomy_groups['REG-COMP'] if n not in ch2])
    chapters.append(('AI Governance, Ethics, and Compliance', ch10))

    # Chapter 11: Data Governance (DATA-GOV)
    ch11 = [n for n in taxonomy_groups['DATA-GOV']]
    chapters.append(('Data Governance and Security', ch11))

    # Chapter 12: IR Platforms & Tools (TRANSFORM - platforms subset)
    transform_nodes = sorted(taxonomy_groups['TRANSFORM'], key=lambda n: depths[n['id']])
    platform_keywords = ['Platform', 'Tools', 'IR', 'Dashboard', 'Bloomberg', 'FactSet',
                         'Nasdaq', 'Salesforce', 'Tableau', 'Power BI', 'Ipreo', 'Q4',
                         'Computershare', 'Broadridge', 'AlphaSense', 'DealCloud']
    ch12 = [n for n in transform_nodes if any(kw in n['label'] for kw in platform_keywords)]
    chapters.append(('IR Platforms, Tools, and Case Studies', ch12))

    # Chapter 13: Transformation Strategy Part 1 (TRANSFORM - strategy)
    strategy_nodes = [n for n in transform_nodes if n not in ch12 and depths[n['id']] <= 3]
    ch13 = strategy_nodes[:len(strategy_nodes)//2]
    chapters.append(('AI Transformation Strategy and Planning', ch13))

    # Chapter 14: Transformation Part 2 (TRANSFORM - execution)
    ch14 = [n for n in transform_nodes if n not in ch12 and n not in ch13]
    chapters.append(('Change Management and Implementation', ch14))

    return chapters, depths, prereqs

def print_chapter_design(chapters, depths, prereqs):
    """Print chapter design for user approval"""
    print("=" * 80)
    print("PROPOSED CHAPTER STRUCTURE FOR 298 CONCEPTS")
    print("=" * 80)
    print()

    total_concepts = sum(len(concepts) for _, concepts in chapters)
    print(f"Total Chapters: {len(chapters)}")
    print(f"Total Concepts: {total_concepts}")
    print(f"Average per Chapter: {total_concepts/len(chapters):.1f}")
    print()

    for i, (title, concepts) in enumerate(chapters, 1):
        print(f"\n{'='*80}")
        print(f"Chapter {i}: {title}")
        print(f"{'='*80}")
        print(f"Concepts: {len(concepts)}")
        print(f"Depth Range: {min(depths[c['id']] for c in concepts)}-{max(depths[c['id']] for c in concepts)}")

        # Show taxonomy distribution
        tax_dist = defaultdict(int)
        for c in concepts:
            tax_dist[c.get('group', 'OTHER')] += 1
        print(f"Taxonomies: {dict(tax_dist)}")

        # Check dependencies
        unmet_deps = []
        assigned_so_far = set()
        for j in range(i):
            assigned_so_far.update(c['id'] for c in chapters[j-1][1])

        for concept in concepts:
            for prereq_id in prereqs[concept['id']]:
                if prereq_id not in assigned_so_far and prereq_id not in [c['id'] for c in concepts]:
                    unmet_deps.append((concept['label'], prereq_id))

        if unmet_deps:
            print(f"⚠️  WARNING: {len(unmet_deps)} unmet dependencies!")
            for clabel, pid in unmet_deps[:3]:
                print(f"     - {clabel} requires concept #{pid}")
        else:
            print("✅ All dependencies satisfied")

        # Show first 10 concepts
        print("\nConcepts (first 10):")
        for c in concepts[:10]:
            depth_marker = "  " * depths[c['id']]
            print(f"  {depth_marker}• {c['label']} (depth {depths[c['id']]})")
        if len(concepts) > 10:
            print(f"  ... and {len(concepts) - 10} more")

    print(f"\n{'='*80}")
    print("VALIDATION SUMMARY")
    print(f"{'='*80}")
    print(f"✅ Total concepts assigned: {total_concepts}")
    print(f"✅ Chapter count: {len(chapters)}")
    print(f"✅ Size range: {min(len(c) for _, c in chapters)}-{max(len(c) for _, c in chapters)} concepts")

if __name__ == '__main__':
    lg_path = Path('/Users/davidberglund/ir-textbook/docs/learning-graph/learning-graph.json')
    lg = load_learning_graph(lg_path)

    chapters, depths, prereqs = design_chapters(lg)
    print_chapter_design(chapters, depths, prereqs)
