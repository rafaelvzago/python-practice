import pytest
from unittest.mock import MagicMock

# Database interaction functions
def add_user_to_database(user_data, db_connection):
    """
    Add a user to the database.
    
    Args:
        user_data (dict): Dictionary containing at minimum 'username' and 'email' keys
        db_connection: Database connection object with insert method
        
    Returns:
        bool: True if the user was added successfully
        
    Raises:
        ValueError: If user_data is missing required fields
        RuntimeError: If the database operation fails
    """
    # Validate user data
    if not isinstance(user_data, dict):
        raise ValueError("User data must be a dictionary")
    
    if "username" not in user_data or "email" not in user_data:
        raise ValueError("User data must contain 'username' and 'email' keys")
    
    try:
        # Insert the user data into the 'users' table
        db_connection.insert("users", user_data)
        return True
    except Exception as e:
        # Wrap any database errors in a RuntimeError
        raise RuntimeError(f"Failed to add user to database: {str(e)}")


def get_user_from_database(username, db_connection):
    """
    Retrieve a user from the database by username.
    
    Args:
        username (str): The username of the user to retrieve
        db_connection: Database connection object with find_by method
        
    Returns:
        dict: The user data if found
        None: If no user with the given username exists
        
    Raises:
        RuntimeError: If the database operation fails
    """
    if not username:
        raise ValueError("Username cannot be empty")
    
    try:
        # Find the user by username in the 'users' table
        return db_connection.find_by("users", "username", username)
    except Exception as e:
        # Wrap any database errors in a RuntimeError
        raise RuntimeError(f"Database error while retrieving user: {str(e)}")


# Pytest fixture for mocking database connection
@pytest.fixture
def mock_db_connection():
    """
    Fixture that provides a mock database connection.
    
    The mock simulates a database with tables and provides insert and find_by methods.
    """
    class MockDBConnection:
        def __init__(self):
            # Internal data structure to simulate database tables
            self.tables = {
                "users": []  # Empty users table
            }
        
        def insert(self, table_name, data):
            """
            Insert data into a specified table.
            
            Args:
                table_name (str): Name of the table
                data (dict): Data to insert
                
            Raises:
                ValueError: If the table doesn't exist
            """
            if table_name not in self.tables:
                raise ValueError(f"Table '{table_name}' does not exist")
            
            # Copy the data to avoid modifying the original
            self.tables[table_name].append(data.copy())
        
        def find_by(self, table_name, key, value):
            """
            Find an entry in a table by a key-value pair.
            
            Args:
                table_name (str): Name of the table
                key (str): The key to search by
                value: The value to search for
                
            Returns:
                dict: The found data if it exists
                None: If no matching data is found
                
            Raises:
                ValueError: If the table doesn't exist
            """
            if table_name not in self.tables:
                raise ValueError(f"Table '{table_name}' does not exist")
            
            # Search for matching entries
            for entry in self.tables[table_name]:
                if key in entry and entry[key] == value:
                    return entry.copy()  # Return a copy to prevent modification
            
            # Return None if no matching entry is found
            return None
    
    # Return an instance of the mock connection
    return MockDBConnection()


# Test cases
def test_add_user_successfully(mock_db_connection):
    """Test that a user can be successfully added to the database."""
    # Arrange
    user_data = {"username": "testuser", "email": "test@example.com"}
    
    # Act
    result = add_user_to_database(user_data, mock_db_connection)
    
    # Assert
    assert result is True
    assert len(mock_db_connection.tables["users"]) == 1
    assert mock_db_connection.tables["users"][0]["username"] == "testuser"
    assert mock_db_connection.tables["users"][0]["email"] == "test@example.com"


def test_add_user_handles_exception(mock_db_connection):
    """Test that add_user_to_database properly handles exceptions."""
    # Arrange
    user_data = {"username": "testuser", "email": "test@example.com"}
    
    # Mock the insert method to raise an exception
    mock_db_connection.insert = MagicMock(side_effect=Exception("Connection error"))
    
    # Act/Assert
    with pytest.raises(RuntimeError) as excinfo:
        add_user_to_database(user_data, mock_db_connection)
    
    # Verify the error message
    assert "Failed to add user to database" in str(excinfo.value)


def test_get_existing_user(mock_db_connection):
    """Test that get_user_from_database returns correct data for existing users."""
    # Arrange - Add a user to the mock database
    user_data = {"username": "existinguser", "email": "existing@example.com"}
    mock_db_connection.tables["users"].append(user_data)
    
    # Act
    result = get_user_from_database("existinguser", mock_db_connection)
    
    # Assert
    assert result is not None
    assert result["username"] == "existinguser"
    assert result["email"] == "existing@example.com"


def test_get_nonexistent_user(mock_db_connection):
    """Test that get_user_from_database returns None for non-existent users."""
    # Act
    result = get_user_from_database("nonexistentuser", mock_db_connection)
    
    # Assert
    assert result is None


def test_add_user_with_invalid_data(mock_db_connection):
    """Test that add_user_to_database validates input data properly."""
    # Test with missing email
    with pytest.raises(ValueError) as excinfo:
        add_user_to_database({"username": "testuser"}, mock_db_connection)
    assert "User data must contain 'username' and 'email' keys" in str(excinfo.value)
    
    # Test with non-dictionary input
    with pytest.raises(ValueError) as excinfo:
        add_user_to_database("not a dictionary", mock_db_connection)
    assert "User data must be a dictionary" in str(excinfo.value)


def test_get_user_with_empty_username(mock_db_connection):
    """Test that get_user_from_database validates the username parameter."""
    with pytest.raises(ValueError) as excinfo:
        get_user_from_database("", mock_db_connection)
    assert "Username cannot be empty" in str(excinfo.value)