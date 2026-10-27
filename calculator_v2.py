from typing import Dict, List, Protocol


class CalculationError(Exception):
    pass


class DivideByZeroError(CalculationError):
    def __init__(self):
        super().__init__("Divide by zero.")


class InvalidOperationError(CalculationError):
    def __init__(self):
        super().__init__("Invalid operation. Try '+' or '-'.")


class OperationProtocol(Protocol):
    def calculate(self, a: float, b: float) -> float:
        ...


class Addition(OperationProtocol):
    def calculate(self, a: float, b: float) -> float:
        return a + b


class Subtraction(OperationProtocol):
    def calculate(self, a: float, b: float) -> float:
        return a - b


class Multiplication(OperationProtocol):
    def calculate(self, a: float, b: float) -> float:
        return a * b


class Division(OperationProtocol):
    def calculate(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError(f"Cannot divide by zero")
        return a / b


class Power(OperationProtocol):
    def calculate(self, a: float, b: float) -> float:
        return a ** b


class CalculatorEngine:
    def __init__(self):
        self._operators: Dict[str, OperationProtocol] = {
            "+": Addition,
            "-": Subtraction,
            "*": Multiplication,
            "/": Division,
            "^": Power,
        }

    def get_available_operations(self) -> List[str]:
        return list(self._operators.keys())


def run_cli():
    calculator = CalculatorEngine()
    operations = calculator.get_available_operations()

    print("=" * 20, "Calculator on Python", "=" * 20)
    print(f"Available operators: {', '.join(operations)}.")


if __name__ == '__main__':
    run_cli()