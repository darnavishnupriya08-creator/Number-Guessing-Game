from game import generate_number, get_max_attempts, check_guess
from validator import validate_guess
from hints import show_hint
from user_input import get_difficulty, get_guess, play_again
from score import calculate_final_score
from utils import display_banner, display_rules, display_result, display_goodbye


def main():
    display_banner()
    display_rules()

    total_score = 0

    while True:
        difficulty = get_difficulty()

        number = generate_number(difficulty)
        max_attempts = get_max_attempts(difficulty)
        attempts_left = max_attempts

        if difficulty == "easy":
            minimum = 1
            maximum = 50
        elif difficulty == "medium":
            minimum = 1
            maximum = 100
        else:
            minimum = 1
            maximum = 200

        print()
        print("Game started!")
        print("Guess the number between", minimum, "and", maximum)
        print("Attempts:", max_attempts)

        while attempts_left > 0:
            guess = get_guess(minimum, maximum)

            valid, message = validate_guess(
                guess, minimum, maximum
            )

            if not valid:
                print(message)
                continue

            result = check_guess(guess, number)

            show_hint(guess, number)

            if result == "correct":
                score = calculate_final_score(
                    attempts_left,
                    max_attempts,
                    difficulty
                )

                total_score += score

                print()
                print("Congratulations!")
                print("You guessed the correct number.")
                print("The number was:", number)
                print("Score for this game:", score)
                break

            attempts_left -= 1
            print("Attempts remaining:", attempts_left)

        else:
            print()
            print("Game Over!")
            print("The correct number was:", number)

        print()
        print("Total Score:", total_score)

        if not play_again():
            break

    display_result(total_score)
    display_goodbye()


if __name__ == "__main__":
    main()
