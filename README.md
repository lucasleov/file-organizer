# File Organizer



A simple Python command-line tool that organizes files in a folder by extension.



---

## Project Goals



The goal of this project is to automate the organization of files in a folder by grouping them into subfolders based on their extensions.

It was also developed as a portfolio project to practice Python, command-line interfaces, file handling, logging, automated tests, and basic project organization.



---

## Features


- Reads a folder path provided by the user
- Validates whether the path exists and is a folder
- Organizes files into subfolders based on their extensions
- Handles files without extension
- Ignores existing subfolders
- Prevents duplicate files from being overwritten
- Supports both interactive and command-line usage
- Generates logs for actions and errors
- Includes basic automated tests with pytest



---

## Technologies Used



- Python
- pathlib
- argparse
- logging
- pytest



---

## How to Install



1. Clone the repository:



```bash
git clone https://github.com/lucasleov/file-organizer.git
cd file-organizer
```



2. Create and activate the virtual environment:



```bash
python -m venv .venv
.venv\Scripts\activate
```



3. Install dependencies:



```bash
pip install -r requirements.txt
```



---

## How to Run



* Run in interactive mode:



```bash
python main.py
```



* Run with a folder path argument:



```bash
python main.py "C:\path\to\your\folder"
```


* Show help:



```bash
python main.py --help
```



---

## Usage Example



Before:



```text
Downloads/

├── photo.jpg

├── notes.txt

├── document.pdf

├── script.py

└── file_without_extension
```


* Run the script in the terminal:



```bash
python main.py "C:\path\to\Downloads"
```



After:



```text
Downloads/

├── jpg/

│   └── photo.jpg

├── txt/

│   └── notes.txt

├── pdf/

│   └── document.pdf

├── py/

│   └── script.py

└── no_extension/

    └── file_without_extension
```



---

## How to Run Tests



```bash
python -m pytest -v
```



Currently tested:



* file extension detection;
* lowercase normalization of extensions;
* files without extension;
* hidden files without extension;
* path existence validation;
* folder validation;
* conversion from string to Path;
* moving files to a destination folder using temporary test folders.



---

## Error handling



The program handles:

* empty folder path
* non-existing path
* path that is not a folder
* empty folders
* duplicated files
* permission or operating system errors during file movement



---

## Logging



The program writes logs to:



logs/file_organizer.log



The log records actions such as:



* folders being read
* files moved
* invalid paths
* duplicated files
* folders with no files to organize



---

## Project Structure


```text
file_organizer/

├── app/

│   ├── __init__.py

│   ├── organizer.py

│   └── utils.py

├── logs/

│   └── .gitkeep

├── tests/

│   └── test_utils.py

├── main.py

├── README.md

├── requirements.txt

└── .gitignore
```



---

## Limitations

* At the moment, the program only organizes files by extension. It does not support custom organization rules.
* Duplicated files, or files with the same name, will not be moved to the destination subfolder and an error entry will be made in the log. The program does not automatically suggest or apply alternative filenames.
* Subfolders will be completely ignored.
* Some parts of the project could be further improved to support more complete automated tests.



Not tested yet:



* command-line argument parsing;
* logging;
* permission errors;
* full interactive execution;
* full folder organization flow.



---

## Next Steps



Future testing improvements:



* test duplicated file behavior;
* test permission error handling;
* test full organize_folder() flow with tmp_path;
* test command-line execution.



---

## Author

Lucas Léo Viégas

---

## Project Status

Functional first portfolio version.
Release: v1.0.0