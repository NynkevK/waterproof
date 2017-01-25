from tkinter import *

class StandardWindow:

    def __init__(self, master):
        #TODO: Misschien een simulatie ervan maken dat men zelf waarden in kan vullen en dat er dan daarop ingespeeld kan worden

        # Frames:
        leftFrame = Frame(root, width=600, height=600, bd=1, relief=SOLID)
        rightFrame = Frame(root, width=400, height=600, bd=1, relief=SOLID)
        leftFrame.pack(fill=BOTH, side=LEFT)
        rightFrame.pack()

        #Textvariables:
        date = StringVar()
        time = StringVar()
        water = StringVar()
        maeslantkering = StringVar()
        pi1 = StringVar()
        pi2 = StringVar()

        # All the labels used:
        emptyLabel = Label(rightFrame, text=" ")
        dateLabel = Label(rightFrame, text="Datum: ")
        timeLabel = Label(rightFrame, text="Tijd: ")
        waterLabel = Label(rightFrame, text="Waterhoogte: ")
        maeslantkeringLabel = Label(rightFrame, text="Maeslantkering: ")
        pi1Label = Label(rightFrame, text="Linker Pi : ")
        pi2Label = Label(rightFrame, text="Rechter Pi: ")
        dateValueLabel = Label(rightFrame, textvariable=date)
        timeValueLabel = Label(rightFrame, textvariable=time)
        waterValueLabel = Label(rightFrame, textvariable=water)
        maeslantkeringValueLabel = Label(rightFrame, textvariable=maeslantkering)
        pi1ValueLabel = Label(rightFrame, textvariable=pi1)
        pi2ValueLabel = Label(rightFrame, textvariable=pi2)

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

        with open("../testdata.csv", "r") as data:
            lines = data.readlines()

            for line in lines:
                print(line)

        #TODO: Dict van maken zodat alles met elkaar uitgelezen kan worden

        #TODO: Alle functies die moeten gebeuren met Ezri langsgaan en kijken hoe en wat

        # Set variable values
        date.set("Haalt datum uit CSV bestand")
        time.set("Geeft tijd bij datum")
        water.set("Geeft waterniveau bij datum en tijd")
        maeslantkering.set("Status Maeslantkering (open/dicht)")
        pi1.set("Geeft status van Linker pi (online/offline)")
        pi2.set("Geeft status van Rechter pi (online/offline")

        def lastDate(event):
            #TODO: Zorgen dat vorige input genomen wordt van CSV bestand
            print("Vorige datum")

        def nextDate(event):
            #TODO: Zorgen dat volgende input genomen wordt van CSV bestand
            print("Volgende datum")

        lastButton = Button(rightFrame, text="Last")
        lastButton.bind("<Button-1>", lastDate)
        lastButton.grid(row=15, column=1, columnspan=2)
        nextButton = Button(rightFrame, text="Next")
        nextButton.bind("<Button-1>", nextDate)
        nextButton.grid(row=15, column=3, columnspan=2)

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

        # How to display a photo:
        # photo = PhotoImage(file="Maeslantkering.png")
        # label = Label(leftFrame, image=photo)
        # label.pack()
