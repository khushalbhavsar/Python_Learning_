# 10. Create a function that prints a star pattern.

def print_star_pattern(rows):
    for i in range(1, rows + 1):
        print('* ' * i)

num_rows = int(input("Enter the number of rows for the star pattern: "))
print_star_pattern(num_rows)
