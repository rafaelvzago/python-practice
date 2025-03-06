import unittest
from unittest.mock import patch


# Let's define a module-level reference to the external API function
# (In a real application, this would probably be imported from another module)
def fetch_data(user_id):
    # This is just a placeholder and should never be called directly in tests
    raise NotImplementedError("This function should be mocked in tests")


# The function we want to implement
def get_user_data(user_id):
    """
    Fetches user data from an external API.
    
    Args:
        user_id: The ID of the user to fetch
        
    Returns:
        dict: A dictionary containing the user data if found
        None: If the user is not found
        
    Raises:
        ConnectionError: If there's a problem connecting to the API
        ValueError: If the user_id is invalid
    """
    # Validate user_id
    if not isinstance(user_id, (int, str)):
        raise ValueError("User ID must be an integer or string")
    
    try:
        # Call the external API function
        data = fetch_data(user_id)
        
        # Return the data directly
        return data
    except Exception as e:
        # Convert any exception from the external API to a ConnectionError
        raise ConnectionError(f"Failed to connect to the API: {str(e)}")


# Unit tests using mocking
class TestGetUserData(unittest.TestCase):
    
    @patch('__main__.fetch_data')  # Mock the external API function
    def test_user_found(self, mock_fetch_data):
        """Test the case where the user is found."""
        # Set up the mock to return a sample user
        mock_fetch_data.return_value = {"user_id": 123, "name": "John Doe", "status": "active"}
        
        # Call the function
        result = get_user_data(123)
        
        # Assert that the mock was called with the correct arguments
        mock_fetch_data.assert_called_once_with(123)
        
        # Assert that the function returns the expected data
        self.assertEqual(result, {"user_id": 123, "name": "John Doe", "status": "active"})
    
    @patch('__main__.fetch_data')
    def test_user_not_found(self, mock_fetch_data):
        """Test the case where the user is not found."""
        # Set up the mock to return None (user not found)
        mock_fetch_data.return_value = None
        
        # Call the function
        result = get_user_data(999)
        
        # Assert that the mock was called with the correct arguments
        mock_fetch_data.assert_called_once_with(999)
        
        # Assert that the function returns None
        self.assertIsNone(result)
    
    @patch('__main__.fetch_data')
    def test_api_exception(self, mock_fetch_data):
        """Test the case where the API raises an exception."""
        # Set up the mock to raise an exception
        mock_fetch_data.side_effect = Exception("API is down")
        
        # Call the function and expect a ConnectionError
        with self.assertRaises(ConnectionError) as context:
            get_user_data(123)
        
        # Assert that the error message is correct
        self.assertIn("Failed to connect to the API", str(context.exception))
    
    def test_invalid_user_id(self):
        """Test the case where an invalid user ID is provided."""
        # Test with invalid user ID types
        with self.assertRaises(ValueError) as context:
            get_user_data(None)
        
        self.assertIn("User ID must be an integer or string", str(context.exception))
        
        # Additional test with another invalid type
        with self.assertRaises(ValueError):
            get_user_data([1, 2, 3])


if __name__ == "__main__":
    # Note: This won't actually run because fetch_data isn't implemented
    # This is just for demonstration purposes
    unittest.main()