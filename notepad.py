from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    textArea.delete(1.0,END)
def openFile():
    global file
    file =askopenfilename(defaultextension=".txt" , filetypes=[("All Files","*.*"),("Text Document",".txt")])
    if file == "":
        file =None
    else:
        root.title(os.path.basename(file)+ "-Notepad")
        textArea.delete(1.0,END)
        f=open(file,"r")
        textArea.insert(1.0,f.read())
        f.close()



def saveFile():
    global file
    if file ==None:
        file=asksaveasfilename(initialfilename='Unitiled.txt',defaultextension=".txt" ,
                           filetypes=[("All Files","*.*"),("Text Document",".txt")])
        if file == " ":
            file=None
        else:
            f=open(file,'w')
            f.write(textArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+ "-Notepad")
        #print("file saved")
    else:
        f = open(file, 'w')
        f.write(textArea.get(1.0, END))
        f.close()

        # save new file

def quit_app():
    root.destroy()
def cut():
    textArea.event_generate(('<<Cut>>'))
def copy():
    textArea.event_generate(('<<Copy>>'))
def paste():
    textArea.event_generate(('<<Paste>>'))
def about():
    showinfo("Notepad","Notepad by Divya ")

if __name__ == "__main__":
    root =Tk()
    root.title("Untitled-Notepad")
    root.geometry("644x788")
    # text area
    file =None
    textArea =Text(root, font='lucida 13')
    #menu bar
    Menu_bar =Menu(root)
    # file menu
    file_menu=Menu(Menu_bar,tearoff=0)
    # open new file
    file_menu.add_command(label="New",command=newFile)

    # to open existing file
    file_menu.add_command(label="Open", command=openFile)

    #save the current file
    file_menu.add_command(label="Save", command=saveFile)
    file_menu.add_separator()
    file_menu.add_command(label="Exit",command=quit_app)
    Menu_bar.add_cascade(label='File', menu=file_menu)

    root.config(menu=Menu_bar)

    # edit menu
    edit_menu =Menu(Menu_bar, tearoff=0)

    edit_menu.add_command(label='Cut', command= cut)
    edit_menu.add_command(label='copy', command= copy)
    edit_menu.add_command(label='paste', command= paste)
    Menu_bar.add_cascade(label='Edit', menu=edit_menu)

    root.config(menu=Menu_bar)

    # help menu
    help_menu=Menu(Menu_bar, tearoff=0)
    help_menu.add_command(label="About ", command=about)
    Menu_bar.add_cascade(label='Help', menu=help_menu)

    # packing test area

    textArea.pack(expand=True,fill=BOTH)

    # adding scrollbar
    scroll_bar=Scrollbar(textArea)
    scroll_bar.pack(side=RIGHT, fill=Y)
    scroll_bar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll_bar.set)

    root.mainloop()