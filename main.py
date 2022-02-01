from tkinter import *

root = Tk()
root.title("Hodisalar bilan ishlash")
root.geometry("500x400+50+50")


def btn_left_clicked(event):
    print(event)


def btn_middle_clicked(event):
    print(event)


def btn_right_clicked(event):
    print(event)


def btn_enter(event):
    lbl_1.config(bg="red")
    btn_1.config(font=("-size 50"))

def btn_leave(event):
    lbl_1.config(bg="yellow")
    btn_1.config(font=("-size 20"))

def btn_return(event):
    print(event)

btn_1 = Button(root, text="Tugma 1", font="-size 20")
btn_1.pack()
btn_1.focus_set()

btn_1.bind("<Button-1>", btn_left_clicked)
btn_1.bind("<Button-2>", btn_middle_clicked)
btn_1.bind("<Button-3>", btn_right_clicked)
btn_1.bind("<Enter>", btn_enter)
btn_1.bind("<Leave>", btn_leave)
btn_1.bind("<Return>", btn_return)

lbl_1 = Label(root,text="Salom", bg="yellow")
lbl_1.pack()

root.mainloop()
