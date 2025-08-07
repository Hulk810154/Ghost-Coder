import unittest
from code_generator.main import generate_function_from_description

class TestCodeGenerator(unittest.TestCase):
    def test_generate_function_from_description(self):
        description = "A test function."
        expected_code = '''def my_function():
    """
    A test function.
    """
    pass
'''
        self.assertEqual(
            generate_function_from_description(description),
            expected_code
        )

if __name__ == '__main__':
    unittest.main()
