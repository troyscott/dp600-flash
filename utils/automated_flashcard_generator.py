#!/usr/bin/env python3
"""
Fully Automated DP-600 Flashcard Generator

Reads PDF chunks, analyzes content, and generates formatted flashcards
directly into the appropriate content/ folders.
"""

import os
import json
import re
from pathlib import Path
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path):
    """Extract and clean text content from PDF"""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        
        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text()
            text += page_text + "\n"
        
        # Clean up the text
        text = re.sub(r'\n+', '\n', text)  # Multiple newlines to single
        text = re.sub(r'[^\w\s\-.,;:()\[\]{}]', '', text)  # Remove odd chars
        text = text.strip()
        
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None


def analyze_content_topic(text):
    """Analyze text to determine the most appropriate content folder"""
    text_lower = text.lower()
    
    # Keywords for each DP-600 objective area
    maintain_keywords = [
        'security', 'governance', 'workspace', 'permission', 'access', 
        'deployment', 'pipeline', 'role', 'authentication', 'authorization',
        'tenant', 'admin', 'management', 'monitor', 'alert'
    ]
    
    data_keywords = [
        'ingestion', 'transformation', 'lakehouse', 'warehouse', 'sql', 
        'kql', 'pipeline', 'dataflow', 'notebook', 'spark', 'data factory',
        'extract', 'load', 'etl', 'delta', 'parquet'
    ]
    
    model_keywords = [
        'semantic', 'model', 'dax', 'measure', 'calculation', 'star schema',
        'dimension', 'fact', 'relationship', 'direct lake', 'power bi',
        'dataset', 'tabular', 'analysis services'
    ]
    
    # Count keyword matches
    maintain_score = sum(1 for keyword in maintain_keywords if keyword in text_lower)
    data_score = sum(1 for keyword in data_keywords if keyword in text_lower)
    model_score = sum(1 for keyword in model_keywords if keyword in text_lower)
    
    # Determine folder
    if maintain_score >= data_score and maintain_score >= model_score:
        return "01-maintain-analytics-solution"
    elif data_score >= model_score:
        return "02-prepare-data"
    else:
        return "03-semantic-models"


def generate_flashcards(text, chunk_name):
    """Generate DP-600 flashcards from text content"""
    
    # Split text into logical sections for card generation
    sections = []
    current_section = ""
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Look for section headers or topic breaks
        if (len(line) < 100 and 
            any(indicator in line.lower() for indicator in 
                ['chapter', 'section', 'overview', 'introduction', 'summary',
                 'objective', 'goal', 'feature', 'component', 'service'])):
            
            if current_section and len(current_section) > 200:
                sections.append(current_section)
            current_section = line + "\n"
        else:
            current_section += line + "\n"
    
    # Add the last section
    if current_section and len(current_section) > 200:
        sections.append(current_section)
    
    # If no clear sections, split by length
    if len(sections) < 2:
        words = text.split()
        chunk_size = max(200, len(words) // 6)  # Aim for ~6 cards
        sections = []
        for i in range(0, len(words), chunk_size):
            section_text = ' '.join(words[i:i + chunk_size])
            if len(section_text) > 100:
                sections.append(section_text)
    
    flashcards = []
    
    for i, section in enumerate(sections[:10]):  # Max 10 cards per chunk
        card_num = i + 1
        
        # Generate question based on content
        question = generate_question_from_content(section, chunk_name)
        
        # Create formatted answer from the section
        answer = format_answer_content(section)
        
        # Determine difficulty
        difficulty = determine_difficulty(section)
        
        # Generate tags
        tags = generate_tags(section)
        
        flashcard = f"""### Card {card_num}
**Q:** {question}
**A:** {answer}

**Difficulty:** {difficulty}
**Tags:** {', '.join(tags)}

---

"""
        flashcards.append(flashcard)
    
    return flashcards


def generate_question_from_content(content, chunk_name):
    """Generate an appropriate question from content"""
    content_lower = content.lower()
    
    # Question patterns based on content type
    if 'security' in content_lower or 'permission' in content_lower:
        return f"What are the key security considerations for {extract_main_topic(content)}?"
    
    elif 'configure' in content_lower or 'setup' in content_lower:
        return f"How do you configure {extract_main_topic(content)}?"
    
    elif 'difference' in content_lower or 'compare' in content_lower:
        return f"What are the key differences between the concepts discussed in {extract_main_topic(content)}?"
    
    elif 'best practice' in content_lower or 'recommend' in content_lower:
        return f"What are the best practices for {extract_main_topic(content)}?"
    
    elif 'troubleshoot' in content_lower or 'error' in content_lower:
        return f"How do you troubleshoot common issues with {extract_main_topic(content)}?"
    
    elif 'performance' in content_lower or 'optimize' in content_lower:
        return f"How do you optimize performance for {extract_main_topic(content)}?"
    
    else:
        topic = extract_main_topic(content)
        return f"Explain the key concepts and implementation of {topic}."


def extract_main_topic(content):
    """Extract the main topic from content"""
    # Look for capitalized terms or common DP-600 concepts
    words = content.split()[:50]  # First 50 words
    
    dp600_terms = [
        'Microsoft Fabric', 'Power BI', 'Azure Synapse', 'Data Factory',
        'Lakehouse', 'Warehouse', 'Semantic Model', 'Direct Lake',
        'DAX', 'KQL', 'Spark', 'Delta Lake', 'OneLake'
    ]
    
    for term in dp600_terms:
        if term.lower() in content.lower():
            return term
    
    # Fallback to a generic topic
    return "Microsoft Fabric analytics"


def format_answer_content(content):
    """Format content as a well-structured answer"""
    lines = content.split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Convert to bullet points for key information
        if len(line) < 200 and any(indicator in line.lower() for indicator in 
                                  ['key', 'important', 'note', 'remember']):
            formatted_lines.append(f"- **{line}**")
        elif line.endswith(':'):
            formatted_lines.append(f"**{line}**")
        else:
            formatted_lines.append(line)
    
    # Join and format
    answer = '\n'.join(formatted_lines)
    
    # Add bullet points for lists
    answer = re.sub(r'^(\d+\.|•|\*)\s*', '- ', answer, flags=re.MULTILINE)
    
    # Bold important terms
    dp600_terms = [
        'Microsoft Fabric', 'Power BI', 'Lakehouse', 'Warehouse', 
        'Direct Lake', 'DAX', 'KQL', 'OneLake', 'Spark'
    ]
    
    for term in dp600_terms:
        answer = re.sub(f'\\b{term}\\b', f'**{term}**', answer, flags=re.IGNORECASE)
    
    return answer


def determine_difficulty(content):
    """Determine difficulty level based on content complexity"""
    content_lower = content.lower()
    
    advanced_indicators = [
        'advanced', 'complex', 'optimization', 'troubleshooting', 
        'architecture', 'enterprise', 'custom', 'api'
    ]
    
    basic_indicators = [
        'introduction', 'overview', 'basic', 'getting started',
        'simple', 'beginner'
    ]
    
    if any(indicator in content_lower for indicator in advanced_indicators):
        return "Advanced"
    elif any(indicator in content_lower for indicator in basic_indicators):
        return "Basic"
    else:
        return "Intermediate"


def generate_tags(content):
    """Generate relevant tags from content"""
    content_lower = content.lower()
    tags = []
    
    # Common DP-600 tags
    tag_mapping = {
        'fabric': ['microsoft-fabric', 'fabric'],
        'power bi': ['power-bi', 'powerbi'],
        'lakehouse': ['lakehouse', 'data-lake'],
        'warehouse': ['warehouse', 'synapse'],
        'security': ['security', 'governance'],
        'dax': ['dax', 'calculations'],
        'sql': ['sql', 'queries'],
        'kql': ['kql', 'kusto'],
        'spark': ['spark', 'notebooks'],
        'pipeline': ['pipelines', 'etl']
    }
    
    for keyword, tag_list in tag_mapping.items():
        if keyword in content_lower:
            tags.extend(tag_list)
    
    # Add general tags
    tags.append('dp-600')
    tags.append('exam')
    
    return list(set(tags))[:5]  # Max 5 unique tags


def save_flashcards(flashcards, folder, filename):
    """Save flashcards to appropriate content folder"""
    script_dir = Path(__file__).parent.parent
    content_dir = script_dir / "content" / folder
    content_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = content_dir / filename
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# DP-600 Flashcards - {filename.stem.replace('-', ' ').title()}\n\n")
        for card in flashcards:
            f.write(card)
    
    return output_file


def main():
    print("🤖 Automated DP-600 Flashcard Generator")
    print("=" * 50)
    
    script_dir = Path(__file__).parent
    output_dir = script_dir / "output"
    
    if not output_dir.exists():
        print("❌ No PDF chunks found in output/ directory")
        print("   Run simple_pdf_splitter.py first!")
        return
    
    pdf_files = list(output_dir.glob("*.pdf"))
    if not pdf_files:
        print("❌ No PDF files found in output/ directory")
        return
    
    print(f"📄 Found {len(pdf_files)} PDF chunks to process")
    print("-" * 50)
    
    generated_files = []
    
    for i, pdf_file in enumerate(sorted(pdf_files), 1):
        print(f"📖 Processing {pdf_file.name}...")
        
        # Extract text
        text_content = extract_text_from_pdf(pdf_file)
        if not text_content:
            print(f"   ⚠️ Skipped - could not extract text")
            continue
        
        if len(text_content) < 500:
            print(f"   ⚠️ Skipped - content too short ({len(text_content)} chars)")
            continue
        
        # Determine content folder
        folder = analyze_content_topic(text_content)
        
        # Generate flashcards
        flashcards = generate_flashcards(text_content, pdf_file.stem)
        
        if not flashcards:
            print(f"   ⚠️ Skipped - no flashcards generated")
            continue
        
        # Create filename
        chunk_match = re.search(r'chunk_(\d+)', pdf_file.name)
        chunk_num = chunk_match.group(1) if chunk_match else f"{i:02d}"
        filename = f"dp600_flashcards_chunk_{chunk_num}.md"
        
        # Save flashcards
        output_file = save_flashcards(flashcards, folder, filename)
        
        print(f"   ✅ Generated {len(flashcards)} cards")
        print(f"   📁 Saved to: {folder}/{filename}")
        
        generated_files.append({
            'file': str(output_file),
            'folder': folder,
            'cards': len(flashcards)
        })
    
    print("-" * 50)
    print(f"🎉 Successfully generated {len(generated_files)} flashcard files")
    
    # Summary by folder
    folder_summary = {}
    total_cards = 0
    
    for file_info in generated_files:
        folder = file_info['folder']
        cards = file_info['cards']
        
        if folder not in folder_summary:
            folder_summary[folder] = {'files': 0, 'cards': 0}
        
        folder_summary[folder]['files'] += 1
        folder_summary[folder]['cards'] += cards
        total_cards += cards
    
    print(f"📊 Summary:")
    print(f"   Total flashcards: {total_cards}")
    for folder, stats in folder_summary.items():
        print(f"   {folder}: {stats['files']} files, {stats['cards']} cards")
    
    print(f"\n🔄 Next Steps:")
    print(f"1. Visit /admin/reload-flashcards in your app")
    print(f"2. Test new flashcards in study modes")
    print(f"3. Review and adjust any cards as needed")


if __name__ == "__main__":
    main()