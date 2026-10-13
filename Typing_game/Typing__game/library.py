import json
import os
from datetime import datetime
FILE = "book.json"
def load_books():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_books(books):
    with open(FILE, "w") as f:
        json.dump(books, f, indent=4)

def add_book():
    books = load_books()
    try:
        title = input("Book title: ").strip()
        if not title:
            print("Title cannot be empty.")
            return
        author = input("Author: ").strip()
        year = int(input("Year published: "))
        if year < 0 or year > datetime.now().year:
            print("Invald Year.")
            return
        book = {
            "title": title,
            "author": author,
            "year": year,
            "added": datetime.now().strftime("%Y-%m-%d"),
            "read": False
        }
        books.append(book)
        save_books(books)
        print(f"Book '{title}' added successfully.")
    except ValueError:
        print("Invalid year (must be a number).")
def list_books():
    books = load_books()
    if not books:
        print("Your Library is empty.")
        return

    print("\nYour Library:")
    for i, b in enumerate(books, 1):
        status = "Read" if b["read"] else "Unread"
        print(f"{i}. {b['title']} by {b['author']} ({b['year']}) - {status}")

def mark_read():
    books = load_books()
    if not books:
        return
    try:
        num = int(input("\nBook number to mark as read: "))
        if 0 <= num < len(books):
            books[num]["read"] = True
            save_books(books)
            print("Marked as read.")
        else:
            print("Invalid book number.")

    except ValueError:
        print("Enter a number.")

def search_books():
    books = load_books()
    if not books:
        print("Library is empty.")
        return
    term = input("search title or author:").lower().strip()
    found = [b for b in books if term in b["title"].lower() 
             or term in b["author"].lower()]
    if not found:
        print("No matches found.")
        return
    print(f"Found {len(found)} book(s):")
    for b in found:
        print(f"{b['title']} by {b['author']} ({b['year']})")

def main():
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. List all Books")
        print("3. Mark as read")
        print("4. Search Books")
        print("5. Exit")
        choice = input("Choose option(1-5):").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            mark_read()
        elif choice == "4":
            search_books()
        elif choice == "5":
            print("Exiting Library.")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()