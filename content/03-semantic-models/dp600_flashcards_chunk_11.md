# DP-600 Flashcards - Dp600_Flashcards_Chunk_11

Generated: 2025-09-08 20:29
Source: Hybrid LLM + Rule-based Generator

### Card 1
**Q:** How do you use calculation groups in DAX to apply time intelligence logic?
**A:** To apply time intelligence logic using a calculation group:
- Create a measure: `Quantity MTD = CALCULATE([Total Quantity], 'Time Intelligence'[Period] = "MTD")`
- Ensure the measure uses the correct calculation item from the Time Intelligence group.
- Avoid directly applying filters to measures like `SUM(Sale[Quantity])` without using a calculation item.

**Difficulty:** Intermediate
**Tags:** dp-600, dax, semantic-model

---

### Card 2
**Q:** What is the purpose of dynamic strings in DAX?
**A:** Dynamic strings allow you to change formatting dynamically based on measure values:
- Set the format property to Dynamic.
- Use expressions like `VAR CurrentValue = SELECTEDMEASURE()`.
- Format numbers conditionally, e.g., adding a "K" suffix for large values.

**Difficulty:** Intermediate
**Tags:** dp-600, dax, dynamic-formatting

---

### Card 3
**Q:** How do you create and apply field parameters in Power BI reports?
**A:** To enable slicer-based switching between fields:
1. Create a parameter or measure that defines the field.
2. Use this parameter to filter data dynamically through slicers.
3. Adjust report visuals based on the selected slicer value.

**Difficulty:** Intermediate
**Tags:** dp-600, power-bi, semantic-model

---

### Card 4
**Q:** What is a star schema and how does it relate to Power BI?
**A:** Star Schema:
- Central fact table surrounded by dimension tables.
- Simplifies data modeling for business intelligence.
- In Power BI: helps in creating efficient queries and reports.

**Difficulty:** Basic
**Tags:** dp-600, semantic-model, star-schema

---

### Card 5
**Q:** What are the benefits of using a semantic model over traditional SQL queries?
**A:** Semantic Model Benefits:
- Optimized for OLAP (Online Analytical Processing).
- Provides advanced data aggregation and filtering.
- Enhances performance through pre-calculated measures and dimensions.

**Difficulty:** Basic
**Tags:** dp-600, semantic-model, olap

---

### Card 6
**Q:** How do you manage permissions in a Power BI semantic model?
**A:** To manage permissions:
1. Define roles with specific access levels.
2. Assign these roles to users or groups.
3. Use DAX expressions for advanced filtering and security measures.

**Difficulty:** Intermediate
**Tags:** dp-600, power-bi, security

---

### Card 7
**Q:** What is a calculation group in Power BI and how does it work?
**A:** Calculation Group:
- A set of related calculations.
- Used to apply consistent time intelligence or other analytical logic across measures.
- Enhances reusability and maintainability.

**Difficulty:** Intermediate
**Tags:** dp-600, dax, semantic-model

---

### Card 8
**Q:** How do you implement dynamic formatting in Power BI using DAX?
**A:** Dynamic Formatting Steps:
1. Use the Format property to set a measure's format as Dynamic.
2. Define logic for conditional formatting within DAX expressions.
3. Utilize functions like `SELECTEDMEASURE()` for context-based formatting.

**Difficulty:** Intermediate
**Tags:** dp-600, dax, dynamic-formatting

---

### Card 9
**Q:** What role does the Warehouse play in a semantic model compared to the Lakehouse?
**A:** In Semantic Models:
- **Warehouse**: Optimized SQL querying and transactional operations.
- **Lakehouse**: Supports unstructured data alongside structured data for analytics.

**Difficulty:** Basic
**Tags:** dp-600, warehouse, lakehouse

---

### Card 10
**Q:** How do you use DAX to enhance the performance of a Power BI semantic model?
**A:** Enhancing Performance:
- Use efficient DAX functions and patterns.
- Implement proper indexing and partitioning for large datasets.
- Leverage calculation groups for consistent time intelligence calculations.

**Difficulty:** Intermediate
**Tags:** dp-600, dax, performance

---

