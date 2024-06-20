def log_operation(operation_name: str, a: int, b: int) -> None:
    print(f"{operation_name} called with arguments:", a, b)


def addition(a: int, b: int) -> int:
    log_operation("Addition", a, b)
    return a + b


def subtraction(a: int, b: int) -> int:
    log_operation("Subtraction", a, b)
    return a - b


def multiplication(a: int, b: int) -> int:
    log_operation("Multiplication", a, b)
    return a * b


def division(a: int, b: int) -> float:
    log_operation("Division", a, b)
    return a / b


def modulus(a: int, b: int) -> int:
    log_operation("Modulus", a, b)
    return a % b
