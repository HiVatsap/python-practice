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


def parse_number(num):
    cleaned = num.strip()
    try:
        val = float(cleaned)
        return int(val) if val.is_integer() else val
    except ValueError:
        raise ValueError(f"'{cleaned}' is not a valid number.")


def main():
    calc = Calculator()
    print("=============== Python Calculator ===============")
    print(f"Available operations: {', '.join(calc._operations.keys())}.")
    print("Enter 'q' to quit.\n")

    while True:
        try:
            row_num1 = input("Enter a first number: ")
            if row_num1.strip().lower() == "q":
                print("Goodbye!")
                break

            op = input("Enter a operation: ").strip()
            if op.strip().lower() == "q":
                print("Goodbye!")
                break

            row_num2 = input("Enter a second number: ")
            if row_num2.strip().lower() == "q":
                print("Goodbye!")
                break

            num1 = parse_number(row_num1)
            num2 = parse_number(row_num2)

            result = calc.calculate(num1, op, num2)

            print(f"\n{num1} {op} {num2} = {result}\n")
        except (ValueError, ZeroDivisionError) as e:
            print(f"\nError: {e}\n")
        except not (ValueError, ZeroDivisionError) as e:
            print(f"\nNot supported error: {e}\n")


if __name__ == '__main__':
    main()