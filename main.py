import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generator():
    #Password Generator Project  
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []
    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    for char in range(nr_symbols):
        password_list += random.choice(symbols)
    for char in range(nr_numbers):
        password_list += random.choice(numbers)
    random.shuffle(password_list)
    password = ""
    password="".join(password_list)
    for char in password_list:
         password += char
    # print(password)
    pyperclip.copy(password)
    password_entry.insert(0,string=password)
    messagebox.showinfo(title="Clipboard",message="Password Copied to Clipboard!")#%50N%%MbZqU1M6oNk



#---------------------------- SEARCH FUNCTIONALITY ------------------------------- #



def search():
    #Used to implement the search functionality
    #print("Search Button pressed!")
    c=0
    with open("passwords.json",mode="r") as xyz:
        data=json.load(xyz)
        try:
            messagebox.showinfo(title="Record Found!",message=f"Website:{website_entry.get()}\nEmail/Username:{data[website_entry.get()]["email"]}\nPassword:{data[website_entry.get()]["password"]}")
        except KeyError:
            messagebox.showinfo(title="Search Result",message="Sorry!No Record Found")
        
                      
    
#---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    #print("Add button clicked!")
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website)*len(email)*len(password)>0:
        is_ok=messagebox.askokcancel(title="Status of data entered",message=f"These are the details entered:\nEmail:{email}\nPassword:{password}.\nDo you want to save this?")       
        
        if is_ok:
            try:
                with open("day#30(Upgradation of Password Manager App)\passwords.json",mode="r") as xyz:
                    #reading old data
                    data=json.load(xyz)#Used to read the contents of the JSON file
                    #Updating old data with new data
                    data.update(new_data)#Used to add the new data to the existing JSON file

                with open("day#30(Upgradation of Password Manager App)\passwords.json",mode="w") as xyz:
                    #Writing the new data to the existing file and saving the updated data
                    json.dump(data,xyz,indent=4)#dump method is used to write to a json file
                    
            except FileNotFoundError:
                with open("day#30(Upgradation of Password Manager App)\passwords.json",mode="w") as xyz:
                    json.dump(new_data,xyz,indent=4)
            finally:
                website_entry.delete(0,tkinter.END)
                password_entry.delete(0,tkinter.END)
    else:

        messagebox.showwarning(title="Status of data entered",message="Some of the fields are empty.Please review entered data once more.")



# ---------------------------- UI SETUP ------------------------------- #



window=tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)



#labels
window_label=tkinter.Label(text="Window:")#font=(FONT_NAME,10,"bold"))
window_label.grid(column=0,row=1)



email_label=tkinter.Label(text="Email/Username:")#font=(FONT_NAME,10,"bold"))
email_label.grid(column=0,row=2)



password_label=tkinter.Label(text="Password:")#,font=(FONT_NAME,10,"bold"))
password_label.grid(column=0,row=3)



##buttons
generator_button = tkinter.Button(text="Generate Password",width=14,command=generator)
generator_button.grid(column=2,row=3,columnspan=1)



add_button=tkinter.Button(text="Add",command=add,width=46)
add_button.grid(column=1,row=4,columnspan=2)



search_button=tkinter.Button(text="Search",command=search,width=14)
search_button.grid(column=2,row=1,columnspan=1)



##Entries
website_entry=tkinter.Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=1)
website_entry.focus()



email_entry=tkinter.Entry(width=54)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"deysoumyadeep110@gmail.com")



password_entry=tkinter.Entry(width=35)
password_entry.grid(column=1,row=3,columnspan=1)



##Putting the image on canvas
canvas=tkinter.Canvas(height=200,width=200,highlightthickness=0)
logo_image=tkinter.PhotoImage(file="day#30(Upgradation of Password Manager App)\logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)



window.mainloop()