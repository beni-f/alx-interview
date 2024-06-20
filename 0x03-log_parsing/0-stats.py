#!/usr/bin/python3
import sys
import signal
import re

# Initialize metrics
total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression to match the input format
log_pattern = re.compile(r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

def print_statistics():
    """ Print the statistics collected so far """
    global total_size, status_count
    print(f"File size: {total_size}")
    for status in sorted(status_count.keys()):
        if status_count[status] > 0:
            print(f"{status}: {status_count[status]}")

def signal_handler(sig, frame):
    """ Signal handler for SIGINT (CTRL + C) """
    print_statistics()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            # Update metrics
            total_size += file_size
            if status_code in status_count:
                status_count[status_code] += 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
finally:
    # Print final statistics upon termination
    print_statistics()
