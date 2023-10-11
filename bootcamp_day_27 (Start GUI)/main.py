from tkinter import *
# * imports all classes used in dictionary


def button_clicked():
    label["text"] = user_input.get()  # gets input in entry and returns it as string.


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)  # add free space on edge of window.

# Label
label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
label["text"] = "New Text"
# label.pack()|pack needs to be called in order to create a layout, i can also make adjustments that vary from default.
label.grid(column=0, row=0)
# config() is used to update multiple attributes
# label.config(text="New Text", ...)
label.config(padx=50, pady=50)

# Button 1
button1 = Button(text="Click Me", command=button_clicked, cursor="hand1")
button1.grid(column=1, row=1)

# Button 2
button2 = Button(text="New Button", command=button_clicked, cursor="hand1")
button2.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
user_input.grid(column=3, row=2)


# keep window on screen
window.mainloop()
