# Scrble2PDF

A lightweight Command-Line Interface (CLI) tool written in Python that automatically compiles exported image files (from Scrble Ink or similar note-taking applications) into a single PDF document with a higher resolution than the base "export to pdf" option. It also includes an auto-cleanup feature to delete the original image files, helping you save storage space.

## Prerequisites

* Python 3.6 or higher
* `Pillow` library

## Installation

1. Clone this repository:
```bash
git clone [https://github.com/Nibanus/scrble2pdf.git](https://github.com/Nibanus/scrble2pdf.git)
cd scrble2pdf
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt

(Alternatively, you can install the library directly: pip install Pillow)
```
## Usage

Run the script from your terminal using the following syntax:
```bash
python main.py /path/to/your/image/directory [-o OUTPUT_FILENAME.pdf]
```
Examples:
Run with the default output filename (compiled.pdf):
```bash
python main.py "C:\Users\Admin\Documents\ScrbleExport"
```
Run and specify a custom output filename:
```bash
python main.py "C:\Users\Admin\Documents\ScrbleExport" -o "Calculus_Notes.pdf"
```
## WARNING!!!
Data Loss Notice: This tool will PERMANENTLY DELETE the original image files once the PDF is successfully generated. Please ensure you actually want to clean up the directory before executing the command.