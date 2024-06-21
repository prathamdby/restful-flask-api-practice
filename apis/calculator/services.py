def log_operation(operation_name: str, a: int, b: int) -> None:
    print(f"{operation_name} called with arguments:", a, b)


def validate_arguments(a, type1, b, type2) -> None:
    if not isinstance(a, type1) or not isinstance(b, type2):
        raise ValueError(f"Arguments must be {type1} and {type2}")


def addition(a: int, b: int) -> int:
    validate_arguments(a, int, b, int)
    log_operation("Addition", a, b)
    return a + b


def subtraction(a: int, b: int) -> int:
    validate_arguments(a, int, b, int)
    log_operation("Subtraction", a, b)
    return a - b


def multiplication(a: int, b: int) -> int:
    validate_arguments(a, int, b, int)
    log_operation("Multiplication", a, b)
    return a * b


def division(a: int, b: int) -> float:
    validate_arguments(a, int, b, int)
    log_operation("Division", a, b)
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")


def modulus(a: int, b: int) -> int:
    validate_arguments(a, int, b, int)
    log_operation("Modulus", a, b)
    return a % b
