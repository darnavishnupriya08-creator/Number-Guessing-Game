def validate_difficulty(difficulty):
    if difficulty in ["easy", "medium", "hard"]:
        return True

    return False


def validate_guess(guess, minimum, maximum):
    if guess < minimum or guess > maximum:
        return False, f"Please enter a number between {minimum} and {maximum}."

    return True, "Valid guess."


def validate_number_input(value):
    try:
        int(value)
        return True
    except ValueError:
        return False  

