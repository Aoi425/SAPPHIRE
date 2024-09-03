import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

class SAPPHIRE:
    def __init__(self, root):
        self.root = root
        self.root.title("Sapphire")

        # --------------------First line
        # Register Button
        self.register_button = tk.Button(root, text="Register", width=15, height=2, command=transition_register_scr)
        self.register_button.grid(row=0, column=0, padx=0, pady=20)

        # --------------------Second line
        table_frame = tk.Frame(self.root, bg="whitesmoke", width=1100, height=500)
        table_frame.grid_propagate(False)
        table_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=8)

        # Books List
        books_list = ttk.Treeview(table_frame, columns=("No", "Title", "Author", "Class", "Read Date", "Note"), show="headings")

        # Config column header
        books_list.heading("No", text="No")
        books_list.heading("Title", text="Title")
        books_list.heading("Author", text="Author")
        books_list.heading("Class", text="Class")
        books_list.heading("Read Date", text="Read Date")
        books_list.heading("Note", text="Note")

        # Config column width
        books_list.column("No", width=50)
        books_list.column("Title", width=300)
        books_list.column("Author", width=150)
        books_list.column("Class", width=100)
        books_list.column("Read Date", width=150)
        books_list.column("Note", width=350)

        books_list.grid(row=0, column=0)

# Register button
def transition_register_scr():
    register_window = tk.Toplevel(root)
    register_window.title("Register Screen")
    register_window.geometry("1200x650+10+10")

    # Books title
    label_title = tk.Label(register_window, text="Title", width=20, height=2, bg="lightgray")
    label_title.grid(row=0, column=0, padx=10, pady=10)

    input_title = tk.Entry(register_window, width=56)
    input_title.grid(row=0, column=1, padx=10, pady=10)

    # Author
    label_author = tk.Label(register_window, text="Author", width=20, height=2, bg="lightgray")
    label_author.grid(row=1, column=0, padx=10, pady=10)

    input_author = tk.Entry(register_window, width=56)
    input_author.grid(row=1, column=1, padx=10, pady=10)

    # Class
    label_class = tk.Label(register_window, text="Class", width=20, height=2, bg="lightgray")
    label_class.grid(row=2, column=0, padx=10, pady=10)

    # List
    options = ["Scrutiny", "Analysis", "Syntopical"]

    selected_option = tk.StringVar()
    selected_option.set(options[0])

    option_class = tk.OptionMenu(register_window, selected_option, *options)
    option_class.grid(row=2, column=1, padx=10, pady=10, sticky="w")

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
    register_button = tk.Button(register_window, text="Register", width=15, height=2, command=form_register)
    register_button.grid(row=5, column=0, padx=10, pady=10)

    # Back button
    back_button = tk.Button(register_window, text="Back", width=15, height=2, command=register_window.destroy)
    back_button.grid(row=5, column=1, padx=10, pady=10, sticky="w")

# Form data register function
def form_register():
    print("Register!!")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x650+10+10")
    app = SAPPHIRE(root)
    root.mainloop()
