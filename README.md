# QR Code Generator

This Python project generates QR codes based on user input and saves them as PNG or SVG files. It consists of several Python scripts:

## Files

### 1. greetings.py

This file contains a greeting message displayed when the program starts.

### 2. input_and_output.py

This file contains classes for handling user input and managing output files.

- `Input`: Represents user input data and its directory.
- `Output`: Manages the saving of generated QR codes as PNG or SVG files.

### 3. generate.py

This file contains the `Generate` class, which is responsible for creating QR codes using the `pyqrcode` library.

### 4. main.py

This is the main script of the project. It ties together the functionalities of the other files and provides the entry point for the program.

## Usage

To use the QR code generator:

1. Make sure you have Python installed on your system.
2. Install the required dependencies by running:
    ```bash
    pip install pyqrcode
    ```

3. Clone the repository or download the Python files.
    ```bash
    git clone https://github.com/shubhangi0301/QR-Code-generator
    ```
    ```bash
    cd  QR-Code-Generator
    ```

4. Run the `main.py` script using Python:
    ```bash
    python main.py
    ```
