from tkinter import *
FONT_NAME = "Arial"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# setup window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="#FFFFFF")


# setup canvas
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
canvas.grid(column=1, row=0)

# Label's
url_label = Label(text="Website:", bg="white", font=(FONT_NAME, 8, "bold"))
url_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:", bg="white", font=(FONT_NAME, 8, "bold"))
username_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white", font=(FONT_NAME, 8, "bold"))
password_label.grid(column=0, row=3)

# # Entries
# url_entry = Entry(width=35, columnspan=2)
# # Add some text to begin with
# url_entry.insert(END, string="www.example.com")
# url_entry.pack(column=1, row=1)

# setup buttons
generate_button = Button(text="Generate Password", bg="white", fg="black", highlightthickness=0)
generate_button.grid(column=3, row=3)


add_button = Button(text="Add", bg="white", fg="black", highlightthickness=0)
add_button.grid(column=2, row=4)

window.mainloop()

