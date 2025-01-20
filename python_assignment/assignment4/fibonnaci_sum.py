def fibonacci_sum(n):
    a, b = 0, 1
    total_sum = 0
    
    for _ in range(n):
        total_sum += a
        a, b = b, a + b
    
    return total_sum

n = int(input("Enter the number of terms in the Fibonacci series: "))
result = fibonacci_sum(n)
print(f"The sum of the first {n} terms of the Fibonacci series is {result}.")
