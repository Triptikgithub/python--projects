from tkinter import *

root = Tk()
root.geometry('500x500')

# entrybox
e = Entry(root, width=56, borderwidth=5)
e.place(x=0, y=0)

# buttons
def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))


b = Button(root, text='1', width=12,command=lambda:click(1))
b.place(x=10, y=60)

b = Button(root, text='2', width=12,command=lambda:click(2))
b.place(x=80, y=60)

b = Button(root, text='3', width=12,command=lambda:click(3))
b.place(x=170, y=60)

b = Button(root, text='4', width=12,command=lambda:click(4))
b.place(x=10, y=120)

b = Button(root, text='5', width=12,command=lambda:click(5))
b.place(x=80, y=120)

b = Button(root, text='6', width=12,command=lambda:click(6))
b.place(x=170, y=120)

b = Button(root, text='7', width=12,command=lambda:click(7))
b.place(x=10, y=180)

b = Button(root, text='8', width=12,command=lambda:click(8))
b.place(x=80, y=180)

b = Button(root, text='9', width=12,command=lambda:click(9))
b.place(x=170, y=180)

b = Button(root, text='0', width=12,command=lambda:click(0))
b.place(x=10, y=240)
#operators
def add():
    n1=e.get()
    global math
    math="addition"
    global i
    i=int(n1)
    e.delete(0,END)

b = Button(root, text='+' ,width=12,command=add)
b.place(x=80, y=240)
def sub():
    n1=e.get()
    global math
    math="subtraction"
    global i
    i=int(n1)
    e.delete(0,END)

b = Button(root, text='-',width=12,command=sub)
b.place(x=170, y=240)
def mul():
    n1=e.get()
    global math
    math="multiplication"
    global i
    i=int(n1)
    e.delete(0,END)

b = Button(root, text='*',width=12,command=mul)
b.place(x=10, y=300)
def div():
    n1=e.get()
    global math
    math="division"
    global i
    i=int(n1)
    e.delete(0,END)

b = Button(root, text='/',width=12,command=div)
b.place(x=80, y=300)
def equal():
    n2=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,i+int(n2))
    elif math=="subtraction":
        e.insert(0,i-int(n2))  
    elif math=="multiplication":
        e.insert(0,i*int(n2))  
    elif math=="division":
        e.insert(0,i/int(n2))            

b = Button(root, text='=' ,width=12,command=equal)
b.place(x=170, y=300)
def clear():
  e.delete(0,END)

b = Button(root, text='clear',width=12,command=clear)
b.place(x=10, y=360)



root.mainloop()