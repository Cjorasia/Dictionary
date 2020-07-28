import json
from difflib import get_close_matches
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title = "Dictionary"

word = StringVar()

# exit button
ext = Button(root , text = "Exit", command = root.destroy)
ext.pack()

# enter word Label
lbl = Label(root, text = "Enter word")
lbl.pack(side = LEFT)

# Word Input
ent = Entry(root, bd = 5, textvariable = word)
ent.pack(side = RIGHT)
ent.focus()

#=================================================================================================
def translate():

    global word

    if word.get() in data:
        return data[word.get()]
    elif word.get().title() in data:
        return data[word.get().title()]
    elif word.get().upper() in data:
        return data[word.get().upper()]
    elif len(get_close_matches(word.get(), data.keys())) > 0:
        print("did you mean %s instead" %get_close_matches(word.get(), data.keys()[0]))
        decide = input("y for yes or n for no")
        if decide == "y":
            return data[get_close_matches(word.get(), data.keys())[0]]
        elif decide == "n":
            return ("maybe you have misspelled word!")
        else:
            return ("wrong input!!!")

    else:
        return ("check spelling and try again!")
#========================================================================================================

data = json.load(open("data.json"))

#========================================================================================================
def result():
    output = translate()
    if type(output)== list:
        for item in output:
            messagebox.showinfo("Meaning",item)
    else:
        messagebox.showinfo("Meaning", output)
#=========================================================================================================

# search button
search = Button(root , text = "Search", command = result)
search.pack()

root.mainloop()