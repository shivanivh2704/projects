import tkinter as tk
from tkinter import messagebox

# Set up the main application window
root = tk.Tk()
root.title("Library Management System")
root.geometry("600x400")

# Sample data (you can replace this with a database or other data source)
books = [
    {"id": 1, "title": "percy jackson", "author": "Riordan", "available": True},
    {"id": 2, "title": "sunrise song", "author": "catherine", "available": True},
    {"id": 3, "title": "kite runner", "author": "khaled hosseini", "available": False},
    {"id": 4, "title": "ponniyin selvan", "author": "kalki", "available": True}
]

# Function to list all books
def list_books():
    listbox_books.delete(0, tk.END)
    for book in books:
        status = "Available" if book["available"] else "Borrowed"
        listbox_books.insert(tk.END, f"{book['id']}. {book['title']} by {book['author']} - {status}")

# Function to add a new book
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    if title and author:
        new_id = max(book["id"] for book in books) + 1
        books.append({"id": new_id, "title": title, "author": author, "available": True})
        list_books()
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both title and author")

# Function to borrow a book
def borrow_book():
    try:
        book_id = int(entry_book_id.get())
        for book in books:
            if book["id"] == book_id:
                if book["available"]:
                    book["available"] = False
                    list_books()
                    entry_book_id.delete(0, tk.END)
                    return
                else:
                    messagebox.showwarning("Unavailable", "This book is already borrowed")
                    return
        messagebox.showwarning("Not Found", "Book ID not found")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid Book ID")

# Function to return a book
def return_book():
    try:
        book_id = int(entry_book_id.get())
        for book in books:
            if book["id"] == book_id:
                if not book["available"]:
                    book["available"] = True
                    list_books()
                    entry_book_id.delete(0, tk.END)
                    return
                else:
                    messagebox.showwarning("Already Available", "This book is not borrowed")
                    return
        messagebox.showwarning("Not Found", "Book ID not found")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid Book ID")

# Function to check if a book is available
def check_availability():
    title = entry_search_title.get()
    book_id = entry_search_id.get()
    
    if title:
        for book in books:
            if book["title"].lower() == title.lower():
                status = "Available" if book["available"] else "Borrowed"
                messagebox.showinfo("Book Status", f"'{book['title']}' by {book['author']} is {status}")
                return
        messagebox.showwarning("Not Found", "Book title not found")
    elif book_id:
        try:
            book_id = int(book_id)
            for book in books:
                if book["id"] == book_id:
                    status = "Available" if book["available"] else "Borrowed"
                    messagebox.showinfo("Book Status", f"'{book['title']}' by {book['author']} is {status}")
                    return
            messagebox.showwarning("Not Found", "Book ID not found")
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid Book ID")
    else:
        messagebox.showwarning("Input Error", "Please enter a title or ID to search")

# Widgets for book listing
label_books = tk.Label(root, text="Book List:")
label_books.pack()

listbox_books = tk.Listbox(root, width=80, height=10)
listbox_books.pack()
list_books()

# Widgets for adding a book
frame_add = tk.Frame(root)
frame_add.pack(pady=10)

label_title = tk.Label(frame_add, text="Title:")
label_title.grid(row=0, column=0, padx=5)

entry_title = tk.Entry(frame_add)
entry_title.grid(row=0, column=1, padx=5)

label_author = tk.Label(frame_add, text="Author:")
label_author.grid(row=1, column=0, padx=5)

entry_author = tk.Entry(frame_add)
entry_author.grid(row=1, column=1, padx=5)

button_add = tk.Button(frame_add, text="Add Book", command=add_book)
button_add.grid(row=2, columnspan=2, pady=5)

# Widgets for borrowing and returning books
frame_borrow_return = tk.Frame(root)
frame_borrow_return.pack(pady=10)

label_book_id = tk.Label(frame_borrow_return, text="Book ID:")
label_book_id.grid(row=0, column=0, padx=5)

entry_book_id = tk.Entry(frame_borrow_return)
entry_book_id.grid(row=0, column=1, padx=5)

button_borrow = tk.Button(frame_borrow_return, text="Borrow Book", command=borrow_book)
button_borrow.grid(row=1, column=0, pady=5)

button_return = tk.Button(frame_borrow_return, text="Return Book", command=return_book)
button_return.grid(row=1, column=1, pady=5)

# Widgets for checking availability
frame_check = tk.Frame(root)
frame_check.pack(pady=10)

label_search_title = tk.Label(frame_check, text="Search by Title:")
label_search_title.grid(row=0, column=0, padx=5)

entry_search_title = tk.Entry(frame_check)
entry_search_title.grid(row=0, column=1, padx=5)

label_search_id = tk.Label(frame_check, text="or Book ID:")
label_search_id.grid(row=1, column=0, padx=5)

entry_search_id = tk.Entry(frame_check)
entry_search_id.grid(row=1, column=1, padx=5)

button_check = tk.Button(frame_check, text="Check Availability", command=check_availability)
button_check.grid(row=2, columnspan=2, pady=5)

# Run the application
root.mainloop()
