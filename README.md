# PDF to JPG and JPG to PDF Converter

This is a Python script that provides a user-friendly interface for converting between PDF and JPG image formats. The script utilizes the `img2pdf` and `pdf2image` libraries to perform the conversions seamlessly.

## Features

- Convert PDF files to individual JPG images.
- Convert multiple JPG images to a single PDF file.
- Choose the output directory and image format for conversions.
- User-friendly graphical interface using the `PySimpleGUI` library.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.6+
- Required Python libraries: `img2pdf`, `pdf2image`, `PySimpleGUI`

## Installation

**Python Libraries:** Install the required Python libraries using the following command in your terminal:


pip install PySimpleGUI img2pdf Pillow pdf2image

**Poppler Installation**

For PDF to image conversion, you'll need to install Poppler. Here's how:

1. **Download:** Visit [Poppler's official website](https://poppler.freedesktop.org/) and download the version compatible with your system.

2. **Installation:** Follow the provided installation instructions for your operating system to install Poppler.

Poppler is essential for converting PDF files to images. Make sure to complete this step before using the program.

## Usage
1. Run the `main.py` script using Python:

   ```bash
   python main.py
2. Select the conversion mode:

   - "PDF to JPG": Converts a PDF to individual JPG images.
   - "JPG to PDF": Merges multiple JPG images into a single PDF file.
3. If converting from PDF to JPG:

   - Choose the PDF file to convert.
   - Specify the output directory where the JPG images will be saved.

4. If converting from JPG to PDF:

   - Select multiple JPG images to include in the PDF.
   - Specify the output directory and desired PDF file name.

5. Click the "Convert" button to start the conversion process.

## Issues
If you encounter any issues or have questions, feel free to create an issue on this repository.
