def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readline()
            if notes:
                print("\nYour Notes:")
                for idx, note in enumerate(notes.splitlines(), start=1):
                    print(f"{idx}. {note.strip()}")
            else:
                print("No notes found. Please add a note first.")
    except FileNotFoundError:
        print("No notes found. Please add a note first.")


def main():
    print("Welcome to the Note-Taking App!")
    while True:
        print("\nMenu:")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            pass  # Placeholder for delete note functionality
        elif choice == "4":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
