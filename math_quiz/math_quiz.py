import random


def generate_random_integer(min_value: int, max_value: int) -> int:
    """
    Generate a random integer within the specified range.

    Args:
        min_value (int): Minimum value for the random integer.
        max_value (int): Maximum value for the random integer.

    Returns:
        int: Random integer in range [min_value, max_value], including both end points.

    Example:
        >>> result = generate_random_integer(1, 10)
        >>> isinstance(result, int)
        True
        >>> 1 <= result <= 10
        True
    """
    return random.randint(min_value, max_value)


def generate_random_operator() -> str:
    """
    Generate a random operator for the math problem.

    Returns:
        str: A string representing a math operator ('+', '-', '*').
    """
    return random.choice(['+', '-', '*'])


def calculate_with_operator(num1: int, num2: int, operator: str) -> tuple[str, int]:
    """
    Generate a math problem and its correct answer based on the operator.

    Args:
        num1 (int): First operand in the math problem.
        num2 (int): Second operand in the math problem.
        operator (str): The operator to use in the problem ('+', '-', '*').

    Returns:
        tuple[str, int]: A tuple containing the problem string and its correct answer.

    Raises:
        TypeError: If operator is not of type str.
        ValueError: If operator is not one of the allowed strings ('+', '-', '*').

    Examples:
        >>> calculate_with_operator(2, 3, '+')
        ('2 + 3', 5)
        >>> calculate_with_operator(5, 2, '-')
        ('5 - 2', 3)
        >>> calculate_with_operator(2, 3, '*')
        ('2 * 3', 6)
    """
    if not isinstance(operator, str):
        raise TypeError("Operator has to be of type string.")
    if operator not in ['+', '-', '*']:
        raise ValueError(f"Operator must be one of the following: '+', '-', '*', but got '{operator}'.")

    problem_statement = f"{num1} {operator} {num2}"
    if operator == '+':
        solution = num1 + num2
    elif operator == '-':
        solution = num1 - num2
    else:
        solution = num1 * num2

    return problem_statement, solution


def math_quiz():
    """
    Main function to run the Math Quiz Game.

    Prompts the user with a series of math problems and calculates their score.

    Raises:
        ValueError: If the user does not enter a value of type float or int.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # For a total of {total_questions} the user gets a problem statement, can type in their answer and score points:
    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem_statement, correct_answer = calculate_with_operator(num1, num2, operator)
        print(f"\nQuestion: {problem_statement}")
        while True:
            try:
                user_answer = int(float(input("Your answer: ")))  # User has to type in the correct answer to the
                # shown math problem. This string is converted first to float and then to int, so that also float values
                # like 4.0 are accepted since it is the same value as int 4.
                break  # break the while loop since the user did now enter the correct input type int
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                # continue  # Skips to the next question if input is invalid

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
