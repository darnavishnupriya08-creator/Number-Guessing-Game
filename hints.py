def give_hint(guess, number):
    difference = abs(guess - number)

    if difference <= 5:
        return "Very close!"

    elif difference <= 15:
        return "You are close!"

    elif difference <= 30:
        return "You are a little far away."

    else:
        return "You are far away."


def give_direction(guess, number):
    if guess < number:
        return "Too low! Try a higher number."

    elif guess > number:
        return "Too high! Try a lower number."

    else:
        return "Correct! You guessed the number."


def show_hint(guess, number):
    print(give_direction(guess, number))

    if guess != number:
        print("Hint:", give_hint(guess, number))

