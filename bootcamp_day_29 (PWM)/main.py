from tkinter import *
FONT_NAME = "Arial"
FONT = (FONT_NAME, 10, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = url_entry.get()
    email = user_entry.get()
    pw = pw_entry.get()
    file = open("C:\Desktop\data.txt", "a")
    file.write(f"Website: {website} | Email: {email} | Password: {pw}\n")
    file.close()
    # clear entries to be ready for next input
    url_entry.delete(0, END)
    pw_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


# setup window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#FFFFFF")


# setup canvas
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label's
url_label = Label(text="Website:", bg="white", font=FONT)
url_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:", bg="white", font=FONT)
username_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white", font=FONT)
password_label.grid(column=0, row=3)

# Entries
url_entry = Entry(width=35)
url_entry.focus()
url_entry.grid(column=1, row=1, columnspan=2)

user_entry = Entry(width=35)
user_entry.insert(END, string="user.pattern@gmail.com")
user_entry.grid(column=1, row=2, columnspan=2)

pw_entry = Entry(width=21, show="*")
pw_entry.grid(column=1, row=3)

# setup buttons
generate_button = Button(text="Generate Password", bg="white")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", bg="white", width=30, command=save())
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

