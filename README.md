# File Organizer



A simple Python command-line tool that organizes files in a folder by extension.



## Objective



Read a folder, identify files by extension, move files to corresponding subfolders, and generate a simple log of the actions performed.



## Features



* Reads a folder path informed by the user
* Validates if the path exists
* Validates if the path is a folder
* Identifies file extensions
* Creates subfolders based on extensions
* Moves files to the corresponding subfolders
* Handles files without extension
* Ignores subfolders
* Handles duplicated files without overwriting them
* Logs actions and erros
* Can be used interactively or with a command-line argument for the folder path



## Project structure



file\_organizer/
├── app/
│   ├── **init**.py
│   ├── organizer.py
│   └── utils.py
├── logs/
│   └── .gitkeep
├── tests/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore



## How to run



* Clone the repository:



git clone <repository-url>
cd file\_organizer



* Create and activate the virtual environment:



python -m venv .venv
.venv\\\\Scripts\\\\activate



* Run in interactive mode:



python main.py



* Run with a folder path argument:



python main.py "C:\\path\\to\\your\\folder"



* Show help:



python main.py --help



## Example



Before:



Downloads/
├── photo.jpg
├── notes.txt
├── document.pdf
├── script.py
└── file\_without\_extension



After:



Downloads/
├── jpg/
│   └── photo.jpg
├── txt/
│   └── notes.txt
├── pdf/
│   └── document.pdf
├── py/
│   └── script.py
└── no\_extension/
└── file\_without\_extension



## Error handling



The program handles:

* empty folder path
* non-existing path
* path that is not a folder
* empty folders
* duplicated files
* permission or operating system errors during file movement



## Logging



The program writes logs to:



logs/file\_organizer.log



The log records actions such as:



* folders being read
* files moved
* invalid paths
* duplicated files
* folders with no files to organize



## Status



Version 1.0.0 - First stable version of the project.

