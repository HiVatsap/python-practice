from typing import Callable


Number = int | float


class Calculator:
    def __init__(self) -> None:
        self._operations: dict[str, Callable[[Number, Number], Number]] = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "**": lambda a, b: a**b,
            "%": lambda a, b: a % b,
        }

    def calculate(self, num1: Number, op: str, num2: Number) -> Number:
        if op not in self._operations:
            raise ValueError("Invalid operation.")
        if op in ("/", "%") and num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return self._operations[op](num1, num2)

    def get_supported_operations(self) -> list[str]:
        return list(self._operations.keys())


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
            raw_num1 = get_input("Enter a first number: ")
            op = get_input("Enter a operation: ")
            raw_num2 = get_input("Enter a second number: ")

            num1 = parse_number(raw_num1)
            num2 = parse_number(raw_num2)

            result = calc.calculate(num1, op, num2)

            print(f"\n{num1} {op} {num2} = {result}\n")
        except EOFError:
            print("\nGoodbye!")
            break
        except (ValueError, ZeroDivisionError) as e:
            print(f"\nError: {e}\n")
        except Exception as e:
            print(f"\nNot supported error: {e}\n")


if __name__ == '__main__':
    main()