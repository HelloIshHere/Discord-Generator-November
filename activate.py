import json
import httpx
import time
import random
import logger

def remove(string):
    return string.replace(" ", "")


with open("config.json") as data:
    config = json.load(data)


apikey = config['sms-activate-apikey']
country = config['sms-activate-country']
operator = config['sms-activate-operator']
sms_api = 'https://api.sms-activate.org/stubs/handler_api.php?'
sms_api2 = 'https://sms-activate.ru/stubs/handler_api.php?'


def buynumber():

    while True:

        try:
            number = httpx.post(
                    sms_api + f'action=getNumber&api_key={apikey}&service=ds&forward=0&country={country}')

            if ':' in number.text:
                phonenumber = '+' + number.text.split(':')[2]
                id = number.text.split(':')[1]

                orderdata = {
                    "number": phonenumber,
                    "id": id
                }

                return orderdata
            else:
                logger.log("No Number Available")
                time.sleep(2)
                continue
        except:
            continue






def checkforsms(orderdata):
    countdown = 30
    id = orderdata['id']

    Nope = "no"
    payload = {'api_key': apikey,"id":id, 'action': 'getStatus'}

    while (countdown):
        response = httpx.get(sms_api2,params=payload)
        time.sleep(1)
        countdown -= 1
        time.sleep(1)

        if response.text != "STATUS_WAIT_CODE":
            stres = str(response.text)
            w = stres.split(":")
            res = w[1]
            newcode = res
            return newcode
        else:
            continue
    return Nope

def cancel(orderdata):
    id = orderdata['id']
    status = httpx.post(sms_api2 + f'action=setStatus&api_key={apikey}&id={id}&status=6')



def finish(orderdata):
    id = orderdata['id']
    status = httpx.post(sms_api2 + f'action=setStatus&api_key={apikey}&id={id}&status=6')










