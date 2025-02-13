"""
Format Converter

Features:
- Allows users to convert paragraphs into formatted comments suitable for various programming languages. It supports converting text to comments with symbols like #, //, --, etc.
- Additionally, the app features an 'EnMoji' function to encrypt and decrypt text using emojis.
- An easter egg feature inspired by the Matrix movie.

To use the app, simply paste or type your text into the input area, select the desired conversion option (comment conversion or emoji encryption/decryption), and click 'Convert'.
The output will be displayed in the output area, where it can be copied to the clipboard.

Test Paragraph:
---------------------------------------------
According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.

"""

from gui import FormatConverterGUI
import tkinter as tk

def main():
    """Initialize and run the Format Converter application."""
    root = tk.Tk()
    root.withdraw()  # Initially hide the window to avoid flickering during setup

    # Initialize the GUI with the root window
    gui = FormatConverterGUI(root)

    # Update idletasks to get accurate dimensions for window centering
    root.update_idletasks()

    # Calculate the center position of the screen
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    window_width, window_height = root.winfo_width(), root.winfo_height()
    center_x, center_y = int(screen_width / 2 - window_width / 2), int(screen_height / 2 - window_height / 2)

    # Set the position of the window to the center of the screen
    root.geometry(f'+{center_x}+{center_y}')

    # Display the window and start the application's main loop
    root.deiconify()  # Make the window visible
    root.mainloop()

if __name__ == '__main__':
    main()
