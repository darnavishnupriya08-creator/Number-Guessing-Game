import random

print("======================================")
print("        NUMBER GUESSING GAME")
print("======================================")

print()
print("Choose Difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    minimum = 1
    maximum = 50
    attempts = 10
    difficulty = "Easy"

elif choice == "2":
    minimum = 1
    maximum = 100
    attempts = 7
    difficulty = "Medium"

elif choice == "3":
    minimum = 1
    maximum = 200
    attempts = 5
    difficulty = "Hard"

else:
    print("Invalid choice.")
    exit()

number = random.randint(minimum, maximum)

print()
print("Difficulty:", difficulty)
print("Guess a number between", minimum, "and", maximum)
print("You have", attempts, "attempts.")
print()

score = 0

while attempts > 0:

    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < minimum or guess > maximum:
        print("Please enter a number within the given range.")
        continue

    if guess == number:
        score = attempts * 10

        if difficulty == "Hard":
            score += 20
        elif difficulty == "Medium":
            score += 10
        else:
            score += 5

        print()
        print("Congratulations!")
        print("You guessed the correct number.")
        print("The correct number was:", number)
        print("Your score:", score)
        break

    elif guess < number:
        print("Too low! Try a higher number.")

    else:
        print("Too high! Try a lower number.")

    difference = abs(guess - number)

    if difference <= 5:
        print("Hint: You are very close!")
    elif difference <= 15:
        print("Hint: You are close!")
    else:
        print("Hint: You are far away.")

    attempts -= 1
    print("Attempts remaining:", attempts)
    print()

else:
    print()
    print("Game Over!")
    print("The correct number was:", number)
    print("Your score: 0")

print()
print("======================================")
print("             GAME FINISHED")
print("======================================")
