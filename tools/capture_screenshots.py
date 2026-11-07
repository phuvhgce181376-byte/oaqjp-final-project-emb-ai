"""Capture the actual Flask UI; never substitute scores or intercept requests."""

import argparse
from pathlib import Path

from playwright.sync_api import expect, sync_playwright


def main():
    """Capture blank-input validation, then attempt real emotion detection."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default="http://127.0.0.1:5000")
    parser.add_argument("--error-only", action="store_true")
    args = parser.parse_args()
    submission = Path(__file__).resolve().parents[1] / "submission"
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 820}, device_scale_factor=1)
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        response = page.goto(args.base_url, wait_until="networkidle")
        assert response.status == 200, response.status
        page.locator("#textToAnalyze").fill("")
        page.get_by_role("button", name="Run Emotion Analysis").click()
        expect(page.locator("#system_response")).to_have_text(
            "Invalid text! Please try again!"
        )
        assert not errors, errors
        error_image = submission / "7c_error_handling_interface.png"
        page.screenshot(path=str(error_image), full_page=True)
        print(f"Saved actual blank-input UI screenshot: {error_image}")

        if not args.error_only:
            page.locator("#textToAnalyze").fill("I am glad this happened")
            with page.expect_response(
                lambda response: "/emotionDetector?" in response.url,
                timeout=90000,
            ) as response_info:
                page.get_by_role("button", name="Run Emotion Analysis").click()
            result = response_info.value
            expect(page.get_by_role("button", name="Run Emotion Analysis")).to_be_enabled()
            text = page.locator("#system_response").inner_text()
            if result.status != 200 or "The dominant emotion is joy." not in text:
                print(f"Deployment success screenshot not created: HTTP {result.status}; {text}")
                browser.close()
                return 1
            for emotion in ("anger", "disgust", "fear", "joy", "sadness"):
                assert f"'{emotion}':" in text, text
            assert not errors, errors
            image = submission / "6b_deployment_test.png"
            page.screenshot(path=str(image), full_page=True)
            print(f"Saved actual Watson deployment result: {image}")
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
