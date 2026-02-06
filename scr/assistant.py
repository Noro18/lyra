from wakeword import wait_for_wakeword
from audio import record, transcribe
from commands import open_cava, open_vscode, open_browser, shutdown
from config import COMMAND_DURATION
from test import    echo_said
def start(debug=False):
    print("🎧 Lyra is running. Say 'Lyra' to activate.")

    while True:
        if echo_said():
            print("✨ Lyra activated")
            open_cava()

            while True:
                audio = record(COMMAND_DURATION)
                command = transcribe(audio)

                if debug and command:
                    print(f"[DEBUG] Command heard: {command}")

                if not command:
                    continue

                if "vscode" in command:
                    open_vscode()

                elif "browser" in command:
                    open_browser()

                elif "shutdown" in command:
                    shutdown()

                elif "stop lyra" in command or "lyra stop" in command:
                    print("🛑 Lyra stopped")
                    return

                else:
                    print("🤔 Unknown command")
