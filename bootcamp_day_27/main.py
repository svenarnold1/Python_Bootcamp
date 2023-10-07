import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
label.pack(side="bottom")


# keep window on screen
window.mainloop()
