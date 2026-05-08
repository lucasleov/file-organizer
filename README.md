\# File Organizer



Python CLI project that organizes files from a folder based on their extensions.



\## Objective



Read a folder, identify files by extension, move files to corresponding subfolders, and generate a simple log of the actions performed.



\## Current features



\- Reads a folder path informed by the user

\- Validates if the path exists

\- Validates if the path is a folder

\- Identifies file extensions

\- Creates subfolders based on extensions

\- Moves files to the corresponding subfolders

\- Handles files without extension using `no\_extension`



\## Technologies used



\- Python

\- pathlib

\- Git

\- Virtual environment (`venv`)



\## Project structure



```text

file\_organizer/

├── app/

│   ├── \_\_init\_\_.py

│   ├── organizer.py

│   └── utils.py

├── logs/

│   └── .gitkeep

├── tests/

├── main.py

├── README.md

├── .gitignore

└── requirements.txt



\## How to run



Create and activate the virtual environment:



python -m venv .venv

.venv\\Scripts\\activate



Run the project:



python main.py



Then inform the path to the folder you want to organize.



\## Status



In development.



\## Next steps



\- Add logging of performed actions

\- Improve error handling

\- Prevent overwriting files with the same name

\- Add confirmation before moving files

\- Add tests

\- Improve CLI experience

