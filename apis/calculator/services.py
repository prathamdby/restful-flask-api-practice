from .types import NumericType


def log_operation(operation_name: str, a: NumericType, b: NumericType) -> None:
    print(f"{operation_name} called with arguments:", a, b)


def validate_arguments(a, type1, b, type2) -> None:
    if not isinstance(a, type1) or not isinstance(b, type2):
        raise ValueError(f"Arguments must be {type1} and {type2}")


def addition(a: NumericType, b: NumericType) -> NumericType:
    validate_arguments(a, NumericType, b, NumericType)
    log_operation("Addition", a, b)
    return a + b


def subtraction(a: NumericType, b: NumericType) -> NumericType:
    validate_arguments(a, NumericType, b, NumericType)
    log_operation("Subtraction", a, b)
    return a - b


def multiplication(a: NumericType, b: NumericType) -> NumericType:
    validate_arguments(a, NumericType, b, NumericType)
    log_operation("Multiplication", a, b)
    return a * b


def division(a: NumericType, b: NumericType) -> float:
    validate_arguments(a, NumericType, b, NumericType)
    log_operation("Division", a, b)
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")


def modulus(a: NumericType, b: NumericType) -> NumericType:
    validate_arguments(a, NumericType, b, NumericType)
    log_operation("Modulus", a, b)
    return a % b
