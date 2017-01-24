import requests
import csv
import xmltodict
import time
import random
import os


def retrieve_status(test=False):
    if test is False:
        try:
            api_url = "ipadress van de pi waar sensors aan hangen"
            response = requests.get(api_url)

            parsedResponse = xmltodict.parse(response.text)

            return parsedResponse
        except:
            return "Error"
    if test:
        return random.choice(["closed", "open", "Error"])


def retrieve_data(test=False):
    if test is False:
        try:
            api_url = "ipadress van de pi waar sensors aan hangen"
            response = requests.get(api_url)

            parsedResponse = xmltodict.parse(response.text)

            save_data(parsedResponse)
            return parsedResponse
        except:
            save_data(2)
            return 2
    elif test:
        data = random.choice([0, 1, 2])
        save_data(data, True)
        return data


def save_data(data, test=False):
    if test is False:
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
    elif test:
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


def execute_decision(action, test=False):
    if test is False:
        api_url = "ipadress van de pi waar sensors aan hangen"
        response = requests.post(api_url, data=action)

        if response.status_code == requests.codes.ok:
            print("No problems")
        else:
            print("Something went wrong, a " + str(response.status_code) + " error was returned")
    elif test:
        print(random.choice(["No problems", "Something went wrong"]))


def make_decision(status, test=False):
    if test is False:
        try:
            data = retrieve_data()
            if data == 0 and status == "open":
                print("Nothing had to be done")
            elif data == 0 and status == "closed":
                print("The \'thing\' will open")
                execute_decision("open")
            elif data == 1 and status == "closed":
                print("Nothing had to be done")
            elif data == 1 and status == "open":
                print("The \'thing\' will close")
                execute_decision("close")
            elif data == 2:
                print("Something went wrong with retrieving the data")
        except:
            print("Something went wrong, we\'ll try again later")
    if test:
        data = retrieve_data(test)
        if data == 0 and status == "open":
            print("Nothing had to be done")
        elif data == 0 and status == "closed":
            print("The \'thing\' will open")
            execute_decision("open", test)
        elif data == 1 and status == "closed":
            print("Nothing had to be done")
        elif data == 1 and status == "open":
            print("The \'thing\' will close")
            execute_decision("close", test)
        elif data == 2:
            print("Something went wrong with retrieving the data")

def main():
    test = eval(input("Is this a test?"))
    while True:
        status = retrieve_status(test)
        make_decision(status, test)
        if test is False:
            time.sleep(600)
        elif test:
            time.sleep(2)

if __name__ == '__main__':
    main()
