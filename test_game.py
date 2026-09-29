import unittest

from game import generate_number, get_max_attempts, check_guess
from validator import validate_difficulty, validate_guess
from score import calculate_score, calculate_bonus


class TestNumberGuessingGame(unittest.TestCase):

    def test_generated_number(self):
        number = generate_number("medium")
        self.assertTrue(1 <= number <= 100)

    def test_easy_attempts(self):
        self.assertEqual(get_max_attempts("easy"), 10)

    def test_medium_attempts(self):
        self.assertEqual(get_max_attempts("medium"), 7)

    def test_hard_attempts(self):
        self.assertEqual(get_max_attempts("hard"), 5)

    def test_correct_guess(self):
        self.assertEqual(check_guess(50, 50), "correct")

    def test_low_guess(self):
        self.assertEqual(check_guess(30, 50), "low")

    def test_high_guess(self):
        self.assertEqual(check_guess(70, 50), "high")

    def test_valid_difficulty(self):
        self.assertTrue(validate_difficulty("easy"))
        self.assertTrue(validate_difficulty("medium"))
        self.assertTrue(validate_difficulty("hard"))

    def test_invalid_difficulty(self):
        self.assertFalse(validate_difficulty("very hard"))

    def test_valid_guess(self):
        valid, message = validate_guess(50, 1, 100)
        self.assertTrue(valid)

    def test_invalid_guess(self):
        valid, message = validate_guess(150, 1, 100)
        self.assertFalse(valid)

    def test_score(self):
        self.assertEqual(calculate_score(5, 7), 50)

    def test_bonus(self):
        self.assertEqual(calculate_bonus("hard"), 20)


if __name__ == "__main__":
    unittest.main()
