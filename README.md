# py_clocks

The `py_clocks` package is a Python-based project designed for displaying multiple timezone clocks in windows desktop.

By default app shows the time in the following timezones:
- Asia/Tokyo
- Asia/Kolkata
- Europe/Berlin

![py_clocks_app](data/py_clocks_app.png)

modify the `py_clocks.py` file to add or remove timezones as per your requirement.

## Building the Project

To build the project, ensure you have Python installed along with the `uv` package. Follow these steps:

1. (optional step) Install the `uv` package if you haven't already:
    ```powershell
    pip install uv
    ```
2. Install the required dependencies:
    ```powershell
    uv sync
    ```
3. Run the project:
    ```powershell
    .venv/Scripts/python.exe -m py_clocks
    ```

## Creating an Executable

To create an executable for the `py_clocks` package using `pyinstaller`, follow these steps:

1. Generate the executable:
    ```powershell
    .venv/Scripts/pyinstaller.exe --onefile --noconsole py_clocks.py
    ```
2. The executable will be located in the `dist` directory.
