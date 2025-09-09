# DP-600 Flashcards - Dp600_Flashcards_Chunk_12

Generated: 2025-09-08 20:30
Source: Hybrid LLM + Rule-based Generator

### Card 1
**Q:** How can you correct a graph showing incorrect quantity sales for black stock items?
**A:** To fix the graph:
- Create this measure:
```DAX
Total Quantity = CALCULATE(SUM(Sale[Quantity]), TREATAS(VALUES('Stock Item'[Stock Item Key]), Sale[Stock Item Key]))
```
This approach ensures accurate aggregation without altering data model relationships.

**Difficulty:** Intermediate  
**Tags:** dp-600, DAX, measures

---

### Card 2
**Q:** What is the best way to create a line chart showing sales quantity by invoice date when the relationship between Date and Sale tables based on Invoice Date Key is inactive?
**A:** To address this:
- Activate the relationship between 'Date'[Date] and Sale[Invoice Date Key].
This action allows direct querying without additional measures.

**Difficulty:** Basic  
**Tags:** dp-600, relationships, DAX

---

### Card 3
**Q:** Why might incremental refresh not be functioning as expected for a dataset sourced from Azure SQL Database?
**A:** The likely issue is:
- A transformation step breaks query folding before date filtering.
This disrupts the ability to leverage server-side processing benefits of incremental refresh.

**Difficulty:** Intermediate  
**Tags:** dp-600, Power BI, transformations

---

### Card 4
**Q:** How do you ensure accurate data aggregation in Power BI when there is a need for complex measure calculations?
**A:** Use DAX measures to handle complex aggregations:
```DAX
Total Quantity = CALCULATE(SUM(Sale[Quantity]), TREATAS(VALUES('Stock Item'[Stock Item Key]), Sale[Stock Item Key]))
```
This ensures the measure correctly aggregates data based on specific filters.

**Difficulty:** Intermediate  
**Tags:** dp-600, DAX, measures

---

### Card 5
**Q:** What is a recommended approach to maintain flexibility and performance in Power BI datasets while supporting both daily sales analysis by delivery date and invoice date?
**A:** Maintain active relationships for both scenarios:
- Keep the relationship between 'Date'[Delivery Date] and Sale[Delivery Date Key].
- Activate the relationship between 'Date'[Invoice Date] and Sale[Invoice Date Key].

This allows simultaneous use of different date keys without disrupting data integrity.

**Difficulty:** Intermediate  
**Tags:** dp-600, relationships, Power BI

---

### Card 6
**Q:** How can you optimize dataset refresh in Power BI when dealing with large fact tables?
**A:** Implement incremental refresh:
1. Configure filtering on the sales date column.
2. Ensure no transformation steps break query folding prior to applying filters.

This method reduces data volume processed during each refresh cycle.

**Difficulty:** Intermediate  
**Tags:** dp-600, Power BI, transformations

---

### Card 7
**Q:** What is the significance of row-level security (RLS) in a Microsoft Fabric workspace?
**A:** RLS in Fabric enhances security by:
- Allowing conditional access based on user roles.
- Enabling granular data visibility control per user or group.

This feature is crucial for environments with diverse user permissions and data sensitivity levels.

**Difficulty:** Intermediate  
**Tags:** dp-600, security, workspace

---

### Card 8
**Q:** How do you create an active physical relationship between the Sale and Stock Item tables in Power BI to ensure accurate data aggregation?
**A:** To establish a robust relationship:
1. Create a new relationship.
2. Link `Sale[Stock Item Key]` with `'Stock Item'[Stock Item Key]`.
3. Ensure this is set as an active, physical relationship for reliable measure calculations.

This setup ensures correct data filtering and aggregation across tables.

**Difficulty:** Basic  
**Tags:** dp-600, relationships, Power BI

---

### Card 9
**Q:** What are the main differences between a Lakehouse and Warehouse in Microsoft Fabric?
**A:** Key distinctions:
- **Lakehouse**: Supports both structured and unstructured data.
- **Warehouse**: Optimized for structured data and SQL queries.
- Storage: Lakehouse uses `Delta Lake` format.
- Performance: Warehouse provides faster analytical query performance.

This understanding helps choose the right storage type based on dataset characteristics.

**Difficulty:** Basic  
**Tags:** dp-600, lakehouse, warehouse

---

### Card 10
**Q:** How do you troubleshoot an issue where incremental refresh in Power BI does not appear to be functioning properly?
**A:** Steps for troubleshooting:
1. Verify query folding is intact before date filtering.
2. Ensure Azure SQL Database supports incremental refresh configurations.

Correcting these can enable efficient dataset refreshing.

**Difficulty:** Intermediate  
**Tags:** dp-600, Power BI, transformations

---

