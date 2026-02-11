import sounddevice as sd
import numpy as np
import speech_recognition as sr
from src.config import SAMPLE_RATE, CHANNELS, SAMPLE_WIDTH

recognizer = sr.Recognizer()

def record(seconds: int) -> sr.AudioData:
    audio_np = sd.rec(
        int(seconds * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16"
    )
    sd.wait()

    return sr.AudioData(
        audio_np.tobytes(),
        SAMPLE_RATE,
        SAMPLE_WIDTH
    )

def transcribe(audio: sr.AudioData) -> str:
    try:
        return recognizer.recognize_google(audio) # uses google to transcribe
    except Exception:
        return ""
