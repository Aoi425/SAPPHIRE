import tkinter as tk
from tkinter import messagebox

class BlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blog Application")

        # 投稿を保持するためのリスト
        self.posts = []

        # 投稿作成のためのウィジェット
        self.title_label = tk.Label(root, text="Title:")
        self.title_label.grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        self.content_label = tk.Label(root, text="Content:")
        self.content_label.grid(row=1, column=0, padx=5, pady=5)
        self.content_text = tk.Text(root, height=10, width=50)
        self.content_text.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Post", command=self.add_post)
        self.add_button.grid(row=2, column=1, padx=5, pady=5, sticky='e')

        # 投稿リストの表示のためのウィジェット
        self.posts_listbox = tk.Listbox(root, height=10, width=70)
        self.posts_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.posts_listbox.bind("<Double-1>", self.show_post)

        self.delete_button = tk.Button(root, text="Delete Post", command=self.delete_post)
        self.delete_button.grid(row=4, column=1, padx=5, pady=5, sticky='e')

    def add_post(self):
        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END).strip()

        if title and content:
            self.posts.append({"title": title, "content": content})
            self.update_posts_listbox()
            self.clear_fields()
        else:
            messagebox.showwarning("Input Error", "Title and Content cannot be empty!")

    def update_posts_listbox(self):
        self.posts_listbox.delete(0, tk.END)
        for post in self.posts:
            self.posts_listbox.insert(tk.END, post["title"])

    def clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)

    def show_post(self, event):
        selected_index = self.posts_listbox.curselection()
        if selected_index:
            post = self.posts[selected_index[0]]
            messagebox.showinfo(post["title"], post["content"])

    def delete_post(self):
        selected_index = self.posts_listbox.curselection()
        if selected_index:
            del self.posts[selected_index[0]]
            self.update_posts_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a post to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BlogApp(root)
    root.mainloop()
