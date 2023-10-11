from tkinter import *
# * imports all classes used in dictionary

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
label.pack() # pack needs to be called in order to create a layout, i can also make adjustments that vary from default.

label["text"] = "New Text"
# config() is used to update multiple attributes
# label.config(text="New Text", ...)


def button_clicked():
    label["text"] = user_input.get()  # gets input in entry and returns it as string.


# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
user_input = Entry(cursor="hand1", width=10)
user_input.pack()


# keep window on screen
window.mainloop()
