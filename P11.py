# 1. Function to add two numbers
def add_numbers(a, b):
    return a + b

# 2. Function with default argument
def greet(name="Guest"):
    return f"Hello, {name}!"

# 3. Function that returns square of a number
def square(num):
    return num * num

# 4. Recursive factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 5. Function with variable arguments (*args)
def sum_all(*args):
    return sum(args)

# 6. Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 7. Function to check prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 8. Function to reverse string
def reverse_string(s):
    return s[::-1]

# 9. Function to find even/odd
def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

# 10. Nested function example
def outer_func(x):
    def inner_func(y):
        return y + 1
    return inner_func(x) * 2

# 11. Lambda function for cube
cube = lambda x: x**3

# 12. Function returning multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

# 13. Simple calculator using functions
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operation"

# 14. Function to count vowels in string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# 15. Recursive Fibonacci function
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibs = fibonacci(n-1)
        fibs.append(fibs[-1] + fibs[-2])
        return fibs


# Test examples to demonstrate usage
print("Add:", add_numbers(3, 5))
print(greet())
print(greet("Alice"))
print("Square:", square(4))
print("Factorial:", factorial(5))
print("Sum all:", sum_all(1, 2, 3, 4))
print_info(name="Bob", age=25)
print("Is 29 prime?", is_prime(29))
print("Reverse 'hello':", reverse_string("hello"))
print("7 is", even_or_odd(7))
print("Nested function result:", outer_func(5))
print("Cube of 3:", cube(3))
print("Min and Max:", min_max([3, 1, 8, 0]))
print("Calculator 10 / 2:", calculator(10, 2, "divide"))
print("Vowels in 'hello world':", count_vowels("hello world"))
print("Fibonacci first 7:", fibonacci(7))
