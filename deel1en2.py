import requests
import csv
import xmltodict
import time
import random
import os


def retrieve_status(api_url, test=False):
    # This function can be used to retrieve the status of the flood defence with an API.
    # The parameter test can be used while the API isn't connected yet so the script can still be tested
    if test is False:
        try:
            response = requests.get(api_url)

            parsedResponse = xmltodict.parse(response.text)

            return parsedResponse
        except:
            return "Error"
    if test:
        return random.choice(["closed", "open", "Error"])


def retrieve_data(api_url, test=False):
    # This function can be used to retrieve the data from the sensors with the API.
    # The parameter test can be used while the API isn't connected yet so the script can still be tested
    if test is False:
        # The function tries to retrieve the data but if it fails it returns a 2 so the rest of the script knows something went wrong
        try:
            response = requests.get(api_url)

            parsedResponse = xmltodict.parse(response.text)

            return parsedResponse
        except:
            return 2
    elif test:
        data = random.choice([0, 1, 2])
        return data


def save_data(data, test=False):
    # This function is used to save the data from the sensors.
    # The parameter test can be used while the API isn't connected yet so the script can still be tested
    if test is False:
        if os.path.isfile("data.csv"):  # This is used to check if the file exist.
            # If the file exists the new data is added at the end of the file.
            with open("data.csv", "a", newline="") as csvfile:
                fieldnames = ["date", "time", "value"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                date = time.strftime("%d-%m-%Y")
                timev = time.strftime("%H:%M:%S")  # This variable as an extra v at the end because otherwise it would be mistaken for the module

                writer.writerow({"date": date, "time": timev, "value": data})
        if os.path.isfile("data.csv") is False:
            # If the file doesn't exist it makes a new file, writes the field names and then adds the data.
            with open("data.csv", "a", newline="") as csvfile:
                fieldnames = ["date", "time", "value"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                date = time.strftime("%d-%m-%Y")
                timev = time.strftime("%H:%M:%S")  # This variable as an extra v at the end because otherwise it would be mistaken for the module

                writer.writeheader()
                writer.writerow({"date": date, "time": timev, "value": data})
    elif test:
        # If it's a test it uses a test file but the rest is the same as above.
        if os.path.isfile("testdata.csv"):
            with open("testdata.csv", "a", 1, newline="") as csvfile:
                fieldnames = ["date", "time", "value"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                date = time.strftime("%d-%m-%Y")
                timev = time.strftime("%H:%M:%S")

                writer.writerow({"date": date, "time": timev, "value": data})
                csvfile.flush()
                os.fsync(csvfile.fileno())
        if os.path.isfile("testdata.csv") is False:
            with open("testdata.csv", "a", 1, newline="") as csvfile:
                fieldnames = ["date", "time", "value"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                date = time.strftime("%d-%m-%Y")
                timev = time.strftime("%H:%M:%S")

                writer.writeheader()
                writer.writerow({"date": date, "time": timev, "value": data})
                csvfile.flush()
                os.fsync(csvfile.fileno())


def execute_decision(action, api_url, test=False):
    # This function is used to open the arms of the flood defence with the API.
    # The parameter test can be used while the API isn't connected yet so the script can still be tested
    if test is False:
        response = requests.post(api_url, data=action)

        if response.status_code == requests.codes.ok:  # This checks if the request went okay
            print("No problems with executing the decision")
        else:  # If the request returned an error code it will be printed for debugging
            print("Something went wrong, a " + str(response.status_code) + " error was returned")
            return "Error"
    elif test:
        random_variable = random.choice(["No problems", "Error"])
        if random_variable == "Error":
            print("Something went wrong with executing the decision")
            return random_variable
        else:
            print("No problems with executing the decision")


def make_decision(status, api_url, test=False):
    # This function uses the retrieved data and status to decide if something has to be done, if something has to be done it executes that decision
    # The parameter test can be used while the API isn't connected yet so the script can still be tested
    if test is False:
        try:
            data = retrieve_data(api_url)
            save_data(data)
            if data == 0 and status == "open":
                print("Nothing had to be done")
            elif data == 0 and status == "closed":
                print("The \'thing\' will open")
                if execute_decision("open", api_url) == "Error":
                    return "Error"
            elif data == 1 and status == "closed":
                print("Nothing had to be done")
            elif data == 1 and status == "open":
                print("The \'thing\' will close")
                if execute_decision("close", api_url) == "Error":
                    return "Error"
            elif data == 2:
                print("Something went wrong with retrieving the data")
                return "Error"
        except:
            print("Something went wrong, we\'ll try again")
            return "Error"
    if test:
        data = retrieve_data(api_url, test)
        save_data(data, test)
        if data == 0 and status == "open":
            print("Nothing had to be done")
        elif data == 0 and status == "closed":
            print("The \'thing\' will open")
            if execute_decision("open", api_url, test) == "Error":
                return "Error"
        elif data == 1 and status == "closed":
            print("Nothing had to be done")
        elif data == 1 and status == "open":
            print("The \'thing\' will close")
            if execute_decision("close", api_url, test) == "Error":
                return "Error"
        elif data == 2:
            print("Something went wrong with retrieving the data")
            return "Error"


def main():
    # This function is used if the script is run as the main program.
    retries_status = 0
    retries_decision = 0
    test = eval(input("Is this a test? "))
    api_url = ""
    if test is False:
        api_url = input("What is the url of the API? ")
    while True:
        status = retrieve_status(api_url, test)
        if status is not "Error":
            retries_status = 0
            if make_decision(status, api_url, test) is not "Error":
                retries_decision = 0
            elif make_decision(status, api_url, test) == "Error":
                if retries_decision < 3:
                    retries_decision += 1
                    print("We\'ll wait for 3 seconds and try again, decision")
                    time.sleep(3)
                    continue
                elif retries_decision >= 3:
                    retries_decision = 0
        elif retries_status < 3 and status == "Error":
            retries_status += 1
            print("We\'ll wait for 3 seconds and try again, status")
            time.sleep(3)
            continue
        elif retries_status >= 3 and status == "Error":
            retries_status = 0

        if test is False:
            time.sleep(600)
        elif test:
            time.sleep(2)

if __name__ == '__main__':  # This checks if the script is run as the main program.
    main()
