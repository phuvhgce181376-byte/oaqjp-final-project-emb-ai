"""Collect actual Pylint and Watson test output for Questions 9 and 16."""

import argparse
from pathlib import Path
import shlex
import subprocess
import sys


def collect(command, destination, required_text):
    """Save successful command output; keep failed output separate."""
    displayed_command = (
        subprocess.list2cmdline(command) if sys.platform == "win32" else shlex.join(command)
    )
    header = f"Working directory: {Path.cwd()}\nCommand: {displayed_command}\n\n"
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    transcript = header + result.stdout + result.stderr
    print(transcript, end="")
    success = result.returncode == 0 and required_text in transcript
    output = destination if success else destination.with_name(destination.stem + "_failed.txt")
    output.write_text(transcript, encoding="utf-8")
    print(f"Saved: {output}")
    return success


def main():
    """Run lint first, then integration tests when the service is reachable."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lint-only", action="store_true")
    args = parser.parse_args()
    project = Path(__file__).resolve().parent
    if Path.cwd() != project:
        parser.error("Run this script from the project directory.")
    submission = project / "submission"
    lint_passed = collect(
        [sys.executable, "-m", "pylint", "server.py"],
        submission / "8b_static_code_analysis.txt",
        "10.00/10",
    )
    if not lint_passed:
        return 1
    if args.lint_only:
        return 0

    print("Checking access to the real Watson service before integration tests...")
    preflight = subprocess.run(
        [sys.executable, "-c",
         "from EmotionDetection import emotion_detector; "
         "r = emotion_detector('I am really mad about this'); "
         "assert r['dominant_emotion'] == 'anger', r"],
        capture_output=True, text=True, check=False,
    )
    if preflight.returncode != 0:
        (submission / "5b_unit_testing_result_failed.txt").write_text(
            "Watson preflight failed; the five integration tests were not run.\n"
            + preflight.stdout + preflight.stderr,
            encoding="utf-8",
        )
        print("Watson is unavailable. Run this command in the IBM course lab.")
        return 1

    return 0 if collect(
        [sys.executable, "test_emotion_detection.py", "-v"],
        submission / "5b_unit_testing_result.txt",
        "\nOK\n",
    ) else 1


if __name__ == "__main__":
    sys.exit(main())
