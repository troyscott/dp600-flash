# DP-600 Flashcards - Dp600_Flashcards_Chunk_09

Generated: 2025-09-08 20:26
Source: Hybrid LLM + Rule-based Generator

### Card 1
**Q:** How do you create a summarized table using DAX functions in Power BI?
**A:** To create a summarized table:
- Use `SUMMARIZE` or `SUMMARIZECOLUMNS`
- Specify columns for grouping and aggregation if needed
- Example: 
```
SUMMARIZE(Sale, 'Date'[Year], 'Date'[Month])
```

**Difficulty:** Basic
**Tags:** dp-600, dax, semantic-model

---

### Card 2
**Q:** What is the difference between `SUMMARIZE` and `SUMMARIZECOLUMNS` in DAX?
**A:** Key differences:
- **SUMMARIZE**: Requires specifying a table name followed by columns to group.
- **SUMMARIZECOLUMNS**: Only requires column names, no need for table specification.

**Difficulty:** Basic
**Tags:** dp-600, dax, semantic-model

---

### Card 3
**Q:** How does `ADDCOLUMNS` function work in DAX?
**A:** `ADDCOLUMNS`:
- Adds new columns to an existing table.
- Example: 
```
ADDCOLUMNS(ALL('Date'[Month], 'Date'[Month Number]), "Sale Rows", CALCULATE(COUNTROWS(Sale)))
```

**Difficulty:** Basic
**Tags:** dp-600, dax, semantic-model

---

### Card 4
**Q:** What role does context transition play in DAX when using `ADDCOLUMNS`?
**A:** Context transition:
- Necessary to get distinct values for each row.
- Example: 
```
CALCULATE(COUNTROWS(Sale))
```

**Difficulty:** Intermediate
**Tags:** dp-600, dax, semantic-model

---

### Card 5
**Q:** How does `SELECTCOLUMNS` function differ from `ADDCOLUMNS` in DAX?
**A:** Differences:
- **SELECTCOLUMNS**: Filters columns to select specific ones.
- **ADDCOLUMNS**: Adds new calculated columns.

**Difficulty:** Basic
**Tags:** dp-600, dax, semantic-model

---

### Card 6
**Q:** What is the purpose of row-level security (RLS) in Power BI?
**A:** RLS:
- Restricts data access for users.
- Applies filters to queries based on user roles.

**Difficulty:** Intermediate
**Tags:** dp-600, rls, semantic-model

---

### Card 7
**Q:** How can you implement row-level security (RLS) in Power BI?
**A:** Steps:
1. Define RLS rules in the data model.
2. Assign roles to users or groups.
3. Apply RLS filters to datasets.

**Difficulty:** Intermediate
**Tags:** dp-600, rls, semantic-model

---

### Card 8
**Q:** What is a semantic model in Power BI?
**A:** A semantic model:
- Represents business data and relationships.
- Includes tables, columns, measures, and relationships.

**Difficulty:** Basic
**Tags:** dp-600, semantic-model, power-bi

---

