from tkinter import *
import os

def btn_clicked():
    main.destroy()
    from personal_details import open
    open()



main = Tk()
main.title("Resume Builder")
main.geometry("1000x600+50+50")
main.configure(bg = "#652bb0")
canvas = Canvas(
    main,
    bg = "#652bb0",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"images/background.png")
background = canvas.create_image(
    0,88,
    image=background_img,anchor=NW)

img0 = PhotoImage(file = f"images/bgbtn.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat",activebackground="#B2B5B8",cursor="hand2")

b0.place(
    x = 390, y = 460,
    width = 232,
    height = 71)

main.resizable(False, False)
main.mainloop()
