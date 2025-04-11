import numpy as np

def calculate_area(radius):
    area = np.pi * radius ** 2
    return area

radius = 5
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
