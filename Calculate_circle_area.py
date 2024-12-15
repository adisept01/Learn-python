import math

def calculate_circle_area(r):
  
    # Ensure the radius is non-negative
    if r < 0:
        return "Radius cannot be negative."
    
    # Calculate the area
    area = math.pi * r ** 2
    return area

# Example usage
radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area}")
