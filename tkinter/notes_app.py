import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("notes app")
root.geometry("400x300")
root.resizable(False, False)

# button style dictionary
button_style = {
    "width": 11,
    "bg": "#222222",
    "fg": "#8edbee",
    "font": "Ubuntu",
    "activebackground": "#414040",
    "activeforeground": "#dcdcdc",
    "relief": "flat",
    "bd": 0,
    "cursor": "hand2",
    "highlightthickness": 0,
    "padx": 10
}

# variables
window_bg = "#333333"
text_area_bg = "#414141"
text_area_fg = "#dcdcdc"

root.config(bg=window_bg)

# functions
def new_note():
    text_area.delete("1.0", tk.END)

def save_note():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", tk.END))

        messagebox.showinfo("Saved", "Note saved successfully!")

def open_note():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)


# top buttons
button_frame = tk.Frame(root, bg=window_bg)
button_frame.pack(fill="x", pady=5, padx=5)

new_btn = tk.Button(
    button_frame,
    text="new",
    **button_style,
    command=new_note
)
new_btn.pack(side="left", padx=5, pady=5)

open_btn = tk.Button(
    button_frame,
    text="open",
    **button_style,
    command=open_note
)
open_btn.pack(side="left", padx=5, pady=5)

save_btn = tk.Button(
    button_frame,
    text="save",
    **button_style,
    command=save_note
)
save_btn.pack(side="left", padx=5, pady=5)

# text area
text_area = tk.Text(
    root,
    font=("Ubuntu", 13),
    bg=text_area_bg,
    relief="flat",
    bd=0,
    highlightthickness=0,
    fg=text_area_fg,
    selectbackground="#C2C2C2",
    insertbackground="#666666",
    padx=10,
    pady=10,
    wrap="word"
)
text_area.pack(
    expand=True,
    fill="both",
    padx=10,
)

root.mainloop()
