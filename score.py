def calculate_score(attempts_left, max_attempts):
    if attempts_left <= 0:
        return 0

    score = attempts_left * 10

    return score


def calculate_bonus(difficulty):
    if difficulty == "easy":
        return 5

    elif difficulty == "medium":
        return 10

    elif difficulty == "hard":
        return 20

    return 0


def calculate_final_score(attempts_left, max_attempts, difficulty):
    score = calculate_score(attempts_left, max_attempts)
    bonus = calculate_bonus(difficulty)

    return score + bonus
    
