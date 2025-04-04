import customtkinter as ctk
from datetime import datetime
import pytz


class ClockWidget(ctk.CTkFrame):
    """
    A widget that displays the current time in a specified timezone.
    """

    # Constants for ClockWidget
    TITLE_FONT = ("Arial", 16)
    TIME_FONT = ("Arial", 24)
    UPDATE_INTERVAL = 1000  # Time in milliseconds to update the clock
    INVALID_TIMEZONE_MSG = "Invalid Timezone"
    ERROR_MSG = "Error"

    def __init__(self, master=None, timezone=None, label_text="", bg_color=None, text_color=None, **kwargs):
        super().__init__(master, **kwargs)
        self.timezone = timezone
        self.label_text = label_text
        self.configure(fg_color=bg_color)

        # Title label for the clock
        self.title_label = ctk.CTkLabel(self, text=self.label_text, font=self.TITLE_FONT, text_color=text_color)
        self.title_label.pack(pady=(10, 5))

        # Time label to display the current time
        self.time_label = ctk.CTkLabel(self, text="", font=self.TIME_FONT, text_color=text_color)
        self.time_label.pack(padx=20, pady=10)

        # Start updating the clock
        self.start_clock_update()

    def start_clock_update(self):
        """
        Starts the periodic update of the clock display.
        """
        self.update_clock()
        self.after(self.UPDATE_INTERVAL, self.start_clock_update)

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
                current_time = self.INVALID_TIMEZONE_MSG
        except pytz.UnknownTimeZoneError:
            current_time = self.INVALID_TIMEZONE_MSG
        except Exception as e:
            current_time = self.ERROR_MSG
            print(f"Error updating clock for {self.label_text}: {e}")
        self.time_label.configure(text=current_time)


class ClockApp:
    """
    A class to encapsulate the clock application logic.
    """

    # Constants for ClockApp
    WINDOW_WIDTH = 215
    WINDOW_HEIGHT = 340
    CLOCK_PADDING = 10

    def __init__(self):
        self.root = None

    def add_clock_widget(self, timezone, label_text, bg_color, text_color):
        """
        Adds a ClockWidget to the application window.

        Args:
            timezone (str): The timezone for the clock.
            label_text (str): The label text to display above the clock.
            bg_color (str): The background color of the widget.
            text_color (str): The text color for the labels.
        """
        clock = ClockWidget(self.root, timezone=timezone, label_text=label_text, bg_color=bg_color, text_color=text_color)
        clock.pack(padx=20, pady=self.CLOCK_PADDING)

    def calculate_window_position(self):
        """
        Calculates the position of the window to be displayed at the bottom-right corner of the screen.

        Returns:
            tuple: The (x, y) coordinates for the window position.
        """
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = screen_width - self.WINDOW_WIDTH
        y = screen_height - self.WINDOW_HEIGHT - 50  # Offset from the bottom
        return x, y

    def configure_window(self):
        """
        Configures the main application window.
        """
        self.root = ctk.CTk()
        self.root.title("World Clocks")
        self.root.overrideredirect(True)  # Removes the window border
        self.root.attributes("-topmost", False)  # Ensures the window is not always on top

        # Calculate the window position
        x, y = self.calculate_window_position()
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{x}+{y}")

    def run(self):
        """
        Runs the clock application.
        Creates a window and adds clock widgets for specified timezones.
        """
        self.configure_window()

        time_zones = [
            ("Asia/Tokyo", "Japan 🏯", "#FFE5CC", "#FF8000"),
            ("Asia/Kolkata", "India 🌴", "#CCFFCC", "#008000"),
            ("Europe/Berlin", "Germany 🚘", "#CCCCFF", "#0000FF"),
        ]

        # Create and add clock widgets for each timezone
        for timezone, label_text, bg_color, text_color in time_zones:
            self.add_clock_widget(timezone, label_text, bg_color, text_color)

        self.root.mainloop()


if __name__ == "__main__":
    app = ClockApp()
    app.run()
