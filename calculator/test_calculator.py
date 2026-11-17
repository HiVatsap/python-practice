import pytest
from calculator import (
    Calculator,
    parse_number,
    CalculatorError,
    CalculationError,
    InvalidArgumentError,
    UnsupportedOperationError,
)


def test_binary_operation() -> None:
    """Test all standard binary operations."""
    calc = Calculator()
    assert calc.calculate("+", 2, 3) == 5
    assert calc.calculate("-", 5, 2) == 3
    assert calc.calculate("*", 3, 4) == 12
    assert calc.calculate("/", 10, 2) == 5
    assert calc.calculate("**", 2, 3) == 8
    assert calc.calculate("%", 5, 2) == 1


def test_unary_operation() -> None:
    """Test unary operations like square root and absolute value."""
    calc = Calculator()
    assert calc.calculate("sqrt", 9) == 3
    assert calc.calculate("abs", -7.5) == 7.5


def test_division_by_zero() -> None:
    """Test that division and modulo by zero raise CalculationError."""
    calc = Calculator()
    with pytest.raises(CalculationError):
        calc.calculate("/", 5, 0)
    with pytest.raises(CalculationError):
        calc.calculate("%", 5, 0)


def test_negative_sqrt() -> None:
    """Test that square root of a negative number raises CalculationError."""
    calc = Calculator()
    with pytest.raises(CalculationError):
        calc.calculate("sqrt", -9)


def test_invalid_arguments_count() -> None:
    """Test that passing wrong number of arguments raises InvalidArgumentError."""
    calc = Calculator()
    with pytest.raises(InvalidArgumentError):
        calc.calculate("+", 5)
    with pytest.raises(InvalidArgumentError):
        calc.calculate("sqrt", 4, 2)


def test_unsupported_operation() -> None:
    """Test that an unknown operation raises UnsupportedOperationError."""
    calc = Calculator()
    with pytest.raises(UnsupportedOperationError):
        calc.calculate("unknown", 2, 2)


def test_last_result_memory() -> None:
    """Test saving and retrieving the last result (ans)."""
    calc = Calculator()
    assert calc.last_result is None

    calc.calculate("+", 10, 5)
    assert calc.last_result == 15

    parsed = parse_number("ans", calc.last_result)
    assert parsed == 15


def test_empty_ans_error() -> None:
    """Test that using 'ans' when memory is empty raises an error."""
    with pytest.raises(CalculatorError):
        parse_number("ans", None)


def test_parse_number() -> None:
    """Test number parsing and integer conversion."""
    assert parse_number("10", None) == 10
    assert parse_number("10.0", 0) == 10 # Checking .is_integer()
    assert parse_number("10.5", None) == 10.5

    with pytest.raises(ValueError):
        parse_number("abc", None)