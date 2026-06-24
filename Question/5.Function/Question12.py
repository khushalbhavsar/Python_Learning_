# 2. Create a function to subtract two numbers.

def sub_numbers(a, b):
    return a - b

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))   
result = sub_numbers(a, b)
print(f"The difference between {a} and {b} is: {result}")