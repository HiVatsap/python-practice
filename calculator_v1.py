import math
from typing import Callable


Number = int | float


class Calculator:
    def __init__(self) -> None:
        self._binary_operations: dict[str, Callable[[Number, Number], Number]] = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "**": lambda a, b: a**b,
            "%": lambda a, b: a % b,
        }

        self._unary_operations: dict[str, Callable[[Number], Number]] = {
            "sqrt": lambda a: math.sqrt(a),
            "abs": lambda a: abs(a),
        }

    def calculate(self, op: str, *args: Number) -> Number:
        """Universal function to calculate binary and unary operations."""
        if op in self._binary_operations:
            if len(args) != 2:
                raise ValueError(f"Operation {op} requires 2 arguments.")
            num1, num2 = args
            if op in ("/", "%") and num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return self._binary_operations[op](num1, num2)

        if op in self._unary_operations:
            if len(args) != 1:
                raise ValueError(f"Operation {op} requires 1 argument.")
            num = args[0]
            if op == "sqrt" and num < 0:
                raise ValueError("'sqrt' operation requires non-negative arguments.")
            return self._unary_operations[op](num)

        raise ValueError(f"'{op}' is not supported.")

    def is_binary(self, op: str) -> bool:
        return op in self._binary_operations

    def is_unary(self, op: str) -> bool:
        return op in self._unary_operations

    def get_supported_operations(self) -> list[str]:
        return list(self._binary_operations.keys()) + list(self._unary_operations.keys())


def get_input(prompt: str) -> str:
    """ Get user input and check for exit command. """
    value = input(prompt).strip()
    if value.lower() == "q":
        raise EOFError("Exiting...")
    return value


def parse_number(num: str) -> Number:
    """ Parse a string input into an int or float. """
    try:
        val = float(num)
        return int(val) if val.is_integer() else val
    except ValueError:
        raise ValueError(f"'{num}' is not a valid number.")


def main() -> None:
    calc = Calculator()
    operations = calc.get_supported_operations()

    print("=============== Python Calculator ===============")
    print(f"Available operations: {', '.join(operations)}.")
    print("Enter 'q' to quit.\n")

    while True:
        try:
            op = get_input("Enter a operation: ")

            if calc.is_binary(op):
                raw_num1 = get_input("Enter first number: ")
                raw_num2 = get_input("Enter second number: ")
                num1 = parse_number(raw_num1)
                num2 = parse_number(raw_num2)
                result = calc.calculate(op, num1, num2)
                print(f"\n{num1} {op} {num2} = {result}\n")

            elif calc.is_unary(op):
                raw_num = get_input("Enter a number: ")
                num = parse_number(raw_num)
                result = calc.calculate(op, num)
                print(f"\n{op}({num}) = {result}\n")

            else:
                raise ValueError(f"'{op}' is not supported.")

        except EOFError:
            print("\nGoodbye!")
            break
        except (ValueError, ZeroDivisionError) as e:
            print(f"\nError: {e}\n")
        except Exception as e:
            print(f"\nNot supported error: {e}\n")


if __name__ == '__main__':
    main()