# Python Practice

---

# 1.py - Log Analysis Function - Core Concepts

## Data Processing with Iteration and String Manipulation
The log analyzer demonstrates efficient data processing by iterating through log entries and extracting meaningful information. The function leverages Python's string manipulation capabilities, particularly the `split()` method with a limit parameter to properly parse structured log data. This technique ensures reliable extraction of timestamps, log levels, and messages from each entry. String manipulation is a fundamental skill in data processing, allowing transformations of raw text into structured information that can be analyzed programmatically.

## Data Structures for Collection and Aggregation
This implementation showcases the strategic use of different data structures for specific purposes. It employs a simple counter (integer) for error tracking, a dictionary for frequency analysis of warning messages, and a set for collecting unique timestamps. Each structure is chosen for its particular advantages: dictionaries provide fast lookups and value associations, sets automatically handle uniqueness constraints, and simple counters offer efficiency for basic tallying. The ability to select appropriate data structures based on the task requirements demonstrates a core principle of efficient algorithm design.

## Dictionary Comprehension and Functional Returns
The function returns a well-structured dictionary that organizes the analysis results into a clear, accessible format. This approach highlights the importance of clean data presentation in programming. The code also demonstrates conditional logic when finding the most frequent warning message using the `max()` function with a key parameter, showcasing how Python's functional programming features can elegantly solve common data analysis problems. The transformation of the set to a list in the return statement further illustrates the importance of providing data in the expected format required by the application's specifications.

---

# 2.py Calculator with Unit Testing - Core Concepts

## Test-Driven Development (TDD)
This code exemplifies Test-Driven Development, a methodology where tests are written before implementing the actual functionality. The `TestCalculator` class defines multiple test cases that establish the expected behavior of the calculator function before it's created. This approach ensures that development is guided by clear requirements and helps prevent feature creep. TDD follows a "red-green-refactor" cycle: first write failing tests (red), then implement code to make tests pass (green), and finally optimize the code without changing its behavior (refactor).

## Unit Testing with the unittest Framework
The implementation leverages Python's built-in `unittest` framework to create structured, organized tests. The code demonstrates several key testing concepts: assertion methods (`assertEqual`), exception testing with context managers (`assertRaises`), and test organization through docstrings and focused test methods. Each test method follows the Arrange-Act-Assert pattern and covers a specific aspect of functionality, including edge cases (division by zero, operations with zero values) and invalid inputs. This comprehensive testing approach helps ensure reliability and maintainability.

## Function Design with Clear Documentation
The `calculate` function exemplifies robust function design with clear documentation through detailed docstrings. The docstring follows a standard format that explains the function's purpose, documents parameters with their types, describes return values, and explicitly states raised exceptions. The implementation itself demonstrates clean conditional logic, proper error handling with custom exception messages, and adherence to the single responsibility principle. This attention to documentation and careful design makes the code more maintainable and accessible to other developers.

---

# 3.py Debounce Function - Core Concepts

## Decorators and Higher-Order Functions
The debounce implementation demonstrates Python's powerful decorator pattern, a form of higher-order function that modifies the behavior of another function without changing its code. The implementation uses a nested function structure where `decorator` returns the `wrapper` function that encapsulates the original function's behavior. The `@functools.wraps(func)` decorator preserves the original function's metadata (like name and docstring), showcasing proper decorator design. This pattern allows for elegant function transformation and is a cornerstone of Python's functional programming capabilities.

## Closure and State Management
This code leverages closures to maintain state between function calls, a key concept in functional programming. The `wrapper` function "closes over" variables from its outer scope (timer, last_args, last_kwargs, last_result), allowing these values to persist across multiple invocations. The use of `nonlocal` declarations makes this relationship explicit. This stateful behavior, combined with thread synchronization via a lock object, enables the debounce mechanism to track and manage multiple function calls over time, showcasing how closures can create functions with "memory" of previous executions.

## Concurrency and Timing Control
The implementation demonstrates thread management and timing control through Python's threading module. It uses `threading.Timer` to schedule delayed execution and provides thread safety with `threading.Lock` to prevent race conditions when multiple threads might call the debounced function simultaneously. The code carefully manages timer cancellation and recreation, ensuring that only the most recent function call is executed after the waiting period. This approach to managing asynchronous execution showcases important principles for building responsive, efficient systems that need to handle bursts of events appropriately.

---

# 4.py Mocking in Unit Tests - Core Concepts

## Dependency Isolation with Mocking
This code demonstrates the powerful concept of dependency isolation using mock objects in unit testing. By using `unittest.mock.patch`, the implementation replaces the external `fetch_data` function with a controlled substitute during tests. This isolation technique allows for testing the `get_user_data` function's behavior independently from its dependencies, ensuring tests are reliable and focused on a single unit of code. Mocking external dependencies is crucial for creating deterministic tests that aren't affected by network issues, API changes, or other external factors, making tests faster and more consistent.

## Test Case Design and Coverage
The implementation showcases comprehensive test case design by covering multiple scenarios: successful retrieval, user not found, API failures, and invalid inputs. Each test method focuses on a specific behavior with clear assertions that verify both the function's return value and its interaction with dependencies. This approach follows the Arrange-Act-Assert pattern and demonstrates how to structure tests to ensure complete code coverage. The tests also show how to verify that functions properly handle edge cases and error conditions, which is essential for building robust software.

## Exception Handling and Input Validation
The code illustrates proper exception handling and input validation techniques. The `get_user_data` function validates input parameters before processing, throws appropriate typed exceptions with meaningful messages, and converts lower-level exceptions from dependencies into domain-specific exceptions. The test suite correspondingly verifies this behavior using context managers (`with self.assertRaises()`) to check both the exception type and content. This demonstrates the importance of creating a clean public API that handles errors gracefully and provides clear feedback to callers, which is a hallmark of well-designed software.

---

# 5.py Pytest Fixtures and Mocking - Core Concepts

## Test Fixtures and Dependency Injection
This implementation showcases pytest fixtures as a powerful dependency injection mechanism for tests. The `mock_db_connection` fixture creates a controlled test environment by providing a simulated database that mimics real behavior without external dependencies. Pytest automatically injects this fixture into test functions that request it as a parameter, demonstrating the framework's dependency injection pattern. This approach promotes test isolation and reusability while keeping test setup code separate from test logic. Fixtures enable consistent test environments across multiple test functions and reduce code duplication, making tests more maintainable.

## Mock Object Patterns and Behavioral Verification
The code demonstrates both custom mock objects and pytest's integration with `unittest.mock`. The custom `MockDBConnection` class simulates database behavior with controlled responses, while `MagicMock` is used to override methods and simulate failures. This multi-faceted approach to mocking shows how to verify both state (checking internal data structures) and behavior (verifying method calls and exception handling). The tests examine not only the return values of functions but also their side effects and interactions with dependencies. This comprehensive verification approach ensures that code functions correctly within its expected context.

## Parameterized Error Testing and Input Validation
The test suite thoroughly examines error cases and input validation through parameterized error tests. Using pytest's `raises` context manager, the tests verify that functions properly validate inputs and raise appropriate exceptions with informative messages. The test cases systematically explore boundary conditions (empty usernames), invalid input types (non-dictionary user data), and internal failure modes (database exceptions). This methodical approach to testing error conditions demonstrates defensive programming principles and ensures the code maintains its integrity even when presented with unexpected inputs or when dependencies fail in unpredictable ways.