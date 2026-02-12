import subprocess
import os

def open_cava():
    terminal = os.environ.get("TERMINAL")

    if terminal:
        subprocess.Popen([terminal, "-e", "cava"])
    else:
        # Fallbacks (try in order)
        for term in ["gnome-terminal", "kitty", "alacritty", "konsole", "xterm"]:
            try:
                subprocess.Popen([term, "-e", "cava"])
                break
            except FileNotFoundError:
                continue

def open_vscode():
    subprocess.Popen(["code"])

def close_vscode():
    subprocess.Popen(["pkill", "code"])

def open_browser():
    subprocess.Popen(["chromium"])

def sleep():
    subprocess.Popen(["pkill", 'cava'])

def shutdown():
    subprocess.Popen(["shutdown", "now"])
