# What is Pandas?

**Pandas** is a powerful, open-source Python library used for **data manipulation, data analysis, and data cleaning**. It provides easy-to-use data structures and functions for working with structured data such as tables, spreadsheets, and CSV files.

It is one of the most widely used libraries in **Data Science, Machine Learning, Artificial Intelligence, and MLOps**.

---

# Why is it called Pandas?

The name **Pandas** comes from **"Panel Data"**, a term used in statistics and econometrics for multidimensional structured datasets.

---

# Why Use Pandas?

Pandas helps you to:

* Read data from CSV, Excel, JSON, SQL, etc.
* Clean missing or incorrect data.
* Filter and sort data.
* Perform statistical analysis.
* Merge and join datasets.
* Prepare data for Machine Learning models.

---

# Main Data Structures

Pandas has two primary data structures:

| Data Structure | Description                                             |
| -------------- | ------------------------------------------------------- |
| **Series**     | A one-dimensional labeled array (like a single column). |
| **DataFrame**  | A two-dimensional labeled table with rows and columns.  |

Example:

```text
Series

0    10
1    20
2    30
```

```text
DataFrame

   Name   Age
0  John    25
1  Alice   30
2  Bob     28
```

---

# Installing Pandas

```bash
pip install pandas
```

---

# Importing Pandas

```python
import pandas as pd
```

`pd` is the standard alias used for Pandas.

---

# Simple Example

```python
import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 28]
}

df = pd.DataFrame(data)

print(df)
```

### Output

```text
    Name   Age
0   John    25
1  Alice    30
2    Bob    28
```

---

# Features of Pandas

* ✅ Fast and efficient data manipulation
* ✅ Easy handling of missing values
* ✅ Powerful filtering and sorting
* ✅ Read and write multiple file formats
* ✅ Grouping and aggregation
* ✅ Merge and join datasets
* ✅ Time-series analysis
* ✅ Built on top of NumPy

---

# Applications of Pandas

* Data Cleaning
* Data Analysis
* Data Visualization (with Matplotlib/Seaborn)
* Machine Learning Data Preprocessing
* Financial Analysis
* Business Intelligence
* Data Engineering

---

# NumPy vs Pandas

| NumPy                             | Pandas                                              |
| --------------------------------- | --------------------------------------------------- |
| Works with arrays                 | Works with tables (DataFrames)                      |
| Faster for numerical computations | Better for data analysis                            |
| Homogeneous data (same data type) | Can store different data types in different columns |
| Mainly numerical operations       | Data manipulation and analysis                      |
| Foundation library                | Built on top of NumPy                               |

---

# Commonly Used Pandas Objects

| Object            | Purpose                     |
| ----------------- | --------------------------- |
| `pd.Series()`     | Create a Series             |
| `pd.DataFrame()`  | Create a DataFrame          |
| `pd.read_csv()`   | Read a CSV file             |
| `pd.read_excel()` | Read an Excel file          |
| `df.head()`       | View the first 5 rows       |
| `df.tail()`       | View the last 5 rows        |
| `df.info()`       | Display dataset information |
| `df.describe()`   | Display statistical summary |

---

# Interview Questions

| Question                                         | Answer                                                      |
| ------------------------------------------------ | ----------------------------------------------------------- |
| What is Pandas?                                  | A Python library for data manipulation and analysis.        |
| What are the two main data structures in Pandas? | Series and DataFrame.                                       |
| Is Pandas built on NumPy?                        | Yes.                                                        |
| Why is Pandas used?                              | To clean, analyze, manipulate, and prepare structured data. |
| What is the standard alias for Pandas?           | `pd`                                                        |

---

# Key Points to Remember

* **Pandas** is a Python library for **data manipulation and analysis**.
* It is built on top of **NumPy**.
* The two main data structures are **Series** and **DataFrame**.
* It is widely used in **Data Science**, **Machine Learning**, **Data Engineering**, and **MLOps**.
* The standard import statement is:

```python
import pandas as pd
```

* Pandas makes it easy to read, clean, transform, analyze, and export structured data.
