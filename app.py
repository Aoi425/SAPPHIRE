import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SAPPHIRE:
    def __init__(self, root):
        self.root = root
        self.root.title("Sapphire")

        # --------------------First line
        # Application Title
        self.title_label = tk.Label(root, text="Sapphire")
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        # --------------------Second line
        # Register Button
        self.register_button = tk.Button(root, text="Register")
        self.register_button.grid(row=1, column=0, padx=10, pady=10)

        # Edit Button
        self.edit_button = tk.Button(root, text="Edit")
        self.edit_button.grid(row=1, column=1, padx=10, pady=10)

        # Delete Button
        self.delete_button = tk.Button(root, text="Delete")
        self.delete_button.grid(row=1, column=2, padx=10, pady=10)

        # --------------------Third line
        table_frame = tk.Frame(self.root, bg="whitesmoke", width=1100, height=500)
        table_frame.grid_propagate(False)
        table_frame.grid(row=2, column=0, padx=10, pady=10, columnspan=8)

        # Books List
        books_list = ttk.Treeview(table_frame, columns=("No", "Title", "Author", "Read Date", "Note"), show="headings")

        # Config column header
        books_list.heading("No", text="No")
        books_list.heading("Title", text="Title")
        books_list.heading("Author", text="Author")
        books_list.heading("Read Date", text="Read Date")
        books_list.heading("Note", text="Note")

        # Config column width
        books_list.column("No", width=50)
        books_list.column("Title", width=300)
        books_list.column("Author", width=200)
        books_list.column("Read Date", width=150)
        books_list.column("Note", width=400)

        books_list.grid(row=0, column=0)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x650+10+10")
    app = SAPPHIRE(root)
    root.mainloop()
