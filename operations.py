# operations.py

from data import library


def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")

    if book_id in library:
        print("Book ID already exists!")
    else:
        library[book_id] = {"name": book_name, "issued": False}
        print("Book added successfully!")


def view_books():
    if not library:
        print("No books available.")
    else:
        print("\nLibrary Books:")
        for book_id, details in library.items():
            status = "Issued" if details["issued"] else "Available"
            print(f"ID: {book_id} | Name: {details['name']} | Status: {status}")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    if book_id in library:
        if not library[book_id]["issued"]:
            library[book_id]["issued"] = True
            print("Book issued successfully!")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")


def return_book():
    book_id = input("Enter Book ID to return: ")

    if book_id in library:
        if library[book_id]["issued"]:
            library[book_id]["issued"] = False
            print("Book returned successfully!")
        else:
            print("Book was not issued.")
    else:
        print("Book not found.")