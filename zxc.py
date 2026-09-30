import math


def calculate_ellipse_area(a, b):
    """
    Calculates the area of an ellipse given its semi-axes.
    a: semi-major axis
    b: semi-minor axis
    """
    # Check to ensure values are not negative
    if a < 0 or b < 0:
        return "Error: axis length cannot be negative."

    area = math.pi * a * b

    # Return the result rounded to two decimal places
    return round(area, 2)


# --- Example usage ---
major_axis = 5
minor_axis = 3

result = calculate_ellipse_area(major_axis, minor_axis)
print(f"The area of the ellipse is: {result}")