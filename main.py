from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web = web_entry.get()
    try:
        with open("password_manager.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found.")
    else:
        if web in data:
            messagebox.showinfo(title = web, message=f"Email: {data[web]["email"]}\nPassword: {data[web]["password"]}")
        else:
            messagebox.showinfo(title= "Error", message=f"No details for {web} exists")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    web = web_entry.get()
    id = id_entry.get()
    password = pass_entry.get()
    new_data = {
        web : {
            "email": id,
            "password" : password,
        }
    }

    if len(web) == 0 or len(id) == 0:
        messagebox.showinfo(title= "Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("password_manager.json", "r") as password_data:
                data = json.load(password_data)
        except FileNotFoundError:
            with open("password_manager.json", "w") as password_data:
                json.dump(new_data, password_data, indent=4)
        else:
            data.update(new_data)
            with open("password_manager.json", "w") as password_data:
                json.dump(data, password_data, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)
canvas = Canvas(width = 200, height = 200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column = 2, row = 1)

website = Label(text= "Website:", font= ('Arial', 12))
website.grid(column=1, row=2)
id_input = Label(text= "Email/Username:", font = ('Arial', 12))
id_input.grid(column=1, row=3)
passwd = Label(text= "Password:", font = ("Arial", 12))
passwd.grid(column=1, row=4)

web_entry = Entry(width = 32)
web_entry.grid(column=2, row=2)
web_entry.focus()

id_entry = Entry(width = 50)
id_entry.grid(column=2, row=3, columnspan=2)
#id_entry.insert(END, "YOUR EMAIL")

pass_entry = Entry(width = 32)
pass_entry.grid(column =2, row=4)

gen_passwd = Button(text = "Generate password", command = generate_password)
gen_passwd.grid(column = 3, row=4)

add_button = Button(text = "Add", width = 43, command= add_info)
add_button.grid(column=2, row= 5, columnspan = 2)

search_button = Button(text= "Search", width= 14, command= find_password)
search_button.grid(column=3, row=2)






window.mainloop()


