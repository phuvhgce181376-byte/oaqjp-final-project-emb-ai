# Final Project

## Emotion Detector

An AI application that detects emotions in English text using IBM Watson NLP.
It returns scores for **anger**, **disgust**, **fear**, **joy**, and **sadness**,
along with the **dominant_emotion** (the emotion with the highest score).

This repository currently covers Tasks 1–4 of the final project. The original
Flask UI starter files are retained for the later deployment task.

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

### Submission files

`submission/2a_emotion_detection.txt` preserves the original, unformatted
implementation. `submission/3a_output_formatting.txt` preserves the formatted
implementation used by the package. Terminal evidence is collected separately
by running `bash collect_evidence.sh` in the course lab at
`/home/project/final_project`.

Original starter repository:
https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai
