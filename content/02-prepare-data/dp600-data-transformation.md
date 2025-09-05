# Data Transformation - DP-600 Flashcards

## Star Schema Implementation

### Card 1
**Q:** What are the key components of a star schema in Fabric?
**A:** 
- **Fact tables** - Central tables with measures/metrics
- **Dimension tables** - Descriptive attributes that provide context
- **Foreign keys** - Connect fact tables to dimensions
- **Surrogate keys** - Artificial keys for dimension tables

**Difficulty:** Basic
**Tags:** star-schema, fact-table, dimension, keys

---

### Card 2
**Q:** When should you use a snowflake schema instead of a star schema?
**A:** 
- When dimension tables are very large and normalization saves significant space
- When dimension hierarchies are complex and change frequently
- **However:** Star schema is usually preferred in Fabric for better performance

**Difficulty:** Intermediate
**Tags:** snowflake-schema, normalization, performance

---

### Card 3
**Q:** How do you create a date dimension table in Fabric?
**A:** 
```sql
-- Option 1: Auto-generated
SELECT * FROM CALENDAR_AUTO()

-- Option 2: Custom range
SELECT * FROM CALENDAR(DATE(2020,1,1), DATE(2025,12,31))

-- Option 3: M query in Power Query
= List.Dates(#date(2020,1,1), 365*5, #duration(1,0,0,0))
```

**Difficulty:** Intermediate
**Tags:** date-dimension, calendar, sql, m-query

---

## Data Denormalization

### Card 4
**Q:** What's the main reason to denormalize data in an analytical solution?
**A:** 
- **Query performance** - Reduces joins needed for analysis
- **Simplicity** - Easier for business users to understand
- **Aggregation efficiency** - Pre-calculated values available
- **Trade-off:** Increased storage space and potential redundancy

**Difficulty:** Basic
**Tags:** denormalization, performance, storage

---

### Card 5
**Q:** How do you handle slowly changing dimensions (SCD) Type 2 in Fabric?
**A:** 
1. Add columns: `ValidFrom`, `ValidTo`, `IsCurrent`
2. Keep historical records with different validity periods
3. Use surrogate keys to track different versions
4. Update logic preserves history while adding new records

**Difficulty:** Advanced
**Tags:** scd, type-2, historical-data, versioning

---

## Data Quality

### Card 6
**Q:** What are the main approaches to handle missing data in Fabric?
**A:** 
- **Remove rows** - When missing data is minimal
- **Default values** - Replace with 0, "Unknown", or calculated defaults
- **Interpolation** - Calculate based on surrounding values
- **Flag columns** - Add indicator columns for missing data

**Difficulty:** Intermediate
**Tags:** missing-data, data-quality, interpolation

---

### Card 7
**Q:** How do you identify duplicate records in a lakehouse using SQL?
**A:** 
```sql
-- Find duplicates
SELECT CustomerID, Email, COUNT(*) as DuplicateCount
FROM customers
GROUP BY CustomerID, Email
HAVING COUNT(*) > 1

-- Remove duplicates (keep first)
SELECT DISTINCT * FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY CustomerID ORDER BY CreatedDate) as rn
  FROM customers
) WHERE rn = 1
```

**Difficulty:** Intermediate
**Tags:** duplicates, sql, row-number, data-cleaning

---

## Data Aggregation

### Card 8
**Q:** What's the difference between aggregating in the lakehouse vs. semantic model?
**A:** 
- **Lakehouse aggregation** - Pre-calculated, stored physically, faster queries
- **Semantic model aggregation** - Calculated at query time, more flexible
- **Best practice** - Pre-aggregate common calculations in lakehouse, detailed calculations in semantic model

**Difficulty:** Advanced
**Tags:** aggregation, lakehouse, semantic-model, performance

---

### Card 9
**Q:** How do you create a rolling average in Fabric SQL?
**A:** 
```sql
SELECT 
  OrderDate,
  OrderAmount,
  AVG(OrderAmount) OVER (
    ORDER BY OrderDate 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) as Rolling7DayAvg
FROM orders
ORDER BY OrderDate
```

**Difficulty:** Advanced
**Tags:** rolling-average, window-functions, sql

---

## Data Merging and Joining

### Card 10
**Q:** What join types are available in Fabric dataflows?
**A:** 
- **Inner join** - Only matching records
- **Left outer join** - All from left, matching from right
- **Right outer join** - All from right, matching from left  
- **Full outer join** - All records from both tables
- **Anti join** - Records in left but not in right
- **Cross join** - Cartesian product

**Difficulty:** Basic
**Tags:** joins, dataflows, inner-join, outer-join

---

### Card 11
**Q:** When should you use merge vs. append in Power Query?
**A:** 
- **Merge** - Combining columns from different tables (horizontal combination)
- **Append** - Combining rows from tables with same structure (vertical combination)
- **Example:** Merge customer data with orders vs. Append Q1, Q2, Q3, Q4 sales data

**Difficulty:** Basic
**Tags:** merge, append, power-query, horizontal, vertical

---

## Advanced Transformations

### Card 12
**Q:** How do you create a bridge table for many-to-many relationships?
**A:** 
1. **Identify** the many-to-many relationship (e.g., Students ↔ Courses)
2. **Create bridge table** with foreign keys from both entities
3. **Remove direct relationship** between main tables
4. **Connect** both main tables to bridge table
5. **Set filter direction** appropriately

**Difficulty:** Advanced
**Tags:** bridge-table, many-to-many, relationships

---

### Practice Scenario

**Q:** You have raw sales data with inconsistent date formats, missing customer names, and duplicate orders. Describe your transformation pipeline.

**A:** 
1. **Data quality assessment** - Profile data to identify issues
2. **Date standardization** - Use Power Query to detect and convert date formats
3. **Missing data handling** - Replace missing customer names with "Unknown Customer"
4. **Duplicate removal** - Use OrderID and Date as composite key for deduplication
5. **Star schema creation** - Separate into fact (sales) and dimension tables (customer, product, date)
6. **Validation** - Add data quality checks and exception handling

**Difficulty:** Expert
**Tags:** scenario, data-pipeline, transformation, real-world