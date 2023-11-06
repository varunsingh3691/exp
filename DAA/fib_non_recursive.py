def fibonacci_non_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_series = [0, 1]
    for i in range(2, n):
        next_num = fibonacci_series[i-1] + fibonacci_series[i-2]
        fibonacci_series.append(next_num)

    return fibonacci_series

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_series = fibonacci_non_recursive(n)
print("Fibonacci Series (Non-Recursive):", fib_series)
