#!/usr/bin/env python3
"""
Automated Flashcard Generator

This script processes PDF chunks and can integrate with AI APIs to automatically 
generate flashcards. Currently set up for manual processing with clear instructions.
"""

import os
import json
from pathlib import Path
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path):
    """Extract text content from PDF"""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        
        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text()
            text += f"\n--- Page {page_num + 1} ---\n{page_text}\n"
        
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None


def create_batch_processing_file():
    """Create a batch file with all PDF text for manual processing"""
    script_dir = Path(__file__).parent
    output_dir = script_dir / "output"
    batch_dir = script_dir / "batch_processing"
    batch_dir.mkdir(exist_ok=True)
    
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
    
    # Process each PDF
    batch_instructions = []
    
    for i, pdf_file in enumerate(sorted(pdf_files), 1):
        print(f"📖 Processing {pdf_file.name}...")
        
        # Extract text
        text_content = extract_text_from_pdf(pdf_file)
        if not text_content:
            continue
        
        # Create individual text file
        text_file = batch_dir / f"chunk_{i:02d}_{pdf_file.stem}.txt"
        with open(text_file, 'w', encoding='utf-8') as f:
            f.write(f"# DP-600 Study Material - Chunk {i}\n")
            f.write(f"# Source: {pdf_file.name}\n\n")
            f.write(text_content)
        
        # Add to batch instructions
        batch_instructions.append({
            "chunk_number": i,
            "source_file": pdf_file.name,
            "text_file": text_file.name,
            "suggested_output": f"dp600_flashcards_chunk_{i:02d}.md"
        })
    
    # Create master instruction file
    instructions_file = batch_dir / "PROCESSING_INSTRUCTIONS.md"
    with open(instructions_file, 'w', encoding='utf-8') as f:
        f.write("""# DP-600 Flashcard Generation Instructions

## 📋 Batch Processing Guide

### For Each Text File:

1. **Open the .txt file** and copy all content
2. **Paste into Claude Desktop** with this prompt:

```
Create comprehensive DP-600 flashcards from this Microsoft Fabric study material.

Use this EXACT format:

### Card 1
**Q:** [Clear, exam-style question]
**A:** [Detailed answer with bullets and formatting]
- Use bullet points for lists  
- **Bold** for important terms
- `Code` for technical terms/commands
- Include practical examples

**Difficulty:** Basic|Intermediate|Advanced
**Tags:** relevant, exam, tags

---

### Card 2
**Q:** [Next question]
**A:** [Answer with proper formatting]

**Difficulty:** [Level]  
**Tags:** [tags]

---

Create 8-12 cards per chunk. Focus on exam objectives: Maintain Analytics Solutions, Prepare Data, Semantic Models.
```

3. **Save the output** as the suggested filename below
4. **Move to appropriate content/ folder** in your DP-600 app

## 📁 Processing List:

""")
        
        for instruction in batch_instructions:
            f.write(f"""
### Chunk {instruction['chunk_number']}
- **Text File:** `{instruction['text_file']}`  
- **Source:** {instruction['source_file']}
- **Save As:** `{instruction['suggested_output']}`
- **Move To:** `content/[appropriate-folder]/`

""")
        
        f.write("""
## 🎯 Content Organization:

**01-maintain-analytics-solution/**
- Security, governance, workspace management
- Deployment pipelines, permissions

**02-prepare-data/**  
- Data ingestion, transformation
- Lakehouses, warehouses, SQL/KQL

**03-semantic-models/**
- Star schemas, DAX calculations  
- Performance optimization, Direct Lake

## ✅ After Processing:

1. Visit `/admin/reload-flashcards` in your app
2. Test new flashcards in study modes
3. Verify formatting looks correct

""")
    
    print(f"✅ Created batch processing files in: {batch_dir}")
    print(f"📄 Text files: {len(pdf_files)} chunks")
    print(f"📋 Instructions: {instructions_file}")
    print("\n🔄 Next Steps:")
    print(f"1. Open {instructions_file}")
    print("2. Follow the step-by-step instructions")
    print("3. Process each text file with Claude Desktop")


def main():
    print("🤖 DP-600 Automated Flashcard Generator")
    print("=" * 50)
    
    create_batch_processing_file()


if __name__ == "__main__":
    main()