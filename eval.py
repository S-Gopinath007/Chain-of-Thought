import os
import sys

def verify_output():
    target_path = "filtered_errors.txt"

    if not os.path.exists(target_path):
        print("FAIL: Target output file `filtered_errors.txt` was not generated.")
        sys.exit(1)

    with open(target_path, "r") as f:
        content = f.read().splitlines()

    expected_matches = [
        "CRITICAL: Database connection lost",
        "FATAL: Memory corruption at segment 0x4F"
    ]

    if content != expected_matches:
        print(f"FAIL: Data mismatch.\nExpected: {expected_matches}\nGot: {content}")
        sys.exit(2)

    print("SUCCESS: The generated code satisfies all grading criteria.")
    sys.exit(0)

if __name__ == "__main__":
    verify_output()
