import random


def generate_number():
    return random.randint(1, 100)


def check_guess(guess, number):
    if guess < number:
        return "low"
    elif guess > number:
        return "high"
    else:
        return "correct"
