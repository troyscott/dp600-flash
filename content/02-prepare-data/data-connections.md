# Data Connections - DP-600 Flashcards

## Data Sources and Ingestion

### Card 1
**Q:** What is the primary language used for data transformation in Microsoft Fabric pipelines?
**A:** The main languages for data transformation in Microsoft Fabric are:

- **SQL** - Most commonly used for data warehouse operations
- **KQL (Kusto Query Language)** - Used for real-time analytics and log queries
- **Power Query M** - Used in dataflows for ETL processes

Example KQL query:
```
Events
| where Timestamp > ago(1h)
| summarize count() by EventType
```

**Difficulty:** Basic
**Tags:** sql, kql, transformation, pipelines

---

### Card 2
**Q:** What is the difference between a lakehouse and data warehouse in Fabric?
**A:** **Lakehouse:**
- Stores **unstructured/semi-structured** data
- Uses *Delta Lake format* for ACID transactions
- Supports both `SQL` and `Spark` APIs
- Optimized for data science workloads

**Data Warehouse:**
- Stores **structured data** only
- Optimized for analytical queries
- Uses `SQL` endpoint exclusively
- Better for traditional BI scenarios

**Difficulty:** Intermediate
**Tags:** lakehouse, data-warehouse, storage, delta-lake

---