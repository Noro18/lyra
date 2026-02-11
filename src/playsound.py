import subprocess

def play_prompting_sound():
    # Non-blocking, simple Linux approach
    subprocess.run(["aplay", "/home/noro18/Documents/Project/LYRA/pre-recorded audio/prompt.wav"])  # replace with your file path
def play_activation_sound():
    # Non-blocking, simple Linux approach
    subprocess.run(["aplay", "/home/noro18/Documents/Project/LYRA/pre-recorded audio/on.wav"])  # replace with your file path

def play_hello():
    subprocess.run(["aplay", "/home/noro18/Documents/Project/LYRA/pre-recorded audio/hello.wav"])

def play_vscode_sound():
    subprocess.run(["aplay", "/home/noro18/Documents/Project/LYRA/pre-recorded audio/vscode.wav"])

def play_shutdown_sound():
    subprocess.run(["aplay", "/home/noro18/Documents/Project/LYRA/pre-recorded audio/shutdown.wav"])