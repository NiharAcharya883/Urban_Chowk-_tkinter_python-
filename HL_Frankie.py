from tkinter import *
from tkinter import messagebox
import mysql.connector as m
import random
#HL Frankie
def view_bill():
    global paneerF,cheeseF,specialF,price,order_id,Name,Number
    paneerF = E1.get()
    cheeseF = E2.get()
    specialF = E3.get()
    Name = name.get()
    Number = Num.get()
    if paneerF =="":
        paneerF = 0
    if cheeseF =="":
        cheeseF = 0
    if specialF =="":
        specialF = 0
    price = (200*int(paneerF)) + (250*int(cheeseF)) + (300*int(specialF))
    order_id =  random.randint(10000,99999)
    #print(order_id)

    L4 = Label(root,text="Order_Id",bg="red",fg="white",font=("Arial bold",20),width=8).grid(row=8,column=0,padx=10,pady=10)
    L5 = Label(root,text="Price",bg="red",fg="white",font=("Arial bold",20),width=8).grid(row=8,column=1,padx=10,pady=10)
    L6 = Label(root,text="ContactNo.",bg="red",fg="white",font=("Arial bold",20),width=8).grid(row=8,column=2,padx=10,pady=10)

    L7 = Label(root,text=order_id,bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=9,column=0,padx=10,pady=10)
    L8 = Label(root,text=price,bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=9,column=1,padx=10,pady=10)
    L9 = Label(root,text=Number,bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=9,column=2,padx=10,pady=10)

    Place = Button(root,text="Place order",bg="red",fg="white",font=("Arial bold",20),width=10,command=Place_order).grid(row=10,column=1,padx=10,pady=10)    
def Place_order():
    pas="nihar"
    db="urban_chawk"
    con=m.connect(host="localhost",user="root",passwd=pas,database=db)
    cur=con.cursor()
    t="HL_Frankie"
    qry="insert into "+t+" values("+str(order_id)+",'"+Name+"',"+str(Number)+","+str(paneerF)+","+str(cheeseF)+","+str(specialF)+","+str(price)+")"
    try:
        cur.execute(qry)
        con.commit()
        L10 = Label(root,text="Order placed",bg="black",fg="white",font=("Arial bold",22),width=10).grid(row=11,column=1,padx=10,pady=10)
    except:
        messagebox.showinfo("Error")

def HL_Frankie():
    global root,name,Num,E1,E2,E3
    root = Tk()
    root.geometry("700x700")
    root.title("Honest")

    L1 = Label(root,text="HL Frankie",bg="red",fg="white",font=("Arial bold",28),width=9).grid(row=0,column=1,padx=10,pady=10)

    I1 = Label(root,text="Item",bg="red",fg="white",font=("Arial bold",22),width=8).grid(row=1,column=0,padx=10,pady=10)
    I2 = Label(root,text="Price",bg="red",fg="white",font=("Arial bold",22),width=8).grid(row=1,column=1,padx=10,pady=10)
    I3 = Label(root,text="Quantity",bg="red",fg="white",font=("Arial bold",22),width=8).grid(row=1,column=2,padx=10,pady=10)
    
    M1 = Label(root,text="Paneer",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=2,column=0,padx=10,pady=10)
    P1 = Label(root,text="Rs 200",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=2,column=1,padx=10,pady=10)
    E1 = Entry(root)
    E1.grid(row=2,column=2,padx=10,pady=10)

    M2 = Label(root,text="Cheese",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=3,column=0,padx=10,pady=10)
    P2 = Label(root,text="Rs 250",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=3,column=1,padx=10,pady=10)
    E2 = Entry(root)
    E2.grid(row=3,column=2,padx=10,pady=10)

    M3 = Label(root,text="HL Special",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=4,column=0,padx=10,pady=10)
    P3 = Label(root,text="Rs 300",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=4,column=1,padx=10,pady=10)
    E3 = Entry(root)
    E3.grid(row=4,column=2,padx=10,pady=10)

    L2 = Label(root,text="Name",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=5,column=0,padx=10,pady=10)
    name = Entry(root)
    name.grid(row=5,column=1,padx=10,pady=10)

    L3 = Label(root,text="ContactNo.",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=6,column=0,padx=10,pady=10)
    Num = Entry(root)
    Num.grid(row=6,column=1,padx=10,pady=10)

    O = Button(root,text="View Bill",bg="red",fg="white",font=("Arial bold",20),width=10,command=view_bill).grid(row=7,column=1,padx=10,pady=10)
    quitt=Button(root,text="Quit",bg="black",fg="white",font=("Arial bold",20),command=root.destroy).grid(row=7,column=2,padx=10,pady=10)

    root.mainloop()
#HL_Frankie()
