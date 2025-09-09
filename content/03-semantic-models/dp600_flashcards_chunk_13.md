# DP-600 Flashcards - Dp600_Flashcards_Chunk_13

Generated: 2025-09-08 20:31
Source: Hybrid LLM + Rule-based Generator

### Card 1
**Q:** What is a Common Table Expression (CTE) in Microsoft Fabric's SQL query editor?
**A:** A CTE, defined using the `WITH` clause, allows for more complex queries such as subqueries and can be used to rank data easily. For example:
```sql
WITH RankedCountries AS (
    SELECT Country, NumberOfHolidays, PaidTimeOff,
           RANK() OVER (ORDER BY NumberOfHolidays DESC) AS HolidayRank
    FROM Countries
)
SELECT * FROM RankedCountries;
```
**Difficulty:** Intermediate  
**Tags:** dp-600, CTE, SQL

---

### Card 2
**Q:** How can the output of a query in Lakehouse Explorer be used?
**A:** The output from queries run in Lakehouse Explorer can be utilized within `SELECT` and `CREATE VIEW`, but not with `CREATE TABLE`. This is because Lakehouse focuses on data transformation rather than storage.

**Difficulty:** Basic  
**Tags:** dp-600, lakehouse-explorer

---

### Card 3
**Q:** What are the main components of Microsoft Fabric's visual query editor?
**A:** The visual query editor uses Power Query Online with a modified display for query folding into native data source language (T-SQL), providing operations that can be viewed and copied as T-SQL code.

**Difficulty:** Basic  
**Tags:** dp-600, visual-query-editor

---

### Card 4
**Q:** How is the `GROUP BY` clause used in Microsoft Fabric?
**A:** The `GROUP BY` clause aggregates data based on common characteristics. For example:
```sql
SELECT Department, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Department;
```
This groups employees by department and counts them.

**Difficulty:** Basic  
**Tags:** dp-600, group-by

---

### Card 5
**Q:** What is the difference between Power BI's visual query editor and Microsoft Fabric's visual query editor?
**A:** While both use Power Query Online, Microsoft Fabric’s visual query editor modifies it for better integration with data sources through query folding, providing T-SQL code translation.

**Difficulty:** Intermediate  
**Tags:** dp-600, power-bi, fabric

---

### Card 6
**Q:** How does OneLake integrate with Lakehouse and Warehouse?
**A:** OneLake integrates by serving as a unified layer that combines the functionalities of both Lakehouse (for unstructured data) and Warehouse (for structured data), providing a single entry point for data exploration and analysis.

**Difficulty:** Intermediate  
**Tags:** dp-600, onelake

---

### Card 7
**Q:** What is query folding in Microsoft Fabric's visual query editor?
**A:** Query folding translates operations performed within the visual query editor into native SQL (T-SQL) code optimized for the underlying data source.

**Difficulty:** Basic  
**Tags:** dp-600, query-folding

---

### Card 8
**Q:** What is a key feature of Microsoft Fabric’s Lakehouse compared to traditional warehouses?
**A:** A key feature is its support for both structured and unstructured data, utilizing Delta Lake storage format for efficient handling.

**Difficulty:** Basic  
**Tags:** dp-600, lakehouse

---

### Card 9
**Q:** How does the visual query editor in Microsoft Fabric differ from traditional SQL editors?
**A:** The visual query editor uses Power Query Online with modifications to support query folding into T-SQL, enabling seamless integration and optimization for data sources.

**Difficulty:** Intermediate  
**Tags:** dp-600, visual-query-editor

---

### Card 10
**Q:** What is the role of Common Table Expressions (CTEs) in enhancing SQL queries within Microsoft Fabric?
**A:** CTEs allow complex queries to be written more clearly and efficiently. They can be used for subqueries, ranking functions, and recursive operations.

**Difficulty:** Intermediate  
**Tags:** dp-600, cte

---

