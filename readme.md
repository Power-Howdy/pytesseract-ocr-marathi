# Python script to extract data from PDF(Marathi) of images using OCR.

## Requirements

- Python 3.10
- Tesseract binary should be installed first.

## Installation

- Install Python 3.10

  https://realpython.com/installing-python/

- Install Tesseract binary

  https://sourceforge.net/projects/tesseract-ocr.mirror/

- Create venv for this project
  
  ```bash
    python -m venv venv
  ```

- Install packages using requirements.txt
  - Activate virtual python environment

  ```bash
  call venv/Scripts/activate.bat
  ```
  - Install packages

  ```bash
  pip install -r requirements.txt
  ```

- Create **pdfs**,  **images** and **result** directories

> Yup, you are ready to go.

## Usage

- Copy pdf files into  **pdfs** directory
- Run the script

  ```bash
  python main.py
  ```
- Enter as required  the pdf file name
- Output will be in **result** directory
