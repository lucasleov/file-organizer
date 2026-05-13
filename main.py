from app.organizer import organize_folder
from app.utils import setup_logging

def main() -> None:
    setup_logging()
    
    print("\nFile organizer\n")
    path = input("Inform the path to the folder you wish to organize: ")
    organize_folder(path)

if __name__ == "__main__":
    main()
