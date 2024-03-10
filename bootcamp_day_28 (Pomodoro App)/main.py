from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
REPS = 0
USER_TEXT = "Timer"
COLOR = GREEN

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    global USER_TEXT
    global COLOR
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        title_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif REPS % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        countdown(work_sec)


def countdown(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# setup window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# setup canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Label's
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)
checkmark_label = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
checkmark_label.grid(column=1, row=3)

# start and reset button
start_button = Button(text="Start", bg="white", fg="black", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", bg="white", fg="black", highlightthickness=0)
reset_button.grid(column=2, row=2)
window.mainloop()
