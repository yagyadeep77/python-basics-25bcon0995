def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

num_str = input("Enter a number: ")

try:
    num = int(num_str)
    result = factorial(num)
    print(f"Factorial of {num} = {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")