import time
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
pomo = 0
countdown = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    pass


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

# buttons
start = tk.Button(text='Start')
start.grid(row=2, column=0)
reset = tk.Button(text='Reset')
reset.grid(row=2, column=2)

# timer text
timer_label = tk.Label(text='Timer', font=(FONT_NAME, 45, 'normal'), fg=GREEN, background=YELLOW, highlightthickness=0)
timer_label.grid(row=0, column=1)

# checkmarks
checkmarks = tk.Label(text='✓', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'normal'))
checkmarks.grid(column=1, row=3)

# Place image on window
canvas.grid(row=1, column=1)


window.mainloop()
