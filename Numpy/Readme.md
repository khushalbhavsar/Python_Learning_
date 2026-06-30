# NumPy Learning Notes

This README contains topic-wise notes for learning Jupyter Notebook and NumPy. It is organized from basic setup to common NumPy operations, with short examples and interview-ready summaries.

## Table of Contents

- [Jupyter Notebook](#jupyter-notebook)
- [Introduction to NumPy](#introduction-to-numpy)
- [NumPy Arrays](#numpy-arrays)
- [Creating NumPy Arrays](#creating-numpy-arrays)
- [Array Attributes and Methods](#array-attributes-and-methods)
- [Reshaping and Resizing](#reshaping-and-resizing)
- [Indexing and Slicing](#indexing-and-slicing)
- [Boolean Indexing](#boolean-indexing)
- [Array Operations](#array-operations)
- [Copying Arrays](#copying-arrays)
- [Array Manipulation](#array-manipulation)
- [Quick Interview Notes](#quick-interview-notes)

## Jupyter Notebook

A **Jupyter Notebook** is an interactive environment where you can write code, notes, equations, visualizations, and outputs in one document. It is commonly used for Python, data science, machine learning, and experimentation.

### Why Use a Notebook?

- Run code one cell at a time.
- See output immediately below the code.
- Add explanations using Markdown.
- Display graphs, tables, and images inline.
- Save the complete experiment in one `.ipynb` file.

### Notebook Cell Types

#### Code Cell

```python
x = 10
y = 20
print(x + y)
```

Output:

```text
30
```

#### Markdown Cell

```markdown
# Addition Example

This notebook demonstrates basic addition.
```

### Common Notebook Platforms

| Platform | Use |
| --- | --- |
| Jupyter Notebook | Classic local notebook environment |
| JupyterLab | Modern interface for notebooks, files, and terminals |
| Google Colab | Cloud notebook with free GPU access options |
| Visual Studio Code | Runs notebooks directly inside VS Code |
| Anaconda Navigator | GUI launcher for Jupyter tools |

### Useful Jupyter Shortcuts

| Shortcut | Action |
| --- | --- |
| `Shift + Enter` | Run current cell and move to next cell |
| `Ctrl + Enter` | Run current cell and stay there |
| `A` | Insert cell above |
| `B` | Insert cell below |
| `DD` | Delete current cell |
| `M` | Convert cell to Markdown |
| `Y` | Convert cell to Code |

### Install and Start Jupyter

```bash
pip install notebook
jupyter notebook
```

### Notebook vs Python Script

| Jupyter Notebook | Python Script (`.py`) |
| --- | --- |
| Interactive | Runs from start to finish |
| Executes one cell at a time | Executes the whole file |
| Best for learning and experiments | Best for reusable applications |
| Displays charts and outputs inline | Outputs appear in terminal or files |

Typical MLOps workflow:

```text
Notebook (.ipynb) -> Python script (.py) -> Git -> CI/CD -> Docker -> Kubernetes -> Deployment
```

## Introduction to NumPy

**NumPy** stands for **Numerical Python**. It is a Python library used for fast numerical computing. NumPy provides the `ndarray`, an efficient N-dimensional array object, plus many functions for mathematical, statistical, and scientific operations.

Install NumPy:

```bash
pip install numpy
```

Import NumPy:

```python
import numpy as np
```

### Why Use NumPy?

- Faster than normal Python lists for numerical work.
- Uses memory more efficiently.
- Supports vectorized operations.
- Provides functions for statistics, linear algebra, random numbers, and array manipulation.
- Forms the base of many data science libraries such as Pandas, SciPy, and scikit-learn.

### Simple Example

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)
```

Output:

```text
[ 2  4  6  8 10]
```

## NumPy Arrays

NumPy arrays are the main data structure in NumPy. They are usually **homogeneous**, meaning all elements share the same data type.

### Python List vs NumPy Array

| Feature | Python List | NumPy Array |
| --- | --- | --- |
| Data type | Can store mixed types | Usually stores one type |
| Speed | Slower for numerical operations | Faster for numerical operations |
| Memory usage | Less efficient | More efficient |
| Math operations | Usually needs loops | Supports vectorized operations |
| Dimensions | Basic nested lists | Built-in multi-dimensional arrays |

### Vectorization

Vectorization means applying operations to the whole array without writing explicit loops.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
```

Output:

```text
[5 7 9]
```

## Creating NumPy Arrays

### From Python Lists

```python
import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(arr_1d)
print(arr_2d)
print(arr_3d)
```

### Common Array Creation Functions

| Function | Purpose | Example |
| --- | --- | --- |
| `np.array()` | Create an array from a list or tuple | `np.array([1, 2, 3])` |
| `np.zeros()` | Create an array filled with zeros | `np.zeros((2, 3))` |
| `np.ones()` | Create an array filled with ones | `np.ones((2, 2))` |
| `np.arange()` | Create values with a step size | `np.arange(1, 10, 2)` |
| `np.linspace()` | Create evenly spaced values | `np.linspace(0, 1, 5)` |
| `np.eye()` | Create an identity matrix | `np.eye(3)` |
| `np.full()` | Create an array filled with one value | `np.full((2, 3), 7)` |

## Array Attributes and Methods

An **attribute** gives information about an array. A **method** performs an operation on an array.

### Important Attributes

| Attribute | Purpose | Example |
| --- | --- | --- |
| `shape` | Dimensions of the array | `arr.shape` |
| `ndim` | Number of dimensions | `arr.ndim` |
| `size` | Total number of elements | `arr.size` |
| `dtype` | Data type of elements | `arr.dtype` |
| `itemsize` | Size of each element in bytes | `arr.itemsize` |
| `nbytes` | Total memory used by the array | `arr.nbytes` |
| `T` | Transpose of the array | `arr.T` |

Example:

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
```

### Important Methods

| Method | Purpose | Example |
| --- | --- | --- |
| `reshape()` | Change array shape | `arr.reshape(3, 2)` |
| `flatten()` | Convert to a 1D copy | `arr.flatten()` |
| `ravel()` | Convert to a 1D view when possible | `arr.ravel()` |
| `transpose()` | Transpose array | `arr.transpose()` |
| `copy()` | Create an independent copy | `arr.copy()` |
| `sort()` | Sort the array in place | `arr.sort()` |
| `sum()` | Sum elements | `arr.sum()` |
| `mean()` | Average elements | `arr.mean()` |
| `max()` | Maximum value | `arr.max()` |
| `min()` | Minimum value | `arr.min()` |
| `argmax()` | Index of maximum value | `arr.argmax()` |
| `argmin()` | Index of minimum value | `arr.argmin()` |

### Attribute vs Method

| Feature | Attribute | Method |
| --- | --- | --- |
| Purpose | Gives information | Performs an action |
| Parentheses | No parentheses | Uses parentheses |
| Example | `arr.shape` | `arr.reshape(2, 3)` |

## Reshaping and Resizing

Reshaping changes how array data is arranged across dimensions.

| Function | Purpose | Changes element count? | Modifies original? |
| --- | --- | --- | --- |
| `reshape()` | Change shape | No | No |
| `resize()` | Change shape and size | Yes | Yes |
| `flatten()` | Convert to 1D copy | No | No |
| `ravel()` | Convert to 1D view when possible | No | Usually no |
| `transpose()` | Swap axes | No | No |
| `T` | Shortcut for transpose | No | No |

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

print(arr.reshape(2, 3))
print(arr.flatten())
```

Output:

```text
[[1 2 3]
 [4 5 6]]
[1 2 3 4 5 6]
```

Important rules:

- `reshape()` cannot change the total number of elements.
- `resize()` can add or remove elements.
- `flatten()` returns a copy.
- `ravel()` usually returns a view, so it can be more memory efficient.

## Indexing and Slicing

**Indexing** selects a single element. **Slicing** selects multiple elements.

### 1D Indexing

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])
```

Output:

```text
10
30
50
```

### 2D Indexing

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 0])
print(arr[1, 2])
```

Output:

```text
10
60
```

### 1D Slicing

Syntax:

```python
arr[start:stop:step]
```

Examples:

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[::2])
print(arr[::-1])
```

Output:

```text
[20 30 40]
[10 20 30]
[30 40 50]
[10 30 50]
[50 40 30 20 10]
```

### 2D Slicing

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[0, :])
print(arr[:, 0])
print(arr[:2, :2])
```

Output:

```text
[10 20 30]
[10 40 70]
[[10 20]
 [40 50]]
```

### Slicing Cheat Sheet

| Expression | Meaning |
| --- | --- |
| `arr[0]` | First element or first row |
| `arr[-1]` | Last element or last row |
| `arr[1:4]` | Elements from index 1 to 3 |
| `arr[:3]` | First three elements |
| `arr[2:]` | From index 2 to the end |
| `arr[::2]` | Every second element |
| `arr[::-1]` | Reverse the array |
| `arr[0, :]` | First row of a 2D array |
| `arr[:, 0]` | First column of a 2D array |

## Boolean Indexing

Boolean indexing filters array values using a condition.

Syntax:

```python
arr[condition]
```

### Examples

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[arr > 30])
print(arr[arr < 25])
print(arr[arr % 20 == 0])
```

Output:

```text
[40 50]
[10 20]
[20 40]
```

### Multiple Conditions

Use `&` for AND and `|` for OR. Put each condition in parentheses.

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[(arr > 20) & (arr < 50)])
print(arr[(arr < 20) | (arr > 40)])
```

Output:

```text
[30 40]
[10 50]
```

### Common Conditions

| Condition | Example |
| --- | --- |
| Greater than | `arr[arr > 20]` |
| Less than | `arr[arr < 20]` |
| Equal to | `arr[arr == 20]` |
| Not equal to | `arr[arr != 20]` |
| Greater than or equal | `arr[arr >= 20]` |
| Less than or equal | `arr[arr <= 20]` |

## Array Operations

NumPy performs mathematical operations element-wise by default.

### Arithmetic Operations

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
```

Output:

```text
[11 22 33]
[ 9 18 27]
[10 40 90]
[10. 10. 10.]
[100 400 900]
```

### Scalar Operations

```python
arr = np.array([1, 2, 3])

print(arr + 10)
print(arr * 5)
print(arr / 2)
```

Output:

```text
[11 12 13]
[ 5 10 15]
[0.5 1.  1.5]
```

### Comparison Operations

```python
arr = np.array([10, 20, 30])

print(arr > 20)
print(arr == 20)
print(arr != 20)
```

Output:

```text
[False False  True]
[False  True False]
[ True False  True]
```

### Aggregate Operations

```python
arr = np.array([10, 20, 30, 40])

print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())
print(arr.std())
print(arr.var())
```

### Universal Functions

| Function | Purpose | Example |
| --- | --- | --- |
| `np.sqrt()` | Square root | `np.sqrt(arr)` |
| `np.square()` | Square | `np.square(arr)` |
| `np.abs()` | Absolute value | `np.abs(arr)` |
| `np.exp()` | Exponential | `np.exp(arr)` |
| `np.log()` | Natural logarithm | `np.log(arr)` |

### Matrix Operations

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A + B)
print(A @ B)
print(A.T)
print(np.linalg.det(A))
```

### `*` vs `np.dot()` vs `@`

| Operation | Meaning | Example |
| --- | --- | --- |
| `*` | Element-wise multiplication | `a * b` |
| `np.dot()` | Dot product or matrix multiplication | `np.dot(a, b)` |
| `@` | Matrix multiplication operator | `A @ B` |

### Broadcasting

Broadcasting lets NumPy perform operations on arrays with compatible shapes.

```python
arr = np.array([1, 2, 3])
print(arr + 10)
```

Output:

```text
[11 12 13]
```

### Searching, Sorting, and Statistics

| Function | Purpose |
| --- | --- |
| `np.sort()` | Sort values |
| `np.argsort()` | Return sorted indexes |
| `np.where()` | Find values by condition |
| `np.unique()` | Return unique values |
| `np.nonzero()` | Return indexes of non-zero elements |
| `np.mean()` | Mean |
| `np.median()` | Median |
| `np.std()` | Standard deviation |
| `np.var()` | Variance |
| `np.percentile()` | Percentile |

### Random Functions

| Function | Purpose |
| --- | --- |
| `np.random.rand()` | Random decimal values from a uniform distribution |
| `np.random.randn()` | Random values from a normal distribution |
| `np.random.randint()` | Random integers |
| `np.random.choice()` | Select random elements |
| `np.random.shuffle()` | Shuffle an array in place |
| `np.random.seed()` | Make random output reproducible |

## Copying Arrays

NumPy has two common copy behaviors: **view** and **copy**.

### Shallow Copy: `view()`

A view shares memory with the original array. Changing one can affect the other.

```python
import numpy as np

arr = np.array([10, 20, 30, 40])
view_arr = arr.view()

view_arr[0] = 100

print(arr)
print(view_arr)
```

Output:

```text
[100  20  30  40]
[100  20  30  40]
```

### Deep Copy: `copy()`

A copy creates a new independent array. Changing the copy does not affect the original.

```python
arr = np.array([10, 20, 30, 40])
copy_arr = arr.copy()

copy_arr[0] = 100

print(arr)
print(copy_arr)
```

Output:

```text
[10 20 30 40]
[100  20  30  40]
```

### View vs Copy

| Feature | View: `arr.view()` | Copy: `arr.copy()` |
| --- | --- | --- |
| Memory | Shared | Separate |
| Changes affect original | Yes | No |
| Speed | Faster | Slower |
| Safety | Less safe for editing | Safer for editing |

Check shared memory:

```python
print(np.shares_memory(arr, view_arr))
print(np.shares_memory(arr, copy_arr))
```

## Array Manipulation

Array manipulation means changing the shape, structure, or arrangement of arrays.

### Common Manipulation Functions

| Function | Purpose | Example |
| --- | --- | --- |
| `reshape()` | Change shape | `arr.reshape(2, 3)` |
| `flatten()` | Convert to 1D copy | `arr.flatten()` |
| `ravel()` | Convert to 1D view when possible | `arr.ravel()` |
| `transpose()` | Swap rows and columns | `arr.transpose()` |
| `concatenate()` | Join arrays along an existing axis | `np.concatenate((a, b))` |
| `stack()` | Join arrays along a new axis | `np.stack((a, b))` |
| `vstack()` | Stack vertically | `np.vstack((a, b))` |
| `hstack()` | Stack horizontally | `np.hstack((a, b))` |
| `split()` | Split an array | `np.split(arr, 2)` |
| `append()` | Add values at the end | `np.append(arr, 6)` |
| `insert()` | Insert values at a position | `np.insert(arr, 2, 100)` |
| `delete()` | Delete values | `np.delete(arr, 1)` |

### Join Arrays

```python
import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])

print(np.concatenate((a, b)))
print(np.vstack((a, b)))
print(np.hstack((a, b)))
```

Output:

```text
[1 2 3 4]
[[1 2]
 [3 4]]
[1 2 3 4]
```

### Split, Append, Insert, and Delete

```python
arr = np.array([1, 2, 3, 4])

print(np.split(arr, 2))
print(np.append(arr, 5))
print(np.insert(arr, 2, 100))
print(np.delete(arr, 1))
```

Output:

```text
[array([1, 2]), array([3, 4])]
[1 2 3 4 5]
[  1   2 100   3   4]
[1 3 4]
```

## Quick Interview Notes

| Question | Short Answer |
| --- | --- |
| What is NumPy? | A Python library for fast numerical computing. |
| What is an `ndarray`? | NumPy's N-dimensional array object. |
| Why is NumPy faster than lists? | It uses optimized C code and vectorized operations. |
| What is vectorization? | Performing operations on entire arrays without explicit loops. |
| What is broadcasting? | Applying operations to arrays of compatible but different shapes. |
| What is the difference between indexing and slicing? | Indexing returns one element; slicing returns a subarray. |
| What is boolean indexing? | Filtering array values using conditions. |
| What is the difference between `reshape()` and `resize()`? | `reshape()` keeps element count; `resize()` can change it. |
| What is the difference between `flatten()` and `ravel()`? | `flatten()` returns a copy; `ravel()` usually returns a view. |
| What is the difference between `view()` and `copy()`? | `view()` shares memory; `copy()` creates independent memory. |
| What is the difference between `*` and `@`? | `*` is element-wise multiplication; `@` is matrix multiplication. |

## Official References

- [NumPy website](https://numpy.org/)
- [NumPy documentation](https://numpy.org/doc/)
- [Jupyter documentation](https://docs.jupyter.org/)
