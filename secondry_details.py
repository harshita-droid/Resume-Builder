from tkinter import *
from tkinter import messagebox
import sqlite3 as db
sqlcon = db.connect('resume.sqlite')
cursor= sqlcon.cursor()
# create="""CREATE TABLE secondry_details(
#             resid int(5),school char(50),year int(5),board char(20),performance int(20));"""
# cursor.execute(create)
file=open("resid.txt","r")
resid = file.read()
file.close()
def clearr():
    school.delete(0,END)
    year.delete(0,END)
    board.delete(0,END)
    performance.delete(0,END)
def saved(resid):
    eschool = school.get()
    eyear = year.get()
    eboard = board.get()
    eperformance = performance.get()
    if eschool:
        if eyear:
            if eboard:
                if eperformance:
                    insert = """INSERT INTO secondry_details(resid,school,year,board,performance) values(?,?,?,?,?)"""
                    cursor.execute(insert,[resid,eschool,eyear,eboard,eperformance])
                    messagebox.showinfo("Success!", "Your secondry details has been saved successfully :)")
                    sqlcon.commit()
                    clearr()
                else:
                    messagebox.showerror("Error!","Please enter your Xth class performance")
            else:
                messagebox.showerror("Error!", "Please enter your Xth class board")
        else:
            messagebox.showerror("Error!", "Please enter your  Xth class year")
    else:
        messagebox.showerror("Error!", "Please enter your Xth class school name")
    window.destroy()
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

background_img = PhotoImage(file = f"images/se_background.png")
background = canvas.create_image(
    0,0,
    image=background_img,anchor=NW)
entry0_img = PhotoImage(file=f"images/se_textBox0.png")
entry0_bg = canvas.create_image(
    230, 160,
    image=entry0_img, anchor=NW)
school = Entry(

    bg="#c4c4c4",
    bd = 0,
    highlightthickness = 0,font="16")

school.place(
    x = 240, y = 170,
    width = 676.0,
    height = 25)
entry1_img = PhotoImage(file=f"images/se_textBox1.png")
entry1_bg = canvas.create_image(
    230, 310,
    image=entry1_img, anchor=NW)
year = Entry(
    bg="#c4c4c4",
    bd = 0,
    highlightthickness = 0,font="16")

year.place(
    x = 240, y = 320,
    width = 220.0,
    height = 25)
entry2_img = PhotoImage(file=f"images/se_textBox2.png")
entry2_bg = canvas.create_image(
    685, 310,
    image=entry2_img, anchor=NW)
board = Entry(
    bg="#c4c4c4",
    bd = 0,
    highlightthickness = 0,font="16")

board.place(
    x = 695, y = 320,
    width = 217.0,
    height = 25)

entry3_img = PhotoImage(file=f"images/se_textBox3.png")
entry3_bg = canvas.create_image(
    230, 430,
    image=entry3_img, anchor=NW)
performance = Entry(
    bd = 0,
    bg="#c4c4c4",
    highlightthickness = 0,font="16")

performance.place(
    x = 240, y = 440,
    width = 217.0,
    height = 25)


img0 = PhotoImage(file = f"images/se_img0.png")
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
