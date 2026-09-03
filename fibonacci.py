def fibonacci_series(n_terms):
    if n_terms <= 0:
        print("Please enter a positive integer.")
        return
    elif n_terms == 1:
        print("Fibonacci Series:")
        print(0)
        return

    first = 0
    second = 1
    print("Fibonacci Series:")
    for i in range(n_terms):
        if i == 0:
            print(first)
        elif i == 1:
            print(second)
        else:
            next_term = first + second
            print(next_term)
            first = second
            second = next_term

# Get input from the user
num_terms_str = input("Enter the number of terms: ")

try:
    num_terms = int(num_terms_str)
    fibonacci_series(num_terms)
except ValueError:
    print("Invalid input. Please enter an integer.")