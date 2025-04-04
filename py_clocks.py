import customtkinter as ctk
from datetime import datetime
import pytz

# Constants for UI configuration
TITLE_FONT = ("Arial", 16)
TIME_FONT = ("Arial", 24)
WINDOW_WIDTH = 215
WINDOW_HEIGHT = 340
CLOCK_PADDING = 10
UPDATE_INTERVAL = 1000  # Time in milliseconds to update the clock


class ClockWidget(ctk.CTkFrame):
    """
    A widget that displays the current time in a specified timezone.
    """
    def __init__(self, master=None, timezone=None, label_text="", bg_color=None, text_color=None, **kwargs):
        super().__init__(master, **kwargs)
        self.timezone = timezone
        self.label_text = label_text
        self.configure(fg_color=bg_color)

        # Title label for the clock
        self.title_label = ctk.CTkLabel(self, text=self.label_text, font=TITLE_FONT, text_color=text_color)
        self.title_label.pack(pady=(10, 5))

        # Time label to display the current time
        self.time_label = ctk.CTkLabel(self, text="", font=TIME_FONT, text_color=text_color)
        self.time_label.pack(padx=20, pady=10)

        # Start updating the clock
        self.update_clock()

    def update_clock(self):
        """
        Updates the displayed time based on the specified timezone.
        If the timezone is invalid, displays an error message.
        """
        try:
            if self.timezone:
                tz = pytz.timezone(self.timezone)
                current_time = datetime.now(tz).strftime("%I:%M:%S %p")
            else:
                current_time = "Invalid Timezone"
        except Exception as e:
            current_time = "Error"
            print(f"Error updating clock for {self.label_text}: {e}")
        self.time_label.configure(text=current_time)
        self.after(UPDATE_INTERVAL, self.update_clock)


def create_clock_widget(root, timezone, label_text, bg_color, text_color):
    """
    Creates and packs a ClockWidget into the specified root window.

    Args:
        root (ctk.CTk): The root window where the widget will be added.
        timezone (str): The timezone for the clock.
        label_text (str): The label text to display above the clock.
        bg_color (str): The background color of the widget.
        text_color (str): The text color for the labels.
    """
    clock = ClockWidget(root, timezone=timezone, label_text=label_text, bg_color=bg_color, text_color=text_color)
    clock.pack(padx=20, pady=CLOCK_PADDING)


def calculate_window_position(screen_width, screen_height):
    """
    Calculates the position of the window to be displayed at the bottom-right corner of the screen.

    Args:
        screen_width (int): The width of the screen.
        screen_height (int): The height of the screen.

    Returns:
        tuple: The (x, y) coordinates for the window position.
    """
    x = screen_width - WINDOW_WIDTH
    y = screen_height - WINDOW_HEIGHT - 50  # Offset from the bottom
    return x, y


def setup_window():
    """
    Sets up the main window for the application.

    Returns:
        ctk.CTk: The configured root window.
    """
    root = ctk.CTk()
    root.title("World Clocks")
    root.overrideredirect(True)  # Removes the window border
    root.attributes("-topmost", False)  # Ensures the window is not always on top

    # Calculate the window position
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x, y = calculate_window_position(screen_width, screen_height)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
    return root


def main():
    """
    Main function to run the clock application.
    Creates a window and adds clock widgets for specified timezones.
    """
    time_zones = [
        ("Asia/Tokyo", "Japan 🏯", "#FFE5CC", "#FF8000"),
        ("Asia/Kolkata", "India 🌴", "#CCFFCC", "#008000"),
        ("Europe/Berlin", "Germany 🚘", "#CCCCFF", "#0000FF"),
    ]

    root = setup_window()

    # Create and add clock widgets for each timezone
    for timezone, label_text, bg_color, text_color in time_zones:
        create_clock_widget(root, timezone, label_text, bg_color, text_color)

    root.mainloop()


if __name__ == "__main__":
    main()
