# 4. Create a function to print the square of a number.

def print_square(number):
    square = number ** 2
    print(f"The square of {number} is {square}")

number = int(input("Enter a number: "))
print_square(number)