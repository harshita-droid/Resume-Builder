from tkinter import *
import os
from tkinter import  messagebox
def btn_clicked():
    os.system("python inserting.py")
    messagebox.showinfo("Success","Your resume has been created sucessfully")
    success = Label(window, bg="#652bb0", fg="white", font="Sacramento 50",
                    text="Thanku for using our App").place(x=200,
                                                           y=315)
def exit():
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

background_img = PhotoImage(file = f"images/gen_background.png")
background = canvas.create_image(
    0, 0,
    image=background_img,anchor=NW)

img1 = PhotoImage(file = f"images/gen_img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat",bg="#652bb0",activebackground="#652bb0",cursor="hand2")

b1.place(
    x = 327, y = 115,
    width = 516,
    height = 115)
exit = Button(
    window,
    text = "Exit",
    font= "30",
    borderwidth = 0,
    highlightthickness = 0,
    command = exit,
    relief = "flat",bg="gray",activebackground="#652bb0",cursor="hand2")
exit.place( x = 900 , y =500,
    width =60 ,
    height = 40)
window.resizable(False, False)
window.mainloop()
