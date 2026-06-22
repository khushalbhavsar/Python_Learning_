# 8. Create a function that prints the first 10 even numbers.

def print_even_numbers():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)
            
print_even_numbers()