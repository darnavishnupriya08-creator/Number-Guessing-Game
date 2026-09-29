def get_difficulty():
    while True:
        print()
        print("Choose Difficulty Level")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            return "easy"

        elif choice == "2":
            return "medium"

        elif choice == "3":
            return "hard"

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def get_guess(minimum, maximum):
    while True:
        try:
            guess = int(
                input(
                    f"Enter your guess ({minimum}-{maximum}): "
                )
            )

            if minimum <= guess <= maximum:
                return guess

            print(
                f"Please enter a number between "
                f"{minimum} and {maximum}."
            )

        except ValueError:
            print("Please enter a valid number.")


def play_again():
    while True:
        choice = input(
            "Do you want to play again? (y/n): "
        ).strip().lower()

        if choice == "y":
            return True

        elif choice == "n":
            return False

        else:
            print("Please enter y or n.")
