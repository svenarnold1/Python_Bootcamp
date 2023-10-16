from tkinter import *
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
def start_timer():
    countdown(5)


def countdown(count):
    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count}")
        window.after(1000, countdown, count - 1)

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
