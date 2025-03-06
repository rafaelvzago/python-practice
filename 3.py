import time
import threading
import functools

def debounce(wait_time):
    """
    Creates a decorator that debounces a function.
    
    When a function is debounced, multiple calls within the wait_time will
    result in only the last call being executed after wait_time has passed.
    
    Args:
        wait_time (float): Time in seconds to wait before executing the function
        
    Returns:
        function: Decorator function
    """
    def decorator(func):
        # Store state between function calls
        timer = None
        last_args = None
        last_kwargs = None
        last_result = None
        lock = threading.Lock()
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal timer, last_args, last_kwargs, last_result
            
            # Store current arguments to use in the delayed call
            with lock:
                last_args = args
                last_kwargs = kwargs
            
                # Cancel previous timer if it exists
                if timer is not None:
                    timer.cancel()
                
                # Define the function to execute after wait time
                def delayed_call():
                    nonlocal last_result
                    with lock:
                        # Execute the function with the most recent arguments
                        last_result = func(*last_args, **last_kwargs)
                
                # Set up a new timer
                timer = threading.Timer(wait_time, delayed_call)
                timer.start()
            
            # Return the result of the last execution (may be None if first call)
            return last_result
        
        return wrapper
    
    return decorator


# Example usage and test
if __name__ == "__main__":
    print("Testing debounce functionality...")
    
    # Use a list to track call count (to avoid the nonlocal binding issue)
    call_stats = [0]
    
    @debounce(1.0)  # 1 second debounce time
    def test_function(value):
        # Increment the counter in the list instead of using nonlocal
        call_stats[0] += 1
        print(f"Function executed with value: {value}")
        return value
    
    # Test with multiple calls in quick succession
    print("Making multiple calls quickly...")
    for i in range(5):
        result = test_function(f"Call {i}")
        print(f"Call {i} returned: {result}")
        time.sleep(0.2)  # 200ms between calls (less than the debounce time)
    
    print("Waiting for debounced function to execute...")
    time.sleep(1.5)  # Wait for the debounced function to execute
    
    print(f"Total actual executions: {call_stats[0]}")
    
    print("\nTesting with calls spaced beyond debounce time...")
    for i in range(5, 8):
        result = test_function(f"Call {i}")
        print(f"Call {i} returned: {result}")
        time.sleep(1.5)  # Wait longer than debounce time
    
    print("Waiting for final call to execute...")
    time.sleep(1.5)
    
    print(f"Final execution count: {call_stats[0]}")