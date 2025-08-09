# 🔠 ASCII-Lib

A lightweight Python library for creating **ASCII art** from text and images.  
Perfect for making your terminal output stylish with banners, images-to-ASCII conversions, colors, and even animations!  

> **The best thing?** It supports **colored and animated ASCII art**, something many other ASCII libs don’t! 🚀

---

## 🚀 Features

- Convert text to ASCII art using **pyfiglet** fonts  
- Convert images to ASCII (with optional color support)  
- Animate ASCII art with custom speeds and loops  
- Built-in **color functions** for text styling  
- Works cross-platform on most terminals  
- Pure Python — no heavy dependencies (only Pillow + pyfiglet)

---

## 📸 Usage Guide
| class            | description                 | arg 1                              | other args                                                                                      |
|------------------|-----------------------------|------------------------------------|-------------------------------------------------------------------------------------------------|
| color_text       | add colors & style to text  | text: *the text you want to color* | - `*`styles: *the styles like RED,BG_BRIGHT_GREEN,BOLD                                          |
| animate_pyfiglet | animate ascii art           | text: *the text*                   | - font: *the font* - delay *the delay of animation* - repeat *times the animation will be tick* |
| text_to_ascii    | make text to ascii          | text: *the text*                   | - font: *the font*                                                                              |
| image_to_ascii   | convert images to ascii art | path: *the path of the image*      | - ascii_chars: *chars used in the art* - new_width: *the new width of the ascii image*          |

``python
from ascii_lib import *
print(color_text(text_to_ascii('hello world','slant'),RED,BOLD,BG_WHITE)) #colored Ascii
print(image_to_ascii('ok.jpg',80)) #image to ascii
```

## 📦 Installation

```bash
git clone https://github.com/Exoo25/ascii-lib/
cd ascii-lib
pip install .
```

## ⚠️ Important

> For best results, use terminals that support ANSI escape codes & UTF-8.
> Some terminals may show approximate colors or break formatting if unsupported.
