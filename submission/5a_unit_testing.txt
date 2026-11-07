"""Integration tests against the real Watson NLP service."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Check dominant emotions for the five course examples."""

    def test_joy(self):
        """A positive statement has joy as its dominant emotion."""
        self.assertEqual(
            emotion_detector("I am glad this happened")["dominant_emotion"], "joy"
        )

    def test_anger(self):
        """An angry statement has anger as its dominant emotion."""
        self.assertEqual(
            emotion_detector("I am really mad about this")["dominant_emotion"], "anger"
        )

    def test_disgust(self):
        """A disgusted statement has disgust as its dominant emotion."""
        self.assertEqual(
            emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"],
            "disgust",
        )

    def test_sadness(self):
        """A sad statement has sadness as its dominant emotion."""
        self.assertEqual(
            emotion_detector("I am so sad about this")["dominant_emotion"], "sadness"
        )

    def test_fear(self):
        """A fearful statement has fear as its dominant emotion."""
        self.assertEqual(
            emotion_detector("I am really afraid that this will happen")["dominant_emotion"],
            "fear",
        )


if __name__ == "__main__":
    unittest.main()
