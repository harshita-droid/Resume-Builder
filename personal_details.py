from tkinter import *
import os
import sqlite3 as db
from tkinter import messagebox

sqlcon = db.connect('resume.sqlite')
cursor= sqlcon.cursor()
# create="""CREATE TABLE details(
#             resid int(5),name char(20),mail char(20),contact int(10),address char(20),PRIMARY KEY (resid));"""
# cursor.execute(create)


def page3():
    pd.destroy()
    os.system("python imagebrowser.py")

def set_resume_id():
    import random
    id=random.randint(1000,9999)
    residd="RES"+str(id)
    return residd
def valid_contact(phn):
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(phn)
def valid_mail(email):
    Pattern = re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
    return Pattern.match(email)
def clearr():
    name.delete(0,END)
    mail.delete(0,END)
    contact.delete(0,END)
    address.delete(0,END)

global resid

resid= set_resume_id()
file = open(r"resid.txt","w+")
file.write(resid)
file.close()

def saved(resid):
    ename= name.get()
    email= mail.get()
    econtact= contact.get()
    eaddress= address.get()



    if ename.strip():
        if email:
            if valid_mail(email):
                if econtact:
                    if valid_contact(econtact):
                        if eaddress:

                            insert = ("INSERT INTO details(resid,name,mail,contact,address) values(?,?,?,?,?)")

                            cursor.execute(insert, [resid, ename, email, econtact, eaddress])
                            sqlcon.commit()
                            messagebox.showinfo("Success!", "Your personal details has been saved successfully :)")
                            clearr()
                        else:
                            messagebox.showerror("Error!", "Please enter your address")
                    else:
                        messagebox.showerror("Error!", "Oops! invalid contact number:(")
                else:
                    messagebox.showerror("Error!", "Please enter your contact number")
            else:
                messagebox.showerror("Error!", "Oops! invalid mail:(")
        else:
            messagebox.showerror("Error!", "Please enter your mail")
    else:
        messagebox.showerror("Error!", "Please enter your name")
global pd
def open():
    global pd
    global name
    global address
    global contact
    global mail
    pd = Tk()
    pd.geometry("1000x600+50+50")
    pd.configure(bg="#652bb0")
    canvas = Canvas(
        pd,
        bg="#652bb0",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    entry0_img = PhotoImage(file=f"images/pd_textBox0.png")
    entry0_bg = canvas.create_image(
        230, 208,
        image=entry0_img, anchor=NW)
    name = Entry(
        bg="#c4c4c4",
        bd=0,
        highlightthickness=0, font="16")

    name.place(
        x=240, y=215,
        width=308.0,
        height=25)
    entry1_img = PhotoImage(file=f"images/pd_textBox1.png")
    entry1_bg = canvas.create_image(
        640, 208,
        image=entry0_img, anchor=NW)
    mail = Entry(
        bd=0,
        bg="#c4c4c4",
        highlightthickness=0, font="16")

    mail.place(
        x=650, y=215,
        width=315.0,
        height=25)
    entry2_img = PhotoImage(file=f"images/pd_textBox2.png")
    entry2_bg = canvas.create_image(
        230, 350,
        image=entry0_img, anchor=NW)

    contact = Entry(
        bd=0,
        bg="#c4c4c4",
        highlightthickness=0, font="16")

    contact.place(
        x=240, y=359,
        width=315.0,
        height=25)

    entry2_img = PhotoImage(file=f"images/pd_textBox3.png")
    entry2_bg = canvas.create_image(
        640, 350,
        image=entry0_img, anchor=NW)

    address = Entry(
        bd=0,
        bg="#c4c4c4",
        highlightthickness=0, font="16")

    address.place(
        x=650, y=355,
        width=315.0,
        height=25)

    img0 = PhotoImage(file=f"images/pd_img0.png")
    forward = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=page3,
        relief="flat", bg="#652BB0", activebackground="#652BB0", cursor="hand2")

    forward.place(
        x=857, y=454,
        width=87,
        height=66)

    img1 = PhotoImage(file=f"images/pd_img1.png")
    back = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat", bg="#652BB0", activebackground="#652BB0", cursor="hand2")

    back.place(
        x=224, y=24,
        width=80,
        height=65)

    background_img = PhotoImage(file=f"images/pdbackground.png")
    background = canvas.create_image(
        0, 0,
        image=background_img, anchor=NW)
    saveimg = PhotoImage(file=f"images/int_img0.png")
    save = Button(
        image=saveimg,
        borderwidth=0,
        highlightthickness=0,
        command=lambda : saved(resid),
        relief="flat", bg="#652bb0", activebackground="#652bb0", cursor="hand2")

    save.place(
        x=700, y=454,
        width=134,
        height=65)

    pd.resizable(False, False)
    pd.mainloop()

