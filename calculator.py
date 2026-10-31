import math
from typing import Callable

Number = int | float


class CalculatorError(Exception):
    """Basic class for all calculator errors."""
    pass


class UnsupportedOperationError(CalculatorError):
    """Raised when the user tries to use an unsupported operation."""
    pass


class InvalidArgumentError(CalculatorError):
    """Raised when the user tries to use an invalid number of arguments."""
    pass


class CalculationError(CalculatorError):
    """Raised when the user tries to use an invalid operation."""
    pass


class Calculator:
    def __init__(self) -> None:
        self.last_result: Number | None = None

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
                raise InvalidArgumentError(f"Operation '{op}' requires 2 arguments.")
            num1, num2 = args
            if op in ("/", "%") and num2 == 0:
                raise CalculationError("Cannot divide by zero.")
            result = self._binary_operations[op](num1, num2)

        elif op in self._unary_operations:
            if len(args) != 1:
                raise InvalidArgumentError(f"Operation '{op}' requires 1 argument.")
            num = args[0]
            if op == "sqrt" and num < 0:
                raise CalculationError("'sqrt' operation requires non-negative arguments.")
            result = self._unary_operations[op](num)

        else:
            raise UnsupportedOperationError(f"'{op}' is not supported.")

        self.last_result = result
        return result

    def is_binary(self, op: str) -> bool:
        return op in self._binary_operations

    def is_unary(self, op: str) -> bool:
        return op in self._unary_operations

    def get_supported_operations(self) -> list[str]:
        return list(self._binary_operations.keys()) + list(self._unary_operations.keys())


def get_input(prompt: str) -> str:
    """Get user input and check for exit command."""
    value = input(prompt).strip()
    if value.lower() == "q":
        raise EOFError("Exiting...")
    return value


def parse_number(num_str: str, last_result: Number | None) -> Number:
    """Parse a string input into an int or float."""
    cleaned = num_str.strip()

    if cleaned == 'ans':
        if last_result is None:
            raise CalculatorError("Last result is empty.")
        return last_result

    try:
        val = float(num_str)
        return int(val) if val.is_integer() else val
    except ValueError:
        raise ValueError(f"'{num_str}' is not a valid number.")


def main() -> None:
    calc = Calculator()
    operations = calc.get_supported_operations()

    print("=============== Python Calculator ===============")
    print(f"Available operations: {', '.join(operations)}.")
    print("Enter 'ans' to use last result.")
    print("Enter 'q' to quit.\n")

    while True:
        try:
            op = get_input("Enter a operation: ")

            if calc.is_binary(op):
                raw_num1 = get_input("Enter first number(or 'ans'): ")
                raw_num2 = get_input("Enter second number(or 'ans'): ")
                num1 = parse_number(raw_num1, calc.last_result)
                num2 = parse_number(raw_num2, calc.last_result)
                result = calc.calculate(op, num1, num2)
                print(f"\n{num1} {op} {num2} = {result}\n")

            elif calc.is_unary(op):
                raw_num = get_input("Enter a number(or 'ans'): ")
                num = parse_number(raw_num, calc.last_result)
                result = calc.calculate(op, num)
                print(f"\n{op}({num}) = {result}\n")

            else:
                raise ValueError(f"'{op}' is not supported.")

        except EOFError:
            print("\nGoodbye!")
            break
        except CalculatorError as e:
            print(f"\nCalculation error: {e}\n")
        except ValueError as e:
            print(f"\nInput error: {e}\n")
        except Exception as e:
            print(f"\nNot supported error: {e}\n")


if __name__ == '__main__':
    main()