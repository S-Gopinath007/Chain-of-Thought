#!/usr/bin/env python3
"""Filter log file for CRITICAL and FATAL log levels."""

import sys


def filter_logs(
    input_path: str = "mock_data.log", output_path: str = "filtered_errors.txt"
) -> None:
    """Reads a log file and extracts lines starting with CRITICAL or FATAL.

    :param input_path: Path to the source log file.
    :param output_path: Path to the destination file.
    """
    target_prefixes = ("CRITICAL", "FATAL")

    try:
        with open(input_path, "r", encoding="utf-8") as infile, open(
            output_path, "w", encoding="utf-8"
        ) as outfile:

            matching_count = 0
            for line in infile:
                # Strip leading whitespace before checking the log level prefix
                if line.lstrip().startswith(target_prefixes):
                    outfile.write(line)
                    matching_count += 1

        print(
            f"Filtering complete. {matching_count} line(s) written to '{output_path}'."
        )

    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.", file=sys.stderr)
    except Exception as err:
        print(f"An unexpected error occurred: {err}", file=sys.stderr)


if __name__ == "__main__":
    filter_logs()