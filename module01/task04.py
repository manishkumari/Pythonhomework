length_str = input("Enter the length of the rectangle:")
length = float (length_str)
width_str = input("Enter the width of the width of the rectangle:")
width = float(width_str)
perimeter = 2* (length + width)
area = length * width
print(f"\nPerimeter of the rectangle:{perimeter:.2f}")
print(f"Area of the rectangle: {area:.2f}")