import unittest
from app.calculator import evaluate_expression

class TestCalculator(unittest.TestCase):
    def test_basic_math(self):
        self.assertEqual(evaluate_expression("2-2"), 0)
        self.assertAlmostEqual(evaluate_expression("sin(pi/2)"), 1.0)

    def test_invalid_expr(self):
        self.assertIn("Error", str(evaluate_expression("2+")))

if __name__ == '__main__':
    unittest.main()
