from tkinter import filedialog, font, messagebox
from tkinter import *


current_file_path = ""

def op(*args):
    global current_file_path
    try:
        filepath = filedialog.askopenfilename(filetypes=(("text file", "*.txt"), ("all files", "*.*")))
        if filepath: # Check if the user actually selected a file
            current_file_path = filepath
            with open(current_file_path, 'r') as file:
                a = file.read()
            d.delete(1.0, END) # Clear existing text before opening new file
            d.insert(1.0, a)
    except Exception as e:
        show_status("Error opening file", "red")

def show_status(msg, color):
    """Helper function to show a temporary status message without freezing the GUI."""
    L.config(text=msg, fg=color)
    L.grid(row=0, column=0, pady=5)
    
    a.after(3000, L.grid_forget)

def save(*args):
    global current_file_path
    try:
        if current_file_path == "":
            
            filepath = filedialog.asksaveasfilename(defaultextension="*.txt", filetypes=(("text file", "*.txt"), ("all files", "*.*")))
            if not filepath: # User cancelled
                return
            current_file_path = filepath
            
        with open(current_file_path, "w") as f:
            f.write(d.get(1.0, END))
            
        show_status("Saved", "green")
    except Exception:
        show_status("Not saved", "red")

def sas(*args):
    global current_file_path
    try:
        filepath = filedialog.asksaveasfilename(defaultextension="*.txt", filetypes=(("text file", "*.txt"), ("all files", "*.*")))
        if not filepath: # User cancelled
            return
            
        current_file_path = filepath
        with open(current_file_path, "w") as f:
            f.write(d.get(1.0, END))
            
        show_status("Saved", "green")
    except Exception:
        show_status("Not saved", "red")

# --- Main Window Setup ---
a = Tk()
a.title("Text editor")

width = 500
height = 500
x = a.winfo_screenwidth()
y = a.winfo_screenheight()
sh = int(x / 2) - int(width / 2)
sw = int(y / 2) - int(height / 2)
a.geometry(f"{width}x{height}+{sh}+{sw}")

# Font Variables
fo = StringVar()
fs = IntVar()
fo.set("Arial") # Changed from "DEFAULT" to a standard font
fs.set(12)

# --- Widgets ---
a.grid_rowconfigure(0, weight=1)
a.grid_columnconfigure(0, weight=1)

# Text Area and Scrollbar
d = Text(a, font=(fo.get(), fs.get()))
s = Scrollbar(a, command=d.yview) 
d.config(yscrollcommand=s.set)

d.grid(row=0, column=0, sticky=N+E+S+W)
s.grid(row=0, column=1, sticky=N+S) 
# Status Label (Hidden by default)
L = Label(a)

# Bottom Frame for Settings
fr = Frame(a)
fr.grid(row=1, column=0, columnspan=2, pady=5)

OptionMenu(fr, fo, *font.families(), command=lambda *args: d.config(font=(fo.get(), fs.get()))).grid(row=0, column=0, padx=5)
Spinbox(fr, from_=1, to=100, textvariable=fs, command=lambda *args: d.config(font=(fo.get(), fs.get())), width=5).grid(row=0, column=1, padx=5)
Button(fr, text="Clear", command=lambda: d.delete(1.0, END)).grid(row=0, column=2, padx=5)

# --- Keyboard Bindings ---
d.bind("<Control-o>", op)
d.bind("<Control-s>", save)

d.bind("<Control-S>", sas) 

# --- Menus ---
b = Menu(a)
a.config(menu=b)

# File Menu
b1 = Menu(b, tearoff=0)
b.add_cascade(label="File", menu=b1)
b1.add_command(label="Open (Ctrl+O)", command=op)
b1.add_separator()
b1.add_command(label="Save (Ctrl+S)", command=save)
b1.add_command(label="Save As (Ctrl+Shift+S)", command=sas)
b1.add_separator()
b1.add_command(label="Quit (Exit)", command=a.quit)

# Edit Menu
b2 = Menu(b, tearoff=0)
b.add_cascade(label="Edit", menu=b2)
b2.add_command(label="Copy (Ctrl+C)", command=lambda: d.event_generate("<<Copy>>"))
b2.add_command(label="Paste (Ctrl+V)", command=lambda: d.event_generate("<<Paste>>"))
b2.add_command(label="Cut (Ctrl+X)", command=lambda: d.event_generate("<<Cut>>"))

# Help Menu
f2 = Menu(b, tearoff=0)
b.add_cascade(label="Help", menu=f2)
f2.add_command(label="About", command=lambda: messagebox.showinfo(title="DONE BY", message="This project is done by :\n  AAKULA LOKESH"))

a.mainloop()