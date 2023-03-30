import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=100, bg=YELLOW)

# Creating canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# create photo image to utilise
tomato = tk.PhotoImage(file='tomato.png')
# Place image on canvas
canvas.create_image(100, 112, image=tomato)
# Create text onto tomato
canvas.create_text(110, 140, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

# Place image on window
canvas.pack()

window.mainloop()
