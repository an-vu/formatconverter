from mapping import ENCRYPTION_MAP, DECRYPTION_MAP
import tkinter as tk
import random

class TextConverter:
    @staticmethod # Static method: no need to create an instance of the class to use this method (like self or cls)
    def cleanup_input(lines):
        """
        Cleans up input lines by stripping leading and trailing whitespace and joining them into a single string.

        Args:
            lines (List[str]): A list of strings representing lines of text.

        Returns:
            str: A single string formed by joining cleaned lines.
        """
        return '\n'.join(line.strip() for line in lines if line.strip())

    @staticmethod
    def format_converter(para, comment_symbol="#"):
        """
        Converts a paragraph into a format where each sentence starts with a specified comment symbol.

        Args:
            para (str): The paragraph to be converted.
            comment_symbol (str, optional): The comment symbol to be used. Defaults to "#".

        Returns:
            str: The formatted string with each sentence starting with the comment symbol.
        """
        sentences = para.replace('. ', '.\n').replace('! ', '!\n').replace('? ', '?\n').split('\n')
        return '\n'.join(f'{comment_symbol} {sentence.strip()}' for sentence in sentences if sentence.strip())

    @staticmethod
    def encrypt_to_emoji(text):
        """
        Converts a text to its corresponding emoji representation based on a predefined mapping.

        Args:
            text (str): The text to be encrypted.

        Returns:
            str: The encrypted text with emojis.
        """
        encrypted_text = ''
        for char in text:
            char_lower = char.lower()
            encrypted_text += ENCRYPTION_MAP.get(char_lower, char)  # Fallback to the original character if not found
        return encrypted_text.replace(' ', 'æ').replace('œ', '   ')  # Handle spaces and triple spaces

    @staticmethod
    def decrypt_from_emoji(emoji_text):
        """
        Converts emoji representation back to its original text form based on a predefined mapping.

        Args:
            emoji_text (str): The emoji text to be decrypted.

        Returns:
            str: The decrypted text.
        """
        decrypted_text = ''
        i = 0
        while i < len(emoji_text):
            # Handling space characters
            if emoji_text[i] == 'æ':
                decrypted_text += ' '
                i += 1
            elif emoji_text[i:i+3] == 'œ':
                decrypted_text += '   '  # Triple space
                i += 3
            else:
                # Attempt to match longer sequences first
                for length in range(5, 0, -1):
                    if i + length <= len(emoji_text):
                        emoji_seq = emoji_text[i:i + length]
                        if emoji_seq in DECRYPTION_MAP:
                            decrypted_text += DECRYPTION_MAP[emoji_seq]
                            i += length
                            break
                else:
                    # If no match found, move to the next character
                    decrypted_text += emoji_text[i]
                    i += 1
        return decrypted_text

class EasterEgg:
    def __init__(self, canvas, num_particles=200, update_rate=80):
        """
        Initialize the EasterEgg effect with specified parameters.

        :param canvas: The Tkinter canvas where the effect will be displayed.
        :param num_particles: Number of rain particles to display.
        :param update_rate: Rate at which the rain effect updates (in milliseconds).
        """
        self.canvas = canvas
        self.num_particles = num_particles
        self.update_rate = update_rate
        self.particles = []
        self.create_particles()

    def create_particles(self):
        """Create the initial set of particles for the rain effect."""
        canvas_width = int(self.canvas['width'])
        canvas_height = int(self.canvas['height'])
        for _ in range(self.num_particles):
            x = random.randint(0, canvas_width)
            y = random.randint(-canvas_height, 0)
            particle = self.canvas.create_text(
                x, y, text=random.choice('0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'),
                fill='green', font=('Courier', 12)
            )
            self.particles.append(particle)

    def start(self):
        """Begin the rain effect."""
        self.update_rain()

    def update_rain(self):
        """Update the position of each rain particle to create the falling effect."""
        canvas_height = int(self.canvas['height'])
        for particle in self.particles:
            self.canvas.move(particle, 0, random.randint(10, 20))  # Move each particle by a random amount
            x, y = self.canvas.coords(particle)
            if y > canvas_height:
                self.canvas.coords(particle, random.randint(0, int(self.canvas['width'])), -20)
        self.canvas.after(self.update_rate, self.update_rain)