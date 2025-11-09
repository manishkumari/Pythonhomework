numbers = []
user_input = input("enter a number (blank to stop): ")
while user_input != "":
    numbers.append(float(user_input))
    user_input = input("enter a number (blank to stop): ")
    if numbers:
        print(f"smallest number: {min(numbers)}")
        print(f"largest number: {max(numbers)}")


    else:
        print("no numbers were entered.")