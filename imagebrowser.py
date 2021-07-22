from tkinter import *
import os
from tkinter import filedialog
import sqlite3 as db
from tkinter import messagebox
# create = "CREATE TABLE info(resid int(5),des char(150))"
sqlcon = db.connect('resume.sqlite')
cursor= sqlcon.cursor()
# cursor.execute(create)
file=open("resid.txt","r")
resid = file.read()
file.close()

def Convert(string):
    li = list(string.split(" "))
    return li
def btn_clicked():
    print("Button Clicked")
def page3():
    window.destroy()
    os.system("python Education.py")
def page2():
    window.destroy()
    from personal_details import open
    open()
def browse():
    global myimage
    window.filename =filedialog.askopenfilename(initialdir ="/",title ="Select an image",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("jpeg files","*.jpeg")))
    file = open(r"imagefile.txt", "w+")
    file.write(window.filename)
    file.close()
    messagebox.showinfo("Success!","Your image has been uploaded successfully")
def clearr():
    des.delete('1.0',END)
def saved(resid):
    edes = des.get("1.0", "end-1c")
    print(edes)
    words=Convert(edes)
    if len(edes) != 0:
        if len(words) < 30:
            insert = "INSERT INTO info(resid,des) values(?,?)"
            cursor.execute(insert, [resid, edes])
            messagebox.showinfo("Success!", "Your info has been successfully saved :)")
            sqlcon.commit()
            clearr()
        else:
            messagebox.showinfo("Note", "You cannot enter more than 30 words")
    else:
        messagebox.showerror("Error!", "Please enter objective/aim")


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
background_img = PhotoImage(file = f"images/browbackground.png")
background = canvas.create_image(
    0,0,
    image=background_img,anchor=NW)
user_name = Label(window,bg="#652bb0",fg="white",font="Sacramento 25",
                  text = "Aim/objective").place(x = 229,
                                           y = 138)
entry0_img = PhotoImage(file = f"images/browimg_textBox0.png")
entry0_bg = canvas.create_image(
    224.0, 198.0,
    image = entry0_img,anchor=NW)

des= Text(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,font="16")

des.place(
    x = 230, y = 200,
    width = 654.0,
    height = 100)

img0 = PhotoImage(file = f"images/browimg0.png")
save = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : saved(resid),
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

save.place(
    x = 750, y = 495,
    width = 138,
    height = 65)

img1 = PhotoImage(file = f"images/browimg1.png")
image = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = browse,
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

image.place(
    x = 488, y = 380,
    width = 109,
    height = 106)

forwardimg = PhotoImage(file = f"images/ed_img0.png")
forward = Button(
    image = forwardimg,
    borderwidth = 0,
    highlightthickness = 0,
    command = page3,
    relief = "flat", bg = "#652bb0",activebackground= "#652bb0",cursor="hand2")

forward.place(
    x=892, y=491,
    width = 87,
    height = 66)

backimg = PhotoImage(file = f"images/ed_img1.png")
back = Button(
    image = backimg,
    borderwidth = 0,
    highlightthickness = 0,
    command = page2,
    relief = "flat", bg = "#652bb0",activebackground= "#652bb0",cursor="hand2")

back.place(
    x=230, y=20,                         #
    width = 80,
    height = 65)
window.resizable(False, False)
window.mainloop()


