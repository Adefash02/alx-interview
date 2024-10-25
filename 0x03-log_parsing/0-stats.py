#!/usr/bin/python3
import sys


def print_stats(total_size, status_counts):
    """Prints the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def process_line(line, total_size, status_counts):
    """Processes a single log line to extract file size and status code."""
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = parts[-2]

        total_size += file_size

        if status_code in status_counts:
            status_counts[status_code] += 1

    except (IndexError, ValueError):
        # Skip the line if it's not in the expected format
        pass

    return total_size


def main():
    """Main function that reads from stdin and computes metrics."""
    total_size = 0
    status_counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if line == "":
                continue

            total_size = process_line(line, total_size, status_counts)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Print the statistics when interrupted with CTRL + C
        print_stats(total_size, status_counts)
        raise

    # Print the final statistics at the end of the input
    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()

