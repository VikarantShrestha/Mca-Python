a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("The triangle is equilateral")
    elif a == b or b == c or a == c:
        print("The triangle is isosceles")
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("The triangle is right-angled.")
    else:
        print("The triangle is scalene.")
else:
    print("The sides do not form a valid triangle.")
