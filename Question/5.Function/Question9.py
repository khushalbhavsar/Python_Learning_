# 9. Create a function that prints the multiplication table of 5.

def print_multiplication_table_of_5():
    print("Multiplication Table of 5:")
    for i in range(1, 11):
        result = 5 * i
        print(f"5 x {i} = {result}")

print_multiplication_table_of_5()