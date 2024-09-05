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

# Save changes
conn.commit()

class SAPPHIRE:
    def __init__(self, root):
        self.root = root
        self.root.title("Sapphire")

        # Register Button
        self.register_button = tk.Button(root, text="Register", width=15, height=2, command=self.open_register_window)
        self.register_button.grid(row=0, column=0, padx=0, pady=20)

        # Table Frame
        table_frame = tk.Frame(self.root, bg="whitesmoke", width=1100, height=500)
        table_frame.grid_propagate(False)
        table_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=8)

        # Books List
        self.books_list = ttk.Treeview(table_frame, columns=("No", "Title", "Author", "Classification", "Read Date", "Note"), show="headings")
        self.books_list.heading("No", text="No")
        self.books_list.heading("Title", text="Title")
        self.books_list.heading("Author", text="Author")
        self.books_list.heading("Classification", text="Classification")
        self.books_list.heading("Read Date", text="Read Date")
        self.books_list.heading("Note", text="Note")

        self.books_list.column("No", width=50, anchor="center")
        self.books_list.column("Title", width=300)
        self.books_list.column("Author", width=150)
        self.books_list.column("Classification", width=100)
        self.books_list.column("Read Date", width=150, anchor="center")
        self.books_list.column("Note", width=350)

        self.books_list.grid(row=0, column=0)

        # Bind the click event to the title column
        self.books_list.bind("<ButtonRelease-1>", self.on_title_click)

        self.refresh_data()

    # Open Register Window
    def open_register_window(self):
        register_window = tk.Toplevel(self.root)
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

        # Classification
        label_classification = tk.Label(register_window, text="Classification", width=20, height=2, bg="lightgray")
        label_classification.grid(row=2, column=0, padx=10, pady=10)

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
        register_button = tk.Button(register_window, text="Register", width=15, height=2,
                                     command=lambda: self.form_register(input_title, input_author, input_classification, input_read_date, input_note))
        register_button.grid(row=5, column=0, padx=10, pady=10)

        # Back button
        back_button = tk.Button(register_window, text="Back", width=15, height=2, command=register_window.destroy)
        back_button.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Form Register
    def form_register(self, input_title, input_author, input_classification, input_read_date, input_note):
        title = input_title.get()
        author = input_author.get()
        classification = input_classification.get()
        read_date = input_read_date.get()
        note = input_note.get("1.0", "end-1c")

        # Insert form data to database
        c.execute("INSERT INTO book_list (title, author, classification, read_date, note) VALUES (?, ?, ?, ?, ?)",
                  (title, author, classification, read_date, note))

        # Save changes
        conn.commit()
        self.refresh_data()

        # Notify registration completion
        tk.messagebox.showinfo("Success", "Data saved to database")

    # Refresh Data
    def refresh_data(self):
        for item in self.books_list.get_children():
            self.books_list.delete(item)

        c.execute("SELECT * FROM book_list")
        for row in c.fetchall():
            self.books_list.insert("", "end", values=row)

    # On Title Click
    def on_title_click(self, event):
        item = self.books_list.selection()[0]
        title = self.books_list.item(item, "values")[1]
        self.open_edit_window(title)

    # Open Edit Window
    def open_edit_window(self, title):
        c.execute("SELECT * FROM book_list WHERE title = ?", (title,))
        data = c.fetchone()

        if data:
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Edit Data")

            input_title = tk.Entry(edit_window, width=56)
            input_title.insert(0, data[1])
            input_title.pack()

            input_author = tk.Entry(edit_window, width=56)
            input_author.insert(0, data[2])
            input_author.pack()

            input_classification = tk.StringVar()
            input_classification.set(data[3])
            option_classification = tk.OptionMenu(edit_window, input_classification, "Scrutiny", "Analysis", "Syntopical")
            option_classification.pack()

            input_read_date = DateEntry(edit_window, width=20)
            input_read_date.set_date(data[4])
            input_read_date.pack()

            input_note = tk.Text(edit_window, width=56, height=6)
            input_note.insert("1.0", data[5])
            input_note.pack()

            update_button = tk.Button(edit_window, text="Update",
                                       command=lambda: self.update_data(data[0], input_title.get(), input_author.get(), input_classification.get(), input_read_date.get(), input_note.get("1.0", "end-1c")))
            update_button.pack()

            delete_button = tk.Button(edit_window, text="Delete",
                                       command=lambda: self.delete_data(data[0]))
            delete_button.pack()

    # Update Data
    def update_data(self, id, title, author, classification, read_date, note):
        c.execute("UPDATE book_list SET title = ?, author = ?, classification = ?, read_date = ?, note = ? WHERE no = ?",
                  (title, author, classification, read_date, note, id))
        conn.commit()
        self.refresh_data()
        tk.messagebox.showinfo("Success", "Data updated successfully")

    # Delete Data
    def delete_data(self, id):
        c.execute("DELETE FROM book_list WHERE no = ?", (id,))
        conn.commit()
        self.refresh_data()
        tk.messagebox.showinfo("Success", "Data deleted successfully")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x650+10+10")
    app = SAPPHIRE(root)
    root.mainloop()
    conn.close()
