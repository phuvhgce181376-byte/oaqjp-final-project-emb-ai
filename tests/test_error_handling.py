"""Offline checks of error handling; separate from Watson integration evidence."""

import unittest
from unittest.mock import Mock, patch

from requests.exceptions import ConnectionError as RequestsConnectionError

from EmotionDetection.emotion_detection import emotion_detector
from server import app


class TestDetectorErrors(unittest.TestCase):
    """Check that invalid input is handled before parsing a response body."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400_returns_all_none(self, post):
        """An upstream 400 must not attempt to parse a non-JSON error body."""
        response = Mock(status_code=400)
        post.return_value = response
        result = emotion_detector("text rejected by the service")
        self.assertEqual(
            set(result), {"anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"}
        )
        self.assertTrue(all(value is None for value in result.values()))
        response.json.assert_not_called()
        response.raise_for_status.assert_not_called()

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_empty_input_does_not_call_service(self, post):
        """Empty, missing and whitespace-only input require no network call."""
        for text in (None, "", "  \t\n"):
            with self.subTest(text=text):
                self.assertIsNone(emotion_detector(text)["dominant_emotion"])
        post.assert_not_called()


class TestFlaskErrors(unittest.TestCase):
    """Exercise HTTP responses with Flask's test client."""

    @patch("server.emotion_detector")
    def test_blank_input(self, detector):
        """The UI endpoint rejects missing, empty and whitespace input."""
        with app.test_client() as client:
            for query in ({}, {"textToAnalyze": ""}, {"textToAnalyze": "  \t"}):
                with self.subTest(query=query):
                    response = client.get("/emotionDetector", query_string=query)
                    self.assertEqual(response.status_code, 200)
                    self.assertEqual(response.get_data(as_text=True),
                                     "Invalid text! Please try again!")
        detector.assert_not_called()

    @patch("server.emotion_detector", return_value={"dominant_emotion": None})
    def test_upstream_invalid_input(self, detector):
        """A rejected service input displays the required error message."""
        with app.test_client() as client:
            response = client.get("/emotionDetector", query_string={"textToAnalyze": "hello"})
        self.assertEqual(response.get_data(as_text=True), "Invalid text! Please try again!")
        detector.assert_called_once_with("hello")

    @patch("server.emotion_detector", side_effect=RequestsConnectionError("offline"))
    def test_service_outage(self, _detector):
        """A service outage returns 503 instead of an input validation error."""
        with app.test_client() as client:
            response = client.get("/emotionDetector", query_string={"textToAnalyze": "hello"})
        self.assertEqual(response.status_code, 503)
        self.assertIn("service is unavailable", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
