import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
from tkcalendar import Calendar

okno = tk.Tk()
okno.title("Zegar i kalendarz")

# Set the window size to a fixed value (width x height)
okno.geometry("400x400")

# Make the window non-resizable
okno.resizable(False, False)

# utwórz StringVar()
date_time = StringVar(okno)


def update_date_time():
    # Pobierz aktualną datę i czas
    current_time = datetime.now()

    # Przygotuj string z datą i czasem
    dt = current_time.strftime("%A, %d %B %Y %H:%M:%S")

    # Ustaw wartość dla StringVar
    date_time.set(dt)

    # Rekurencyjne odświeżanie etykiety co 1000 ms (1 sekunda)
    okno.after(1000, update_date_time)


current_time = datetime.now()

date_time_label = Label(
    okno,
    textvariable=date_time,
    font=("Arial", 14),
    background="white",
    padx=10,
    pady=10,
)
date_time_label.pack(anchor="center")

cal = Calendar(
    okno,
    selectmode="day",
    year=datetime.now().year,
    month=datetime.now().month,
    day=datetime.now().day,
)
cal.pack(pady=10)

update_date_time()

okno.mainloop()
