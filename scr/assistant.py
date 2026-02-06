from wakeword import wait_for_wakeword
from audio import record, transcribe
from commands import open_cava, open_vscode, open_browser, shutdown
from config import COMMAND_DURATION
from test import echo_said  # assuming you still want to use this
import subprocess

# ---- Play activation sound ----
def play_activation_sound():
    # Non-blocking, simple Linux approach
    subprocess.run(["aplay", "/home/noro18/Documents/Project/LYRA/pre-recorded audio/on.wav"])  # replace with your file path

def play_hello():
    subprocess.run(["aplay", "/home/noro18/Documents/Project/LYRA/pre-recorded audio/hello.wav"])

def start(debug=False):
    print("🎧 Lyra is running. Say 'Lyra' to activate.")

    active = False  # state flag

    while True:
        # --------------------
        # WAIT FOR WAKE WORD
        # --------------------
        if not active:
            if echo_said():  # or use wait_for_wakeword()
                active = True
                print("✨ Lyra activated")
                open_cava()
                play_activation_sound()  # only plays ONCE per activation
                play_hello()
            continue

        # --------------------
        # COMMAND LOOP
        # --------------------
        audio = record(COMMAND_DURATION)
        command = transcribe(audio)

        if debug:
            print(f"[DEBUG] Command heard: {command}")

        if not command:
            continue

        # --------------------
        # HANDLE COMMANDS
        # --------------------
        if "vscode" in command:
            open_vscode()

        elif "browser" in command:
            open_browser()

        elif "shutdown" in command:
            shutdown()

        elif "stop lyra" in command or "lyra stop" in command:
            print("🛑 Lyra stopped")
            active = False  # reset state, back to waiting for wake word

        else:
            print("🤔 Unknown command")
