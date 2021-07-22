from tkinter import *
from tkinter import messagebox
import sqlite3 as db
sqlcon = db.connect('resume.sqlite')
cursor= sqlcon.cursor()
# create="CREATE TABLE project_details(resid int(5),title char(120),link char(30),start_year char(10),end_year char(10),desc char(150));"
#
# cursor.execute(create)
file=open("resid.txt","r")
resid = file.read()
file.close()
def Convert(string):
    li = list(string.split(" "))
    return li
def clearr():
    title.delete(0, END)
    link.delete(0, END)
    start.delete(0, END)
    end.delete(0, END)
    des.delete('1.0', END)
def saved(resid):
    etitle = title.get()
    elink = link.get()
    estart = start.get()
    eend = end.get()
    edesc = des.get("1.0", "end-1c")
    words = Convert(edesc)
    if etitle:
        if estart:
            if eend:
                if len(edesc)!=0:
                    if len(words)<=45:
                        insert = (
                            "INSERT INTO project_details(resid,title,link,start_year,end_year,desc) values(?,?,?,?,?,?)")

                        cursor.execute(insert, [resid, etitle, elink, estart, eend, edesc])
                        sqlcon.commit()
                        messagebox.showinfo("Success!", "Your project details has been saved successfully :)")
                        clearr()
                    else:
                        messagebox.showinfo("Note!", "You cannot write more than 45 words")
                else:
                    messagebox.showerror("Error!", "Please enter your project's description")
            else:
                messagebox.showerror("Error!", "Please enter end year")
        else:
            messagebox.showerror("Error!", "Please enter start year")
    else:
        messagebox.showerror("Error!", "Please enter your project title")
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

background_img = PhotoImage(file = f"images/probackground.png")
background = canvas.create_image(
    0,0,
    image=background_img,anchor=NW)

entry0_img = PhotoImage(file = f"images/int_textBox0.png")
entry0_bg = canvas.create_image(
    540, 140,
    image = entry0_img)

title = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,font="16")

title.place(
    x = 235 , y = 130,
    width = 615.0,
    height = 25)
entry1_img = PhotoImage(file = f"images/int_textBox0.png")
entry1_bg = canvas.create_image(
    227,218,
    image = entry1_img,anchor=NW)


link = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,font="16")

link.place(
    x = 235, y = 230,
    width = 205.0,
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
