from tkinter import *
import csv

class StandardWindow:

    def __init__(self, master):
        # Global Variables:
        global dateValueLabel, index, maeslantkeringValueLabel, photo, index_2, image
        index = -1
        index_2 = 0

        # Frames:
        leftFrame = Frame(root, width=600, height=600, bd=1, relief=SOLID)
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

            if dataList[index]['value'] == "1":
                maeslantkeringValueLabel["text"] = "Dicht"
                closeGate()
            else:
                maeslantkeringValueLabel["text"] = "Open"
                openGate()
            print("Vorige datum")

        def nextDate(event):
            global dateValueLabel, index, maeslantkeringValueLabel
            index += 1
            dateValueLabel["text"] = str(dataList[index]['date'])
            timeValueLabel["text"] = str(dataList[index]['time'])
            waterValueLabel["text"] = str(dataList[index]['value'])

            if dataList[index]['value'] == "1":
                maeslantkeringValueLabel["text"] = "Dicht"
                closeGate()
            else:
                maeslantkeringValueLabel["text"] = "Open"
                openGate()
            print("Volgende datum")

        def openCloseButtton(event):
            global index_2
            if ((index_2 % 2) == 0):
                openGate()
                print("Open gate")
                index_2 += 1
            else:
                closeGate()
                print("Close gate")
                index_2 += 1

        lastButton = Button(rightFrame, text="Last")
        lastButton.bind("<Button-1>", lastDate)
        lastButton.grid(row=15, column=1, columnspan=2)
        nextButton = Button(rightFrame, text="Next")
        nextButton.bind("<Button-1>", nextDate)
        nextButton.grid(row=15, column=3, columnspan=2)
        changeButton = Button(rightFrame, text="change")
        changeButton.bind("<Button-1>", openCloseButtton)
        changeButton.grid(row=15, column=5, columnspan=2)

        def closeGate():
            global photo, image
            photo = PhotoImage(file='armen/dicht.png')
            image.configure(image=photo)
            image.image = photo
            print("dicht")

        def openGate():
            global photo, image
            photo = PhotoImage(file='armen/open.png')
            image.configure(image=photo)
            image.image = photo
            print("open")

        if maeslantkeringValueLabel == "Open":
            photo = PhotoImage(file='armen/open.png')
        else:
            photo = PhotoImage(file='armen/dicht.png')
        image = Label(leftFrame, image=photo)
        image.image = photo
        image.pack()

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
