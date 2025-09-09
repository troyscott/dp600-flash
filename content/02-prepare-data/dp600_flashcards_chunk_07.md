# DP-600 Flashcards - Dp600_Flashcards_Chunk_07

Generated: 2025-09-08 20:25
Source: Hybrid LLM + Rule-based Generator

### Card 1
**Q:** How do you avoid inefficient transformations in Microsoft Fabric dataflows?
**A:** To avoid inefficient transformations:
- Disable sorting unless necessary during development.
- Turn off Staging for small volumes and simple transformations to reduce overhead.

**Difficulty:** Basic
**Tags:** dp-600, dataflow, transformation

---

### Card 2
**Q:** What are the best practices for writing efficient Spark code in Microsoft Fabric Notebooks?
**A:** Best practices include:
- Choosing appropriate data abstractions.
- Using cache effectively.
- Employing efficient joins and shuffles.
- Configuring Spark compute to reduce max nodes and executors.

**Difficulty:** Intermediate
**Tags:** dp-600, spark, notebook

---

### Card 3
**Q:** How can you optimize SQL queries in Microsoft Fabric?
**A:** Optimization techniques include:
- Selecting only necessary columns.
- Filtering data early with CTEs or subqueries.
- Keeping calculations and aggregations simple.

**Difficulty:** Basic
**Tags:** dp-600, sql, optimization

---

### Card 4
**Q:** Why is it important to gather statistics on warehouse tables in Microsoft Fabric?
**A:** Gathering statistics helps:
- Optimize query plans.
- Improve performance by enabling automatic optimizations.

**Difficulty:** Intermediate
**Tags:** dp-600, statistics, warehouse

---

### Card 5
**Q:** What is the role of a star schema in optimizing queries for warehouses in Microsoft Fabric?
**A:** A star schema helps:
- Write more efficient queries.
- Simplify query structure and improve performance.

**Difficulty:** Basic
**Tags:** dp-600, schema, optimization

---

### Card 6
**Q:** How does the Staging option work in Microsoft Fabric dataflows and when should it be used?
**A:** The Staging option:
- Loads all data to a hidden lakehouse.
- Can benefit complex transformations but adds overhead for simple ones.

**Difficulty:** Intermediate
**Tags:** dp-600, staging, transformation

---

### Card 7
**Q:** How can you effectively manage Spark sessions in Microsoft Fabric Notebooks?
**A:** Effective management includes:
- Ending active sessions when not needed.
- Using `spark.stop()` for scheduled notebooks to release resources.

**Difficulty:** Intermediate
**Tags:** dp-600, spark, notebook

---

### Card 8
**Q:** What is the purpose of using a Lakehouse versus a Warehouse in Microsoft Fabric?
**A:** Purpose:
- **Lakehouse**: Handles both structured and unstructured data.
- **Warehouse**: Optimized for structured data and SQL queries.

**Difficulty:** Basic
**Tags:** dp-600, lakehouse, warehouse

---

### Card 9
**Q:** How does OneLake in Microsoft Fabric enhance data management?
**A:** OneLake enhances:
- Data integration across different sources.
- Unified data storage and access for analytics and engineering tasks.

**Difficulty:** Intermediate
**Tags:** dp-600, onelake, management

---

### Card 10
**Q:** What are the benefits of using a query insights schema in Microsoft Fabric warehouses?
**A:** Benefits include:
- Access to views showing frequently run queries.
- Identification and optimization of long-running queries.

**Difficulty:** Basic
**Tags:** dp-600, warehouse, performance

---

