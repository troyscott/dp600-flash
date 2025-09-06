#!/usr/bin/env python3
"""
Flashcard Loader for DP-600 Study App

Loads flashcards from markdown files in the content/ directory.
Parses Q: and A: format with --- separators between cards.
"""

import os
import re
from pathlib import Path
from typing import List, Dict


def parse_markdown_file(file_path: Path) -> List[Dict]:
    """
    Parse a single markdown file to extract flashcards.
    
    Args:
        file_path: Path to the markdown file
        
    Returns:
        List of flashcard dictionaries
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []
    
    # Split content by --- separators
    card_blocks = content.split('---')
    
    flashcards = []
    card_id = 1
    
    # Determine category from directory structure
    category = get_category_from_path(file_path)
    
    for block in card_blocks:
        block = block.strip()
        if not block:
            continue
            
        # Extract Q: and A: sections
        question_match = re.search(r'\*\*Q:\*\*\s*(.*?)(?=\*\*A:\*\*)', block, re.DOTALL)
        answer_match = re.search(r'\*\*A:\*\*\s*(.*?)(?=\*\*Difficulty:\*\*|$)', block, re.DOTALL)
        
        if question_match and answer_match:
            question = question_match.group(1).strip()
            answer = answer_match.group(1).strip()
            
            # Clean up formatting
            question = clean_text(question)
            answer = clean_text(answer)
            
            if question and answer:
                flashcard = {
                    "id": card_id,
                    "category": category,
                    "question": question,
                    "answer": answer,
                    "source_file": str(file_path.name)
                }
                flashcards.append(flashcard)
                card_id += 1
    
    return flashcards


def get_category_from_path(file_path: Path) -> str:
    """
    Extract category name from directory path.
    
    Args:
        file_path: Path to the markdown file
        
    Returns:
        Human-readable category name
    """
    parent_dir = file_path.parent.name
    
    # Map directory names to display names
    category_mapping = {
        "01-maintain-analytics-solution": "Maintain Analytics Solution",
        "02-prepare-data": "Prepare Data", 
        "03-semantic-models": "Semantic Models"
    }
    
    return category_mapping.get(parent_dir, parent_dir.replace('-', ' ').title())


def clean_text(text: str) -> str:
    """
    Clean up text formatting while preserving markdown structure.
    
    Args:
        text: Raw text from markdown
        
    Returns:
        Cleaned text with preserved formatting
    """
    # Remove leading/trailing whitespace but preserve internal structure
    text = text.strip()
    
    # Remove excessive blank lines (3+ consecutive newlines become 2)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Clean up line endings but preserve list structure
    text = re.sub(r'[ \t]+\n', '\n', text)  # Remove trailing spaces
    text = re.sub(r'\n[ \t]+', '\n', text)  # Remove leading spaces on new lines
    
    return text


def load_all_flashcards() -> List[Dict]:
    """
    Load all flashcards from content/ directory.
    
    Returns:
        List of all flashcard dictionaries with sequential IDs
    """
    content_dir = Path("content")
    
    if not content_dir.exists():
        print("Warning: content/ directory not found")
        return []
    
    all_flashcards = []
    current_id = 1
    
    # Recursively find all .md files
    for md_file in content_dir.rglob("*.md"):
        print(f"Loading flashcards from: {md_file}")
        
        file_cards = parse_markdown_file(md_file)
        
        # Reassign sequential IDs
        for card in file_cards:
            card["id"] = current_id
            current_id += 1
            
        all_flashcards.extend(file_cards)
        
        print(f"  → Loaded {len(file_cards)} cards")
    
    print(f"\nTotal flashcards loaded: {len(all_flashcards)}")
    print_category_summary(all_flashcards)
    
    return all_flashcards


def print_category_summary(flashcards: List[Dict]) -> None:
    """Print summary of flashcards by category."""
    categories = {}
    for card in flashcards:
        category = card['category']
        categories[category] = categories.get(category, 0) + 1
    
    print("\nFlashcards by category:")
    for category, count in categories.items():
        print(f"  • {category}: {count} cards")


def reload_flashcards() -> List[Dict]:
    """
    Reload all flashcards (useful for development).
    
    Returns:
        Fresh list of all flashcard dictionaries
    """
    print("Reloading flashcards from markdown files...")
    return load_all_flashcards()


if __name__ == "__main__":
    # Test the loader
    flashcards = load_all_flashcards()
    
    if flashcards:
        print(f"\n📚 Example flashcard:")
        example = flashcards[0]
        print(f"ID: {example['id']}")
        print(f"Category: {example['category']}")
        print(f"Question: {example['question']}")
        print(f"Answer: {example['answer']}")
        print(f"Source: {example['source_file']}")
    else:
        print("No flashcards found!")