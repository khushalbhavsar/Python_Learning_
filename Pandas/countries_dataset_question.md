# Pandas Practice Questions – Countries Dataset (25 Questions)

## Level 1: Data Exploration

1. Load the `Countries(1).csv` dataset into a Pandas DataFrame.

2. Display the first 10 rows and the last 10 rows of the dataset.

3. Find:

   * Number of rows and columns
   * Column names
   * Data types of all columns
   * Memory usage of the dataset

4. Display the statistical summary of all numerical columns.

---

## Level 2: Selecting Data

5. Display only the following columns:

   * `country`
   * `capital_city`
   * `continent`
   * `population`

6. Display the first 15 countries using `iloc`.

7. Display the country, GDP, and population of the country at index 50 using `loc`.

---

## Level 3: Filtering

8. Display all countries from **Asia**.

9. Display all countries whose population is greater than **100 million**.

10. Display all countries where:

* Internet access is greater than **80%**
* Life expectancy is greater than **75 years**

11. Display all countries having **GDP greater than the average GDP**.

---

## Level 4: Sorting

12. Sort the countries by **GDP** in descending order.

13. Display the **Top 10 countries by population**.

14. Display the **Top 10 countries with the highest life expectancy**.

---

## Level 5: Missing Data

15. Find the total number of missing values in each column.

16. Display only the rows that contain missing values.

17. Replace all missing numerical values with the column mean.

---

## Level 6: Data Operations

18. Create a new column:

**Population Density**

Formula:

```
Population / Land Area
```

19. Create another column:

**Male Percentage**

Formula:

```
(population_male / population) * 100
```

---

## Level 7: GroupBy & Aggregation

20. Find the average GDP of each continent.

21. Find:

* Maximum population
* Minimum population
* Average life expectancy

for each continent.

22. Count how many countries belong to each democracy type.

---

## Level 8: Pivot Tables

23. Create a pivot table showing:

* Rows → Continent
* Values → Population
* Aggregation → Sum

24. Create a pivot table showing:

* Rows → Democracy Type
* Columns → Continent
* Values → GDP
* Aggregation → Mean

---

## Level 9: Advanced Analysis

25. Find the following:

* Country with the highest GDP
* Country with the highest population
* Country with the highest life expectancy
* Country with the highest internet usage
* Country with the highest democracy score

---

# Concepts Covered

* Reading CSV (`read_csv`)
* DataFrame exploration
* `head()`, `tail()`
* `shape`, `columns`, `dtypes`, `info()`
* `describe()`
* Column selection
* `loc` and `iloc`
* Filtering
* Sorting
* Missing data handling (`isnull()`, `fillna()`)
* Creating new columns
* Arithmetic operations
* GroupBy
* Aggregation (`sum`, `mean`, `max`, `min`, `count`)
* Pivot Tables
* Real-world data analysis
