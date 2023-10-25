#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Oct. 24, 2023
# This is program will allow you guess the random number and tell if you were correct or not.


from random import randint


def main():
    user_guess = str(input("Enter your Number (0,9):\n"))
    num = randint(0, 9)

    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Your number isn't valid")
    else:
        if user_guess == num:
            print(f"You were correct! it was {num}")
        else:
            print(f"You were wrong it was {num}")
    finally:
        print("End")


if __name__ == "__main__":
    main()
