# Conversion factor
inches_to_cm = 2.54

while True:
    try:
        inches = float(input("Enter the length in inches (negative value to quit): "))

        # Check if the input is a negative value
        if inches < 0:
            print("Negative value detected. Program ending.")
            break

        # Convert inches to centimeters
        centimeters = inches * inches_to_cm

        # Print the result
        print(f"{inches} inches is equal to {centimeters:.2f} centimeters.")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")