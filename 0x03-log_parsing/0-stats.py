#!/usr/bin/python3
import sys
import signal

# Dictionary to hold the count of each status code
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0

def print_stats():
    """
    Function to print the accumulated metrics:
    Total file size and count of status codes.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def parse_line(line):
    """
    Parse a single line and update the total file size and status code count.
    """
    global total_size
    try:
        # Splitting the line to extract necessary components
        parts = line.split()
        if len(parts) < 9:
            return
        # Extracting file size and status code
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        
        # Update total file size
        total_size += file_size

        # Update status code count if it's a valid code
        if status_code in status_codes:
            status_codes[status_code] += 1
    except Exception:
        pass

def signal_handler(sig, frame):
    """
    Signal handler to print stats on keyboard interruption (CTRL + C)
    """
    print_stats()
    sys.exit(0)

# Registering signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read from standard input (stdin)
for line in sys.stdin:
    parse_line(line)
    line_count += 1

    # Print stats every 10 lines
    if line_count % 10 == 0:
        print_stats()

# If EOF is reached, print stats
print_stats()

