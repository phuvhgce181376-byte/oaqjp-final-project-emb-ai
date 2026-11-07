"""Detect and format emotions using the Watson NLP EmotionPredict service."""

import requests


def emotion_detector(text_to_analyze):
    """Return five emotion scores and the emotion with the highest score."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    emotions = response.json()["emotionPredictions"][0]["emotion"]
    result = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }
    result["dominant_emotion"] = max(result, key=result.get)
    return result
