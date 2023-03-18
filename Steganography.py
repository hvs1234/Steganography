#Libraries
from tkinter import *
from tkinter import messagebox,filedialog
from stegano import lsb
import os
from PIL import Image,ImageTk

#Application Setup
root = Tk()
root.title("Steganography")
root.resizable(False,False)
root.geometry("700x500+340+80")
root.configure(bg="#2f4155")

#Functions
def open_file():
    global file
    file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                      title="Select File",
                                      filetype=(("PNG File","*.png"),
                                                 ("JPG File","*.jpg"),
                                                 ("All Files","*.txt")))
    image_open = Image.open(file)
    image_open = ImageTk.PhotoImage(image_open)
    f1_l1.config(image=image_open,width=250,height=250)
    f1_l1.image=image_open


def hide():
    global secret
    message = t1.get(1.0,END)
    secret = lsb.hide(str(file), message)

def show():
    clear_message = lsb.reveal(file)
    t1.delete(1.0, END)
    t1.insert(END, clear_message)

def save_file():
    secret.save("hidden.png")


#Application Creation
img1 = PhotoImage(file="E:\\pyImages\\steganography logo.png")
img2 = PhotoImage(file="E:\\pyImages\\access.png")
root.iconphoto(False,img1)
l1 = Label(root,image=img2,bg="#2f4155")
l1.place(x=10,y=0)
l2 = Label(root,text="CYBER SCIENCE",bg="#2f4155",fg="#fff",font="Algerian 25 bold")
l2.place(x=100,y=20)
f1 = Frame(root,bd=4,width=340,height=280,bg="black",relief=RAISED)
f1.place(x=10,y=80)
f1_l1 = Label(f1,bg="black") ; f1_l1.place(x=40,y=10)
f2 = Frame(root,width=340,height=280,bg="white",bd=4,relief=GROOVE)
f2.place(x=350,y=80)
t1 = Text(f2,bg="slate blue",fg="aqua",font="Roboto 20 bold",
relief=GROOVE,cursor="hand2",wrap=WORD)
t1.place(x=0,y=0,width=330,height=270)
sc1 = Scrollbar(f2)
sc1.place(x=320,y=0,height=300) ; sc1.configure(command=t1.yview) ; 
t1.configure(yscrollcommand=sc1.set)
f3 = Frame(root,bd=4,relief=GROOVE,width=330,height=100,bg="#2f4155")
f3.place(x=10,y=370)
btn1 = Button(f3,text="Open Image",width=10,height=2,font="Arial 14 bold",fg="cyan",bg="#2f4155",
activebackground="#2f4155",activeforeground="cyan",command=open_file)
btn1.place(x=20,y=30)
btn2 = Button(f3,text="Save Image",width=10,height=2,font="Arial 14 bold",fg="cyan",bg="#2f4155",
activebackground="#2f4155",activeforeground="cyan",command=save_file)
btn2.place(x=180,y=30)
f3_l1 = Label(f3,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)
f4 = Frame(root,bd=4,relief=GROOVE,width=330,height=100,bg="#2f4155")
f4.place(x=360,y=370)
btn3 = Button(f4,text="Hide Data",width=10,height=2,font="Arial 14 bold",fg="cyan",bg="#2f4155",
activebackground="#2f4155",activeforeground="cyan",command=hide)
btn3.place(x=20,y=30)
btn4 = Button(f4,text="Show Data",width=10,height=2,font="Arial 14 bold",fg="cyan",bg="#2f4155",
activebackground="#2f4155",activeforeground="cyan",command=show)
btn4.place(x=180,y=30)
f4_l1 = Label(f4,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

root.mainloop()
