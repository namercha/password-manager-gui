from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry boxes
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

pw_entry = Entry(width=18)
pw_entry.grid(column=1, row=3)

# Buttons
generate_pwd_button = Button(text="Generate Password")
generate_pwd_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
