#!/usr/bin/env python3
"""
Generate structured glossary data JSON from glossary.md and learning-graph.json
"""

import json
import re
from pathlib import Path

def parse_glossary_md(glossary_path):
    """Parse glossary.md and extract term definitions"""
    with open(glossary_path, 'r', encoding='utf-8') as f:
        content = f.read()

    terms = []

    # Split by #### headers (term titles)
    sections = re.split(r'\n#### ', content)

    for section in sections[1:]:  # Skip introduction
        lines = section.strip().split('\n')
        if not lines:
            continue

        # First line is the term name
        term_name = lines[0].strip()

        # Extract definition and example
        definition = ""
        example = ""

        # Find definition (text before **Example:**)
        example_idx = None
        for i, line in enumerate(lines[1:], 1):
            if line.strip().startswith('**Example:**'):
                example_idx = i
                break

        if example_idx:
            # Definition is between term and example
            definition_lines = lines[1:example_idx]
            definition = ' '.join(l.strip() for l in definition_lines if l.strip())

            # Example is after **Example:** marker
            example_lines = lines[example_idx+1:]
            example = ' '.join(l.strip() for l in example_lines if l.strip())
        else:
            # No example, everything is definition
            definition_lines = lines[1:]
            definition = ' '.join(l.strip() for l in definition_lines if l.strip())

        terms.append({
            'name': term_name,
            'definition': definition,
            'example': example
        })

    return terms

def load_learning_graph(lg_path):
    """Load learning graph JSON"""
    with open(lg_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_color_config(color_path):
    """Load color configuration"""
    with open(color_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def map_terms_to_graph(terms, learning_graph):
    """Map glossary terms to learning graph concepts"""
    # Create lookup from label to node
    node_lookup = {}
    for node in learning_graph['nodes']:
        node_lookup[node['label']] = node

    # Enrich terms with taxonomy data
    enriched_terms = []
    for term in terms:
        term_data = {
            'name': term['name'],
            'definition': term['definition'],
            'example': term['example']
        }

        # Find matching node in learning graph
        if term['name'] in node_lookup:
            node = node_lookup[term['name']]
            term_data['category'] = node.get('group', 'OTHER')
            term_data['id'] = node.get('id')

            # Check if it's a foundation concept (shape: box)
            term_data['isCore'] = node.get('shape') == 'box'
        else:
            # Term not in learning graph
            term_data['category'] = 'OTHER'
            term_data['id'] = None
            term_data['isCore'] = False

        enriched_terms.append(term_data)

    return enriched_terms

def determine_difficulty_level(term, learning_graph):
    """Determine difficulty level based on concept dependencies"""
    # Find node in graph
    node_lookup = {node['label']: node for node in learning_graph['nodes']}

    if term['name'] not in node_lookup:
        return 'intermediate'

    node_id = node_lookup[term['name']]['id']

    # Count incoming edges (dependencies)
    incoming_count = sum(1 for edge in learning_graph['edges'] if edge['to'] == node_id)

    # Categorize based on dependencies
    if incoming_count == 0:
        return 'beginner'
    elif incoming_count <= 2:
        return 'intermediate'
    else:
        return 'advanced'

def generate_glossary_data():
    """Main function to generate glossary data"""

    base_path = Path('/Users/davidberglund/ir-textbook')

    # Load source files
    print("Loading glossary.md...")
    terms = parse_glossary_md(base_path / 'docs' / 'glossary.md')
    print(f"  Found {len(terms)} terms")

    print("Loading learning-graph.json...")
    learning_graph = load_learning_graph(base_path / 'docs' / 'learning-graph' / 'learning-graph.json')
    print(f"  Found {len(learning_graph['nodes'])} concepts")

    print("Loading color-config.json...")
    color_config = load_color_config(base_path / 'docs' / 'learning-graph' / 'color-config.json')
    print(f"  Found {len(color_config)} categories")

    # Map terms to graph
    print("Mapping terms to learning graph...")
    enriched_terms = map_terms_to_graph(terms, learning_graph)

    # Add difficulty levels
    print("Determining difficulty levels...")
    for term in enriched_terms:
        term['difficulty'] = determine_difficulty_level(term, learning_graph)

    # Create final structure
    glossary_data = {
        'metadata': {
            'title': 'AI for Investor Relations - Glossary',
            'version': '2.0',
            'totalTerms': len(enriched_terms),
            'generated': '2025-11-06'
        },
        'categories': color_config,
        'terms': enriched_terms
    }

    # Write output
    output_path = base_path / 'docs' / 'glossary-app' / 'glossary-data.json'
    print(f"Writing to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(glossary_data, f, indent=2, ensure_ascii=False)

    print(f"✅ Successfully generated glossary-data.json with {len(enriched_terms)} terms")

    # Print statistics
    category_counts = {}
    difficulty_counts = {'beginner': 0, 'intermediate': 0, 'advanced': 0}
    core_count = sum(1 for t in enriched_terms if t.get('isCore', False))

    for term in enriched_terms:
        cat = term.get('category', 'OTHER')
        category_counts[cat] = category_counts.get(cat, 0) + 1
        diff = term.get('difficulty', 'intermediate')
        difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1

    print("\n📊 Statistics:")
    print(f"  Core concepts: {core_count}")
    print(f"\n  By difficulty:")
    for level, count in sorted(difficulty_counts.items()):
        print(f"    {level}: {count}")
    print(f"\n  By category:")
    for cat, count in sorted(category_counts.items(), key=lambda x: -x[1])[:5]:
        cat_name = color_config.get(cat, {}).get('classifierName', cat)
        print(f"    {cat_name}: {count}")

if __name__ == '__main__':
    generate_glossary_data()
