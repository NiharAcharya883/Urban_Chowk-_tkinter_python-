from tkinter import *
from Honest import *
from Lapinoz import *
from HL_Frankie import *

root = Tk()
root.geometry("600x600")
root.title("Urban Chawk")

H1 = Label(root,text="Urban Chowk",bg="red",fg="white",font=("Arial bold",28),width=12).grid(row=0,column=2,padx=10,pady=10)

B1 = Button(root,text="Honest",bg="black",fg="white",font=("Arial bold",20),width=8,command=Honest).grid(row=1,column=2,padx=10,pady=10)

B2 =Button(root,text="Lapinoz",bg="black",fg="white",font=("Arial bold",20),width=8,command=Lapinoz).grid(row=2,column=2,padx=10,pady=10)

B3 = Button(root,text="HL Frankie",bg="black",fg="white",font=("Arial bold",20),width=8,command=HL_Frankie).grid(row=3,column=2,padx=10,pady=10)

quitt=Button(root,text="Quit",bg="black",fg="white",font=("Arial bold",20),command=root.destroy).grid(row=4,column=3,padx=10,pady=10)

root.mainloop()
