length = float(input("Enter len of rectangle : "))
breadth = float(input("Enter breadth of rectangle : "))
radius = float(input("Enter radius of circle : "))

rectangle_area = length * breadth
rectangle_perimeter = 2*(length+breadth)

circle_area = 3.14 * radius * radius
circle_circumference = 2 * 3.14 * radius

print("area of rectangle : ", round(rectangle_area, 2))
print("perimeter of rectangle : ", round(rectangle_perimeter, 2))
print("area of rectangle : ", round(circle_area, 2))
print("circumference of rectangle : ", round(circle_circumference, 2))