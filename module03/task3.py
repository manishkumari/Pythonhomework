def is_prime(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False

    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def check_prime():
    try:
        # Ask the user for an integer
        user_input = int(input("Enter an integer: "))

        # Check if the number is prime
        if is_prime(user_input):
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")


# Run the prime number checker
check_prime()