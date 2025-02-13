# Format Converter

Small Python-based GUI application that converts text into formatted comments for various programming languages and provides a fun emoji-based encryption/decryption feature called EnMoji.

## Features

- **Comment Conversion:**
    - Transforms paragraphs into properly formatted comments for different languages.
    - Supports comment symbols: #, //, --, %, ;, ' (Python, C, Java, SQL, MATLAB, Lisp, Visual Basic, etc.).
- **EnMoji:**
    - Encrypts text into emojis and decrypts it back to readable text.
    - Uses a predefined emoji mapping system for encoding and decoding.
- Hidden Easter Egg

## Technologies Used

- Backend:
    - Python
    - Custom encryption mapping (mapping.py)
- Frontend:
    - Tkinter for the GUI
    - ttk for styled widgets

## How to Use

- Simply paste or type your text into the input area.
- Choose your conversion option:
    - Comment style from the list
    - Or Emoji encryption/decryption
- Click **Convert**.
- View the output and copy it to the clipboard.

## Installation

1. Clone the repository:

```
git clone https://github.com/an-vu/formatconverter.git
cd format-converter
```

2. Run the program:
```
python main.py
```

## Test Paragraph

```
---------------------------------------------
According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.
```
