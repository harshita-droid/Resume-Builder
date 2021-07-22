from tkinter import *
import os

def btn_clicked():
    print("Button Clicked")
def page2():
    window.destroy()
    os.system("python imagebrowser.py")
def gd_details():
    os.system("python graduation.py")
def secondry_higher_details():
    os.system("python senior_secondry_details.py")
def secondry_details():
    os.system("python secondry_details.py")
def page4():
    window.destroy()
    os.system("python academic_details.py")
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

img0 = PhotoImage(file = f"images/ed_img0.png")
forward = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = page4,
    relief = "flat", bg = "#652bb0",activebackground= "#652bb0",cursor="hand2")

forward.place(
    x=892, y=491,
    width = 87,
    height = 66)

img1 = PhotoImage(file = f"images/ed_img1.png")
back = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = page2,
    relief = "flat", bg = "#652bb0",activebackground= "#652bb0",cursor="hand2")

back.place(
    x=230, y=20,                         #
    width = 80,
    height = 65)

background_img = PhotoImage(file = f"images/ed_background.png")
background = canvas.create_image(
    0,0,
    image=background_img,anchor=NW)

img2 = PhotoImage(file = f"images/ed_img2.png")
gd = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = gd_details,
    relief = "flat", bg = "#652bb0",activebackground= "#652bb0",cursor="hand2")

gd.place(
    x = 396, y = 193,
    width = 49,
    height = 44)

img3 = PhotoImage(file = f"images/ed_img3.png")
ss = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = secondry_higher_details,
    relief = "flat",bg = "#652bb0",activebackground= "#652bb0",cursor="hand2")

ss.place(
    x = 396, y = 306,
    width = 49,
    height = 44)

img4 = PhotoImage(file = f"images/ed_img4.png")
se = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = secondry_details,
    relief = "flat",bg = "#652bb0",activebackground= "#652bb0",cursor="hand2")

se.place(
    x = 396, y = 420,
    width = 49,
    height = 44)

window.resizable(False, False)
window.mainloop()
