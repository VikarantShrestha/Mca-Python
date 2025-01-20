def power(a, b):
    return a ** b

a = float(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))
result = power(a, b)
print(f"The result of {a} raised to the power {b} is {result}")
