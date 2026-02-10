from audio import record, transcribe 
from config import WAKE_WORD, WAKE_DURATION
def echo_said(duration=2.9):
    print(f"🎧 Recording for {duration} seconds...")
    audio = record(duration)
    
    print("📝 Transcribing...")
    text = transcribe(audio)
    if text:
        print(f"🗣️ You said: {text}")
    else:
        print("❌ Could not transcribe audio.")
    print("the text is:", text.lower())

    # Check if text is not empty AND contains wake word
    result = text and WAKE_WORD.lower() in text.lower()
    print(result)
    return result
    