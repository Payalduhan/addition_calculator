from tkinter import *
root =Tk()
'''mylabel1=Label(root,text="hello world")
mylabel2=Label(root,text=" i am payal") 
mylabel1.pack()
mylabel2.pack()'''
#taking input
'''e=Entry(root,width=50,bg="blue",fg="yellow",borderwidth=30)
e.pack()
#creating function
def myclick():
    hello="hello"+" "+e.get()
    mylabel=Label(root,text=hello)
    mylabel.pack()
mybutton=Button(root,text="enter your name",command=myclick,fg="red",bg="blue")
mybutton.pack()'''
#creating simple calculator
root.title("simple calculator")
e=Entry(root,bg="green" ,fg="pink",font=("Arial",16),borderwidth=20)
e.grid(row=0,column=0,columnspan=3)
#e.pack()
def button_add(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
 e.delete(0,END)
def button_plus():
    first_no= e.get()
    global f_num
    f_num=int(first_no)
    e.delete(0,END)
def button_equal():
    second_no=e.get()
    e.delete(0,END)
    e.insert(0,f_num+int(second_no))
mybutton=Button(root,text="1",fg="white",bg="black",padx=40,pady=20,command=lambda: button_add(1))
mybutton2=Button(root,text="2",fg="white",bg="black",padx=40,pady=20,command=lambda: button_add(2))
mybutton3=Button(root,text="3",fg="white",bg="black",padx=40,pady=20,command=lambda: button_add(3))
mybutton4=Button(root,text="4",fg="white",bg="black",padx=40,pady=20,command=lambda: button_add(4))
mybutton5=Button(root,text="5",fg="white",bg="black",padx=40,pady=20,command=lambda: button_add(5))
mybutton6=Button(root,text="6",fg="white",bg="black",padx=40,pady=20,command=lambda: button_add(6))
mybutton7=Button(root,text="7",fg="white",bg="black",padx=40,pady=20,command=lambda: button_add(7))
mybutton8=Button(root,text="8",fg="white",bg="black",padx=40,pady=20,command=lambda: button_add(8))
mybutton9=Button(root,text="9",fg="white",bg="black",padx=40,pady=20,command=lambda: button_add(9))
mybutton0=Button(root,text="0",fg="white",bg="black",padx=40,pady=20,command=lambda:button_add(0))
mybutton_add=Button(root,text="+",fg="white",bg="black",padx=39,pady=20,command=lambda: button_plus())
mybutton_equal=Button(root,text="=",fg="white",bg="black",padx=91,pady=20,command=lambda: button_equal())
mybutton_clear=Button(root,text="clear",fg="white",bg="black",padx=79,pady=20,command=lambda: button_clear())
mybutton_clear=Button(root,text="clear",fg="white",bg="black",padx=79,pady=20,command=lambda: button_clear())
mybutton.grid(row=3,column=0)
mybutton2.grid(row=3 ,column=1)
mybutton3.grid(row=3,column=2)
mybutton4.grid(row=2 ,column=0)
mybutton5.grid(row=2 ,column=1)
mybutton6.grid(row=2,column=2)
mybutton7.grid(row=1 ,column=0)
mybutton8.grid(row=1 ,column=1)
mybutton9.grid(row=1 ,column=2)
mybutton0.grid(row=4,column=0)
mybutton_clear.grid(row=4,column=1,columnspan=2)
mybutton_add.grid(row=5,column=0)
mybutton_equal.grid(row=5,column=1,columnspan=2)

root.mainloop()
