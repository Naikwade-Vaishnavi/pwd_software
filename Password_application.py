#from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import random
import glob
from tkinter import messagebox

root = tk.Tk()
root.title('Image')
root.state('zoomed')
root.config(bg='black')
#root.geometry("1200x700")

global my_label
global pwd

passw_var = tk.StringVar()
name_var=tk.StringVar()

#to start new window
def newin():

    password = passw_var.get()
    passw_var.set("")
    name = name_var.get()
    name_var.set("")
    
    if password == "Kashmir" :
        root.destroy()
        messagebox.showinfo("information","Welcome")
    elif password == "Kerala" :
        root.destroy()
        messagebox.showinfo("information","Welcome")
    elif password == "Telangana" :
        root.destroy()
        messagebox.showinfo("information","Welcome")
    elif password == "Odisha" :
        root.destroy()
        messagebox.showinfo("information","Welcome")
    elif password == "Rajasthan" :
        root.destroy()
        messagebox.showinfo("information","Welcome")
    elif password == "Maharashtra" :
        root.destroy()
        messagebox.showinfo("information","Welcome")
    elif password == "Punjab" :
        root.destroy()
        messagebox.showinfo("information","Welcome")
    elif password == "Karnataka" :
        root.destroy()
        messagebox.showinfo("information","Welcome")
    elif password == "Delhi" :
        root.destroy()
        messagebox.showinfo("information","Welcome")
    elif password == "UttarPradesh" :
        root.destroy()
        messagebox.showinfo("information","Welcome")
    elif password == "UttarPradesh" :
        root.destroy()
        messagebox.showinfo("information","Welcome")
    elif password == "Goa" :
        root.destroy()
        messagebox.showinfo("information","Welcome")
    
    else:
        messagebox.showinfo("information","Wrong Password\nTry Again")

# TO Load random Images and the images should be in same folder as that of the source code file .

# Add more images..........  .................

rdm_img = ["a1.jpg","a2.jpg","a3.jpg","a4.jpg","a6.jpg","a7.jpg","a8.jpg","a9.jpg","a10.jpg","a11.jpg","a12.jpg","a13.jpg"]

a1 = glob.glob("D:\python program by me\Practise\image_loading\a1.jpg")
a2 = glob.glob("D:\python program by me\Practise\image_loading\a2.jpg")
a3 = glob.glob("D:\python program by me\Practise\image_loading\a3.jpg")
a4 = glob.glob("D:\python program by me\Practise\image_loading\a4.jpg")
a6 = glob.glob("D:\python program by me\Practise\image_loading\a6.jpg")
a7 = glob.glob("D:\python program by me\Practise\image_loading\a7.jpg")
a8 = glob.glob("D:\python program by me\Practise\image_loading\a8.jpg")
a9 = glob.glob("D:\python program by me\Practise\image_loading\a9.jpg")
a10 = glob.glob("D:\python program by me\Practise\image_loading\a10.jpg")
a11 = glob.glob("D:\python program by me\Practise\image_loading\a11.jpg")
a12 = glob.glob("D:\python program by me\Practise\image_loading\a12.jpg")
a13 = glob.glob("D:\python program by me\Practise\image_loading\a13.jpg")

my_img = ImageTk.PhotoImage(Image.open(random.choice(rdm_img)))
my_label = tk.Label(image=my_img)
#my_label.pack(side=LEFT)
my_label.place(x = 125,y = 130)

#LOGO Image
my_img1 = ImageTk.PhotoImage(Image.open("logo.jpg")) 
my_label1 = tk.Label(image=my_img1)
my_label1.place(x = 1200,y = 170)


# Password
pwdl = tk.Label(root,text = "Password",bg = "black",fg = "white",font = "arial 25").place(x = 1180,y = 370)
pwd = tk.Entry(root,textvariable = passw_var,width=15,bd=2,font = 60,show = "*").place(x = 1170,y = 470)

#Adding frame

f1 = tk.Frame(root,bg="white",width=10,height=1000).place(x = 900,y = 0)

button = tk.Button(root,text=" Login ",fg="white",bg="black",width=10,height=2,font=20,command=newin)
button.place(x=1190,y=570)

root.mainloop()
