import tkinter as tk
from tkinter import filedialog, messagebox

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            text_content = text.get(1.0, "end-1c")  # Retrieve text content from the Text widget
            file.write(text_content)
        messagebox.showinfo("Success", "File saved successfully.")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, "end")  # Clear previous content
            text.insert(1.0, file.read())  # Insert content from the opened file

root = tk.Tk()
root.title("Simple Text Editor")

text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
