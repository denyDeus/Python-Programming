# Library Management System

## Overview

The Library Management System is a console-based Python application that allows users to manage book records efficiently. The system uses JSON file handling to store and retrieve book information permanently. Users can add, search, delete, and display books through a menu-driven interface.

This project demonstrates the use of Python functions, lists, dictionaries, loops, conditional statements, and file handling techniques.

---

## Features

* Add new books to the library
* Prevent duplicate Book IDs
* Search for books using Book ID
* Delete books from the library
* Display all available books
* Display the total number of books
* Validate year input
* Store data permanently using a JSON file

---

## Technologies Used

* Python 3
* VScode
* JSON File Handling

---

## Project Structure

```text
LibraryManagementSystem/
│
├── main.py
├── books.json
└── README.md
```

### File Description

* **main.py** – Contains the Library Management System source code.
* **books.json** – Stores book records in JSON format.
* **README.md** – Project documentation.

---

## Data Structure Used

### List

The system stores all books in a list:

```python
books = []
```

### Dictionary

Each book is represented as a dictionary:

```python
{
    "id": "B001",
    "title": "Python Basics",
    "author": "John Doe",
    "year": 2024
}
```

---

## Program Functions

### 1. load_books()

Reads data from the JSON file and returns a list of books.

### 2. save_books(books)

Saves the current list of books to the JSON file.

### 3. add_book(books)

Allows users to add a new book after validating the Book ID and publication year.

### 4. search_book(books)

Searches for a book using its Book ID.

### 5. delete_book(books)

Removes a book from the library using its Book ID.

### 6. display_books(books)

Displays all books currently stored in the system.

### 7. main()

Controls the menu-driven interaction and program execution.

---

## How to Run the Program

### Step 1: Ensure Python is Installed

Check Python installation:

```bash
python --version
```

or

```bash
python3 --version
```

### Step 2: Create the JSON File

Create a file named:

```text
books.json
```

Add the following content:

```json
[]
```

### Step 3: Run the Program

```bash
python main.py
```

---

## Sample Menu

```text
===== Library Management System =====
1. Add Book
2. Search Book
3. Delete Book
4. Display All Books
5. Exit
```

---

## Sample Book Record

```json
[
    {
        "id": "B001",
        "title": "Python Basics",
        "author": "John Doe",
        "year": 2024
    }
]
```

---

## Concepts Demonstrated

* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* File Handling
* JSON Serialization and Deserialization
* Input Validation
* Menu-Driven Programming

---

## License

This project is developed for academic and learning purposes.
