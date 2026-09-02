#!/bin/bash
# ==============================================================================
# Project Dynamo Golden Solution Script
# Description: Deterministic log extraction matching Project Dynamo standards.
# ==============================================================================

# Ensure the script exits immediately if any command fails
set -e

# Define path constants matching the task workspace
LOG_INPUT="mock_data.log"
LOG_OUTPUT="filtered_errors.txt"

# Verify input log availability
if [ ! -f "$LOG_INPUT" ]; then
    echo "Error: Input log file '$LOG_INPUT' not found." >&2
    exit 1
fi

echo "Starting deterministic log parsing workflow..."

# Extract ERROR and CRITICAL entries while maintaining original sequence
grep -E "ERROR|CRITICAL" "$LOG_INPUT" > "$LOG_OUTPUT" || true

echo "Workflow complete. Filtered results successfully saved to '$LOG_OUTPUT'."
