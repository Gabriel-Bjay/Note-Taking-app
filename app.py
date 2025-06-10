def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                print("\nYour Notes:")
                for idx, note in enumerate(notes.splitlines(), start=1):
                    print(f"{idx}. {note.strip()}")
            else:
                print("No notes found. Please add a note first.")
    except FileNotFoundError:
        print("No notes found. Please add a note first.")


def delete_notes():
    view_notes()
    try:
        note_number = int(input("Enter the note number to delete: "))
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if 1 <= note_number <= len(notes):
            removed_note = notes.pop(note_number - 1)
            with open("notes.txt", "w") as file:
                file.writelines(notes)
            print(f"{removed_note}: deleted successfully!")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")


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
            delete_notes()
        elif choice == "4":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
