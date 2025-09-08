# DP-600 Flashcards - Dp600_Flashcards_Chunk_05

Generated: 2025-09-08 01:04
Source: Hybrid LLM + Rule-based Generator

### Card 3
**Q:** How do you add a new column to a DataFrame in Lakehouse using the `withColumn()` function?
**A:** To add a new column:
- Use the `withColumn()` function
- Pass the new column name and data type as arguments
- The function returns a new DataFrame with the added column

Example: `df = df.withColumn("new_column", lit("value"))`

**Difficulty:** Basic
**Tags:** lakehouse, data preparation

---

### Card 4
**Q:** What is the purpose of Delta Lake in Microsoft Fabric?
**A:** Delta Lake is a format used in Lakehouse that enables:
- Efficient storage and retrieval of data
- Incremental updates and versioning
- Support for ACID transactions

It provides a more efficient way to store data compared to traditional formats.

**Difficulty:** Basic
**Tags:** lakehouse, delta lake

---

### Card 5
**Q:** How do you modify an existing table in Warehouse using T-SQL?
**A:** Due to limitations in Warehouse Explorer and SQL endpoint:
- You cannot use `ALTER TABLE ADD COLUMN`
- Instead, delete the table and create it again with the desired columns

However, within Lakehouse Explorer, you can edit Delta tables schema using notebooks or SparkJobs.

**Difficulty:** Intermediate
**Tags:** warehouse, t-sql

---

### Card 6
**Q:** What is OneLake in Microsoft Fabric?
**A:** OneLake is a unified data framework that integrates:
- Data Factory
- Lakehouse
- Warehouse
- Fabric
It enables seamless data preparation, transformation, and analysis across all these components.

**Difficulty:** Basic
**Tags:** onelake, microsoft fabric

---

### Card 7
**Q:** How do you create a stored procedure in Microsoft Fabric using T-SQL?
**A:** To create a stored procedure:
- Open the T-SQL editor
- Use the `CREATE PROCEDURE` statement
- Define the procedure name and body
- Execute the procedure to test it

Example: `CREATE PROCEDURE my_procedure AS SELECT * FROM table_name;`

**Difficulty:** Intermediate
**Tags:** t-sql, stored procedures

---

### Card 8
**Q:** What is the main difference between Lakehouse and Warehouse in Microsoft Fabric?
**A:** The primary difference lies in their data storage and query capabilities:
- Lakehouse supports both structured and unstructured data
- Warehouse optimizes for structured data and SQL queries

Choose the right one based on your data type and query requirements.

**Difficulty:** Basic
**Tags:** lakehouse, warehouse

---

### Card 9
**Q:** How do you connect to a Workspace in Microsoft Fabric using Azure Data Studio or SQL Management Studio?
**A:** To connect:
- Open Azure Data Studio or SQL Management Studio
- Select the workspace and data item
- Use the provided templates for creating views, functions, and stored procedures

These tools provide a seamless experience for working with Microsoft Fabric workspaces.

**Difficulty:** Intermediate
**Tags:** azure data studio, sql management studio

---

### Card 10
**Q:** What is the purpose of `Row-Level Security (RLS)` in Microsoft Fabric?
**A:** RLS enables fine-grained access control to data:
- It enforces permissions based on row-level security policies
- It ensures that users only access authorized rows and columns

This feature enhances data security and privacy within workspaces.

**Difficulty:** Intermediate
**Tags:** rls, row-level security

---

