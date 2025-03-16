import json
import datetime

# File to store library data
FILE_NAME = "library.json"

# ANSI Escape Codes for Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

def banner():
    """Display the library banner."""
    print(f"""
{CYAN}====================================
        📚 Personal Library Manager 📚
===================================={RESET}
""")

def load_library():
    """Load the library from a file if it exists."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save the library to a file."""
    with open(FILE_NAME, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Add a new book to the library."""
    title = input(f"{YELLOW}\nEnter the book title: {RESET}").strip()
    author = input(f"{YELLOW}Enter the author: {RESET}").strip()
    year = input(f"{YELLOW}Enter the publication year: {RESET}").strip()
    genre = input(f"{YELLOW}Enter the genre: {RESET}").strip()
    read_status = input(f"{YELLOW}Have you read this book? (yes/no): {RESET}").strip().lower() in ["yes", "y"]
    date_added = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status,
        "date_added": date_added
    }
    library.append(book)
    save_library(library)
    input(f"{GREEN}Book added successfully! 📖 ✅\nPress enter to continue...{RESET}")

def remove_book(library):
    """Remove a book by title."""
    title = input(f"{RED}\nEnter the title of the book to remove: {RESET}").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print(f"{GREEN}Book removed successfully! ❌{RESET}\n")
            return
    print(f"{RED}Book not found!{RESET}\n")
    input(f"{GREEN}Press enter to continue...{RESET}")

def search_book(library):
    """Search for a book by title or author."""
    print(f"{BLUE}\nSearch by:\n1. Title\n2. Author{RESET}")
    choice = input(f"{CYAN}Enter your choice: {RESET}").strip()
    query = input(f"{CYAN}Enter the search term: {RESET}").strip()
    
    matches = [book for book in library if book["title"].lower() == query.lower() or book["author"].lower() == query.lower()]
    
    if matches:
        print(f"{GREEN}Matching Books:{RESET}")
        for i, book in enumerate(matches, 1):
            status = f"{GREEN}Read{RESET}" if book["read"] else f"{RED}Unread{RESET}"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status} - Added: {book['date_added']}")
    else:
        print(f"{RED}No matching books found!{RESET}")
    input(f"{GREEN}Press enter to continue...{RESET}")

def display_books(library):
    """Display all books in the library."""
    if not library:
        print(f"{YELLOW}Your library is empty. 📚❌{RESET}\n")
        return
    
    print(f"{CYAN}Your Library:{RESET}")
    for i, book in enumerate(library, 1):
        status = f"{GREEN}Read{RESET}" if book["read"] else f"{RED}Unread{RESET}"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status} - Added: {book['date_added']}")
    input(f"{GREEN}Press enter to continue...{RESET}")

def display_statistics(library):
    """Show statistics about the library."""
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
    
    print(f"\n\n{YELLOW}📊 Library Statistics 📊{RESET}")
    print(f"{BLUE}Total books: {CYAN}{total_books}{RESET}")
    print(f"{BLUE}Percentage read: {CYAN}{read_percentage:.2f}%{RESET}\n")
    input(f"{GREEN}Press enter to continue...{RESET}")

def update_read_status(library):
    """Update the read status of a book."""
    title = input(f"{YELLOW}\nEnter the title of the book to update read status: {RESET}").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            new_status = input(f"{CYAN}Have you read this book? (yes/no): {RESET}").strip().lower() in ["yes", "y"]
            book["read"] = new_status
            save_library(library)
            print(f"{GREEN}Read status updated successfully! ✅{RESET}\n")
            return
    print(f"{RED}Book not found!{RESET}\n")
    input(f"{GREEN}Press enter to continue...{RESET}")
    

def edit_book(library):
    """Edit book details."""
    if not library:
        print(f"{YELLOW}Your library is empty. 📚❌{RESET}\n")
        return
    
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']}")
    title = input(f"{YELLOW}\nEnter the Title of the book to edit: {RESET}").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            print(f"{CYAN}Enter new details (leave blank to keep existing value):{RESET}")
            new_title = input(f"{YELLOW}New title: {RESET}").strip() or book["title"]
            new_author = input(f"{YELLOW}New author: {RESET}").strip() or book["author"]
            new_year = input(f"{YELLOW}New publication year: {RESET}").strip() or book["year"]
            new_genre = input(f"{YELLOW}New genre: {RESET}").strip() or book["genre"]
            
            book["title"] = new_title
            book["author"] = new_author
            book["year"] = int(new_year)
            book["genre"] = new_genre
            
            save_library(library)
            print(f"{GREEN}Book updated successfully! ✅{RESET}\n")
            return
    print(f"{RED}Book not found!{RESET}\n")
    input(f"{GREEN}Press enter to continue...{RESET}")

def main():
    library = load_library()
    
    while True:
        banner()
        print(f"{CYAN}1. Add a book{RESET}")
        print(f"{CYAN}2. Remove a book{RESET}")
        print(f"{CYAN}3. Search for a book{RESET}")
        print(f"{CYAN}4. Display all books{RESET}")
        print(f"{CYAN}5. Display statistics{RESET}")
        print(f"{CYAN}6. Update read status{RESET}")
        print(f"{CYAN}7. Edit book details{RESET}")
        print(f"{CYAN}8. Exit{RESET}")
        
        choice = input(f"{GREEN}Enter your choice: {RESET}").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            update_read_status(library)
        elif choice == "7":
            edit_book(library)
        elif choice == "8":
            save_library(library)
            print(f"{GREEN}Library saved. Goodbye! 📚{RESET}")
            break
        else:
            print(f"{RED}Invalid choice, please try again.{RESET}\n")

if __name__ == "__main__":
    main()
