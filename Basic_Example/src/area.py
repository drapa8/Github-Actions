def calculate_area_square(length: int | float) -> int | float:
    # Function to calculate the area of a square
    if not isinstance(length, (int, float)) or length <= 0:
        raise TypeError("Length must be a positive non-zero number")
    return length * length