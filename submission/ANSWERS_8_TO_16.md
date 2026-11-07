# Answers for Questions 8–16

| Question | Submission |
| --- | --- |
| 8 | Copy all code from `5a_unit_testing.txt`. |
| 9 | Paste the actual successful output in `5b_unit_testing_result.txt`, after collecting it in the IBM lab. |
| 10 | Copy all code from `6a_server.txt`. |
| 11 | Upload `6b_deployment_test.png` after a real successful Watson result. |
| 12 | Copy all code from `7a_error_handling_function.txt`. |
| 13 | Copy all code from `7b_error_handling_server.txt`. |
| 14 | Upload `7c_error_handling_interface.png`. |
| 15 | Copy all code from `8a_server_modified.txt`. |
| 16 | Paste all text from `8b_static_code_analysis.txt`. |

## Collect the remaining unit-test evidence

In the IBM course lab, with the latest repository files in
`/home/project/final_project`, run:

```bash
cd /home/project/final_project
python3 -m pip install -r requirements-dev.txt
python3 collect_remaining_evidence.py
```

This writes Pylint evidence and, only if the real Watson service is reachable
and all five emotion tests pass, the unit-test evidence for Question 9.
The extra tests in `tests/test_error_handling.py` use mocks to check error
handling offline. They are separate from the five real emotion tests and
their output is not used as the Question 9 submission.

## Capture the successful deployment screenshot

In one lab terminal:

```bash
python3 server.py
```

Open the lab's application preview on port **5000**. Enter
`I am glad this happened`, click **Run Emotion Analysis**, and confirm that
the result includes all five emotion scores and the dominant emotion **joy**.
Capture the input and result together as **6b_deployment_test.png**.

For error validation, clear the input and click the button. Capture the empty
input and **Invalid text! Please try again!** as
**7c_error_handling_interface.png**. A screenshot of that actual interaction
can also be captured locally, without needing the Watson service.

An optional Playwright helper is provided in `tools/capture_screenshots.py`.
It requires Playwright and an installed Chromium browser; it connects to a
running Flask server and saves successful real UI states only.

The code snapshots preserve the assignment stages: `6a_server.txt` is the
initial Flask deployment; `7b_error_handling_server.txt` and
`8a_server_modified.txt` contain the final documented server with input and
service error handling.
