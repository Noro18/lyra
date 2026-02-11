from src.audio import record, transcribe
from src.config import WAKE_WORD, WAKE_DURATION

def wait_for_wakeword(debug=False) -> bool:
    audio = record(WAKE_DURATION)
    text = transcribe(audio)

    if debug and text:
        print(f"[DEBUG] Wake heard: {text}")

    return WAKE_WORD in text
