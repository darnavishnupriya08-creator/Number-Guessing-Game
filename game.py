import random


def generate_number(difficulty):
    if difficulty == "easy":
        return random.randint(1, 50)

    elif difficulty == "medium":
        return random.randint(1, 100)

    elif difficulty == "hard":
        return random.randint(1, 200)


def get_max_attempts(difficulty):
    if difficulty == "easy":
        return 10

    elif difficulty == "medium":
        return 7

    elif difficulty == "hard":
        return 5


def check_guess(guess, number):
    if guess < number:
        return "low"

    elif guess > number:
        return "high"

    else:
        return "correct"


def play_game(difficulty):
    number = generate_number(difficulty)
    max_attempts = get_max_attempts(difficulty)
    attempts_left = max_attempts

    print()
    print("================================")
    print("        GAME STARTED")
    print("================================")

    if difficulty == "easy":
        print("Guess a number between 1 and 50.")

    elif difficulty == "medium":
        print("Guess a number between 1 and 100.")

    else:
        print("Guess a number between 1 and 200.")

    print("You have", max_attempts, "attempts.")
    print()

    while attempts_left > 0:

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        result = check_guess(guess, number)

        if result == "correct":
            print()
            print("Congratulations!")
            print("You guessed the correct number.")
            print("The number was:", number)

            score = attempts_left * 10
            print("Your score:", score)

            return score

        elif result == "low":
            print("Too low! Try again.")

        else:
            print("Too high! Try again.")

        attempts_left -= 1
        print("Attempts remaining:", attempts_left)
        print()
        

    print("Game Over!")
    print("The correct number was:", number)

    return 0
