import argparse

from app.organizer import organize_folder
from app.utils import setup_logging

def get_arguments():
    parser = argparse.ArgumentParser(
        description="Organize files in a folder by extension."
        )

    parser.add_argument(
        "folder_path",
        nargs="?",
        help="Path to the folder that will be organized."
        )
    return parser.parse_args()

def main() -> None:
    setup_logging()

    args = get_arguments()
    
    print("\nFile organizer\n")

    if args.folder_path:
        path = args.folder_path
    else:
        path = input("Inform the path to the folder you wish to organize: ")

    organize_folder(path)

if __name__ == "__main__":
    main()
