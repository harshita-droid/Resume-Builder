from tkinter import *
import os
from tkinter import messagebox


def btn_clicked():
    print("Button Clicked")
def achievement_details():
    os.system("python achievement_details.py")
def page4():
    window.destroy()
    os.system("python academic_details.py")
def forward():
    window.destroy()
    os.system("python generate.py")
counter = 0
def skills():
    global counter
    counter+=1
    if counter>6:
        messagebox.showinfo("Note!","You cannot add more than 6 skills")
    else:
        os.system("python skills.py")


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

img0 = PhotoImage(file = f"images/ex_img0.png")
forward = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = forward,
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

forward.place(
    x = 892, y = 491,
    width = 87,
    height = 66)

img1 = PhotoImage(file = f"images/ex_img1.png")
back = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = page4,
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

back.place(
    x = 215, y = 20,
    width = 80,
    height = 65)

background_img = PhotoImage(file = f"images/ex_background.png")
background = canvas.create_image(
    0,0,
    image=background_img,anchor=NW)

img2 = PhotoImage(file = f"images/ex_img2.png")
achieve = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = achievement_details,
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

achieve.place(
    x = 396, y = 193,
    width = 49,
    height = 44)

img3 = PhotoImage(file = f"images/ex_img3.png")
skills = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = skills,
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

skills.place(
    x = 400, y = 372,
    width = 49,
    height = 44)

window.resizable(False, False)
window.mainloop()
