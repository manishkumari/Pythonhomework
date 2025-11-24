def find_min_max():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to quit): ")

        if user_input == "":
            break

        try:
            number = float(user_input)  # Convert input to float to handle decimals as well
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")

    if numbers:
        print(f"The smallest number is: {min(numbers)}")
        print(f"The largest number is: {max(numbers)}")
    else:
        print("No numbers were entered.")

# Run the program
find_min_max()