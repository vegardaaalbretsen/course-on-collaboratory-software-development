"""
Simple Calculator Module
This module provides basic arithmetic operations.
"""

from src.utils import validate_numbers, format_result


def add(a, b):
    """
    Add two numbers together.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: Sum of a and b

    Raises:
        TypeError: If inputs are not numbers
    """
    validate_numbers(a, b)
    result = a + b
    return format_result(result)


def subtract(a, b):
    """
    Subtract second number from first number.

    Args:
        a (float): First number
        b (float): Second number to subtract

    Returns:
        float: Difference of a and b

    Raises:
        TypeError: If inputs are not numbers
    """
    validate_numbers(a, b)
    result = a - b
    return format_result(result)


def divide(a, b):
    """
    Divide first number by second number.
    Args:
        a (float): Numerator
        b (float): Denominator
    Returns:
        float: Result of division a / b
    Raises:
        ValueError: If attempting to divide by zero
    """

    validate_numbers(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    return format_result(result)


def multiply(a, b):
    """
    Multiply two numbers together.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: Product of a and b

    Raises:
        TypeError: If inputs are not numbers
    """
    validate_numbers(a, b)
    result = a * b
    return format_result(result)


def main():
    """
    Simple interactive calculator for testing.
    """
    print("Simple Calculator")
    print("Available operations: add, subtract, divide")
    print("Type 'quit' to exit")

    while True:
        operation = (
            input("\nEnter operation (add/subtract/divide/quit): ").lower().strip()
        )

        if operation == "quit":
            print("Goodbye!")
            break
        if operation not in ["add", "subtract", "divide", "multiply"]:
            print(
                "Invalid operation. Please use 'add', 'subtract', 'divide' or 'multiply'"
            )
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if operation == "add":
                result = add(a, b)
                print(f"Result: {a} + {b} = {result}")
            elif operation == "subtract":
                result = subtract(a, b)
                print(f"Result: {a} - {b} = {result}")
            elif operation == "divide":
                result = divide(a, b)
                print(f"Result: {a} / {b} = {result}")
            elif operation == "multiply":
                result = multiply(a, b)
                print(f"Result: {a} * {b} = {result}")
        except ValueError:
            print("Please enter valid numbers")
        except TypeError as e:
            print(f"Error: {e}")
