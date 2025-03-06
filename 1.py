def analyze_logs(logs):
    error_count = 0
    warning_messages = {}
    info_timestamps = set()
    
    for line in logs:
        parts = line.split(' ', 2)  # Split only at first two spaces to properly separate parts
        timestamp = parts[0]
        level = parts[1]
        message = parts[2]
        
        # Counting the ERRORs
        if level == 'ERROR':
            error_count += 1
        
        # Finding most frequent warning message
        elif level == 'WARNING':
            if message not in warning_messages:
                warning_messages[message] = 0
            warning_messages[message] += 1
            
        # List of unique timestamps for INFO messages
        elif level == 'INFO':
            info_timestamps.add(timestamp)
    
    # Finding the most frequent warning message
    most_frequent_warning = None
    if warning_messages:  # Check if there are any warning messages
        most_frequent_warning = max(warning_messages, key=warning_messages.get)
        
    # Return the result as a dictionary as specified in requirements
    return {
        "error_count": error_count,
        "most_frequent_warning": most_frequent_warning,
        "info_timestamps": list(info_timestamps)
    }

# Test with example data
log_example = [
    "1678886400 INFO User logged in",
    "1678886460 WARNING Disk space low",
    "1678886520 ERROR Database connection failed",
    "1678886580 INFO User logged out",
    "1678886640 WARNING Disk space low",
    "1678886700 ERROR Invalid credentials",
    "1678886760 INFO User logged in",
    "1678886780 WARNING Disk space low"
]

result = analyze_logs(log_example)
print(result)