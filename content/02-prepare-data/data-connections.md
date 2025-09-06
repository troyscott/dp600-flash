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
**A:** Here are the key differences between these two storage options:

**Lakehouse Features:**
1. **Data Types**
   - Unstructured data (JSON, images, logs)
   - Semi-structured data (Parquet, CSV)
   - Structured data (tables)

2. **Technology Stack**
   - Uses *Delta Lake format* for ACID transactions
   - Supports both `SQL` and `Spark` APIs
   - Schema-on-read approach

3. **Best Use Cases**
   - Data science workloads
   - Real-time analytics
   - Data exploration and discovery

**Data Warehouse Features:**
1. **Data Types**
   - Structured data only
   - Predefined schemas required

2. **Technology Stack** 
   - Uses `SQL` endpoint exclusively
   - Traditional relational database model
   - Schema-on-write approach

3. **Best Use Cases**
   - Traditional BI scenarios
   - Complex analytical queries
   - Enterprise reporting

**Performance Comparison:**
- **Lakehouse**: Better for flexible analytics and ML
- **Data Warehouse**: Better for consistent, high-performance queries

**Difficulty:** Intermediate
**Tags:** lakehouse, data-warehouse, storage, delta-lake

---