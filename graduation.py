
global college
global start_year
global end_year
global degree
global stream
global performance
from tkinter import *
import os
import sqlite3 as db
from tkinter import messagebox
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
sqlcon = db.connect('resume.sqlite')
cursor= sqlcon.cursor()
# create="""CREATE TABLE details(
#             resid int(5),name char(20),mail char(20),contact int(10),address char(20),PRIMARY KEY (resid));"""
# cursor.execute(create)
file=open("resid.txt","r")
resid = file.read()
file.close()
def clearrg():
    college.delete(0, END)
    start_year.delete(0, END)
    end_year.delete(0, END)
    degree.delete(0, END)
    stream.delete(0, END)
    performance.delete(0, END)

def savedg(resid):
    ecollege = college.get()
    estart = start_year.get()
    eend = end_year.get()
    edegree = degree.get()
    estream = stream.get()
    eperformance = performance.get()
    if ecollege:
        if estart:
            if eend:
                if edegree:
                    if estream:
                        if eperformance:
                            insert = """INSERT INTO graduation_details(resid,college,start_year,end_year,degree,stream,performance) values(?,?,?,?,?,?,?)"""
                            cursor.execute(insert, [resid,ecollege, estart, eend, edegree, estream, eperformance])
                            messagebox.showinfo("Success!",
                                                "Your graduation details has been saved successfully :)")
                            sqlcon.commit()
                            clearrg()
                            gd.destroy()
                        else:
                            messagebox.showerror("Error!", "Please enter your college performance")
                    else:
                        messagebox.showerror("Error!", "Please enter stream")
                else:
                    messagebox.showerror("Error!", "Please enter your degree")
            else:
                messagebox.showerror("Error!", "Please enter end year")
        else:
            messagebox.showerror("Error!", "Please enter your start year")
    else:
        messagebox.showerror("Error!", "Please enter your college name")


gd = Tk()

gd.geometry("1000x600+50+50")
gd.configure(bg="#652bb0")
canvas = Canvas(
    gd,
    bg="#652bb0",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"images/gd_background.png")
background = canvas.create_image(
    0, 0,
    image=background_img, anchor=NW)
entry0_img = PhotoImage(file=f"images/gd_textBox0.png")
entry0_bg = canvas.create_image(
    590, 180,
    image=entry0_img)

college = Entry(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0, font="16")

college.place(
    x=240, y=171,
    width=702.0,
    height=25)

entry1_img = PhotoImage(file=f"images/gd_textBox1.png")
entry1_bg = canvas.create_image(
    350, 300,
    image=entry1_img)

start_year = Entry(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0, font="16")

start_year.place(
    x=240, y=290,
    width=220.0,
    height=25)

entry2_img = PhotoImage(file=f"images/gd_textBox2.png")
entry2_bg = canvas.create_image(
    830, 300,
    image=entry2_img)

end_year = Entry(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0, font="16")

end_year.place(
    x=721, y=290,
    width=217.0,
    height=25)

entry3_img = PhotoImage(file=f"images/gd_textBox3.png")
entry3_bg = canvas.create_image(
    350.0, 415,
    image=entry3_img)

degree = Entry(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0, font="16")

degree.place(
    x=240, y=405,
    width=220.0,
    height=25)

entry4_img = PhotoImage(file=f"images/gd_textBox4.png")
entry4_bg = canvas.create_image(
    830, 415,
    image=entry4_img)
stream = Entry(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0, font="16")

stream.place(
    x=730, y=405,
    width=200.0,
    height=25)

entry5_img = PhotoImage(file=f"images/gd_textBox5.png")
entry5_bg = canvas.create_image(
    330, 530,
    image=entry5_img)

performance = Entry(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0, font="16")

performance.place(
    x=235, y=520,
    width=188.0,
    height=25)

img0 = PhotoImage(file=f"images/gd_img0.png")
save = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: savedg(resid),
    relief="flat", bg="#652bb0", activebackground="#652bb0", cursor="hand2")

save.place(
    x=815, y=510,
    width=133,
    height=63)

gd.resizable(False, False)
gd.mainloop()