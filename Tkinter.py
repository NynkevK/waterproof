from tkinter import *
import csv
import time

class StandardWindow:

    def __init__(self, master):
        # Global Variables:
        global dateValueLabel, index, maeslantkeringValueLabel, photoRight, photoLeft
        index = -1

        # Frames:
        leftFrame = Frame(root, width=590, height=600, bd=1, relief=SOLID)
        rightFrame = Frame(root, width=410, height=600,bd=1, relief=SOLID)
        leftFrame.pack(side=LEFT)
        leftFrame.pack_propagate(0)
        rightFrame.pack()
        rightFrame.pack_propagate(0)

        # Reading from data file:
        dataList = []

        with open("testdata.csv") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                print(row)
                dataList.append(row)

        # All the labels used:
        emptyLabel = Label(rightFrame, text=" ")
        dateLabel = Label(rightFrame, text="Datum: ")
        timeLabel = Label(rightFrame, text="Tijd: ")
        waterLabel = Label(rightFrame, text="Waterhoogte: ")
        maeslantkeringLabel = Label(rightFrame, text="Maeslantkering: ")
        pi1Label = Label(rightFrame, text="Linker Pi : ")
        pi2Label = Label(rightFrame, text="Rechter Pi: ")
        dateValueLabel = Label(rightFrame, text=dataList[index]['date'])
        timeValueLabel = Label(rightFrame, text=dataList[index]['time'])
        waterValueLabel = Label(rightFrame, text=dataList[index]['value'])
        maeslantkeringValueLabel = Label(rightFrame, text="Dicht")
        pi1ValueLabel = Label(rightFrame, text="leeg")
        pi2ValueLabel = Label(rightFrame, text="leeg")

        # Show all the labels in the window:
        dateLabel.grid(row=1, column=1, sticky=E)
        timeLabel.grid(row=2, column=1, sticky=E)
        emptyLabel.grid(row=3, columnspan=5)
        waterLabel.grid(row=4, column=1, sticky=E)
        maeslantkeringLabel.grid(row=5, column=1, sticky=E)
        emptyLabel.grid(row=6, columnspan=5)
        pi1Label.grid(row=7, column=1, sticky=E)
        pi2Label.grid(row=8, column=1, sticky=E)
        dateValueLabel.grid(row=1, column=2, sticky=W)
        timeValueLabel.grid(row=2, column=2, sticky=W)
        waterValueLabel.grid(row=4, column=2, sticky=W)
        maeslantkeringValueLabel.grid(row=5, column=2, sticky=W)
        pi1ValueLabel.grid(row=7, column=2, sticky=W)
        pi2ValueLabel.grid(row=8, column=2, sticky=W)

        def lastDate(event):
            global dateValueLabel, index, maeslantkeringValueLabel
            index -= 1
            dateValueLabel["text"] = str(dataList[index]['date'])
            timeValueLabel["text"] = str(dataList[index]['time'])
            waterValueLabel["text"] = str(dataList[index]['value'])
            if waterValueLabel == "1":
                maeslantkeringValueLabel["text"] = "Dicht"
            else:
                maeslantkeringValueLabel["text"] = "Open"
            print("Vorige datum")

        def nextDate(event):
            global dateValueLabel, index, maeslantkeringValueLabel
            index += 1
            dateValueLabel["text"] = str(dataList[index]['date'])
            timeValueLabel["text"] = str(dataList[index]['time'])
            waterValueLabel["text"] = str(dataList[index]['value'])
            if waterValueLabel["text"] == "1":
                maeslantkeringValueLabel["text"] = "Dicht"
            else:
                maeslantkeringValueLabel["text"] = "Open"
            print("Volgende datum")

        lastButton = Button(rightFrame, text="Last")
        lastButton.bind("<Button-1>", lastDate)
        lastButton.grid(row=15, column=1, columnspan=2)
        nextButton = Button(rightFrame, text="Next")
        nextButton.bind("<Button-1>", nextDate)
        nextButton.grid(row=15, column=3, columnspan=2)

        def openGate():
            for number in range(0, 21, 2):
                global photoLeft, photoRight
                photoLeft = PhotoImage(file='linkerarm/linker' + str(number) + '.png')
                photoRight = PhotoImage(file='rechterarm/rechter' + str(number) + '.png')
                time.sleep(0.1)

        def closeGate():
            for number in range(20, -1, 2):
                global photoLeft, photoRight
                photoLeft = PhotoImage(file='linkerarm/linker' + str(number) + '.png')
                photoRight = PhotoImage(file='rechterarm/rechter' + str(number) + '.png')
                time.sleep(0.1)

        if maeslantkeringValueLabel == "Open":
            photoLeft = PhotoImage(file='linkerarm/linker0.png')
        else:
            photoLeft = PhotoImage(file='linkerarm/linker20.png')
        imageLeft = Label(leftFrame, image=photoLeft)
        imageLeft.image = photoLeft
        imageLeft.pack(side=LEFT)

        if maeslantkeringValueLabel == "Open":
            photoRight = PhotoImage(file='rechterarm/rechter0.png')
        else:
            photoRight = PhotoImage(file='rechterarm/rechter20.png')
        imageRigth = Label(leftFrame, image=photoRight)
        imageRigth.image = photoRight
        imageRigth.pack(side=RIGHT)

root = Tk()
root.geometry("1000x600")
s = StandardWindow(root)
root.mainloop()

# Canvas drawing test:
# canvas = Canvas(leftFrame, width=700, height=700)
# canvas.pack()
# Drawings:
# greenbox = canvas.create_rectangle(50, 50, 150, 150, fill="green")
# blackLine = canvas.create_line(0, 0, 700, 700)
# redLine = canvas.create_line(200,0, 0, 200, fill="red")
