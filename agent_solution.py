def filter_critical_fatal_logs(
    input_filepath: str = "mock_data.log",
    output_filepath: str = "filtered_errors.txt",
) -> None:
    """Reads a log file and extracts lines starting with CRITICAL or FATAL.

    Args:
        input_filepath (str): Path to the source log file.
        output_filepath (str): Path to save filtered log lines.
    """
    target_prefixes = ("CRITICAL", "FATAL")

    with (
        open(input_filepath, "r", encoding="utf-8") as infile,
        open(output_filepath, "w", encoding="utf-8") as outfile,
    ):
        for line in infile:
            if line.startswith(target_prefixes):
                outfile.write(line)


if __name__ == "__main__":
    filter_critical_fatal_logs()