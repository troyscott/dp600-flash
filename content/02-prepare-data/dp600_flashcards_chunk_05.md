# DP-600 Flashcards - Dp600_Flashcards_Chunk_05

Generated: 2025-09-08 20:23
Source: Hybrid LLM + Rule-based Generator

### Card 1
**Q:** How do you create stored procedures in Microsoft Fabric?
**A:** To create stored procedures:
- Navigate to `SQL endpoint` or `Warehouse Explorer`
- Use T-SQL commands like `CREATE PROCEDURE`
- Can also use Azure Data Studio or SQL Management Studio for templates

**Difficulty:** Intermediate  
**Tags:** dp-600, stored-procedures, sql-endpoint

---

### Card 2
**Q:** What are the steps to enrich data using Microsoft Fabric?
**A:** To enrich data:
- Use `Ingest Items` and T-SQL in Microsoft Fabric
- Add new columns or modify existing ones via SQL queries
- For Lakehouse Explorer: Edit Delta tables’ schema with notebooks or SparkJobs

**Difficulty:** Intermediate  
**Tags:** dp-600, data-preparation, enrichment

---

### Card 3
**Q:** How can you extend DataFrame schemas in Microsoft Fabric?
**A:** To extend DataFrame schemas:
- Use `withColumn()` to add new columns or modify existing ones
- Utilize `select()` to rename, retyping columns, and apply functions like `explode()`
- Works within notebooks for Delta tables

**Difficulty:** Basic  
**Tags:** dp-600, dataframe, schema-extension

---

### Card 4
**Q:** What are the limitations of altering table schemas in Microsoft Fabric's Warehouse Explorer?
**A:** Limitations:
- Cannot use T-SQL `ALTER TABLE ADD COLUMN`
- Need to delete and recreate tables for adding columns
- Use Lakehouse Explorer with notebooks or SparkJobs instead

**Difficulty:** Basic  
**Tags:** dp-600, warehouse-explorer, limitations

---

### Card 5
**Q:** How does OneLake enhance data integration in Microsoft Fabric?
**A:** OneLake:
- Unifies storage for both structured and unstructured data
- Streamlines data movement between Lakehouse and Warehouse
- Simplifies data governance across different environments

**Difficulty:** Intermediate  
**Tags:** dp-600, onelake, data-integration

---

### Card 6
**Q:** What are the key differences between a Data Factory and Microsoft Fabric?
**A:** Key differences:
- **Data Factory**: Centralized platform for ETL/ELT processes
- **Microsoft Fabric**: End-to-end analytics solution including Lakehouse/Warehouse
- **Use Case**: Data Factory focuses on data integration, while Fabric covers broader analytics needs

**Difficulty:** Basic  
**Tags:** dp-600, data-factory, microsoft-fabric

---

### Card 7
**Q:** How do you create a view in Microsoft Fabric's Warehouse Explorer?
**A:** To create a view:
- Use `SQL endpoint` or `Warehouse Explorer`
- Write T-SQL `CREATE VIEW` statement
- Utilize Azure Data Studio or SQL Management Studio templates for assistance

**Difficulty:** Basic  
**Tags:** dp-600, warehouse-explorer, views

---

### Card 8
**Q:** What are the advantages of using Delta Lake in Microsoft Fabric's Lakehouse?
**A:** Advantages:
- Supports both ACID transactions and schema evolution
- Enables efficient storage and querying for large datasets
- Provides snapshot isolation to ensure data consistency

**Difficulty:** Intermediate  
**Tags:** dp-600, delta-lake, lakehouse

---

### Card 9
**Q:** How can you manage security in Microsoft Fabric's Data Factory?
**A:** To manage security:
- Use **Azure Active Directory (AAD) integration**
- Configure role-based access control (RBAC)
- Utilize secure connection management for data sources

**Difficulty:** Intermediate  
**Tags:** dp-600, security, data-factory

---

### Card 10
**Q:** What are the steps to migrate a dataset from Data Factory to Microsoft Fabric's Lakehouse?
**A:** To migrate:
- Use **Data Factory’s Copy Activity**
- Specify source and sink datasets in Microsoft Fabric's Lakehouse
- Ensure compatibility with Delta Lake format for seamless integration

**Difficulty:** Intermediate  
**Tags:** dp-600, migration, lakehouse

---

