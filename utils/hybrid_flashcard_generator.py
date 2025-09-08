#!/usr/bin/env python3
"""
Hybrid DP-600 Flashcard Generator - Best Quality Results

Combines rule-based content analysis with LLM generation for optimal
exam-style flashcard quality. Supports both local (Ollama) and cloud LLMs.
"""

import os
import json
import re
from pathlib import Path
from PyPDF2 import PdfReader
import requests
from datetime import datetime

# Configuration
CONFIG = {
    "llm_provider": "ollama",  # Options: "ollama", "openai", "anthropic"
    "model": "llama3.2:3b",    # Ollama models: llama3.2:3b, qwen2.5:7b, etc.
    "api_key": "",             # Only needed for cloud providers
    "ollama_url": "http://localhost:11434",
    "max_cards_per_chunk": 12,
    "min_content_length": 500
}


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
        text = re.sub(r'[^\w\s\-.,;:()\[\]{}/"\'%$#@!?]', '', text)  # Clean special chars
        text = text.strip()
        
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None


def analyze_content_structure(text):
    """Advanced rule-based content analysis for LLM context"""
    
    analysis = {
        "primary_topic": None,
        "content_folder": None,
        "technical_terms": [],
        "concepts": [],
        "difficulty_indicators": [],
        "content_type": "general",
        "key_sections": [],
        "exam_relevance": "medium"
    }
    
    text_lower = text.lower()
    
    # 1. Determine primary DP-600 exam objective area
    maintain_keywords = [
        'security', 'governance', 'workspace', 'permission', 'access control',
        'deployment', 'pipeline', 'role', 'authentication', 'authorization',
        'tenant', 'admin', 'management', 'monitor', 'alert', 'compliance'
    ]
    
    data_keywords = [
        'ingestion', 'transformation', 'lakehouse', 'warehouse', 'sql', 'kql',
        'pipeline', 'dataflow', 'notebook', 'spark', 'data factory', 'extract',
        'load', 'etl', 'delta', 'parquet', 'streaming', 'batch processing'
    ]
    
    model_keywords = [
        'semantic model', 'dax', 'measure', 'calculation', 'star schema',
        'dimension', 'fact table', 'relationship', 'direct lake', 'power bi',
        'dataset', 'tabular', 'analysis services', 'aggregation', 'partition'
    ]
    
    # Score each area
    maintain_score = sum(2 if keyword in text_lower else 0 for keyword in maintain_keywords)
    data_score = sum(2 if keyword in text_lower else 0 for keyword in data_keywords)  
    model_score = sum(2 if keyword in text_lower else 0 for keyword in model_keywords)
    
    if maintain_score >= data_score and maintain_score >= model_score:
        analysis["primary_topic"] = "Analytics Solution Management"
        analysis["content_folder"] = "01-maintain-analytics-solution"
    elif data_score >= model_score:
        analysis["primary_topic"] = "Data Preparation & Engineering" 
        analysis["content_folder"] = "02-prepare-data"
    else:
        analysis["primary_topic"] = "Semantic Modeling"
        analysis["content_folder"] = "03-semantic-models"
    
    # 2. Extract technical terms and concepts
    dp600_terms = [
        'Microsoft Fabric', 'Power BI', 'Azure Synapse', 'Data Factory',
        'Lakehouse', 'Warehouse', 'OneLake', 'Direct Lake', 'DAX', 'KQL',
        'Spark', 'Delta Lake', 'Semantic Model', 'Star Schema', 'Dataflow',
        'Pipeline', 'Workspace', 'Tenant', 'Row-level Security', 'RLS'
    ]
    
    found_terms = [term for term in dp600_terms if term.lower() in text_lower]
    analysis["technical_terms"] = found_terms
    
    # 3. Identify content type and complexity
    if any(word in text_lower for word in ['step', 'procedure', 'how to', 'configure']):
        analysis["content_type"] = "procedural"
    elif any(word in text_lower for word in ['compare', 'difference', 'versus', 'vs']):
        analysis["content_type"] = "comparative"
    elif any(word in text_lower for word in ['best practice', 'recommendation', 'guideline']):
        analysis["content_type"] = "best_practices"
    elif any(word in text_lower for word in ['troubleshoot', 'error', 'issue', 'problem']):
        analysis["content_type"] = "troubleshooting"
    elif any(word in text_lower for word in ['overview', 'introduction', 'concept']):
        analysis["content_type"] = "conceptual"
    
    # 4. Difficulty assessment
    advanced_indicators = [
        'advanced', 'complex', 'enterprise', 'custom', 'api', 'programmatic',
        'optimization', 'performance tuning', 'architecture', 'integration'
    ]
    
    basic_indicators = [
        'introduction', 'overview', 'basic', 'getting started', 'beginner',
        'simple', 'fundamentals', 'basics'
    ]
    
    if any(indicator in text_lower for indicator in advanced_indicators):
        analysis["difficulty_indicators"] = ["advanced"]
    elif any(indicator in text_lower for indicator in basic_indicators):
        analysis["difficulty_indicators"] = ["basic"]
    else:
        analysis["difficulty_indicators"] = ["intermediate"]
    
    # 5. Extract key sections for targeted questions
    lines = text.split('\n')
    current_section = ""
    
    for line in lines:
        line = line.strip()
        if len(line) < 100 and any(indicator in line.lower() for indicator in 
                                  ['key', 'important', 'note', 'summary', 'objective']):
            if current_section and len(current_section) > 100:
                analysis["key_sections"].append(current_section[:200])
            current_section = line
        else:
            current_section += " " + line
    
    if current_section and len(current_section) > 100:
        analysis["key_sections"].append(current_section[:200])
    
    return analysis


def create_enhanced_prompt(text, analysis):
    """Create optimized prompt with rule-based analysis context"""
    
    prompt = f"""You are creating DP-600 exam flashcards. Follow this format EXACTLY:

### Card 1
**Q:** How do you configure Microsoft Fabric workspace security?
**A:** To configure workspace security:
- Navigate to **Workspace settings**
- Set **Role-based access** permissions
- Configure `Row-Level Security (RLS)` for datasets
- Enable **Azure AD integration**

**Difficulty:** Intermediate
**Tags:** dp-600, security, workspace

---

### Card 2
**Q:** What are the key differences between Lakehouse and Warehouse in Fabric?
**A:** Key differences:
- **Lakehouse**: Supports both structured and unstructured data
- **Warehouse**: Optimized for structured data and SQL queries
- **Storage**: Lakehouse uses `Delta Lake` format
- **Performance**: Warehouse provides faster analytical queries

**Difficulty:** Basic
**Tags:** dp-600, lakehouse, warehouse

---

Now create 8-10 similar flashcards from this content:

TOPIC: {analysis['primary_topic']}
KEY TERMS: {', '.join(analysis['technical_terms'][:5])}

CONTENT:
{text[:2000]}

Remember: Use **Q:** and **A:** exactly as shown in the examples above. Each card must end with ---"""
    
    return prompt


def call_llm(prompt, provider="ollama"):
    """Call the specified LLM provider"""
    
    try:
        if provider == "ollama":
            return call_ollama(prompt)
        elif provider == "openai":
            return call_openai(prompt)
        elif provider == "anthropic":
            return call_anthropic(prompt)
        else:
            raise ValueError(f"Unsupported provider: {provider}")
    
    except Exception as e:
        print(f"❌ LLM call failed: {e}")
        return None


def call_ollama(prompt):
    """Call local Ollama instance"""
    
    url = f"{CONFIG['ollama_url']}/api/generate"
    
    payload = {
        "model": CONFIG["model"],
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "top_p": 0.9,
            "max_tokens": 4000
        }
    }
    
    try:
        response = requests.post(url, json=payload, timeout=300)
        response.raise_for_status()
        
        result = response.json()
        return result.get("response", "")
    
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Ollama. Is it running? Start with: ollama serve")
        return None
    except Exception as e:
        print(f"❌ Ollama error: {e}")
        return None


def call_openai(prompt):
    """Call OpenAI API"""
    
    if not CONFIG["api_key"]:
        print("❌ OpenAI API key required. Set CONFIG['api_key']")
        return None
    
    import openai
    
    openai.api_key = CONFIG["api_key"]
    
    try:
        response = openai.chat.completions.create(
            model=CONFIG.get("model", "gpt-4"),
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=4000
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"❌ OpenAI error: {e}")
        return None


def call_anthropic(prompt):
    """Call Anthropic Claude API"""
    
    if not CONFIG["api_key"]:
        print("❌ Anthropic API key required. Set CONFIG['api_key']")
        return None
    
    import anthropic
    
    client = anthropic.Anthropic(api_key=CONFIG["api_key"])
    
    try:
        response = client.messages.create(
            model=CONFIG.get("model", "claude-3-sonnet-20240229"),
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=4000
        )
        
        return response.content[0].text
    
    except Exception as e:
        print(f"❌ Anthropic error: {e}")
        return None


def validate_and_clean_flashcards(llm_output):
    """Validate LLM output and ensure proper formatting"""
    
    if not llm_output:
        return []
    
    # First, try to convert Front/Back format to Q/A format
    llm_output = llm_output.replace('**Front:**', '**Q:**')
    llm_output = llm_output.replace('**Back:**', '**A:**')
    
    # Split into individual cards - try multiple separators
    if '---' in llm_output:
        cards = llm_output.split('---')
    elif '**Card' in llm_output:
        # Split on Card headers
        parts = re.split(r'\*\*Card \d+\*\*', llm_output)
        cards = [part for part in parts if part.strip()]
    else:
        # Try to identify cards by Q:/A: patterns
        card_pattern = r'(\*\*Q:\*\*.*?\*\*A:\*\*.*?)(?=\*\*Q:\*\*|$)'
        cards = re.findall(card_pattern, llm_output, re.DOTALL)
    
    validated_cards = []
    
    for i, card in enumerate(cards, 1):
        try:
            if isinstance(card, tuple):
                card = card[0]
            card = str(card).strip()
            if not card:
                continue
            
            # Check for required format (flexible matching)
            has_question = any(marker in card for marker in ['**Q:**', '**Front:**', 'Q:', 'Front:'])
            has_answer = any(marker in card for marker in ['**A:**', '**Back:**', 'A:', 'Back:'])
        except Exception as e:
            print(f"   ⚠️ Error processing card {i}: {e}")
            continue
        
        if has_question and has_answer:
            
            # Convert any remaining Front/Back to Q/A (handle all variations)
            card = card.replace('**Front:**', '**Q:**')
            card = card.replace('**Back:**', '**A:**')
            card = card.replace('Front:', '**Q:**')
            card = card.replace('Back:', '**A:**')
            
            # Ensure proper card numbering
            if not card.startswith('### Card'):
                card = f"### Card {i}\n{card}"
            
            # Ensure difficulty and tags are present
            if '**Difficulty:**' not in card:
                card += "\n\n**Difficulty:** Intermediate"
            
            if '**Tags:**' not in card:
                card += "\n**Tags:** dp-600, exam"
            
            # Add separator
            card += "\n\n---\n"
            validated_cards.append(card)
    
    return validated_cards


def save_flashcards(flashcards, folder, filename):
    """Save validated flashcards to content directory"""
    
    if not flashcards:
        return None
    
    script_dir = Path(__file__).parent.parent
    content_dir = script_dir / "content" / folder
    content_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = content_dir / filename
    
    # Create file header
    filename_path = Path(filename) if isinstance(filename, str) else filename
    header = f"""# DP-600 Flashcards - {filename_path.stem.replace('-', ' ').title()}

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}
Source: Hybrid LLM + Rule-based Generator

"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(header)
        for card in flashcards:
            f.write(card)
            f.write('\n')
    
    return output_file


def main():
    print("🚀 Hybrid DP-600 Flashcard Generator (Best Quality)")
    print("=" * 60)
    print(f"🤖 LLM Provider: {CONFIG['llm_provider']}")
    print(f"📊 Model: {CONFIG['model']}")
    
    # Check LLM availability
    if CONFIG['llm_provider'] == 'ollama':
        try:
            response = requests.get(f"{CONFIG['ollama_url']}/api/tags", timeout=5)
            if response.status_code != 200:
                print("❌ Ollama not available. Start with: ollama serve")
                return
            print("✅ Ollama connection verified")
        except:
            print("❌ Cannot connect to Ollama. Install and start with: ollama serve")
            return
    
    print("-" * 60)
    
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
    print("-" * 60)
    
    generated_files = []
    
    for i, pdf_file in enumerate(sorted(pdf_files), 1):
        print(f"\n📖 Processing {pdf_file.name} ({i}/{len(pdf_files)})...")
        
        # 1. Extract text content
        text_content = extract_text_from_pdf(pdf_file)
        if not text_content:
            print(f"   ⚠️ Skipped - could not extract text")
            continue
        
        if len(text_content) < CONFIG["min_content_length"]:
            print(f"   ⚠️ Skipped - content too short ({len(text_content)} chars)")
            continue
        
        # 2. Rule-based content analysis
        print("   🔍 Analyzing content structure...")
        analysis = analyze_content_structure(text_content)
        print(f"   📊 Topic: {analysis['primary_topic']}")
        print(f"   📁 Folder: {analysis['content_folder']}")
        print(f"   🎯 Type: {analysis['content_type']}")
        
        # 3. Create enhanced prompt
        enhanced_prompt = create_enhanced_prompt(text_content, analysis)
        
        # 4. Generate flashcards with LLM
        print("   🤖 Generating flashcards with LLM...")
        llm_output = call_llm(enhanced_prompt, CONFIG['llm_provider'])
        
        if not llm_output:
            print("   ❌ Failed to generate flashcards")
            continue
        
        # Debug: Show first part of LLM output
        print(f"   🔍 LLM output preview: {llm_output[:200]}...")
        
        # 5. Validate and clean output
        print("   ✅ Validating flashcard format...")
        flashcards = validate_and_clean_flashcards(llm_output)
        
        if not flashcards:
            print(f"   🔍 Debug: Raw LLM output length: {len(llm_output)}")
            print(f"   🔍 Looking for Q: and A: in output...")
            if '**Q:**' in llm_output:
                print("   ✅ Found **Q:** in output")
            else:
                print("   ❌ Missing **Q:** in output")
            if '**A:**' in llm_output:
                print("   ✅ Found **A:** in output") 
            else:
                print("   ❌ Missing **A:** in output")
        
        if not flashcards:
            print("   ❌ No valid flashcards generated")
            continue
        
        # 6. Save flashcards
        chunk_match = re.search(r'chunk_(\d+)', pdf_file.name)
        chunk_num = chunk_match.group(1) if chunk_match else f"{i:02d}"
        filename = f"dp600_flashcards_chunk_{chunk_num}.md"
        
        output_file = save_flashcards(flashcards, analysis['content_folder'], filename)
        
        if output_file:
            print(f"   ✅ Generated {len(flashcards)} high-quality cards")
            print(f"   📁 Saved to: {analysis['content_folder']}/{filename}")
            
            generated_files.append({
                'file': str(output_file),
                'folder': analysis['content_folder'],
                'cards': len(flashcards),
                'topic': analysis['primary_topic']
            })
        else:
            print("   ❌ Failed to save flashcards")
    
    # Final summary
    print("\n" + "=" * 60)
    print(f"🎉 Successfully generated {len(generated_files)} flashcard files")
    
    if generated_files:
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
        
        print(f"\n📊 Generation Summary:")
        print(f"   Total flashcards: {total_cards}")
        for folder, stats in folder_summary.items():
            print(f"   {folder}: {stats['files']} files, {stats['cards']} cards")
        
        print(f"\n🔄 Next Steps:")
        print(f"1. Visit /admin/reload-flashcards in your app")
        print(f"2. Test the new high-quality flashcards")
        print(f"3. Review and fine-tune any cards as needed")


if __name__ == "__main__":
    main()