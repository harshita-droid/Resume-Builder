from tkinter import *
import sqlite3 as db
from tkinter import messagebox
# create = "CREATE TABLE extra_details(resid int(5),des char(150))"
sqlcon = db.connect('resume.sqlite')
cursor= sqlcon.cursor()
# cursor.execute(create)
file=open("resid.txt","r")
resid = file.read()
file.close()
def clearr():
    des.delete('1.0',END)


# Python code to convert string to list

def Convert(string):
    li = list(string.split(" "))
    return li
def saved(resid):
    edes=des.get("1.0","end-1c")
    words=Convert(edes)
    if len(edes)!=0:
        if len(words)<30:
            insert="INSERT INTO extra_details(resid,des) values(?,?)"
            cursor.execute(insert,[resid,edes])
            messagebox.showinfo("Success!","Your achievement details have been successfully saved :)")
            sqlcon.commit()
            clearr()
            window.destroy()
        else:
            messagebox.showinfo("Note","You cannot enter more than 30 words")
    else:
        messagebox.showerror("Error!","Please enter description")


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

background_img = PhotoImage(file = f"images/ach_background.png")
background = canvas.create_image(
    0,0,
    image=background_img,anchor= NW)

entry0_img = PhotoImage(file = f"images/ach_textBox0.png")
entry0_bg = canvas.create_image(
    239, 240,
    image = entry0_img,anchor=NW)

des = Text(window, height = 10,
                width = 25,
                bg = "#c4c4c4",highlightthickness=0,font="16",bd=0)

des.place(
    x = 242, y = 243,
    width = 654.0,
    height = 200)

img0 = PhotoImage(file = f"images/ach_img0.png")
save = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : saved(resid),
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

save.place(
    x = 790, y = 506,
    width = 138,
    height = 65)

window.resizable(False, False)
window.mainloop()
