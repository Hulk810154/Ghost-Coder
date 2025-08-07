import unittest
from code_generator.main import generate_function_from_description

class TestCodeGenerator(unittest.TestCase):
    def test_generate_sum_function(self):
        description = "a function to calculate the sum of x and y"
        expected_code = '''def calculate_sum(x, y):
    """
    a function to calculate the sum of x and y
    """
    return x + y'''
        self.assertEqual(
            generate_function_from_description(description).strip(),
            expected_code.strip()
        )

    def test_generate_difference_function(self):
        description = "a function to find the difference between a and b"
        expected_code = '''def find_difference(a, b):
    """
    a function to find the difference between a and b
    """
    return a - b'''
        self.assertEqual(
            generate_function_from_description(description).strip(),
            expected_code.strip()
        )

    def test_fallback_behavior(self):
        description = "a generic function"
        expected_code = '''def my_function():
    """
    a generic function
    """
    pass'''
        self.assertEqual(
            generate_function_from_description(description).strip(),
            expected_code.strip()
        )

    def test_generate_multiplication_function(self):
        description = "a function that multiplies a by b"
        expected_code = '''def multiply(a, b):
    """
    a function that multiplies a by b
    """
    return a * b'''
        self.assertEqual(
            generate_function_from_description(description).strip(),
            expected_code.strip()
        )

if __name__ == '__main__':
    unittest.main()
