# Number Guessing Game

## Description

The Number Guessing Game is a Python-based interactive game in which the computer generates a random number and the player tries to guess it.

The game provides different difficulty levels, hints, limited attempts, and a scoring system. The project is divided into multiple Python modules to make the program organized and easy to understand.

## Features

- Generate a random number
- Three difficulty levels: Easy, Medium, and Hard
- Different number ranges for each difficulty
- Limited attempts
- "Too high" and "Too low" hints
- Additional hints based on the distance from the correct number
- Input validation
- Score calculation
- Difficulty-based bonus score
- Play again option
- Total score tracking
- Game over message
- Separate testing module

## Difficulty Levels

### Easy
- Number range: 1 to 50
- Attempts: 10

### Medium
- Number range: 1 to 100
- Attempts: 7

### Hard
- Number range: 1 to 200
- Attempts: 5

## Technologies Used

- Python 3
- Random module
- Unittest module
- Python standard library

## Project Structure

```text
number-guessing-game/
├── main.py
├── game.py
├── validator.py
├── hints.py
├── user_input.py
├── score.py
├── utils.py
├── test_game.py
├── requirements.txt
└── README.md

