import math

cx=int(input("Enter value of x coordinate of center of circle: "))
cy=int(input("Enter value of y coordinate of center of circle: "))

r=float(input("Enter radius of circle : "))

x=int(input("Enter value of x coordinate of any point: "))
y=int(input("Enter value of x coordinate of any point: "))

distance = math.sqrt(math.pow((cx-x),2) + math.pow((cy-y),2))

if distance<r:
    print("The point lies inside the circle")
elif distance==r:
    print("The point lies on the circle")
else:
    print("The point lies outside the circle")