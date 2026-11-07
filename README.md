# Final Project

## Emotion Detector

An AI application that detects emotions in English text using IBM Watson NLP.
It returns scores for **anger**, **disgust**, **fear**, **joy**, and **sadness**,
along with the **dominant_emotion** (the emotion with the highest score).

This repository implements Tasks 1–8 of the final project, including Flask
deployment, HTTP 400 and blank-input handling, unit tests, and static analysis.

### Setup

```bash
python3 -m pip install -r requirements.txt
```

### Use the package

```python
from EmotionDetection.emotion_detection import emotion_detector

print(emotion_detector('I am very angry'))
```

### Integration tests

```bash
python3 test_emotion_detection.py
```

The detector and these tests call the actual Watson NLP service. They require
network access to the Skills Network course endpoint; no scores are simulated.

### Flask application

```bash
python3 server.py
```

Open `http://localhost:5000` or the IBM lab's application preview for port 5000.
Blank input displays `Invalid text! Please try again!`. A Watson HTTP 400
returns all six dictionary values as `None`. A service connection failure
returns HTTP 503 and a service-unavailable message.

### Static analysis and offline error checks

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pylint server.py
python3 -m unittest discover -s tests -v
```

The offline checks use mocks for error cases. They do not replace or claim
successful Watson emotion predictions.

### Submission files

`submission/2a_emotion_detection.txt` preserves the original, unformatted
implementation. `submission/3a_output_formatting.txt` preserves the formatted
implementation used by the package. Terminal evidence is collected separately
by running `bash collect_evidence.sh` in the course lab at
`/home/project/final_project`.

See `submission/ANSWERS_1_TO_7.md` and `submission/ANSWERS_8_TO_16.md` for
the exact question-to-file mapping. Run `python3 collect_remaining_evidence.py`
to collect actual Pylint and integration-test evidence for Questions 9 and 16.

Original starter repository:
https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai
