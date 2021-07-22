from tkinter import *
import sqlite3 as db
from tkinter import messagebox
sqlcon = db.connect('resume.sqlite')
cursor= sqlcon.cursor()
# create = "CREATE TABLE skills(resid int(5),skill char(30))"
# cursor.execute(create)
file=open("resid.txt","r")
resid = file.read()
file.close()
def clearr():  #haomat do
    skill.delete(0,END)
def saved(resid):
    pass
    eskill=skill.get()
    if eskill:
        insert="INSERT INTO skills(resid,skill) values(?,?)"
        cursor.execute(insert,[resid,eskill])
        messagebox.showinfo("Success!","Your skill have been successfully saved :)")
        sqlcon.commit()
        clearr()
    else:
        messagebox.showerror("Error!","Please enter skill")


    window.destroy()


window = Tk()

window.geometry("1000x313+50+150")
window.configure(bg = "#652bb0")
canvas = Canvas(
    window,
    bg = "#652bb0",
    height = 313,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"images/skill_background.png")
background = canvas.create_image(
    0, 0,
    image=background_img,anchor=NW)

entry0_img = PhotoImage(file = f"images/skill_textBox0.png")
entry0_bg = canvas.create_image(
    222, 156,
    image = entry0_img,anchor=NW)

skill = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,font="16")

skill.place(
    x = 230, y = 164,
    width = 654.0,
    height = 25)

img0 = PhotoImage(file = f"images/skill_img0.png")
save = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : saved(resid),
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

save.place(
    x = 827, y = 235,
    width = 138,
    height = 65)

window.resizable(False, False)
window.mainloop()
