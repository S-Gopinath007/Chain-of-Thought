# Task Specification: Log Analysis Pipeline

## Objective
Analyze a system log file to filter and extract critical errors for further engineering triage. You must extract all logs matching specific severity thresholds without modifying the baseline structure.

## Working Directory
`/workspace`

## Input Files
*   `mock_data.log`: Raw system text logs containing mixed log levels (`INFO`, `DEBUG`, `WARN`, `ERROR`, `CRITICAL`).

## Required Output
*   `filtered_errors.txt`: A clean text file containing only the extracted lines that meet the criteria.

## Constraints & Rules
*   Do **NOT** alter the timestamps or the sequence of the logs.
*   Filter exclusively for lines containing `ERROR` or `CRITICAL`.
*   The execution must be fully automated, deterministic, and non-interactive.
