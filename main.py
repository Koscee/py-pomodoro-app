import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
DEFAULT_CAPTION = "Timer"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_id = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_id)
    canvas.itemconfig(timer_text, text="00:00")
    caption_label.config(text=DEFAULT_CAPTION, fg=GREEN)
    check_mark.config(text="")
    start_btn.config(state="active")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_btn.config(state="disabled")

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_break_sec)
        caption_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        caption_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        caption_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    count_sec = f"0{count_sec}" if count_sec < 10 else count_sec

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_id
        timer_id = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # add check mark every time a work session is completed
        if reps % 2 == 0:
            check_mark.config(text=f"{check_mark['text']}✔")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

caption_label = Label(text=DEFAULT_CAPTION, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
caption_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", font=("", 13), padx=6, pady=3, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset",  font=("", 13), padx=6, pady=3, command=reset_timer)
reset_btn.grid(row=2, column=2)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14, "bold"))
check_mark.grid(row=3, column=1)


window.mainloop()
