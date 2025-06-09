from tkinter import *
import pickle

dict1 = {}

def add():
    fname = textbox1.get()
    lname = textbox2.get()
    number = textbox3.get()
    dict1.update({number: fname + " " + lname})
    label5.config(text="Saved")
    
    try:
        with open("info.pickle", "rb") as f:
            data = pickle.load(f)
    except:
        data = {}
        
    data.update(dict1)
    with open("info.pickle", "wb") as f:
        pickle.dump(data, f)

def delete():
    listbox1.delete(0, END)
    phone = textbox4.get()
    try:
        with open("info.pickle", "rb") as f:
            loaddel = pickle.load(f)
        if phone in loaddel:
            del loaddel[phone]
            with open("info.pickle", "wb") as f:
                pickle.dump(loaddel, f)
            listbox1.insert(1, "Deleted successfully")
        else:
            listbox1.insert(1, "Number not found")
    except:
        listbox1.insert(1, "Error: Could not delete the number")

def search():
    listbox1.delete(0, END)
    phone2 = textbox4.get()
    try:
        with open("info.pickle", "rb") as f:
            loads = pickle.load(f)
            if phone2 in loads:
                listbox1.insert(1, f"Phone number found: {loads[phone2]}")
            else:
                listbox1.insert(1, "Phone number not found")
    except:
        listbox1.insert(1, "Error: Could not search")

def show_all():
    listbox1.delete(0, END)
    try:
        with open("info.pickle", "rb") as f:
            loadsh = pickle.load(f)
            for number, name in loadsh.items():
                listbox1.insert(END, f"{number}: {name}")
    except:
        listbox1.insert(1, "No data available")


root = Tk()
root.geometry("500x500")
root.title("Phonebook")
root.config(bg="orange")

label1 = Label(root, text="Enter your name:")
label1.grid(row=0, column=0)

label2 = Label(root, text="Enter your lastname:")
label2.grid(row=1, column=0)

label3 = Label(root, text="Enter your phone number:")
label3.grid(row=2, column=0)

textbox1 = Entry(root)
textbox1.grid(row=0, column=1)

textbox2 = Entry(root)
textbox2.grid(row=1, column=1)

textbox3 = Entry(root)
textbox3.grid(row=2, column=1)

btn1 = Button(root, text="Add", command=lambda: add())
btn1.grid(row=3, column=1)

label5 = Label(root)
label5.grid(row=4, column=0)

label4 = Label(root, text="Search your phone number:")
label4.grid(row=5, column=0)

textbox4 = Entry(root)
textbox4.grid(row=5, column=1)

btn2 = Button(root, text="Delete", command=lambda: delete())
btn2.grid(row=7, column=0)

btn3 = Button(root, text="Search", command=lambda: search())
btn3.grid(row=7, column=1)

btn4 = Button(root, text="Show All", command=lambda: show_all())
btn4.grid(row=7, column=2)

listbox1 = Listbox(root)
listbox1.grid(row=6, column=1)

root.mainloop()
