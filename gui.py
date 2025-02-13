import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from converter import TextConverter
from converter import EasterEgg

class FormatConverterGUI:
    def __init__(self, master):
        self.master = master
        self.configure_style()
        self.setup_gui()

    def configure_style(self):
        """
        Configure the style for ttk widgets using the 'clam' theme.
        
        Set the background color for the TFrame and TRadiobutton widgets,
        and the background and foreground colors for the TButton widgets.
        """
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use a theme that allows custom styling
        
        # Configure styles for ttk widgets
        self.style.configure('TFrame', background='#f6f6df')
        self.style.configure('TRadiobutton', background='#f6f6df', foreground='#000000')
        self.style.configure('TButton', background='#fafaef', foreground='#000000')

    def setup_gui(self):
        """
        Set up the GUI by configuring the window and creating various GUI components.
        This includes the input area, convert button, output area, copy button, grid weights, radio buttons, and the 'Take the Red Pill' button.
        """
        self.configure_window()
        self.create_input_area()
        self.create_convert_button()
        self.create_output_area()
        self.create_copy_button()
        self.configure_grid_weights()
        self.create_radio_buttons()
        self.create_red_pill_button() # Easter egg

    def configure_window(self):
        """
        Configure the main application window by setting the title, geometry, padding, and background color.
        """
        self.master.title("Format Converter")
        self.master.geometry("900x900")
        self.master['padx'] = 15
        self.master['pady'] = 15
        self.master.configure(bg='#f6f6df')  # Updated to uniform background color

    def configure_grid_weights(self):
        """
        Configure the weights for grid rows and columns in the main window.
        This ensures that certain parts of the GUI will expand proportionally when the window is resized.
        """
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(4, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=0)

    def create_input_area(self):
        """
        Create the input text area within the main window.

        This method initializes a label and a text widget where the user can enter their paragraph.
        The text widget is configured with specific background and foreground colors,
        word wrapping, font settings, and grid positioning.
        """
        label = tk.Label(self.master, text="Enter your paragraph:", bg='#f5f5dc', fg='#000000')
        label.grid(row=0, column=0, pady=10, padx=10, sticky='w')
        self.input_text = tk.Text(self.master, wrap='word', height=10, bg='#232323', fg='#00ff00', 
                                  font=("Courier", 12))
        self.input_text.grid(row=1, column=0, pady=10, padx=10, sticky='nsew')

    def create_output_area(self):
        """
        Create the output text area within the main window.

        This method initializes a label and a text widget for displaying the converted text.
        The text widget is configured to be read-only with specific background and foreground colors,
        word wrapping, font settings, and grid positioning. It spans two columns to make full use of the window width.
        """
        label = tk.Label(self.master, text="Converted Text:", bg='#f5f5dc', fg='#000000')
        label.grid(row=3, column=0, pady=10, padx=10, sticky='w')
        self.output_text = tk.Text(self.master, wrap='word', height=10, state='disabled', bg='#232323', fg='#00ff00', 
                                   font=("Courier", 15))
        self.output_text.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

    def create_convert_button(self):
        """
        Create the 'Convert' button within the main window.

        This method initializes a button widget labeled 'Convert' and assigns the on_convert method as its command.
        The button is placed on the grid with specific padding.
        """
        convert_button = ttk.Button(self.master, text="Convert", command=self.on_convert)
        convert_button.grid(row=2, column=0, pady=20, padx=10)

    def on_convert(self):
        """
        Handle the conversion process when the 'Convert' button is clicked.

        This method retrieves the input data from the input text widget, determines the selected conversion option,
        and then calls the appropriate conversion function from the TextConverter class. It updates the output text widget
        with the conversion results or displays an error message if no input data is provided or no valid option is selected.
        """
        input_data = self.input_text.get("1.0", tk.END).strip()
        if not input_data:
            messagebox.showerror("Error", "There is nothing to convert.")
            return

        selected_option = self.selected_option.get()

        # Handling different conversion options
        if selected_option.startswith("comment"):
            selected_comment_symbol = selected_option.replace("comment", "")
            cleaned_data = TextConverter.cleanup_input(input_data.split('\n'))
            converted_data = TextConverter.format_converter(cleaned_data, selected_comment_symbol)
        elif selected_option == "emojiEncrypt":
            converted_data = TextConverter.encrypt_to_emoji(input_data)
        elif selected_option == "emojiDecrypt":
            converted_data = TextConverter.decrypt_from_emoji(input_data)
        else:
            messagebox.showerror("Error", "No valid conversion option selected.")
            return

        # Display the result in the output text area
        self.output_text.configure(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, converted_data)
        self.output_text.configure(state='disabled')

    def create_copy_button(self):
        """
        Create the 'Copy to Clipboard' button within the main window.

        This method initializes a button widget labeled 'Copy to Clipboard' and assigns the copy_to_clipboard method as its command.
        The button spans two columns and is placed on the grid with specific padding to align with the other widgets.
        """
        copy_button = ttk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

    def copy_to_clipboard(self):
        """
        Copy the content of the output text widget to the system clipboard.
        
        This method is called when the 'Copy to Clipboard' button is clicked. It retrieves the text from the output
        text widget, clears the current content of the system clipboard, appends the text to the clipboard, and 
        then notifies the user that the operation was successful.
        """
        result = self.output_text.get("1.0", tk.END).strip()
        self.master.clipboard_clear()
        self.master.clipboard_append(result)
        messagebox.showinfo("Info", "Text copied to clipboard!")

    def create_radio_buttons(self):
        """
        Create radio buttons for comment type and EnMoji selection.

        This method initializes a frame to hold all radio buttons and sets up two groups of radio buttons:
        one for selecting the comment type for different programming languages and another for choosing between
        Encrypt and Decrypt options for the EnMoji feature. It also includes descriptive labels and separators for clarity.
        """
        self.check_frame = ttk.Frame(self.master)
        self.check_frame.grid(row=1, column=1, rowspan=4, padx=10, pady=10, sticky='nw')
        
        # Shared variable for all radio buttons
        self.selected_option = tk.StringVar(value="comment#")

        # Label for Comment Converter
        comment_converter_label = tk.Label(self.check_frame, text="Comment Converter", bg='#f5f5dc', fg='#000000')
        comment_converter_label.pack(anchor='w', padx=5, pady=(0, 5))

        # Comment Type Selection
        comment_options = [
            ("#", "Python, Ruby, Shell scripts, PowerShell", "comment#"),
            ("//", "C, C++, Java, JavaScript, C#, Swift, Go", "comment//"),
            ("--", "SQL", "comment--"),
            ("%", "MATLAB", "comment%"),
            (";", "Lisp, Clojure", "comment;"),
            ("'", "Visual Basic", "comment'")
        ]
        for symbol, description, value in comment_options:
            radio_text = f"  {symbol}\t{description}"
            radio_button = ttk.Radiobutton(self.check_frame, text=radio_text, variable=self.selected_option, value=value)
            radio_button.pack(anchor='w', padx=5, pady=2)
            
        # Separator
        separator = ttk.Separator(self.check_frame, orient='horizontal')
        separator.pack(fill='x', pady=5)

        # Label for EnMoji 🍄
        enmoji_label = tk.Label(self.check_frame, text="EnMoji 🍄", bg='#f5f5dc', fg='#000000')
        enmoji_label.pack(anchor='w', padx=5, pady=(5, 0))

        # Encrypt/Decrypt Selection
        encrypt_decrypt_options = [("Encrypt", "emojiEncrypt"), ("Decrypt", "emojiDecrypt")]
        for text, value in encrypt_decrypt_options:
            radio_button = ttk.Radiobutton(self.check_frame, text=text, variable=self.selected_option, value=value)
            radio_button.pack(anchor='w', padx=5, pady=2)

    def create_red_pill_button(self):
        """
        Create and place a button labeled 'Take the Red Pill 🍎' on the GUI.

        This button, when clicked, triggers the start_easter_egg method, which initiates a special visual effect.
        """
        red_pill_button = ttk.Button(self.master, text="Take the Red Pill 🍎", command=self.start_easter_egg, width=20)
        red_pill_button.grid(row=2, column=1, pady=20, padx=80, sticky='nw')

    def start_easter_egg(self):
        """
        Start the Easter Egg visual effect, displaying a 'Matrix Rain' animation on the canvas.

        The method checks if the canvas for the animation already exists. If not, it creates a new canvas over the
        output text widget and starts the Matrix Rain animation. If the canvas exists, it toggles the visibility 
        of the animation.
        """
        # Ensure that any pending geometry management has been processed
        self.master.update_idletasks()

        if not hasattr(self, 'canvas'):
            # Get coordinates of the output text widget relative to its parent
            output_box_x = self.output_text.winfo_x()
            output_box_y = self.output_text.winfo_y()
            output_box_width = self.output_text.winfo_width() - 5
            output_box_height = self.output_text.winfo_height() - 5

            # Create the canvas
            self.canvas = tk.Canvas(self.master, width=output_box_width, height=output_box_height, bg='black')
            # Use place geometry manager to position the canvas
            self.canvas.place(x=output_box_x - 15, y=output_box_y - 15)  # Adjust the position as needed
            self.matrix_rain = EasterEgg(self.canvas)
            self.matrix_rain.start()
        else:
            # Toggle the canvas and rain effect
            if self.canvas.winfo_ismapped():
                self.canvas.place_forget()
            else:
                self.canvas.place(x=output_box_x - 15, y=output_box_y - 15)  # Adjust the position as needed
                self.matrix_rain.start()