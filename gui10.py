from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title('Notepad')
root.geometry('644x344')
def file1():
    print('Create your New Project')
def New1():
    print('Create New file')
def open1():
    print("Open Your file")
def save1():
    print("Save Your File")
def  print1():
    print("Print data present in your file")

def help():
    print("I will hbelp you")
    tmsg.showinfo('Help', 'Pradhumna Gui help you')

def rate():
    print("Rate us")
    value = tmsg.showinfo("Was your exprience Good?")
    if value == 'yes':
        msg = 'Great.Rate us on our app Please!'
    else:
        msg = "Tell us what went Wrong"
    tmsg.showinfo("Exprience", msg)
menu = Menu(root)

m1 = Menu(menu)
m1.add_command(label='NewProject', command=file1)
m1.add_command(label='New', command=New1)
m1.add_command(label='Open', command=open1)
m1.add_separator()
m1.add_command(label='Save', command=save1)
m1.add_command(label='Print', command=print1)
root.config(menu=menu)

menu.add_cascade(label='File', menu=m1)

m2 = Menu(menu)
m2.add_command(label='Copy', command=file1)
m2.add_command(label='Cut', command=New1)
m2.add_command(label='Paste', command=open1)
m2.add_separator()
m2.add_command(label='Delete', command=save1)
root.config(menu=menu)

menu.add_cascade(label='Edit', menu=m2)

m3 = Menu(menu)
m3.add_command(label='Help', command=help)
m3.add_command(label='Rate us', command=rate)
root.config(menu=menu)
menu.add_cascade(label='Rate', menu=m3)

#menu.config()




root.mainloop()