from audio import record, transcribe 
from config import WAKE_WORD, WAKE_DURATION
def echo_said(duration=4, samplerate=16000):
    print(f"🎧 Recording for {duration} seconds...")
    audio = record(duration)
    
    print("📝 Transcribing...")
    text = transcribe(audio)
    if text:
        print(f"🗣️ You said: {text}")
    else:
        print("❌ Could not transcribe audio.")
    

    
    return text.lower() in WAKE_WORD