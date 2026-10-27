class Calculator:
    def __init__(self):
        self._operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "**": lambda a, b: a**b,
            "%": lambda a, b: a % b,
        }

    def calculate(self, num1, op, num2):
        if op not in self._operations:
            raise ValueError("Invalid operation.")
        if (op == "/" or op == "%") and num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return self._operations[op](num1, num2)

    def get_supported_operations(self):
        return list(self._operations.keys())


def get_input(prompt):
    value = input(prompt).strip()
    if value.lower() == "q":
        print("Goodbye!")
        exit(0)
    return value


def parse_number(num):
    cleaned = num.strip()
    try:
        val = float(cleaned)
        return int(val) if val.is_integer() else val
    except ValueError:
        raise ValueError(f"'{cleaned}' is not a valid number.")


def main():
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
        except (ValueError, ZeroDivisionError) as e:
            print(f"\nError: {e}\n")
        except Exception as e:
            print(f"\nNot supported error: {e}\n")


if __name__ == '__main__':
    main()