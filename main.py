from PIL import Image
import pyfiglet as pf

# ASCII characters from dark to light (4 chars)
ASCII_CHARS = "*:. "
# Reset
RESET = "\x1b[0m"

# Styles
BOLD      = "\x1b[1m"
DIM       = "\x1b[2m"
UNDERLINE = "\x1b[4m"
BLINK     = "\x1b[5m"
REVERSE   = "\x1b[7m"
HIDDEN    = "\x1b[8m"

# Normal Colors
BLACK   = "\x1b[30m"
RED     = "\x1b[31m"
GREEN   = "\x1b[32m"
YELLOW  = "\x1b[33m"
BLUE    = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN    = "\x1b[36m"
WHITE   = "\x1b[37m"

# Bright Colors
BRIGHT_BLACK   = "\x1b[90m"
BRIGHT_RED     = "\x1b[91m"
BRIGHT_GREEN   = "\x1b[92m"
BRIGHT_YELLOW  = "\x1b[93m"
BRIGHT_BLUE    = "\x1b[94m"
BRIGHT_MAGENTA = "\x1b[95m"
BRIGHT_CYAN    = "\x1b[96m"
BRIGHT_WHITE   = "\x1b[97m"

# Background Colors
BG_BLACK   = "\x1b[40m"
BG_RED     = "\x1b[41m"
BG_GREEN   = "\x1b[42m"
BG_YELLOW  = "\x1b[43m"
BG_BLUE    = "\x1b[44m"
BG_MAGENTA = "\x1b[45m"
BG_CYAN    = "\x1b[46m"
BG_WHITE   = "\x1b[47m"

# Bright Background Colors
BG_BRIGHT_BLACK   = "\x1b[100m"
BG_BRIGHT_RED     = "\x1b[101m"
BG_BRIGHT_GREEN   = "\x1b[102m"
BG_BRIGHT_YELLOW  = "\x1b[103m"
BG_BRIGHT_BLUE    = "\x1b[104m"
BG_BRIGHT_MAGENTA = "\x1b[105m"
BG_BRIGHT_CYAN    = "\x1b[106m"
BG_BRIGHT_WHITE   = "\x1b[107m"

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)  # Adjust for font height
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_chars_length = len(ASCII_CHARS)
    chars = ""
    for pixel in pixels:
        # Scale pixel value to 0-(len(ASCII_CHARS)-1)
        index = pixel * (ascii_chars_length - 1) // 255
        chars += ASCII_CHARS[index]
    return chars

def image_to_ascii(path, new_width=100):
    try:
        image = Image.open(path)
    except Exception as e:
        return f"Unable to open image file: {e}"

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_img = "\n".join(ascii_str[i:i+img_width] for i in range(0, len(ascii_str), img_width))

    return ascii_img
def text_to_ascii(text,font):
    return pf.figlet_format(text,font=font)
def color_text(text, *styles):
    """
    Colorize text with given ANSI codes.
    Example:
        color_text("Hello", BRIGHT_RED, BOLD)
    """
    return "".join(styles) + text + RESET
