#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    """Print the current statistics"""
    print("File size: {}".format(total_size))
    for status in sorted(status_count.keys()):
        if status_count[status] > 0:
            print("{}: {}".format(status, status_count[status]))

def signal_handler(sig, frame):
    """Handle keyboard interruption"""
    print_stats()
    sys.exit(0)

# Set up signal handling for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()

        # Skip lines that do not match the required format
        if len(parts) < 7 or parts[5] != "\"GET" or parts[6] != "/projects/260" or parts[7] != "HTTP/1.1\"":
            continue

        # Extract file size and status code
        try:
            status_code = parts[-2]
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue

        # Update total file size
        total_size += file_size

        # Update status count
        if status_code in status_count:
            status_count[status_code] += 1

        # Increment line count and check if we need to print stats
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Print stats at the end if the loop ends naturally
print_stats()
