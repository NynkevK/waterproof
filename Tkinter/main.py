from tkinter import *

root = Tk()
root.geometry("1000x700")

leftFrame = Frame(root, width=500, height=700, bd=1, relief=SOLID)
#flat, groove, raised, ridge, solid or sunken
rightFrame = Frame(root, width=500, height=700, bd=1, relief=SOLID)
leftFrame.pack(fill=BOTH, side=LEFT, expand=1)
rightFrame.pack(side=RIGHT)

waterLabel = Label(rightFrame, text="Waterhoogte: ")
pi1Label = Label(rightFrame, text="Linker Pi : ")
pi2Label = Label(rightFrame, text="Rechter Pi: ")
waterValueLabel = Label(rightFrame, text="Moet geüpdatet worden")
pi1ValueLabel = Label(rightFrame, text="online/offline")
pi2ValueLabel = Label(rightFrame, text="online/offline")

canvas = Canvas(leftFrame, width=700, height=700)
canvas.pack()

greenbox = canvas.create_rectangle(50, 50, 150, 150, fill="green")
blackLine = canvas.create_line(0, 0, 700, 700)
redLine = canvas.create_line(200,0, 0, 200, fill="red")

# photo = PhotoImage(file="Maeslantkering.png")
# label = Label(leftFrame, image=photo)
# label.pack()

waterLabel.grid(row=2)
pi1Label.grid(row=3)
pi2Label.grid(row=4)
waterValueLabel.grid(row=2, column=1)
pi1ValueLabel.grid(row=3, column=1)
pi2ValueLabel.grid(row=4, column=1)

root.mainloop()
