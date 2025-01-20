x1=int(input("Enter value of x1 : "))
y1=int(input("Enter value of y1 : "))
x2=int(input("Enter value of x2 : "))
y2=int(input("Enter value of y2 : "))
x3=int(input("Enter value of x3 : "))
y3=int(input("Enter value of y3 : "))

if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("The points are collinear")
else:
    print("The points are not collinear")