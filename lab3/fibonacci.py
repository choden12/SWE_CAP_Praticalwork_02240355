#import
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# this is to test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")


import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")



def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Test the generator
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")



def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")


# Exercise Answers
print("\nExercise Answers:")

# Exercise 1: Generate a Fibonacci Sequence up to n and Return as a List
print('\nExercise 1:')
def fibonacci_list(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n + 1):
        fib_sequence.append(a)
        a, b = b, a + b  
    return fib_sequence

# Print the Fibonacci sequence up to the 10th term
print("Fibonacci sequence up to n (list):", fibonacci_list(10))

# Exercise 2: Find the Index of the First Fibonacci Number Exceeding a Given Value
print('\nExercise 2:')
def first_fib_above(value):
    a, b = 0, 1
    index = 0
    while a <= value:
        a, b = b, a + b  
        index += 1  
    return index

value = 100
# Display the index of the first Fibonacci number that exceeds 100
print(f"Index of the first Fibonacci number exceeding 100: {first_fib_above(value)}")

# Exercise 3: Check if a Given Number is a Fibonacci Number
print('\nExercise 3:')
def is_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b  
    return a == num

num = 21
# Display whether the number 21 is a Fibonacci number
print(f"Is {num} a Fibonacci number? {'Yes' if is_fibonacci(num) else 'No'}")

# Exercise 4: Calculate the Ratios of Consecutive Fibonacci Numbers
print('\nExercise 4:')
def fibonacci_ratio(n):
    ratios = []
    a, b = 1, 1  
    for _ in range(2, n + 1):
        ratios.append(b / a)  # Append the ratio of the current term to the previous term
        a, b = b, a + b  # Move to the next Fibonacci numbers
    return ratios

# Display the ratios of consecutive Fibonacci numbers up to the 10th term
print("Ratios of consecutive Fibonacci numbers:", fibonacci_ratio(10))
