from tkinter import *
import pymysql.cursors
import customtkinter

from tkinter import ttk, messagebox

# ***********mysql - Connection & making main tables*********


#       CONNECTION

connection = pymysql.connect(host="localhost",
                             user="root",
                             password="****",
                             database="the db name",
                             cursorclass=pymysql.cursors.DictCursor)
cur = connection.cursor()



#       TABLES

cur.execute("""CREATE TABLE customer (ssn INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL,surname VARCHAR(255) NOT NULL,adress VARCHAR(255),dob DATE, tel INT NOT NULL)""")

cur.execute("""CREATE TABLE product (product_code INT AUTO_INCREMENT PRIMARY KEY,brand VARCHAR(255) NOT NULL,product_name VARCHAR(255) NOT NULL)""")



#   BASIC SQL DATA IMPLEMENTATION

sql = """INSERT INTO pythondeneme.customer (ssn, name,surname, adress, dob, tel) VALUES (%s, %s, %s, %s, %s, %s)"""
val = [
    ('11111', 'emir', 'basogul', 'The adress is set.', '01.01.2002', '4440444'),
    ('22222', 'mine', 'tugay', 'The adress is set.', '01.01.2002', '4440444'),
    ('33333', 'onur', 'akcay', 'The adress is set.', '01.01.2001', '4440444'),
    ('44444', 'nese', 'gündogdu', 'The adress is set.', '01.01.2000', '4440444'),
    ('55555', 'ali', 'halicioglu', 'The adress is set.', '01.01.200', '4440444'),
    ('66666', 'onur', 'göl', 'The adress is set.', '01.01.2000', '4440444'),
    ('77777', 'tuna', 'tavus', 'The adress is set.', '01.01.2001', '4440444'),
    ('88888', 'elon', 'musk', 'USA, California, San Francisko, siliconvalley street sok no 1', '01.01.2001', '4440444')
]

cur.executemany(sql, val)


#   BASIC SQL DATA IMPLEMENTATION

sql = """INSERT INTO pythondeneme.product (product_code, brand,product_name) VALUES (%s, %s, %s)"""
val = [
    ('112', 'arcelik', 'iron'),
    ('113', 'arcelik', 'television'),
    ('001', 'istikbal', 'sofa'),
    ('002', 'istikbal', 'pillow'),
    ('222', 'bellona', 'pillow'),
    ('220', 'bellona', 'cupboard'),
    ('235', 'bellona', 'commode')

]

cur.executemany(sql, val)



# ***********  GUI part starts *********

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# mainframe
root = customtkinter.CTk()
root.geometry("500x1000")


# login func prints the values when we press the save button. It is an temprory function.
def login():
    print("test")
    print(username.get())  # username.get() gives us the username that has been written when the login button pressed
    print(surname.get())


# This func will be improved
def register_data():

        sql = """INSERT INTO pythondeneme.customer (ssn, name,surname, adress, dob, tel) VALUES (%s, %s, %s, %s, %s, %s)"""
        val = [
            (ssn, username, surname, adress, dob, tel)
        ]

        cur.executemany(sql, val)

        sql = """INSERT INTO pythondeneme.product (product_code, brand,product_name) VALUES (%s, %s, %s)"""
        val = [
            (productCode, brand, productName)

        ]


# we defined username and surname global bcs we need to reach them in other classes.
global username
global surname
global ssn
global dob
global tel
global adress
global productCode
global productName
global brand

# Get the username and surname with Stringvar() command
username = StringVar()
surname = StringVar()
ssn = StringVar()
dob = StringVar()
tel = StringVar()
adress = StringVar()
productCode = StringVar()
productName = StringVar()
brand = StringVar()

# The text "information page"
label = customtkinter.CTkLabel(master=root, text="Hi, please enter your contact informations. Thanks!",
                               font=customtkinter.CTkFont(size=15, weight="bold"))


# We defined main frame 1
frame1 = customtkinter.CTkFrame(master=root, width=300, height=600,)
frame1.grid(row=0, column=0, rowspan=4,padx=(20, 0), pady=(20, 20), sticky="nsew")


# We defined main frame 2
frame2 = customtkinter.CTkFrame(master=root, width=300, height=600,)
frame2.grid(row=0, column=1, columnspan=4, padx=(20, 0), pady=(20, 20), sticky="nsew")




# the text username
label = customtkinter.CTkLabel(master=frame1, text="Username")
label.pack(pady=1, padx=10)

# An entry block to enter a name.
entryName = customtkinter.CTkEntry(master=frame1, placeholder_text="Name", textvariable=username)
entryName.pack(pady=1, padx=10)

#           empty label.
label = customtkinter.CTkLabel(master=frame1, text="")
label.pack(pady=1, padx=10)



# the text surname
label = customtkinter.CTkLabel(master=frame1, text="Surname")
label.pack(pady=1, padx=10)

# An entry block to enter a surname.
entrySurname = customtkinter.CTkEntry(master=frame1, placeholder_text="Surname", textvariable=surname)
entrySurname.pack(pady=1, padx=10)

#           empty label.
label = customtkinter.CTkLabel(master=frame1, text="")
label.pack(pady=2, padx=10)




# A button to submit the writtens.
button = customtkinter.CTkButton(master=frame1, text="Save", command=login)
button.pack(pady=4, padx=10)

#           empty label.
label = customtkinter.CTkLabel(master=frame1, text="")
label.pack(pady=1, padx=10)



# the text ssn
label = customtkinter.CTkLabel(master=frame1, text="SSN Number")
label.pack(pady=1, padx=10)

# An entry block to enter a ssn.
entryName = customtkinter.CTkEntry(master=frame1, placeholder_text="SSN", textvariable=ssn)
entryName.pack(pady=1, padx=10)

#           empty label.
label = customtkinter.CTkLabel(master=frame1, text="")
label.pack(pady=1, padx=10)



# the text Date of birth
label = customtkinter.CTkLabel(master=frame1, text="date of birth")
label.pack(pady=1, padx=10)

# An entry block to enter a Dob.
entryName = customtkinter.CTkEntry(master=frame1, placeholder_text="date of birth", textvariable=dob)
entryName.pack(pady=1, padx=10)

#           empty label.
label = customtkinter.CTkLabel(master=frame1, text="")
label.pack(pady=1, padx=10)



# the text tel
label = customtkinter.CTkLabel(master=frame1, text="telephone number")
label.pack(pady=1, padx=10)

# An entry block to enter a telephone number.
entryName = customtkinter.CTkEntry(master=frame1, placeholder_text="telephone number", textvariable=tel)
entryName.pack(pady=1, padx=10)

#           empty label.
label = customtkinter.CTkLabel(master=frame1, text="")
label.pack(pady=1, padx=10)


# the text adress
label = customtkinter.CTkLabel(master=frame1, text="Delivery Adress")
label.pack(pady=1, padx=10)

# An entry block to enter adress.
entryName = customtkinter.CTkEntry(master=frame1, placeholder_text="Write your adress detailed", textvariable=adress)
entryName.pack(pady=1, padx=10)

#           empty label.
label = customtkinter.CTkLabel(master=frame1, text="")
label.pack(pady=1, padx=10)



# the text productName
label = customtkinter.CTkLabel(master=frame2, text="Product Name")
label.pack(pady=1, padx=10)

# An entry block to enter a product Name.
entryName = customtkinter.CTkEntry(master=frame2, placeholder_text="Product Name", textvariable=productName)
entryName.pack(pady=1, padx=10)

#           empty label.
label = customtkinter.CTkLabel(master=frame2, text="")
label.pack(pady=1, padx=10)



# the text productCode
label = customtkinter.CTkLabel(master=frame2, text="Product Code")
label.pack(pady=1, padx=10)

# An entry block to enter a Product Code.
entryName = customtkinter.CTkEntry(master=frame2, placeholder_text="Product code", textvariable=productCode)
entryName.pack(pady=1, padx=10)

#           empty label.
label = customtkinter.CTkLabel(master=frame2, text="")
label.pack(pady=1, padx=10)



# the text Brand
label = customtkinter.CTkLabel(master=frame2, text="Brand of the product")
label.pack(pady=1, padx=10)

# An entry block to enter a brand.
entryName = customtkinter.CTkEntry(master=frame2, placeholder_text="Brand", textvariable=brand)
entryName.pack(pady=1, padx=10)

# Empty label.
label = customtkinter.CTkLabel(master=frame2, text="")
label.pack(pady=1, padx=10)



root.mainloop()
