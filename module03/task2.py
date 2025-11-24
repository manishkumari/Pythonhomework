def find_top_five():
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
        # Sort the numbers in descending order and pick the top 5
        numbers.sort(reverse=True)
        top_five = numbers[:5]  # Get the first 5 numbers from the sorted list

        print(f"The five greatest numbers are: {top_five}")
    else:
        print("No numbers were entered.")

# Run the program
find_top_five()