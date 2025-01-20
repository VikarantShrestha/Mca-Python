x = float(input("Enter the coordinates of the point x : "))
y = float(input("Enter the coordinates of the point y : "))

if x == 0 and y == 0:
    print("The point lies at the origin.")
elif y == 0 and x != 0:
    print("The point lies on the x-axis.")
elif x == 0 and y != 0:
    print("The point lies on the y-axis.")
else:
    print("The point not lies on the x-axis, y-axis, or at the origin.")
