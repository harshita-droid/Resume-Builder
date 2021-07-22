from tkinter import *
import os

def btn_clicked():
    print("Button Clicked")
def page3():
    window.destroy()
    os.system("python Education.py")
def internship_details():
    os.system("python internship_details.py")
def project_details():
    os.system("python project_details.py")
def training_details():
    os.system("python training_details.py")
def page5():
    window.destroy()
    os.system("python extra_details.py")
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

img0 = PhotoImage(file = f"images/ad_img0.png")
forward = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = page5,
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

forward.place(
    x = 892, y = 491,
    width = 87,
    height = 66)

img1 = PhotoImage(file = f"images/ad_img1.png")
back = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = page3,
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

back.place(
    x = 215, y = 20,
    width = 80,
    height = 65)

background_img = PhotoImage(file = f"images/ad_background.png")
background = canvas.create_image(
    0, 0,
    image=background_img,anchor=NW)

img2 = PhotoImage(file = f"images/ad_img2.png")
intern = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = internship_details,
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

intern.place(
    x = 396, y = 193,
    width = 49,
    height = 44)

img3 = PhotoImage(file = f"images/ad_img3.png")
pro = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = project_details,
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

pro.place(
    x = 396, y = 306,
    width = 49,
    height = 44)

img4 = PhotoImage(file = f"images/ad_img4.png")
tr = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = training_details,
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

tr.place(
    x = 396, y = 420,
    width = 49,
    height = 44)

window.resizable(False, False)
window.mainloop()
