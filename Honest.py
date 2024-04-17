from tkinter import *
from tkinter import messagebox
import mysql.connector as m
import random
import os
import smtplib
import math

#Honest
def view_bill():
    global pavBhaji,Email,pulav,pepsi,price,order_id,Name,Number
    pavBhaji = E1.get()
    
    #print(pavBhaji)
    pulav = E2.get()
    pepsi = E3.get()
    Name = name.get()
    Number = Num.get()
    Email = mail.get()
    if pavBhaji =="":
        pavBhaji = 0
    if pulav =="":
        pulav = 0
    if pepsi =="":
        pepsi = 0
    price = (200*int(pavBhaji)) + (100*int(pulav)) + (20*int(pepsi))
    #print(price)
    order_id =  random.randint(10000,99999)
    #print(order_id)

    L4 = Label(root,text="Order_Id",bg="red",fg="white",font=("Arial bold",20),width=8).grid(row=9,column=0,padx=10,pady=10)
    L5 = Label(root,text="Price",bg="red",fg="white",font=("Arial bold",20),width=8).grid(row=9,column=1,padx=10,pady=10)
    L6 = Label(root,text="ContactNo.",bg="red",fg="white",font=("Arial bold",20),width=8).grid(row=9,column=2,padx=10,pady=10)

    L7 = Label(root,text=order_id,bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=10,column=0,padx=10,pady=10)
    L8 = Label(root,text=price,bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=10,column=1,padx=10,pady=10)
    L9 = Label(root,text=Number,bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=10,column=2,padx=10,pady=10)
    send = Button(root,text="Send OTP",bg="red",fg="white",font=("Arial bold",20),width=10,command=send_otp).grid(row=11,column=1,padx=10,pady=10)    
def send_otp():
    global OTP,E10
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"
    msg= otp
    HOST = "smtp.gmail.com"
    PORT = 587
    FROM_EMAIL = "abc@gmail.com"
    PASSWORD = "yabu ipqw qcgv tbmk"
    smtp = smtplib.SMTP(HOST, PORT)
    status_code, response = smtp.ehlo()
    # print(f"[*] Echoing the server: {status_code} {response}")
    status_code, response = smtp.starttls()
    # print(f"[*] Starting TLS connection: {status_code} {response}")
    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    # print(f"[*] Logging in: {status_code} {response}")
    try:
        smtp.sendmail(FROM_EMAIL, Email , msg)
        # print("Email sent successfully")
    except:
        messagebox.showinfo("Email not sent")
    smtp.quit()
    L10 = Label(root,text="Enter OTP",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=12,column=0,padx=10,pady=10)
    E10 = Entry(root,width=8,font=("Arial bold",18))
    E10.grid(row=12,column=1,padx=10,pady=10)
    place = Button(root,text="Place Order",bg="red",fg="white",font=("Arial bold",20),width=10,command=Place_order).grid(row=12,column=2,padx=10,pady=10)    
def Place_order():
    check_otp = E10.get()
    if (check_otp == OTP):

        pas="nihar"
        db="urban_chawk"
        con=m.connect(host="localhost",user="root",passwd=pas,database=db)
        cur=con.cursor()
        t="Honest"
        qry="insert into "+t+" values("+str(order_id)+",'"+Name+"',"+str(Number)+","+str(pavBhaji)+","+str(pulav)+","+str(pepsi)+","+str(price)+",'"+Email+"')"
        try:
            cur.execute(qry)
            con.commit()
            messagebox.showinfo("","Your Order has been placed")
            # L11 = Label(root,text="Order placed",bg="black",fg="white",font=("Arial bold",22),width=10).grid(row=13,column=1,padx=10,pady=10)
        except:
            messagebox.showinfo("Error")
    else:
        messagebox.showinfo("OTP Incorrect.\nOrder Failed")       
    
def Honest():
    global root,name,Num,mail,E1,E2,E3
    
    root = Tk()
    root.geometry("1100x1100")
    root.title("Honest")
    s=Scrollbar(root).grid(row=0,column=3)
    L1 = Label(root,text="Honest",bg="red",fg="white",font=("Arial bold",28),width=9).grid(row=0,column=1,padx=10,pady=10)

    I1 = Label(root,text="Item",bg="red",fg="white",font=("Arial bold",22),width=8).grid(row=1,column=0,padx=10,pady=10)
    I2 = Label(root,text="Price",bg="red",fg="white",font=("Arial bold",22),width=8).grid(row=1,column=1,padx=10,pady=10)
    I3 = Label(root,text="Quantity",bg="red",fg="white",font=("Arial bold",22),width=8).grid(row=1,column=2,padx=10,pady=10)
    
    M1 = Label(root,text="PavBhaji",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=2,column=0,padx=10,pady=10)
    P1 = Label(root,text="Rs 200",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=2,column=1,padx=10,pady=10)
    E1 = Entry(root,width=8,font=("Arial bold",18))
    E1.grid(row=2,column=2,padx=10,pady=10)

    M2 = Label(root,text="Pulav",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=3,column=0,padx=10,pady=10)
    P2 = Label(root,text="Rs 100",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=3,column=1,padx=10,pady=10)
    E2 = Entry(root,width=8,font=("Arial bold",18))
    E2.grid(row=3,column=2,padx=10,pady=10)

    M3 = Label(root,text="Pepsi",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=4,column=0,padx=10,pady=10)
    P3 = Label(root,text="Rs 20",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=4,column=1,padx=10,pady=10)
    E3 = Entry(root,width=8,font=("Arial bold",18))
    E3.grid(row=4,column=2,padx=10,pady=10)

    L2 = Label(root,text="Name",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=5,column=0,padx=10,pady=10)
    name = Entry(root,width=8,font=("Arial bold",18))
    name.grid(row=5,column=1,padx=10,pady=10)

    L3 = Label(root,text="ContactNo.",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=6,column=0,padx=10,pady=10)
    Num = Entry(root,width=8,font=("Arial bold",18))
    Num.grid(row=6,column=1,padx=10,pady=10)

    L4 = Label(root,text="Email_ID",bg="black",fg="white",font=("Arial bold",20),width=8).grid(row=7,column=0,padx=10,pady=10)
    mail = Entry(root,width=8,font=("Arial bold",18))
    mail.grid(row=7,column=1,padx=10,pady=10)

    O = Button(root,text="View Bill",bg="red",fg="white",font=("Arial bold",20),width=10,command=view_bill).grid(row=8,column=1,padx=10,pady=10)
    quitt=Button(root,text="Quit",bg="black",fg="white",font=("Arial bold",20),command=root.destroy).grid(row=8,column=2,padx=10,pady=10)

    root.mainloop()
Honest()
