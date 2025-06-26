# py_clocks

The `py_clocks` package is a Python-based project designed for displaying multiple timezone clocks on a Windows desktop.

By default, the app shows the time in the following timezones:
- **Asia/Tokyo**
- **Asia/Kolkata**
- **Europe/Berlin**

![py_clocks_app](py_clocks_app.png)

*Screenshot of the `py_clocks` application showing multiple timezone clocks.*

To customize the timezones displayed, edit the [`py_clocks.py`](py_clocks.py) file and modify the `time_zones` list in the `run()` method.

---

## Prerequisites

- Python (version 3.11 or higher is required)
- The [`uv`](https://github.com/astral-sh/uv) package (used for dependency management)

---

## Setting Up the Development Environment

1. **Create and set up the virtual environment**  
   Run the provided script to create a virtual environment and install dependencies:
   ```bat
   venv_setup.bat
   ```

   This script will:
   - Create a `.venv` directory if it does not exist
   - Install or upgrade `pip` and `uv`
   - Sync dependencies from [`pyproject.toml`](pyproject.toml)

---

## Building and Running the Project

1. **Activate the virtual environment** (if not already activated):
   ```powershell
   .venv\Scripts\activate
   ```

2. **Run the project**:
   ```powershell
   .venv\Scripts\python.exe py_clocks.py
   ```

---

## Creating an Executable

To create a standalone executable for the `py_clocks` package using PyInstaller, use the provided script:

1. **Build the executable**:
   ```bat
   create_exe.bat
   ```

   This script checks for the virtual environment and PyInstaller, then builds the executable.

2. **Locate the executable**:  
   The generated executable will be located in the `dist` directory as `py_clocks.exe`.

---

## Troubleshooting

- **Missing Dependencies**: If you encounter issues with missing dependencies, run `venv_setup.bat` again to ensure all packages are installed.
- **Python Version**: Ensure you are using Python 3.11 or higher.
- **Executable Issues**: If the executable does not run, verify that all required files (e.g., timezone data) are included in the build. Check the `build/` directory for logs.

---

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for details.
