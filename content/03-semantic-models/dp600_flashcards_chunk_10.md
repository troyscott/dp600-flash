# DP-600 Flashcards - Dp600_Flashcards_Chunk_10

Generated: 2025-09-08 20:27
Source: Hybrid LLM + Rule-based Generator

### Card 1
**Q:** What is the `COUNTROWS` DAX function used for?
**A:** The `COUNTROWS` DAX function counts the number of rows in a table or an expression that returns a table.
Example: `Sale Rows = COUNTROWS(Sale)`
This measure returns the count of rows within the Sale table.

**Difficulty:** Basic
**Tags:** dp-600, dax, semantic-model

---

### Card 2
**Q:** How does the DISTINCTCOUNT DAX function work?
**A:** The `DISTINCTCOUNT` function counts the number of distinct values in a column or columns.
Example: `Distinct Customers = DISTINCTCOUNT(Sales[CustomerID])`
This measure returns the count of unique Customer IDs.

**Difficulty:** Basic
**Tags:** dp-600, dax, semantic-model

---

### Card 3
**Q:** What is the difference between COUNT and COUNTA in DAX?
**A:** 
- `COUNT` counts non-blank values but only for numeric types.
Example: `Count Numeric = COUNT(Sales[OrderQty])`
- `COUNTA` counts all non-blank values regardless of data type.
Example: `All NonBlank = COUNTA(Sales[CustomerName])`

**Difficulty:** Basic
**Tags:** dp-600, dax, semantic-model

---

### Card 4
**Q:** Explain the purpose and usage of the DISTINCTCOUNTNOBLANK function in DAX.
**A:** The `DISTINCTCOUNTNOBLANK` is used to count distinct non-blank values in a column. It's useful when you need to ignore blank entries while counting unique items.
Example: 
```
Distinct NonBlankCustomers = DISTINCTCOUNTNOBLANK(Sales[CustomerID])
```

**Difficulty:** Intermediate
**Tags:** dp-600, dax, semantic-model

---

### Card 5
**Q:** What does the COUNTX function do in DAX?
**A:** The `COUNTX` function counts rows where a given expression is not blank.
Example:
```DAX
CountXInvoiceDelivery = COUNTX(Sales, Sales[InvoiceDateKey] <> BLANK() || Sales[DeliveryDateKey] <> BLANK())
```
This measure returns the count of sales entries where either invoice or delivery date keys are non-blank.

**Difficulty:** Intermediate
**Tags:** dp-600, dax, semantic-model

---

### Card 6
**Q:** How is COUNTAX used in DAX?
**A:** The `COUNTAX` function counts the number of rows that satisfy a condition where an expression evaluates to non-blank.
Example: 
```DAX
CountWithCondition = COUNTAX(Sales, Sales[OrderQty] > 0)
```
This measure returns the count of sales orders with positive quantities.

**Difficulty:** Intermediate
**Tags:** dp-600, dax, semantic-model

---

### Card 7
**Q:** What is the use of SUMMARIZE in DAX?
**A:** The `SUMMARIZE` function creates an in-memory table that contains a summary or rollup of data from the specified table.
Example:
```DAX
YearsAndMonths = SUMMARIZE(Sales, 'Date'[Year], 'Date'[Month])
```
This generates a table summarizing sales by year and month.

**Difficulty:** Intermediate
**Tags:** dp-600, dax, semantic-model

---

### Card 8
**Q:** What does the COUNTBLANK function do in DAX?
**A:** The `COUNTBLANK` function counts the number of blank values within a column.
Example:
```DAX
BlankDeliveryDates = COUNTBLANK(Sales[DeliveryDateKey])
```
This measure returns the count of rows where Delivery Date Key is blank.

**Difficulty:** Basic
**Tags:** dp-600, dax, semantic-model

---

### Card 9
**Q:** How do you use SUMMARIZE and COUNTROWS together in DAX?
**A:** `SUMMARIZE` can be used to group data by one or more columns, and then `COUNTROWS` counts the resulting rows.
Example:
```DAX
DistinctYearMonth = COUNTROWS(SUMMARIZE(Sales, 'Date'[Year], 'Date'[Month]))
```
This measure returns the count of distinct year-month combinations in sales.

**Difficulty:** Intermediate
**Tags:** dp-600, dax, semantic-model

---

### Card 10
**Q:** What is the role of COUNTAX when dealing with dynamic tables?
**A:** `COUNTAX` evaluates an expression for each row within a table and counts the number of non-blank results.
Example:
```DAX
DynamicTableCount = COUNTAX(DynamicTable, [ColumnExpression] <> BLANK())
```
This measure returns the count of rows where the evaluated expression is not blank.

**Difficulty:** Intermediate
**Tags:** dp-600, dax, semantic-model

---

