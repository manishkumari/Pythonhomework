import random
secret_number = random.randint(1,10)

while True:
    your_guess=input("enter your guess:")
    if not your_guess.isdigit():
        print("please enter a valid number:")
        continue
        guess=int(your_guess)
        if guess < secret_number:
            print("too low! try again:")
        elif guess > secret_number:
            print("too high! try again:")
    else:
    print("correct! you guessed it")
    break
