# DAX Calculations - DP-600 Flashcards

## DAX Variables and Functions

### Card 1
**Q:** What's the benefit of using VAR in DAX calculations?
**A:** 
- **Performance** - Avoids recalculating same expression multiple times
- **Readability** - Makes complex formulas easier to understand
- **Debugging** - Easier to test intermediate results
- **Maintainability** - Changes only need to be made in one place

**Difficulty:** Basic
**Tags:** var, performance, readability

---

### Card 2
**Q:** Write a DAX measure to calculate Year-over-Year growth percentage.
**A:** 
```dax
YoY Growth % = 
VAR CurrentYearSales = SUM(Sales[Amount])
VAR PreviousYearSales = 
    CALCULATE(
        SUM(Sales[Amount]),
        SAMEPERIODLASTYEAR(Calendar[Date])
    )
RETURN
    DIVIDE(
        CurrentYearSales - PreviousYearSales,
        PreviousYearSales,
        0
    )
```

**Difficulty:** Advanced
**Tags:** yoy, sameperiodlastyear, divide, time-intelligence

---

### Card 3
**Q:** What's the difference between FILTER and KEEPFILTERS in DAX?
**A:** 
- **FILTER** - Replaces existing filter context
- **KEEPFILTERS** - Adds to existing filter context (intersection)
- **Example:** `CALCULATE(SUM(Sales), FILTER(...))` vs `CALCULATE(SUM(Sales), KEEPFILTERS(...))`

**Difficulty:** Intermediate
**Tags:** filter, keepfilters, filter-context

---

## Iterator Functions

### Card 4
**Q:** Name the main X-iterator functions in DAX and their use cases.
**A:** 
- **SUMX** - Sum expression for each row
- **AVERAGEX** - Average expression for each row  
- **COUNTX** - Count non-blank expressions
- **MAXX/MINX** - Maximum/minimum expression value
- **CONCATENATEX** - Concatenate expressions with delimiter

**Difficulty:** Basic
**Tags:** iterators, sumx, averagex, countx

---

### Card 5
**Q:** Write a DAX measure to calculate the number of customers who made purchases above $1000.
**A:** 
```dax
High Value Customers = 
COUNTX(
    SUMMARIZE(
        Sales,
        Sales[CustomerID],
        "CustomerTotal", SUM(Sales[Amount])
    ),
    IF([CustomerTotal] > 1000, 1, BLANK())
)
```

**Difficulty:** Advanced
**Tags:** countx, summarize, if, customer-analysis

---

## Table Filtering Functions

### Card 6
**Q:** What's the difference between ALL, ALLEXCEPT, and ALLSELECTED?
**A:** 
- **ALL(table)** - Removes all filters from specified table/column
- **ALLEXCEPT(table, column1, column2)** - Removes all filters except specified columns
- **ALLSELECTED(table)** - Removes filters but keeps explicit selections from visual

**Difficulty:** Intermediate
**Tags:** all, allexcept, allselected, filter-removal

---

### Card 7
**Q:** How do you create a "% of Grand Total" calculation?
**A:** 
```dax
% of Grand Total = 
VAR CurrentValue = SUM(Sales[Amount])
VAR GrandTotal = 
    CALCULATE(
        SUM(Sales[Amount]),
        ALL(Products[Category])
    )
RETURN
    DIVIDE(CurrentValue, GrandTotal, 0)
```

**Difficulty:** Intermediate
**Tags:** percentage, grand-total, all, divide

---

## Windowing Functions

### Card 8
**Q:** What windowing functions are available in DAX?
**A:** 
- **INDEX** - Get value at specific position in sorted table
- **OFFSET** - Get value at relative position 
- **WINDOW** - Apply aggregation over defined window
- **RANK** - Assign rank based on expression values

**Difficulty:** Advanced
**Tags:** windowing, index, offset, window, rank

---

### Card 9
**Q:** Write DAX to calculate a running total of sales.
**A:** 
```dax
Running Total = 
CALCULATE(
    SUM(Sales[Amount]),
    FILTER(
        ALL(Calendar[Date]),
        Calendar[Date] <= MAX(Calendar[Date])
    )
)
```

**Difficulty:** Advanced
**Tags:** running-total, calculate, filter, time-calculation

---

## Information Functions

### Card 10
**Q:** What information functions help with debugging DAX?
**A:** 
- **HASONEVALUE** - Check if column has single value in context
- **ISBLANK/ISEMPTY** - Check for blank/empty values
- **VALUES** - Return distinct values in current context
- **SELECTEDVALUE** - Get single value or blank if multiple

**Difficulty:** Intermediate
**Tags:** information, hasonevalue, isblank, values, debugging

---

### Card 11
**Q:** How do you handle division by zero errors in DAX?
**A:** 
```dax
Safe Division = 
VAR Numerator = SUM(Sales[Amount])
VAR Denominator = SUM(Sales[Quantity])
RETURN
    IF(
        Denominator = 0,
        0,  -- or BLANK()
        DIVIDE(Numerator, Denominator)
    )
```

**Difficulty:** Basic
**Tags:** divide, error-handling, if, blank

---

## Calculation Groups

### Card 12
**Q:** What are calculation groups and when should you use them?
**A:** 
**Purpose:** Apply same calculations across multiple measures without duplicating code

**Use cases:**
- Time intelligence (YTD, QTD, Previous Year)
- Format variations (Currency, Percentage)
- Mathematical operations (Growth, Moving Average)

**Benefits:** Reduces measure proliferation, easier maintenance

**Difficulty:** Advanced
**Tags:** calculation-groups, time-intelligence, maintenance

---

### Card 13
**Q:** Create a calculation group item for "Previous Year" comparison.
**A:** 
```dax
-- Calculation Group Item: Previous Year
CALCULATE(
    SELECTEDMEASURE(),
    SAMEPERIODLASTYEAR(Calendar[Date])
)

-- Format String Expression (optional)
IF(
    SELECTEDMEASURE() IN {[Sales Amount], [Profit]},
    "$#,0",
    "#,0"
)
```

**Difficulty:** Expert
**Tags:** calculation-groups, selectedmeasure, sameperiodlastyear, format-string

---

## Dynamic Format Strings

### Card 14
**Q:** How do you create dynamic format strings based on measure values?
**A:** 
```dax
-- Format String Expression
VAR MeasureValue = [Sales Amount]
RETURN
    SWITCH(
        TRUE(),
        MeasureValue >= 1000000, "$#,0,,.0M",
        MeasureValue >= 1000, "$#,0,.0K", 
        "$#,0"
    )
```

**Difficulty:** Advanced
**Tags:** dynamic-format, format-string, switch, conditional-formatting

---

### Practice Scenario

**Q:** Create a DAX measure that shows sales performance vs. target, with dynamic formatting: green for over-target, red for under-target, and displays appropriate suffixes (K, M, B).

**A:** 
```dax
-- Sales vs Target
Sales vs Target = 
VAR ActualSales = SUM(Sales[Amount])
VAR TargetSales = SUM(Targets[Target])
VAR Performance = DIVIDE(ActualSales, TargetSales, 0)
VAR IsOverTarget = Performance >= 1
RETURN
    Performance

-- Format String Expression
VAR Value = [Sales vs Target]
VAR Color = IF(Value >= 1, "Green", "Red")
VAR Suffix = 
    SWITCH(
        TRUE(),
        ABS(Value) >= 1000000000, "B",
        ABS(Value) >= 1000000, "M",
        ABS(Value) >= 1000, "K",
        ""
    )
RETURN
    "_-" & Color & "* #,0" & 
    IF(Suffix <> "", ",," & Suffix, "") & 
    "_-"
```

**Difficulty:** Expert
**Tags:** scenario, performance, conditional-formatting, dynamic-format, real-world