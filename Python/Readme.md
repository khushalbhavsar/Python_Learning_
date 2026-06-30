# Complete Python Learning Guide

A topic-wise Python reference for beginners. It keeps the core concepts, removes repeated explanations, and uses compact examples for quick revision.

## Table of Contents

1. [Basics and Core Data Handling](#1-basics-and-core-data-handling)
2. [Operators and Expressions](#2-operators-and-expressions)
3. [Conditional Statements](#3-conditional-statements)
4. [Loops](#4-loops)
5. [Functions](#5-functions)
6. [Data Structures](#6-data-structures)
7. [Exception and File Handling](#7-exception-and-file-handling)

---

## 1. Basics and Core Data Handling

### What is Python?

Python is a high-level, interpreted programming language known for simple syntax and readability. It supports procedural, object-oriented, and functional programming styles.

```python
print("Hello, World!")
```

### Python Interpreter

The Python interpreter reads and executes code line by line. This makes it useful for quick testing, debugging, and interactive programming.

```python
>>> print("Hello, Python!")
```

### Comments

Comments explain code and are ignored during execution.

```python
# Single-line comment
print("Hello")  # Inline comment
```

### Variables

A variable stores a value in memory.

```python
age = 25
name = "Alice"
print(name, age)
```

### Variable Naming Rules

- Start with a letter or underscore.
- Use letters, digits, and underscores only.
- Names are case-sensitive.
- Do not use Python keywords such as `if`, `for`, or `while`.
- Prefer descriptive `snake_case` names.

```python
user_name = "Alice"
user_age = 30
```

### Built-in Data Types

| Type | Meaning | Example |
| --- | --- | --- |
| `int` | Whole number | `10` |
| `float` | Decimal number | `3.14` |
| `str` | Text | `"Python"` |
| `bool` | Boolean value | `True` |
| `complex` | Complex number | `2 + 3j` |

```python
integer_var = 10
float_var = 3.14
string_var = "Hello"
boolean_var = True
complex_var = 2 + 3j
```

### Type Conversion

Type conversion changes a value from one type to another.

```python
num_str = "123"
num_int = int(num_str)
num_float = float(num_int)

print(type(num_str))    # <class 'str'>
print(type(num_int))    # <class 'int'>
print(type(num_float))  # <class 'float'>
```

Common conversion functions:

- `int()`
- `float()`
- `str()`
- `bool()`

```python
print(bool(1))       # True
print(bool(0))       # False
print(bool("Hi"))    # True
print(bool(""))      # False
```

### Implicit and Explicit Conversion

```python
# Implicit conversion
result = 5 + 2.5
print(result)        # 7.5
print(type(result))  # <class 'float'>

# Explicit conversion
number = int("10")
print(number)
```

### Strings

A string is a sequence of characters enclosed in quotes.

```python
message = "Hello, Python!"
print(message[0])      # H
print(message[-1])     # !
print(message[7:13])   # Python
print(message[::-1])   # Reverse string
```

Useful string methods:

```python
text = "  Hello, World!  "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("World", "Python"))
```

### String Formatting

```python
name = "Alice"
age = 30

print("My name is " + name)
print(f"My name is {name} and I am {age} years old.")
```

### Input and Output

`input()` reads user input as a string. `print()` displays output.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you are {age} years old.")
```

---

## 2. Operators and Expressions

Operators perform operations on values. Expressions combine values, variables, and operators to produce a result.

### Arithmetic Operators

| Operator | Meaning |
| --- | --- |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulus |
| `**` | Exponent |
| `//` | Floor division |

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
```

### Comparison Operators

```python
x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
```

### Logical Operators

```python
age = 20
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
```

### Assignment Operators

```python
count = 5
count += 3
count *= 2
print(count)
```

### Bitwise Operators

```python
m = 6  # 110
n = 3  # 011

print(m & n)
print(m | n)
print(m ^ n)
print(~m)
print(m << 1)
print(m >> 1)
```

### Operator Precedence

Python follows operator precedence when evaluating expressions.

```python
result = 10 + 5 * 2
print(result)  # 20
```

Use parentheses to make expressions clear.

```python
result = (10 + 5) * 2
print(result)  # 30
```

---

## 3. Conditional Statements

Conditional statements run different code based on conditions.

### If, Elif, and Else

```python
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
```

### Nested If

```python
money = int(input("Enter amount: "))

if money >= 100:
    if money >= 500:
        print("You can buy a laptop.")
    else:
        print("You can buy a smartphone.")
else:
    print("You can buy a snack.")
```

### Conditional Practice Questions

1. Print the greatest of two numbers.
2. Print a greeting based on gender input.
3. Check whether a number is even or odd.
4. Check whether a person is eligible to vote.
5. Check whether a year is a leap year.
6. Classify temperature as freezing, cold, pleasant, hot, or very hot.

Example:

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Note: Indentation is required in Python because it defines code blocks.

---

## 4. Loops

Loops repeat a block of code.

- `for` loop: Used when iterating over a sequence.
- `while` loop: Used while a condition remains true.

### Range Function

```python
print(list(range(5)))        # [0, 1, 2, 3, 4]
print(list(range(1, 6)))     # [1, 2, 3, 4, 5]
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]
```

### For Loop

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### While Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Nested Loops

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")
```

### Break and Continue

```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```

### Loop Else

The `else` block runs when a loop finishes normally without `break`.

```python
for i in range(1, 4):
    print(i)
else:
    print("Loop completed.")
```

### Loop Practice Questions

1. Print `"Hello, World!"` `n` times.
2. Print natural numbers from `1` to `n`.
3. Print numbers from `n` to `1`.
4. Print a multiplication table.
5. Find the sum of first `n` natural numbers.
6. Find the factorial of a number.
7. Print all factors of a number.
8. Find the sum of even and odd numbers up to `n`.
9. Check whether a number is perfect.
10. Check whether a number is prime.
11. Reverse a string.
12. Check whether a string is a palindrome.
13. Count letters, digits, and symbols in a string.
14. Separate each digit of a number.
15. Reverse a number.
16. Check whether a number is a palindrome.
17. Build a number guessing game.

Example:

```python
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"Sum: {total}")
```

---

## 5. Functions

A function is a reusable block of code that performs a specific task.

### Defining and Calling a Function

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

### Parameters and Arguments

- Parameters are names in the function definition.
- Arguments are values passed during a function call.

```python
def add(a, b):
    return a + b

print(add(5, 3))
```

### Types of Arguments

```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))              # Default argument
print(power(2, 3))           # Positional arguments
print(power(exponent=3, base=2))  # Keyword arguments
```

### Return vs Print

- `return` sends a value back to the caller.
- `print()` displays a value on the screen.

```python
def square(number):
    return number * number

result = square(4)
print(result)
```

### Function Practice Example

```python
def is_palindrome(text):
    return text == text[::-1]

word = "radar"

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not palindrome")
```

Key points:

- Use `def` to create functions.
- Use parameters for input.
- Use `return` when the result is needed later.
- Functions reduce repetition and improve readability.

---

## 6. Data Structures

Data structures organize and store data. Common Python data structures are lists, tuples, sets, and dictionaries.

### Lists

A list is an ordered, mutable collection that allows duplicate values.

```python
numbers = [10, 20, 30]
numbers.append(40)
numbers[0] = 5

print(numbers)
```

Common list operations:

```python
numbers = [3, 1, 4, 2]

numbers.append(5)
numbers.remove(1)
numbers.sort()
numbers.reverse()

print(len(numbers))
print(numbers)
```

### Tuples

A tuple is an ordered, immutable collection.

```python
point = (10, 20)
x, y = point

print(x, y)
```

Tuple methods:

```python
values = (1, 2, 2, 3)

print(values.count(2))
print(values.index(3))
```

### Sets

A set is an unordered collection of unique values.

```python
numbers = {1, 2, 2, 3}
numbers.add(4)

print(numbers)  # {1, 2, 3, 4}
```

Set operations:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
```

### Dictionaries

A dictionary stores key-value pairs.

```python
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

print(student["name"])
print(student.get("age"))
```

Common dictionary operations:

```python
student["age"] = 21
student.update({"city": "Delhi"})

for key, value in student.items():
    print(key, value)

student.pop("city")
print(student.keys())
print(student.values())
```

### Shallow Copy and Deep Copy

Use deep copy when nested data must be fully independent.

```python
import copy

original = [1, 2, [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[2][0] = 99

print(original)  # [1, 2, [99, 4]]
print(shallow)   # [1, 2, [99, 4]]
print(deep)      # [1, 2, [3, 4]]
```

### Data Structure Summary

| Structure | Ordered | Mutable | Allows Duplicates | Syntax |
| --- | --- | --- | --- | --- |
| List | Yes | Yes | Yes | `[]` |
| Tuple | Yes | No | Yes | `()` |
| Set | No | Yes | No | `{}` |
| Dictionary | Yes | Yes | Keys are unique | `{key: value}` |

### Data Structure Practice Questions

1. Print positive and negative numbers from a list.
2. Find the mean of list elements.
3. Find the greatest element and its index.
4. Find the second greatest element.
5. Check whether a list is sorted.
6. Merge two dictionaries.
7. Sum all dictionary values.
8. Count frequency of elements.
9. Combine two dictionaries by adding common values.

---

## 7. Exception and File Handling

### Errors and Exceptions

Errors interrupt program execution. Exception handling lets you respond to runtime errors gracefully.

Common error types:

- Syntax error: Invalid Python syntax.
- Runtime error: Error during execution.
- Logical error: Program runs but gives wrong output.

Common exception keywords:

- `try`: Code that might fail.
- `except`: Handles an exception.
- `else`: Runs if no exception occurs.
- `finally`: Always runs.
- `raise`: Manually raises an exception.

### Exception Handling Example

```python
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter numbers only.")
else:
    print(f"Result: {result}")
finally:
    print("Program finished.")
```

### File Handling

File handling means creating, reading, writing, and closing files.

Common file modes:

| Mode | Meaning |
| --- | --- |
| `r` | Read |
| `w` | Write and overwrite |
| `a` | Append |
| `b` | Binary mode |

Use `with` because it closes the file automatically.

```python
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Exception Handling with Files

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("File operation failed.")
else:
    print(content)
finally:
    print("File handling completed.")
```

Key points:

- Use `try-except` for risky code.
- Catch specific exceptions where possible.
- Use `with open(...)` for file operations.
- Use `finally` for cleanup tasks.

---

## End of Guide

Use this README as a quick revision guide and practice checklist for Python basics.
