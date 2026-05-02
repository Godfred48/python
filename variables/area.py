import math
#area for square
print()
square_length = int(input("Enter the length of the square: "))
square_area = square_length * square_length
print(f"The area of the square is {square_area:.1f}")

#area of a rectangle 
print()
print("=" * 50)
rectangle_length = int(input("Enter the length of the rectangle: "))
rectangle_width =  int(input("Enter the width of the rectangle: "))
rectangle_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is {rectangle_area:.1f}")

#area of a circle 
print()
print("=" * 50)
circle_radius = float(input("Enter circle radius: "))
circle_area = math.pi * circle_radius
print(f"The area of the circle is {circle_area:.2f}")