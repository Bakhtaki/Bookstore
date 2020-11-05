import  os
import  random
from tkinter import Label
import colorama
import tkinter as tk
from tkinter import  *
import backend

def ClearList():
    Listbox1.delete(0,END)

def FillListBox(BookList):
        for each in BookList:
            Listbox1.insert(END,each)

def ViewCommand():
    ClearList()
    Books =backend.Veiw()
    FillListBox(Books)
    
               
def SearchCommand():
    ClearList()
    BookList = backend.search(TitleText.get(),AuthorText.get(),PYearText.get(),ISBNText.get())
    FillListBox(BookList)

def AddCommand():
    backend.insert(TitleText.get(),AuthorText.get(),PYearText.get(),ISBNText.get())
    ViewCommand()

def Get_SelectedRow(event):
    
    global SelectedBook
    if len(Listbox1.curselection())> 0:
        Index = Listbox1.curselection()[0]
        SelectedBook = Listbox1.get(Index)
        Entry1.delete(0,END)
        Entry1.insert(END,SelectedBook[1])
        
        Entry2.delete(0,END)
        Entry2.insert(END,SelectedBook[2])
        
        Entry3.delete(0,END)
        Entry3.insert(END,SelectedBook[3])
        
        Entry4.delete(0,END)
        Entry4.insert(END,SelectedBook[4])
        
def UpdateCommand():
    backend.update(SelectedBook[0],TitleText.get(),AuthorText.get(),PYearText.get(),ISBNText.get())
    ViewCommand()
    
def DeleteCommand():
    backend.delete(SelectedBook[0])
    ViewCommand()

window = tk.Tk()
window.title("Library Managment System")


######################Lables###############################
Label1 = Label(window,text = "Book Title: ")
Label1.grid(row=0,column=0)

Label2 = Label(window,text = "Author: ")
Label2.grid(row=0,column=2)

Label3 = Label(window,text = "Published Year: ")
Label3.grid(row=2,column=0)

Label4 = Label(window,text = "ISBN: ")
Label4.grid(row=2,column=2)

#######################TextBoxes###################################
TitleText  = StringVar()
Entry1= Entry(window,textvariable = TitleText)
Entry1.grid(row=0, column=1)

AuthorText  = StringVar()
Entry2= Entry(window,textvariable = AuthorText)
Entry2.grid(row=0, column=3)

PYearText  = StringVar()
Entry3= Entry(window,textvariable = PYearText)
Entry3.grid(row=2, column=1)

ISBNText  = StringVar()
Entry4= Entry(window,textvariable = ISBNText)
Entry4.grid(row=2, column=3)

#################################ListBox&Scroll#######################################
Listbox1= Listbox(window,width = 35, height = 10)
Listbox1.grid(row=3,column=0, rowspan=6,columnspan=2)

Scrollbar1 = Scrollbar(window)
Scrollbar1.grid(row=2,column=2,rowspan=6)

Listbox1.configure(yscrollcommand = Scrollbar1.set)
Scrollbar1.configure(command = Listbox1.yview)
Listbox1.bind("<<ListboxSelect>>",Get_SelectedRow)

############################# Buttons #######################################
Button1 = Button(window,text ="Veiw All",width = 18,command = lambda:ViewCommand())
Button1.grid(row = 3, column = 3)

Button2 = Button(window,text ="Search",width = 18,command=lambda: SearchCommand())
Button2.grid(row = 4, column = 3)

Button3 = Button(window,text ="Add ",width = 18,command=lambda :AddCommand())
Button3.grid(row = 5, column = 3)

Button4 = Button(window,text ="Update",width = 18,command = lambda: UpdateCommand())
Button4.grid(row = 6, column = 3)

Button5 = Button(window,text ="Delete",width = 18,command= lambda : DeleteCommand() )
Button5.grid(row = 7, column = 3)

Button6 = Button(window,text ="Close",width = 18, command =window.destroy)
Button6.grid(row = 8, column = 3)


window.mainloop()




