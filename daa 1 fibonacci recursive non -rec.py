import timeit

# Non-recursive Fibonacci function
def fibonacci(n):
    """Non recursive fibonacci function"""
    # Calculate the Fibonacci sequence iteratively
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    return fib_list[n]

# Recursive Fibonacci function
def fibonacci_recursive(n):
    """Recursive fibonacci function"""
    # Calculate the Fibonacci sequence recursively
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Store results to prevent redundant calculations
    fib_recur_list[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return fib_recur_list[n]

# Taking input from the user
N = int(input("Enter the value of N for Fibonacci sequence: "))
RUNS = 1000  # Number of runs for timeit

print(f"Given N = {N}\n{RUNS} runs")

# Initializing lists for non-recursive and recursive methods
fib_list = [0] * (N + 1)
fib_list[0] = 0
fib_list[1] = 1

# Calculate and measure time for non-recursive Fibonacci
print(
    "Fibonacci non-recursive:",
    fibonacci(N),
    "\tTime:",
    f'{timeit.timeit("fibonacci(N)", setup=f"from __main__ import fibonacci;N={N}", number=RUNS):5f}',
    "O(n)\tSpace: O(1)",
)

# Initializing list for the recursive method
fib_recur_list = [0] * (N + 1)
fib_recur_list[0] = 0
fib_recur_list[1] = 1

# Calculate and measure time for recursive Fibonacci
print(
    "Fibonacci recursive:\t",
    fibonacci_recursive(N),
    "\tTime:",
    f'{timeit.timeit("fibonacci_recursive(N)", setup=f"from __main__ import fibonacci_recursive;N={N}", number=RUNS):5f}',
    "O(2^n)\tSpace: O(n)",
)

"""
Theory:

Working & Methodology:
Non-Recursive Approach:
Explanation:
Iteratively computes the Fibonacci sequence, avoiding redundant calculations by storing values in a list.
Key Point:
Utilizes a loop to calculate each Fibonacci number once and stores it for future reference.
Recursive Approach:
Explanation:
Solves the Fibonacci sequence using recursive calls and identifies subproblems.
Discusses the need to store results to prevent re-computation of overlapping subproblems.
Key Point:
Involves recursive function calls, leading to overlapping subproblems and redundant calculations.
Time Measurement:
Explanation:
Employs the timeit module to measure the execution time for both methods.
Emphasizes the importance of multiple runs (RUNS) for accurate time measurements.
Key Point:
Uses a standardized module to benchmark and measure execution times.
Conclusion & Results:
Time Complexity:
Non-Recursive Method:
Time Complexity: O(n)
Explanation: Linear time due to a single loop iterating through the range, storing results for future reference.
Recursive Method:
Time Complexity: O(2^n)
Explanation: Exponential time due to repetitive function calls, causing redundant calculations and an exponential increase in calls.
Space Complexity:
Non-Recursive Method:
Space Complexity: O(1)
Explanation: Constant space as values are updated in a fixed-size list/variables without additional storage.
Recursive Method:
Space Complexity: O(n)
Explanation: Linear space due to recursive function call stack growth, proportional to the input size n.

"""