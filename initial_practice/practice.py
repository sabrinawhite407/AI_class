# This script shows simple area calculations for different shapes.
# We will use variables to store the dimensions of each shape.
# Then we calculate the area using the correct formula for each one.

# Rectangle formula: area = length * width
rectangle_length = 10
rectangle_width = 5
rectangle_area = rectangle_length * rectangle_width

# Square formula: area = side * side
square_side = 4
square_area = square_side * square_side

# Triangle formula: area = 1/2 * base * height
triangle_base = 8
triangle_height = 6
triangle_area = 0.5 * triangle_base * triangle_height

# Circle formula: area = pi * radius * radius
# We use 3.14159 as an approximate value for pi.
pi = 3.14159
circle_radius = 3
circle_area = pi * circle_radius * circle_radius

# Print the answers for each shape.
print("Rectangle area:", rectangle_area)
print("Square area:", square_area)
print("Triangle area:", triangle_area)
print("Circle area:", circle_area)

# Extra beginner example: perimeter calculations
# Perimeter is the total distance around the outside of a shape.
rectangle_perimeter = 2 * (rectangle_length + rectangle_width)
square_perimeter = 4 * square_side
circle_circumference = 2 * pi * circle_radius

print("Rectangle perimeter:", rectangle_perimeter)
print("Square perimeter:", square_perimeter)
print("Circle circumference:", circle_circumference)