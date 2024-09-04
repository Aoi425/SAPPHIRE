import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import sqlite3

# Connect SQLite Database(If not exist database file, create database file)
conn = sqlite3.connect('sapphire.db')

# Create cursor object
c = conn.cursor()

# Create table book_list
c.execute('''CREATE TABLE IF NOT EXISTS book_list
             (no INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              author TEXT,
              classification TEXT,
              read_date TEXT,
              note TEXT)''')

# 変更を保存
conn.commit()

class SAPPHIRE:
    def __init__(self, root):
        self.root = root
        self.root.title("Sapphire")

        # --------------------First line
        # Register Button
        self.register_button = tk.Button(root, text="Register", width=15, height=2, command=lambda: open_register_window(self))
        self.register_button.grid(row=0, column=0, padx=0, pady=20)

        # --------------------Second line
        self.table_frame = tk.Frame(self.root, bg="whitesmoke", width=1100, height=500)
        self.table_frame.grid_propagate(False)
        self.table_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=8)

        # Books List
        self.books_list = ttk.Treeview(self.table_frame, columns=("No", "Title", "Author", "Classification", "Read Date", "Note"), show="headings")
        
        # Config column header
        self.books_list.heading("No", text="No", anchor="center")
        self.books_list.heading("Title", text="Title", anchor="center")
        self.books_list.heading("Author", text="Author", anchor="center")
        self.books_list.heading("Classification", text="Classification", anchor="center")
        self.books_list.heading("Read Date", text="Read Date", anchor="center")
        self.books_list.heading("Note", text="Note", anchor="center")

        # Config column width
        self.books_list.column("No", width=50, anchor="center")
        self.books_list.column("Title", width=300, anchor="w")
        self.books_list.column("Author", width=150, anchor="w")
        self.books_list.column("Classification", width=100, anchor="center")
        self.books_list.column("Read Date", width=150, anchor="center")
        self.books_list.column("Note", width=350, anchor="w")

        self.books_list.grid(row=0, column=0)

        # Display existing books in the database
        self.load_books()

    def load_books(self):
        # Clear existing entries in the treeview
        for row in self.books_list.get_children():
            self.books_list.delete(row)

        # Fetch data from the database
        c.execute("SELECT * FROM book_list")
        books = c.fetchall()

        # Insert data into the treeview
        for book in books:
            self.books_list.insert("", "end", values=book)

# Register button
def open_register_window(app):
    register_window = tk.Toplevel(app.root)
    register_window.title("Register Screen")
    register_window.geometry("1200x650+10+10")

    # Books title
    label_title = tk.Label(register_window, text="Title", width=20, height=2, bg="lightgray")
    label_title.grid(row=0, column=0, padx=10, pady=10)

    input_title = tk.Entry(register_window, width=56)
    input_title.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Author
    label_author = tk.Label(register_window, text="Author", width=20, height=2, bg="lightgray")
    label_author.grid(row=1, column=0, padx=10, pady=10)

    input_author = tk.Entry(register_window, width=56)
    input_author.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Class
    label_classification = tk.Label(register_window, text="Classification", width=20, height=2, bg="lightgray")
    label_classification.grid(row=2, column=0, padx=10, pady=10)

    # List
    options = ["Scrutiny", "Analysis", "Syntopical"]

    input_classification = tk.StringVar()
    input_classification.set(options[0])

    option_classification = tk.OptionMenu(register_window, input_classification, *options)
    option_classification.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Read Date
    label_read_date = tk.Label(register_window, text="Read Date", width=20, height=2, bg="lightgray")
    label_read_date.grid(row=3, column=0, padx=10, pady=10)

    input_read_date = DateEntry(register_window, width=20, background='darkblue', foreground='white', borderwidth=2)
    input_read_date.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Note
    label_note = tk.Label(register_window, text="Note", width=20, height=6, bg="lightgray")
    label_note.grid(row=4, column=0, padx=10, pady=10)

    input_note = tk.Text(register_window, width=56, height=6)
    input_note.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # Register Button
    register_button = tk.Button(register_window, text="Register", width=15, height=2, command=lambda: form_register(input_title, input_author, input_classification, input_read_date, input_note, app))
    register_button.grid(row=5, column=0, padx=10, pady=10)

    # Back button
    back_button = tk.Button(register_window, text="Back", width=15, height=2, command=register_window.destroy)
    back_button.grid(row=5, column=1, padx=10, pady=10, sticky="w")

def form_register(input_title, input_author, input_classification, input_read_date, input_note, app):
    # Get form data
    title = input_title.get()
    author = input_author.get()
    classification = input_classification.get()
    read_date = input_read_date.get()
    note = input_note.get("1.0", "end-1c")

    # Insert form data to database
    c.execute("INSERT INTO book_list (title, author, classification, read_date, note) VALUES (?, ?, ?, ?, ?)", (title, author, classification, read_date, note))

    # Save changes
    conn.commit()

    # Notify registration completion
    tk.messagebox.showinfo("Success", "Data saved to database")

    # Refresh the book list in the main application
    app.load_books()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x650+10+10")
    app = SAPPHIRE(root)
    root.mainloop()
    conn.close()
