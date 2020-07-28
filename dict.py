import json
from difflib import get_close_matches
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Dictionary")

word = StringVar()

                            # EXIT FUNCTION #
#=========================================================================================================================#
def ExitApplication():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')

    if MsgBox == 'yes':
       root.destroy()

    else:
        messagebox.showinfo('Return','You will now return to the application screen')
#=========================================================================================================================#

# exit button

                            # TRANSLATE FUNCTION # 
#=================================================================================================#
def translate():

    global word

    if word.get() in data:
        return data[word.get()]

    elif word.get().title() in data:
        return data[word.get().title()]

    elif word.get().upper() in data:
        return data[word.get().upper()]

    elif word.get().lower() in data:
        return data[word.get().lower()]

    elif len(get_close_matches(word.get(), data.keys())) > 0:
        decide = messagebox.askyesno("No Match Found!",f"did you mean {get_close_matches(word.get(), data.keys())[0]} instead")
        if decide == True:
            return data[get_close_matches(word.get(), data.keys())[0]]
        elif decide == False:
            return ("maybe you have misspelled word!")

    else:
        return ("check spelling and try again!")
#====================================================================================================#

data = json.load(open("data.json"))

                                # RESULT FUNCTION #
#=====================================================================================================#
def result():
    output = translate()

    if type(output)== list:
        for item in output:
            messagebox.showinfo("Meaning",item)

    else:
        messagebox.showinfo("Meaning", output)
#======================================================================================================#

ext = Button (root, text='Exit',command=ExitApplication,bg='#D50000',fg='white',activebackground='#EA0000',activeforeground="white",cursor="hand2")
ext.pack(side = RIGHT)

# enter word Label
lbl = Label(root, text = "Enter word")
lbl.pack(side = LEFT)

# Word Input
ent = Entry(root, bd = 3, textvariable = word)
ent.pack(side = LEFT)
ent.focus()


# search button
search = Button(root , text = "Search", command = result, bg='skyblue',fg='black',cursor="hand2")
search.pack(side = RIGHT)

root.mainloop()