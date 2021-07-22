# from personal_details import genereateresid
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from tkinter import *
import sqlite3 as db
from tkinter import messagebox
sqlcon = db.connect('resume.sqlite')
cursor= sqlcon.cursor()
# create="CREATE TABLE internship_details(resid int(5),profile char(120),Location char(30),Organization char(30),start_year char(10),end_year char(10),desc char(150));"
#
# cursor.execute(create)
file=open("resid.txt","r")
resid = file.read()
file.close()
def clearr():
    profile.delete(0,END)
    location.delete(0,END)
    org.delete(0,END)
    start.delete(0,END)
    end.delete(0,END)
    des.delete('1.0',END)
def Convert(string):
    li = list(string.split(" "))
    return li
def saved(resid):
    eprofile = profile.get()
    eorg = org.get()
    eloc = location.get()
    estart = start.get()
    eend=end.get()
    edesc=des.get("1.0","end-1c")
    words = Convert(edesc)
    if eprofile:
        if eloc:
            if eorg:
                if estart:
                    if eend:
                        if len(edesc)!=0:
                            if len(words)<=45:
                                insert = (
                                    "INSERT INTO internship_details(resid,profile,Location,Organization,start_year,end_year,desc) values(?,?,?,?,?,?,?)")

                                cursor.execute(insert, [resid, eprofile, eloc, eorg, estart, eend, edesc])
                                sqlcon.commit()
                                messagebox.showinfo("Success!", "Your personal details has been saved successfully :)")
                                clearr()

                                window.destroy()
                            else:
                                messagebox.showinfo("Note!","You cannot write more than 45 words")

                        else:
                            messagebox.showerror("Error!", "Please enter your internship's description")
                    else:
                        messagebox.showerror("Error!","Please enter your ending month")
                else:
                    messagebox.showerror("Error!", "Please enter your start month")
            else:
                messagebox.showerror("Error!", "Please enter your internship's Organization")
        else:
            messagebox.showerror("Error!", "Please enter your internship's Loation")
    else:
        messagebox.showerror("Error!", "Please enter your intership's profile")

window = Tk()

window.geometry("1000x600+50+50")
window.configure(bg = "#652bb0")
canvas = Canvas(
    window,
    bg = "#652bb0",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"images/int_background.png")
background = canvas.create_image(
    0,0,
    image=background_img,anchor=NW)

entry0_img = PhotoImage(file = f"images/int_textBox0.png")
entry0_bg = canvas.create_image(
    540, 140,
    image = entry0_img)

profile = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,font="16")

profile.place(
    x = 235 , y = 130,
    width = 615.0,
    height = 25)

entry1_img = PhotoImage(file = f"images/int_textBox1.png")
entry1_bg = canvas.create_image(
    227, 220,
    image = entry1_img,anchor=NW)

location = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,font="16")

location.place(
    x = 235, y = 230,
    width = 205.0,
    height = 25)

entry2_img = PhotoImage(file = f"images/int_textBox2.png")
entry2_bg = canvas.create_image(
    637,220,
    image = entry2_img,anchor=NW)

org = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,font="16")

org.place(
    x = 647, y = 230,
    width = 211.0,
    height = 25)

entry3_img = PhotoImage(file = f"images/int_textBox3.png")
entry3_bg = canvas.create_image(
    224, 323,
    image = entry3_img,anchor=NW)

start = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,font=NW)

start.place(
    x = 234, y = 333,
    width = 214.0,
    height = 25)

entry4_img = PhotoImage(file = f"images/int_textBox4.png")
entry4_bg = canvas.create_image(
    637, 325,
    image = entry4_img,anchor=NW)

end = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,font="16")

end.place(
    x = 647, y = 333,
    width = 205.0,
    height = 25)

entry5_img = PhotoImage(file = f"images/int_textBox5.png")
entry5_bg = canvas.create_image(
    224, 429,
    image = entry5_img,anchor=NW)

des = Text(window, height = 10,
                width = 25,
                bg = "#c4c4c4",highlightthickness=0,font="16",bd=0)
des.place(
    x = 230, y = 431,
    width = 618.0,
    height = 85)

img0 = PhotoImage(file = f"images/int_img0.png")
save = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : saved(resid),
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

save.place(
    x = 858, y = 527,
    width = 134,
    height = 65)

window.resizable(False, False)
window.mainloop()
