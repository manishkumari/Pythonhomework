2.2# Size limit for a zander in centimeters
size_limit = 42

# Ask the fisher for the length of the zander
zander_length = float(input("Enter the length of the zander in centimeters: "))

# Check if the zander meets the size limit
if zander_length >= size_limit:
    print("The zander meets the size limit, you can keep it.")
else:
    difference = size_limit - zander_length
    print(f"The zander is {difference:.1f} centimeters below the size limit. Please release it back into the lake.")