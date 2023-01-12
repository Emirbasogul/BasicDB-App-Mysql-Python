from tkinter import *
import customtkinter


#We set the backgrounds-themes
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#mainframe
root = customtkinter.CTk()
root.geometry("1000x1000")

# login func prints the results.
def login():
    print("test")
    print(username.get()) #username.get() gives us the username that has been written when the login button pressed
    print(surname.get())

#we defined username and surname global bcs we need to reach them in other classes.
global username
global surname

# We defined main frame.
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# The text "information page"
label = customtkinter.CTkLabel(master=frame, text="Information Page")
label.pack(pady=12, padx=10)

# Get the username and surname with Stringvar() command
username = StringVar()
surname = StringVar()

# An entry block to enter a name.
entryName = customtkinter.CTkEntry(master=frame, placeholder_text="Name", textvariable=username)
entryName.pack(pady=12, padx=10)

# An entry block to enter a name.
entrySurname = customtkinter.CTkEntry(master=frame, placeholder_text="Surname", textvariable=surname)
entrySurname.pack(pady=12, padx=10)

# A button to submit the writtens.
button = customtkinter.CTkButton(master=frame, text="Save", command=login)
button.pack(pady=12, padx=10)

root.mainloop()
