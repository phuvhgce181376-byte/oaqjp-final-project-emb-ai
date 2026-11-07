#!/usr/bin/env bash
# Run in the IBM course lab. Each file contains actual executed commands/results.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
if [[ "$PWD" != /home/project/final_project ]]; then
    echo "Run this script from the course repository at /home/project/final_project." >&2
    exit 1
fi

python3 -c 'import requests'
mkdir -p submission
backup_dir=$(mktemp -d)
cp emotion_detection.py "$backup_dir/emotion_detection.py"
cp test_emotion_detection.py "$backup_dir/test_emotion_detection.py"
restore_files() {
    cp "$backup_dir/emotion_detection.py" emotion_detection.py
    cp "$backup_dir/test_emotion_detection.py" test_emotion_detection.py
}
trap restore_files EXIT

# First confirm that the real service is reachable. Never create fake evidence.
echo "Checking the Watson service before collecting submission evidence..."
python3 - <<'PY'
from EmotionDetection.emotion_detection import emotion_detector
result = emotion_detector('I am very angry')
assert result['dominant_emotion'] == 'anger', result
assert set(result) == {'anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion'}
print('Watson service is reachable; packaging and output format checks passed.')
PY

cp submission/2a_emotion_detection.txt emotion_detection.py
cp submission/raw_smoke_test.txt test_emotion_detection.py
if (
    export PS4='+ ${PWD}$ '
    set -x
    python3 -i <<'PY'
from emotion_detection import emotion_detector
print(emotion_detector('I am really mad about this'))
exit()
PY
    python3 test_emotion_detection.py
) 2>&1 | tee submission/2b_application_creation.pending; then
    if ! grep -q 'Traceback' submission/2b_application_creation.pending; then
        mv submission/2b_application_creation.pending submission/2b_application_creation.txt
    else
        mv submission/2b_application_creation.pending submission/2b_application_creation_failed.txt
        exit 1
    fi
else
    mv submission/2b_application_creation.pending submission/2b_application_creation_failed.txt
    exit 1
fi

cp submission/3a_output_formatting.txt emotion_detection.py
if (
    export PS4='+ ${PWD}$ '
    set -x
    python3 -i <<'PY'
from emotion_detection import emotion_detector
print(emotion_detector('I am really mad about this'))
exit()
PY
) 2>&1 | tee submission/3b_formatted_output_test.pending; then
    if ! grep -q 'Traceback' submission/3b_formatted_output_test.pending; then
        mv submission/3b_formatted_output_test.pending submission/3b_formatted_output_test.txt
    else
        mv submission/3b_formatted_output_test.pending submission/3b_formatted_output_test_failed.txt
        exit 1
    fi
else
    mv submission/3b_formatted_output_test.pending submission/3b_formatted_output_test_failed.txt
    exit 1
fi

restore_files
if (
    export PS4='+ ${PWD}$ '
    set -x
    python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
) 2>&1 | tee submission/4b_packaging_test.pending; then
    mv submission/4b_packaging_test.pending submission/4b_packaging_test.txt
else
    mv submission/4b_packaging_test.pending submission/4b_packaging_test_failed.txt
    exit 1
fi

echo "Evidence collected. Paste the contents of the three .txt files into Questions 3, 5 and 7."
