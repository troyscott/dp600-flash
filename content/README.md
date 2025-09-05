# DP-600 Flashcard Content

This directory contains flashcards organized by DP-600 exam objectives.

## Directory Structure

```
content/
├── 01-maintain-analytics-solution/
│   ├── security-governance.md
│   ├── workspace-access-controls.md
│   ├── item-level-access.md
│   ├── development-lifecycle.md
│   └── deployment-pipelines.md
├── 02-prepare-data/
│   ├── get-data.md
│   ├── data-connections.md
│   ├── onelake-integration.md
│   ├── transform-data.md
│   ├── star-schema.md
│   ├── query-analyze-sql.md
│   └── query-analyze-kql.md
└── 03-semantic-models/
    ├── design-build-models.md
    ├── dax-calculations.md
    ├── storage-modes.md
    ├── performance-optimization.md
    └── direct-lake.md
```

## Markdown Format for Claude Desktop

When creating flashcards with Claude Desktop, use this exact format:

```markdown
# Topic Name - DP-600 Flashcards

## Section Name

### Card 1
**Q:** Your question here?
**A:** Your answer here. Can include:
- Bullet points
- **Bold text**
- Multiple lines

**Difficulty:** Basic|Intermediate|Advanced
**Tags:** tag1, tag2, tag3

---

### Card 2
**Q:** Another question?
**A:** Another answer with detailed explanation.

**Difficulty:** Intermediate
**Tags:** more, tags

---
```

## Important Notes

- Each card MUST be separated by `---`
- Questions start with `**Q:**`
- Answers start with `**A:**`
- Difficulty and Tags are optional (currently ignored by app)
- Categories are auto-detected from directory names
- File names should be descriptive (e.g., `security-governance.md`)

## Claude Desktop Prompt Template

Use this prompt when uploading PDF chunks to Claude Desktop:

```
Create DP-600 flashcards from this study material using the following format:

**Q:** [question]
**A:** [detailed answer]

**Difficulty:** [Basic/Intermediate/Advanced]
**Tags:** [relevant, tags, here]

---

Focus on exam-relevant concepts. Make answers detailed but concise. 
Separate each flashcard with --- dividers.
```

## Adding New Content

1. Create or edit .md files in appropriate subdirectories
2. Follow the **Q:**/**A:** format with `---` separators
3. Visit `/admin/reload-flashcards` to reload without restarting the app
4. Test your flashcards in the study modes

## Categories

The app automatically maps directory names to categories:

- `01-maintain-analytics-solution/` → "Maintain Analytics Solution"
- `02-prepare-data/` → "Prepare Data"
- `03-semantic-models/` → "Semantic Models"