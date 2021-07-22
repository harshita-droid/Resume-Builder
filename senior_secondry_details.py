from tkinter import *
import sqlite3 as db
from tkinter import messagebox
sqlcon = db.connect('resume.sqlite')
cursor= sqlcon.cursor()
# create="""CREATE TABLE senior_secondry_details(
#             resid int(5),school char(50),year int(5),board char(20),stream char(10),performance int(5))"""
# cursor.execute(create)
file=open("resid.txt","r")
resid = file.read()
file.close()
def clearr():
    school.delete(0,END)
    year.delete(0,END)
    board.delete(0,END)
    stream.delete(0,END)
    performance.delete(0,END)

def saved(resid):
    eschool = school.get()
    eyear = year.get()
    eboard = board.get()
    estream = stream.get()
    eperformance = performance.get()
    if eschool:
        if eyear:
            if eboard:
                if estream:
                    if eperformance:

                        insert = """INSERT INTO senior_secondry_details(resid,school,year,board,stream,performance) values(?,?,?,?,?,?)"""
                        cursor.execute(insert, [resid,eschool, eyear, eboard, estream, eperformance])
                        messagebox.showinfo("Success!", "Your higher secondry details has been saved successfully :)")
                        sqlcon.commit()
                        clearr()
                    else:
                        messagebox.showerror("Error!", "Please enter your Xth class performance")
                else:
                    messagebox.showerror("Error!", "Please enter your XIIth class stream")
            else:
                messagebox.showerror("Error!", "Please enter your XIIth class board")
        else:
            messagebox.showerror("Error!", "Please enter your  XIIth class year")
    else:
        messagebox.showerror("Error!", "Please enter your XIIth class school name")
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

background_img = PhotoImage(file = f"images/ss_background.png")
background = canvas.create_image(
    0, 0,
    image=background_img,anchor=NW)
entry0_img = PhotoImage(file=f"images/ss_textBox0.png")
entry0_bg = canvas.create_image(
    230, 160,
    image=entry0_img, anchor=NW)
school = Entry(
    bg = "#c4c4c4",
    bd = 0,
    highlightthickness = 0,font="16")

school.place(
    x = 240, y = 170,
    width = 676.0,
    height = 25)
entry1_img = PhotoImage(file=f"images/ss_textBox1.png")
entry1_bg = canvas.create_image(
    230, 290,
    image=entry1_img, anchor=NW)
year = Entry(
bg = "#c4c4c4",
    bd = 0,
    highlightthickness = 0,font="16")

year.place(
    x = 240, y = 300,
    width = 220.0,
    height = 25)
entry2_img = PhotoImage(file=f"images/ss_textBox2.png")
entry2_bg = canvas.create_image(
    690, 290,
    image=entry2_img, anchor=NW)
board = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,font="16")

board.place(
    x = 700, y = 300,
    width = 217.0,
    height = 25)
entry3_img = PhotoImage(file=f"images/ss_textBox3.png")
entry3_bg = canvas.create_image(
    230, 420,
    image=entry2_img, anchor=NW)
stream = Entry(
    bd = 0,
    bg="#c4c4c4",
    highlightthickness = 0,font=16)

stream.place(
    x = 240, y = 430,
    width = 217.0,
    height = 25)
entry4_img = PhotoImage(file=f"images/ss_textBox4.png")
entry4_bg = canvas.create_image(
    690, 420,
    image=entry2_img, anchor=NW)
performance = Entry(
    bd = 0,
    bg="#c4c4c4",
    highlightthickness = 0,font="16")

performance.place(
    x = 700, y = 430,
    width = 220.0,
    height = 25)

img0 = PhotoImage(file = f"images/ss_img0.png")
save = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : saved(resid),
    relief = "flat",activebackground="#652bb0",cursor="hand2")

save.place(
    x = 790, y = 509,
    width = 142,
    height = 65)

window.resizable(False, False)
window.mainloop()
