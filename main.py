from organizer import FileOrganizer

def main():

    print("=== FILE ORGANIZER FROM SCRATCH ===")

    path = input("Enter folder path: ")

    app = FileOrganizer(path)
    app.start()


if __name__ == "__main__":
    main()
