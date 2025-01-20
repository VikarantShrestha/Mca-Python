def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Enter n (total items): "))
r = int(input("Enter r (selected items): "))
result = combination(n, r)
print(f"The combination C({n}, {r}) is {result}.")
