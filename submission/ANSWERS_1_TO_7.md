# Answers for Questions 1–7

## Question 1 — URL

https://github.com/phuvhgce181376-byte/oaqjp-final-project-emb-ai/blob/main/README.md

## Question 2 — TEXT

Copy all Python code from `2a_emotion_detection.txt` into the answer box.

## Question 3 — TEXT

Run `bash collect_evidence.sh` in the IBM course lab at
`/home/project/final_project`. Paste the complete contents of
`submission/2b_application_creation.txt` into the answer box.

This file is created only after the real service responds and the initial
import, application call, and smoke test complete successfully.

## Question 4 — TEXT

Copy all Python code from `3a_output_formatting.txt` into the answer box.

## Question 5 — TEXT

After collecting real evidence, paste the complete contents of
`submission/3b_formatted_output_test.txt` into the answer box.

## Question 6 — URL

https://github.com/phuvhgce181376-byte/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py

## Question 7 — TEXT

After collecting real evidence, paste the complete contents of
`submission/4b_packaging_test.txt` into the answer box.

The command imports directly from `EmotionDetection.emotion_detection` and
calls `emotion_detector('I am very angry')`. The output must contain the five
real scores and `'dominant_emotion': 'anger'`.

## Collecting evidence in the course lab

If `/home/project/final_project` does not exist yet:

```bash
cd /home/project
git clone https://github.com/phuvhgce181376-byte/oaqjp-final-project-emb-ai.git final_project
cd final_project
python3 -m pip install -r requirements.txt
bash collect_evidence.sh
```

If the lab already has this project, bring its files up to date with this
repository first, then run the last two commands from that project directory.
Do not overwrite any unrelated lab work.

The collection script temporarily uses the Task 2 and Task 3 versions of
`emotion_detection.py` and restores the packaged project on exit. The Task 2
test is a smoke test for the original raw response. The root
`test_emotion_detection.py` contains the five later integration tests.

No successful terminal output has been supplied or invented in advance.
