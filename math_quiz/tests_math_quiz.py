import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_with_operator


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        for _ in range(1000):
            self.assertIn(generate_random_operator(), ['+', '-', '*'])

    def test_calculate_with_operator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (-4, 2, '+', '-4 + 2', -2),
                (5, -2, '*', '5 * -2', -10),
                (5, 7, '-', '5 - 7', -2),
                (3, 3, '*', '3 * 3', 9),
                (-3, -3, '*', '-3 * -3', 9),
                (8, 4, '-', '8 - 4', 4),
                (2, 6, '+', '2 + 6', 8),
                (-10, -5, '+', '-10 + -5', -15),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem_statement, calc_answer = calculate_with_operator(num1, num2, operator)
                self.assertEqual((problem_statement, calc_answer), (expected_problem, expected_answer))

if __name__ == "__main__":
    unittest.main()
