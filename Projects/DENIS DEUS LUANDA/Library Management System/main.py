import json

#Read data from json file and return it as a list of dictionaries
def load_books():
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
            return books
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
#Letting the function save the list of books to the json file
def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

#Function to add a new book to the library
def add_book(books):

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists!")
            return

    title = input("Enter Title: ")
    author = input("Enter Author: ")
    
    while True:
        year = input("Enter Year Published: ")

        if year.isdigit():
            year = int(year)
            break
        else:
            print("Invalid input. Please enter a valid year.")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "year": year
    }

    books.append(book)
    save_books(books)

    print("Book added successfully!")

#Function to search for a book by its ID
def search_book(books):

    search_id = input("Enter Book ID to search: ")

    for book in books:

        if book["id"] == search_id:
            print("\nBook Found")
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])
            return

    print("Book not found")

#Function to delete a book by its ID
def delete_book(books):

    delete_id = input("Enter Book ID to delete: ")

    for book in books:

        if book["id"] == delete_id:

            books.remove(book)

            save_books(books)

            print("Book deleted successfully!")

            return

    print("Book not found")

#Function to display all books in the library
def display_books(books):

    if not books:
        print("No books available.")
        return
    
    print(f"\nTotal Books: {len(books)}")

    for book in books:
        print("-" * 30)
        print(f"Book ID : {book['id']}")
        print(f"Title   : {book['title']}")
        print(f"Author  : {book['author']}")
        print(f"Year    : {book['year']}")

#Main function to run the library management system
def main():

    books = load_books()

    while True:

        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Delete Book")
        print("4. Display All Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)

        elif choice == "2":
            search_book(books)

        elif choice == "3":
            delete_book(books)

        elif choice == "4":
            display_books(books)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

#Run the main function to start the library management system
if __name__ == "__main__":
    main()