# Claude Desktop Prompt Kit for DP-600 Flashcards

## 🎯 Primary Prompt (Paste this with each PDF chunk)

```
Create comprehensive DP-600 flashcards from this Microsoft Fabric study material using the exact format below.

Focus on exam-relevant concepts, practical scenarios, and key differences between technologies.

**EXACT FORMAT TO USE:**

### Card 1
**Q:** [Clear, exam-style question]
**A:** [Detailed answer with bullets, examples, and formatting]
- Use bullet points for lists
- **Bold** for important terms
- `Code` for technical terms, commands, SQL
- Include practical examples when relevant

**Difficulty:** Basic|Intermediate|Advanced
**Tags:** relevant, exam, tags

---

### Card 2
**Q:** [Next question]
**A:** [Answer with proper formatting]

**Difficulty:** [Level]
**Tags:** [tags]

---

REQUIREMENTS:
- Create 8-12 flashcards per PDF chunk
- Questions should test understanding, not just memorization  
- Include practical scenarios and "what would you do" questions
- Use bullet points for multi-part answers
- Bold key terms and concepts
- Use backticks for code, commands, and technical terms
- Each card MUST be separated by ---
- Focus on DP-600 exam objectives: Maintain Analytics Solutions, Prepare Data, Semantic Models
```

## 🔄 Follow-up Prompts (if needed)

### More Detailed Cards:
```
These flashcards need more detail. For each card, expand the answers to include:
- Step-by-step procedures where applicable
- Key differences between similar concepts
- Common pitfalls or gotchas
- Real-world examples
- Keep the same format with --- separators
```

### Focus on Specific Topics:
```
Create additional flashcards specifically focused on [TOPIC] from this material:
- Include scenario-based questions
- Add troubleshooting scenarios
- Use the same markdown format with --- separators
```

### Convert to Different Difficulty:
```
Convert these flashcards to [Basic/Intermediate/Advanced] level:
- Adjust question complexity
- Add or remove technical details as needed
- Keep the same markdown format
```

## 📝 Saving Instructions

1. **Copy the generated flashcards**
2. **Save as .md files** in appropriate folders:
   - `content/01-maintain-analytics-solution/[topic].md`
   - `content/02-prepare-data/[topic].md`  
   - `content/03-semantic-models/[topic].md`
3. **Visit `/admin/reload-flashcards`** in your app
4. **Test the new cards** in your study modes

## 🎯 Topic Organization Guide

**01-maintain-analytics-solution/**
- security-governance.md
- workspace-management.md
- deployment-pipelines.md
- item-permissions.md

**02-prepare-data/**
- data-ingestion.md
- data-transformation.md
- lakehouse-warehouse.md
- sql-kql-queries.md

**03-semantic-models/**
- star-schema-design.md
- dax-calculations.md
- performance-optimization.md
- direct-lake-mode.md

## ✅ Quality Checklist

Before saving flashcards, ensure:
- [ ] Each card has **Q:** and **A:**
- [ ] Cards are separated by **---**
- [ ] Answers use proper formatting (bullets, bold, code)
- [ ] Questions test understanding, not memorization
- [ ] Difficulty and tags are included
- [ ] Focus is on exam-relevant content