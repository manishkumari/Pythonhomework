import random


def roll_dice():
    # Ask the user how many dice to roll
    try:
        num_dice = int(input("How many dice would you like to roll? "))
        if num_dice <= 0:
            print("Please enter a positive number.")
            return

        # Initialize the sum of dice rolls
        total_sum = 0

        # Roll the dice and calculate the sum
        for _ in range(num_dice):
            roll = random.randint(1, 6)  # Each die roll is a random number between 1 and 6
            total_sum += roll

        # Print the result
        print(f"The total sum of rolling {num_dice} dice is: {total_sum}")

    except ValueError:
        print("Please enter a valid integer.")


# Run the dice rolling program
roll_dice()