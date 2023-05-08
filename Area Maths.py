import math
print("AREA OF A SQUARE")
print("****************")
side =float(input("Enter the side value:"))
area_square = side ** 2
print("Area of a square =%.3f" %area_square)
print("AREA OF A RECTANGLE")
print("*******************")
length =float(input("Enter the length value:"))
breadth = float(input("Enter the breadth value:"))
area_rectangle = length * breadth
print("Area of a rectangle =%.3f" %area_rectangle)
print("AREA OF A TRIANGLE")
print("*******************")
base =float(input("Enter the base value:"))
height= float(input("Enter the height value:"))
area_triangle = (base * height)/2
print("Area of a triangle =%.2f" %area_triangle)
print("AREA OF A CIRCLE")
print("*******************")
radius =float(input("Enter the radius value:"))
area_circle = math.pi * radius * radius
print("Area of a circle = %.2f" %area_circle) 