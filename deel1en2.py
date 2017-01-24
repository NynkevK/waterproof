import requests
import csv
import xmltodict
import time
import random
import os

def retrieve_data(test=False):
    if test==False:
        try:
            api_url = "ipadress van de pi waar sensors aan hangen"
            response = requests.get(api_url)

            parsedResponse = xmltodict.parse(response.text)

            return parsedResponse
        except:
            return 2
    elif test==True:
        return random.choice([0,1])

def save_data(data, test=False):
    if test==False:
        if os.path.isfile("data.csv"):
            with open("data.csv", "a", newline="") as csvfile:
                fieldnames = ["date","time","value"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                date = time.strftime("%w-%m-%Y")
                timev = time.strftime("%H:%M:%S")

                writer.writerow({"date": date,"time": timev,"value": data})
        if os.path.isfile("data.csv") == False:
            with open("data.csv", "a", newline="") as csvfile:
                fieldnames = ["date","time","value"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                date = time.strftime("%w-%m-%Y")
                timev = time.strftime("%H:%M:%S")

                writer.writeheader()
                writer.writerow({"date": date,"time": timev,"value": data})
    elif test==True:
        if os.path.isfile("testdata.csv"):
            with open("testdata.csv", "a", newline="") as csvfile:
                fieldnames = ["date","time","value"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                date = time.strftime("%w-%m-%Y")
                timev = time.strftime("%H:%M:%S")

                writer.writerow({"date": date,"time": timev,"value": data})
        if os.path.isfile("testdata.csv") == False:
            with open("testdata.csv", "a", newline="") as csvfile:
                fieldnames = ["date","time","value"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                date = time.strftime("%w-%m-%Y")
                timev = time.strftime("%H:%M:%S")

                writer.writeheader()
                writer.writerow({"date": date,"time": timev,"value": data})
for keer in range(0, 20):
    save_data(retrieve_data(True), True)
