import unittest
from ..services import addition, subtraction, multiplication, division, modulus


class TestCalculator(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(addition(1, 2), 3)

    def test_subtract(self) -> None:
        self.assertEqual(subtraction(2, 1), 1)

    def test_multiply(self) -> None:
        self.assertEqual(multiplication(3, 4), 12)

    def test_divide(self) -> None:
        self.assertEqual(division(12, 3), 4)

    def test_modulus(self) -> None:
        self.assertEqual(modulus(10, 3), 1)


if __name__ == "__main__":
    unittest.main()
