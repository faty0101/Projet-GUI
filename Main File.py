import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog

root = tk.Tk()
root.title("projet py")
root.geometry("600x400")

menu_bar = tk.Menu(root)

# Menu Fichier
file_menu = tk.Menu(menu_bar, tearoff=0)
def new_file():
    notepad.delete(1.0, tk.END)
file_menu.add_command(label="Nouveau", command=new_file)

def open_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "r") as file:
            content = file.read()
            notepad.delete(1.0, tk.END)
            notepad.insert(tk.END, content)
file_menu.add_command(label="Ouvrir", command=open_file)

def save_file():
    content = notepad.get(1.0, tk.END)
    if not content.strip():
        messagebox.showwarning("Attention", "Le contenu est vide.")
        return
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            file.write(content)
file_menu.add_command(label="Enregistrer", command=save_file)

def save_as_file():
    content = notepad.get(1.0, tk.END)
    if not content.strip():
        messagebox.showwarning("Attention", "Le contenu est vide.")
        return
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            file.write(content)
file_menu.add_command(label="Enregistrer Sous", command=save_as_file)

def quit_app():
    root.quit()
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=quit_app)

# Menu Édition
edit_menu = tk.Menu(menu_bar, tearoff=0)
def copy_text():
    root.clipboard_clear()
    text = notepad.get(tk.SEL_FIRST, tk.SEL_LAST)
    root.clipboard_append(text)
edit_menu.add_command(label="Copier", command=copy_text)

def paste_text():
    text = root.clipboard_get()
    notepad.insert(tk.INSERT, text)
edit_menu.add_command(label="Coller", command=paste_text)

# Menu Options
options_menu = tk.Menu(menu_bar, tearoff=0)
def change_font_size():
    size = simpledialog.askinteger("Taille de Police", "Entrez la taille de police:")
    if size:
        notepad.config(font=("Arial", size))
options_menu.add_command(label="Taille de Police", command=change_font_size)

def change_text_color():
    color = tk.colorchooser.askcolor()
    if color:
        notepad.config(fg=color[1])
options_menu.add_command(label="Couleur du Texte", command=change_text_color)

# Menu Outils
outils_menu = tk.Menu(menu_bar, tearoff=0)
def calculatrice():
    calculator_window = tk.Toplevel(root)
    calculator_window.title("Calculatrice")

    calculator_display = tk.Entry(calculator_window, font=("Arial", 14), justify="right")
    calculator_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
    ]

    def button_click(event):
        current_text = calculator_display.get()
        button_text = event.widget.cget("text")
        if button_text == "=":
            try:
                result = eval(current_text)
                calculator_display.delete(0, tk.END)
                calculator_display.insert(tk.END, str(result))
            except Exception as e:
                calculator_display.delete(0, tk.END)
                calculator_display.insert(tk.END, "Error")
        elif button_text == "C":
            calculator_display.delete(0, tk.END)
        else:
            calculator_display.insert(tk.END, button_text)

    for (text, row, column) in buttons:
        button = tk.Button(calculator_window, text=text, width=5, height=2)
        button.grid(row=row, column=column, padx=5, pady=5)
        button.bind("<Button-1>", button_click)

    clear_button = tk.Button(calculator_window, text="C", width=5, height=2)
    clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
    clear_button.bind("<Button-1>", button_click)
outils_menu.add_command(label="Calculatrice ", command=calculatrice)

menu_bar.add_cascade(label="Fichier", menu=file_menu)
menu_bar.add_cascade(label="Édition", menu=edit_menu)
menu_bar.add_cascade(label="Options", menu=options_menu)
menu_bar.add_cascade(label="Outils", menu=outils_menu)

root.config(menu=menu_bar)

# Créer le bloc-notes
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1)
tabControl.pack(expand=1, fill="both")

notepad = tk.Text(tab1)
notepad.pack(expand=True, fill="both")

root.mainloop()
