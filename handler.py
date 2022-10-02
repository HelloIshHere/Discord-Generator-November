import client
import json
import logger

with open("config.json") as data:
    config = json.load(data)

def handler(choice):

    if choice == 1:
        logger.log("Starting to Create EMAIL VERIFIED ACCS")
        if config['keeprunning'] == "yes":
            while True:

                client.handleregister_normal()
        else:
            client.handleregister_normal()

    if choice == 2:
        logger.log("Starting to Create FULLY VERIFIED ACCS")
        if config['keeprunning'] == "yes":
            while True:

                client.handleregister_phone()
        else:

            client.handleregister_phone()


    if choice == 3:
        logger.log("Starting to Create Unverified ACCS")
        if config['keeprunning'] == "yes":
            while True:
                client.handleunverified()
        else:
            client.handleunverified()




