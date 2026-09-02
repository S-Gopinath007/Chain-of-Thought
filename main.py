import os
import re
import subprocess
import sys

from google import genai
from google.genai import types

from environment import setup_sandbox
from prompts import SYSTEM_INSTRUCTION, TASK_QUERY


def run_agent_inference(api_key, system_prompt, query_prompt, feedback_history):
    client = genai.Client(api_key=api_key)

    contents = [query_prompt]
    if feedback_history:
        contents.append(
            "\n\n=== PREVIOUS ERRORS AND FEEDBACK ===\n"
            + "\n".join(feedback_history)
        )

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL", "gemini-2.0-flash"),
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.1,
        ),
    )

    return response.text or ""


def parse_generated_code(response_text):
    match = re.search(
        r"```(?:python|py)\s*(.*?)```",
        response_text,
        re.DOTALL | re.IGNORECASE,
    )
    return match.group(1).strip() if match else None


def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY is not set.", file=sys.stderr)
        sys.exit(1)

    setup_sandbox()

    max_attempts = 3
    feedback_history = []
    solution_path = "agent_solution.py"

    final_response = ""
    final_verification = ""
    verified = False

    for attempt in range(1, max_attempts + 1):
        print(f"Running agent optimization iteration: {attempt}/{max_attempts}...")

        final_response = run_agent_inference(
            api_key,
            SYSTEM_INSTRUCTION,
            TASK_QUERY,
            feedback_history,
        )

        extracted_code = parse_generated_code(final_response)
        if not extracted_code:
            feedback_history.append(
                "FAULT: Return the Python script inside a ```python ... ``` block."
            )
            continue

        with open(solution_path, "w", encoding="utf-8") as file:
            file.write(extracted_code)

        python_cmd = sys.executable

        runtime = subprocess.run(
            [python_cmd, solution_path],
            capture_output=True,
            text=True,
            timeout=120,
        )

        verification = subprocess.run(
            [python_cmd, "eval.py"],
            capture_output=True,
            text=True,
            timeout=120,
        )

        final_verification = (
            verification.stdout.strip() or verification.stderr.strip()
        )

        if verification.returncode == 0:
            verified = True
            break

        feedback_history.append(
            f"ATTEMPT {attempt} FAILED:\n"
            f"Validation output:\n{final_verification}\n"
            f"Runtime output:\n{runtime.stderr.strip()}"
        )

    print("\n" + "=" * 60)
    print("FINAL VERIFIED RESULT" if verified else "FINAL ATTEMPT RESULT")
    print("=" * 60)
    print(final_response)
    print("\nVERIFICATION RESULT:")
    print(final_verification)


if __name__ == "__main__":
    main()