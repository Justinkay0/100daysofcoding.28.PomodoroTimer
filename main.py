import math
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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global pomo
    window.after_cancel(timer)
    checkmarks.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    pomo = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global pomo
    pomo += 1

    if pomo % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text='BREAK', fg=PINK)
    elif pomo % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text='BREAK', fg=PINK)
        checkmarks.config(text=('✓' * math.ceil(pomo / 2)))
    elif pomo % 2 != 0:
        count_down(WORK_MIN * 60)
        timer_label.config(text='WORK', fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)

    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=100, bg=YELLOW)

# Timer, after is in millisecond

# Creating canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# create photo image to utilise
tomato = tk.PhotoImage(file='tomato.png')
# Place image on canvas
canvas.create_image(100, 112, image=tomato)
# Create text onto tomato
timer_text = canvas.create_text(110, 140, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

# buttons
start = tk.Button(text='Start', command=start_timer)
start.grid(row=2, column=0)
reset_button = tk.Button(text='Reset',command=reset)
reset_button.grid(row=2, column=2)

# timer text
timer_label = tk.Label(text='Timer', font=(FONT_NAME, 45, 'normal'), fg=GREEN, background=YELLOW, highlightthickness=0)
timer_label.grid(row=0, column=1)

# checkmarks
checkmarks = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'normal'))
checkmarks.grid(column=1, row=3)

# Place image on window
canvas.grid(row=1, column=1)


window.mainloop()
