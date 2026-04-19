from organizer import FileOrganizer

def main():

    print("=== FILE ORGANIZER SYSTEM (INDUSTRY LEVEL) ===")

    path = input("Enter folder path: ")

    organizer = FileOrganizer(path)

    organizer.create_folders()
    organizer.organize()

    print("Files organized successfully ✔")


if __name__ == "__main__":
    main()