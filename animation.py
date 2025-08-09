import os
import time
import pyfiglet

# ANSI escape color codes
COLORS = [
    "\x1b[91m",  # Red
    "\x1b[93m",  # Yellow
    "\x1b[92m",  # Green
    "\x1b[96m",  # Aqua
    "\x1b[94m",  # Blue
    "\x1b[95m",  # Purple
]

RESET = "\x1b[0m"

def animate_pyfiglet(text, font="slant", delay=0.2, repeat=3):
    figlet = pyfiglet.Figlet(font=font)
    ascii_text = figlet.renderText(text)

    for _ in range(repeat):
        for color in COLORS:
            os.system("cls" if os.name == "nt" else "clear")
            print(color + ascii_text + RESET)
            time.sleep(delay)

if __name__ == "__main__":
    animate_pyfiglet("ASCII-Lib", font="standard", delay=0.15, repeat=5)
