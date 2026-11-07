"use strict";

async function runEmotionAnalysis(event) {
    event.preventDefault();
    const button = document.getElementById("analyze-button");
    const result = document.getElementById("system_response");
    const text = document.getElementById("textToAnalyze").value;
    const params = new URLSearchParams({ textToAnalyze: text });

    button.disabled = true;
    result.textContent = "Analyzing...";
    try {
        const response = await fetch(`/emotionDetector?${params.toString()}`);
        result.textContent = await response.text();
    } catch {
        result.textContent = "Unable to connect to the application. Please try again.";
    } finally {
        button.disabled = false;
    }
}

document.getElementById("emotion-form").addEventListener("submit", runEmotionAnalysis);
