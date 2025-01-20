a = float(input("Enter the first side of triangle: "))
b = float(input("Enter the second side of triangle: "))
c = float(input("Enter the third side of triangle: "))

if a + b > c and a + c > b and b + c > a:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
