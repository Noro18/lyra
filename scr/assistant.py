from wakeword import wait_for_wakeword
from audio import record, transcribe
from commands import open_cava, open_vscode, open_browser, shutdown, close_vscode
from config import COMMAND_DURATION
from test import echo_said  # assuming you still want to use this
import subprocess
from playsound import play_activation_sound, play_hello, play_prompting_sound, play_vscode_sound, play_shutdown_sound
# ---- Play activation sound ----


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
        print(f"Command: {command}")
        if debug:
            print(f"[DEBUG] Command heard: {command}")

        if not command:
            continue

        # --------------------
        # HANDLE COMMANDS
        # --------------------
        if ("vscode" in command or "code" in command or "visual studio" in command) and 'open' in command:           
            play_vscode_sound()
            open_vscode()
        if ("vscode" in command or "code" in command or "visual studio" in command) and 'close' in command:           
            play_vscode_sound()
            close_vscode()
        elif "browser" in command:
            open_browser()

        elif "shutdown" in command or "shut down" in command or "power off" in command: 
            play_shutdown_sound()
            shutdown()

        elif "stop lyra" in command or "lyra stop" in command:
            print("🛑 Lyra stopped")
            active = False  # reset state, back to waiting for wake word

        else:
            print("🤔 Unknown command")

        play_prompting_sound()  # play prompting sound after each command
