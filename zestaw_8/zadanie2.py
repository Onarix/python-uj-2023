import PyPDF2
import tkinter as tk
from tkinter import filedialog

okno = tk.Tk()
okno.title("My PDF text extractor")
okno.resizable(True, True)

# Create a Frame to hold the Text widget
text_frame = tk.Frame(okno)
text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Add a resizable Text widget inside the Frame
text = tk.Text(text_frame, wrap=tk.WORD, width=80, height=20)
text.pack(fill=tk.BOTH, expand=True)


def clear_text():
    text.delete(1.0, tk.END)


def open_pdf():
    file = filedialog.askopenfilename(
        title="Select a PDF", filetype=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
    )
    if file:
        pdf_file = PyPDF2.PdfReader(file)
        for i in range(len(pdf_file.pages)):
            page = pdf_file.pages[i]
            content = page.extract_text()
            text.insert(tk.END, content)


def quit_app():
    okno.destroy()


# Create Menu and its structure
menu_bar = tk.Menu(okno)
okno.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_app)

okno.mainloop()
