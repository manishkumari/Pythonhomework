numbers = []
while True:
    user_input = input("Enter a number (leave blank to stop): ")

    if user_input == "":
        break
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Please enter a valid number.")

if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"\nSmallest number: {smallest}")
    print(f"Largest number: {largest}")


else:
    print("\nNo numbers were entered.")