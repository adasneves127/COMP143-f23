
def calculate_area(r):
    # print(f"Square with Side-length {r}: {r ** 2}")
    # print(f"Circle with radius {r}: {r ** 2 * 3.1415926}")
    if r < 0:
        raise ValueError(f"Value {r} cannot be negative!")

    return r**2
