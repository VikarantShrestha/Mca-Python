l=float(input("Enter length of rectangle : "))
b=float(input("Enter breadth of rectangle : "))

if l*b > 2*(l+b):
    print("area is greater than perimeter")
else :
    print("area is not greater than perimeter")