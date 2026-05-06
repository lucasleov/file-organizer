from app.organizer import organize_folder

def main() -> None:
    print("File organizer")

    path = input("Inform the path to the folder you wish to organize: ")
    organize_folder(path)

if __name__ == "__main__":
    main()
