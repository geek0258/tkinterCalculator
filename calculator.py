from tkinter import *
from tkinter import messagebox
def sddddddddddddfdsfwe():
    if(a.get()=='' or b.get()==''):
        messagebox.showerror('Error', 'input box is not null')
    elif(not a.get().isdigit() or not b.get().isdigit()):
        messagebox.showerror('Error', 'aldaa')
    else:
        sum1 = str(int(a.get())+int(b.get()))
        c.set(sum1)
def sdfstscsdt():
    if(d.get()=='' or e.get()==''):
        messagebox.showerror('Error', 'input box is not null')
    elif(not d.get().isdigit() or not e.get().isdigit()):
        messagebox.showerror('Error', 'aldaa')
    else:
        sum1 = str(int(d.get())-int(e.get()))
        f.set(sum1)
mainWindow  = Tk()
mainWindow.geometry("400x300")
mainWindow["bg"] = "green"
a = StringVar()
b = StringVar()
c = StringVar()
aInput = Entry(mainWindow, textvariable = a).grid(row=0, column=0)
plus = Label(mainWindow, text="+").grid(row=0, column=1)
bInput = Entry(mainWindow, textvariable = b).grid(row=0, column=2)
equal = Label(mainWindow, text="=").grid(row=0, column=3)
cInput = Entry(mainWindow, textvariable = c).grid(row=0, column=4)
button = Button(mainWindow, text="nemeh", command = sddddddddddddfdsfwe, bg="red")
button.place(x=250, y=80)

d = StringVar()
e = StringVar()
f = StringVar()
dInput = Entry(mainWindow, textvariable = d).grid(row=1, column=0)
sub = Label(mainWindow, text="-").grid(row=1, column=1)
eInput = Entry(mainWindow, textvariable = e).grid(row=1, column=2)
equal1 = Label(mainWindow, text="=").grid(row=1, column=3)
fInput = Entry(mainWindow, textvariable = f).grid(row=1, column=4)
button1 = Button(mainWindow, text="hasah", command = sdfstscsdt)
button1.place(x=150, y=80)

mainWindow.mainloop()
