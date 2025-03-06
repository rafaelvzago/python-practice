import unittest

# First, let's write our tests (Test-Driven Development)
class TestCalculator(unittest.TestCase): # Inherit from unittest.TestCase
    
    def test_addition(self):
        """Test that addition works correctly."""
        self.assertEqual(calculate("add", 5, 3), 8)
        self.assertEqual(calculate("add", -1, 1), 0)
        self.assertEqual(calculate("add", 0.5, 0.5), 1.0)
    
    def test_subtraction(self):
        """Test that subtraction works correctly."""
        self.assertEqual(calculate("subtract", 5, 3), 2)
        self.assertEqual(calculate("subtract", -1, 1), -2)
        self.assertEqual(calculate("subtract", 0.5, 0.5), 0.0)
    
    def test_multiplication(self):
        """Test that multiplication works correctly."""
        self.assertEqual(calculate("multiply", 5, 3), 15)
        self.assertEqual(calculate("multiply", -1, 1), -1)
        self.assertEqual(calculate("multiply", 0.5, 0.5), 0.25)
    
    def test_division(self):
        """Test that division works correctly."""
        self.assertEqual(calculate("divide", 6, 3), 2)
        self.assertEqual(calculate("divide", -1, 1), -1)
        self.assertEqual(calculate("divide", 0.5, 0.5), 1.0)
    
    def test_invalid_operation(self):
        """Test that an invalid operation returns an error message."""
        self.assertEqual(calculate("power", 2, 3), "Operation not defined")
        self.assertEqual(calculate("", 5, 3), "Operation not defined")
    
    def test_division_by_zero(self):
        """Test that division by zero raises a ValueError."""
        with self.assertRaises(ValueError):
            calculate("divide", 5, 0)
    
    def test_zero_values(self):
        """Test operations with zero values."""
        self.assertEqual(calculate("add", 0, 0), 0)
        self.assertEqual(calculate("subtract", 0, 0), 0)
        self.assertEqual(calculate("multiply", 0, 5), 0)
        self.assertEqual(calculate("divide", 0, 5), 0)


# Now, let's implement the function to make the tests pass
def calculate(operation, num1, num2):
    """
    Perform a simple arithmetic operation.
    
    Args:
        operation (str): "add", "subtract", "multiply", or "divide"
        num1 (int/float): First number
        num2 (int/float): Second number
        
    Returns:
        int/float: Result of the operation
        str: "Operation not defined" if operation is invalid
        
    Raises:
        ValueError: If attempting to divide by zero
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    else:
        return "Operation not defined"


if __name__ == "__main__":
    unittest.main()