# 5. Create a function to print the cube of a number.

def print_cube(number):
    cube = number ** 3
    print(f"The cube of {number} is {cube}")

number = int(input("Enter a number: "))
print_cube(number)
