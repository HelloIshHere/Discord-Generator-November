import httpx
import random
import time
import json
import captcha

with open("config.json") as data:
    config = json.load(data)




def buynumber():
    token = config['fivesim-apikey']  # account secret key
    country = config['fivesim-country']  # specify country
    operator = config['fivesim-operator']  # specify operator
    product = 'discord'

    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
    }

    timelimit = False

    while timelimit is not True:
        val = "POS"
        # Buy Number
        while True:
            try:
                response = httpx.get(
                    'https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product,
                    headers=headers)
                print(response.text)
                notfound = 'not found'
                if notfound not in response.text:
                    time.sleep(2)
                    # Getting OrderID and PhoneNumber for future use
                    id = response.json()['id']
                    orderid = str(id)
                    phonenumber = response.json()['phone']

                    orderdata = {
                        'id': orderid,
                        'number': phonenumber
                    }

                    return orderdata
            except:
                continue





def cancelorder(orderdata):
    headers = {
        'Authorization': 'Bearer ' + config['fivesim-apikey'],
        'Accept': 'application/json',
    }
    httpx.get('https://5sim.net/v1/user/cancel/' + orderdata['id'], headers=headers)


def checkforsms(orderdata):
    headers = {
        'Authorization': 'Bearer ' + config['fivesim-apikey'],
        'Accept': 'application/json',
    }

    Nope ="no"

    countdown = 30
    while (countdown):
        response = httpx.get('https://5sim.net/v1/user/check/' + orderdata['id'], headers=headers)
        time.sleep(1)
        countdown -= 1
        sms = response.json()['sms']
        if str(sms) != "[]" and "null":
            code = response.json()['sms'][0]['code']

            # Finishing the current order as code is recieved
            code = str(code)
            return code
        else:
            continue
    return Nope

def finishorder(orderdata):
    headers = {
        'Authorization': 'Bearer ' + config['fivesim-apikey'],
        'Accept': 'application/json',
    }
    httpx.get('https://5sim.net/v1/user/finish/' + orderdata['id'], headers=headers)


def submitphone(acctoken,phonenumber):
    proxy = config['proxy']
    pro = {
        "all://": f"http://{proxy}"
    }

    header1 = {
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        "Accept-Encoding": 'gzip, deflate, br',
        "Accept-Language": 'en-US,en;q=0.5',
        "Connection": 'keep-alive',
        "DNT": '1',
        "Host": 'discord.com',
        "Sec-Fetch-Dest": 'document',
        "Sec-Fetch-Mode": 'navigate',
        "Sec-Fetch-Site": 'none',
        "Sec-Fetch-User": '?1',
        "Upgrade-Insecure-Requests": '1',
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0'
    }

    getcookie = httpx.get("https://discord.com", headers=header1).headers['set-cookie']

    sep = getcookie.split(";")
    sx = sep[0]
    sx2 = sx.split("=")
    dfc = sx2[1]

    split = sep[6]
    split2 = split.split(",")
    split3 = split2[1]
    split4 = split3.split("=")
    sdc = split4[1]

    header2 = {
        "Accept": '*/*',
        "Accept-Language": 'en-US,en;q=0.5',
        "Connection": 'keep-alive',
        "DNT": '1',
        "Cookie": f'__dcfduid={dfc}; __sdcfduid={sdc}; locale=en-US',
        "Referer": 'https://discord.com/register',
        "Host": 'discord.com',
        "Sec-Fetch-Dest": 'empty',
        "Sec-Fetch-Mode": 'cors',
        "Sec-Fetch-Site": 'same-origin',
        "TE": 'trailers',
        "X-Track": 'eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6OTQuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC85NC4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTQuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNSIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5OTk5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0'
    }

    fingerprintreq = httpx.get("https://discord.com/api/v9/experiments", headers=header2, timeout=10)

    time.sleep(2)

    fingerprint = fingerprintreq.json()['fingerprint']

    f = fcs
    c = []

    c = f.generate(f, length=32, cbank="a0", amount=1)

    cookiesample = f'OptanonConsent=isIABGlobal=false&datestamp=Thu+Dec+30+2021+00%3A45%3A47+GMT%2B0530+(India+Standard+Time)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _gcl_au=1.1.1954317774.1640805348; locale=en-US; _ga=GA1.2.1805929657.1640805348; _gid=GA1.2.1453957326.1640805348; _gat_UA-53577205-2=1; __dcfduid={dfc}; __sdcfduid={sdc}'
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    daynum = ['10', '12', '13', '14', '20', '21']
    replaceday = cookiesample.replace("Thu", random.choice(days))
    replacedate = cookiesample.replace("30", random.choice(daynum))
    cookie = cookiesample.replace("Dec", random.choice(months))

    headerforphone = {
        "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkRpc2NvcmQgQ2xpZW50IiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X3ZlcnNpb24iOiIwLjAuMjYzIiwib3NfdmVyc2lvbiI6IjE5LjYuMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NDU0MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
        "X-Fingerprint": fingerprint,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.264 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "Authorization": acctoken,
        "Cookie": cookie
    }

    payload = {
        "phone": str(phonenumber)
    }

    while True:
        try:
            activate = httpx.post('https://discord.com/api/v9/users/@me/phone', headers=headerforphone,
                                  json=payload, timeout=20, proxies=pro)
            print(activate.text)
            message = "You need to update your app to verify your phone number."
            if message in activate.text:
                key = captcha.getcaptchatoken()
                payload = {
                    "phone": str(phonenumber),
                    "captcha_key": key
                }
                activate = httpx.post('https://discord.com/api/v9/users/@me/phone', headers=headerforphone,
                                      json=payload, timeout=20, proxies=pro)
                print(activate.text)
                return activate.status_code
            else:
                return activate.status_code

        except:
            continue

def submitrecievedcode(accpass,acctoken,phonenumber,code):
    proxy = config['proxy']
    pro = {
        "all://": f"http://{proxy}"
    }

    header1 = {
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        "Accept-Encoding": 'gzip, deflate, br',
        "Accept-Language": 'en-US,en;q=0.5',
        "Connection": 'keep-alive',
        "DNT": '1',
        "Host": 'discord.com',
        "Sec-Fetch-Dest": 'document',
        "Sec-Fetch-Mode": 'navigate',
        "Sec-Fetch-Site": 'none',
        "Sec-Fetch-User": '?1',
        "Upgrade-Insecure-Requests": '1',
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0'
    }

    getcookie = httpx.get("https://discord.com", headers=header1).headers['set-cookie']

    sep = getcookie.split(";")
    sx = sep[0]
    sx2 = sx.split("=")
    dfc = sx2[1]

    split = sep[6]
    split2 = split.split(",")
    split3 = split2[1]
    split4 = split3.split("=")
    sdc = split4[1]

    header2 = {
        "Accept": '*/*',
        "Accept-Language": 'en-US,en;q=0.5',
        "Connection": 'keep-alive',
        "DNT": '1',
        "Cookie": f'__dcfduid={dfc}; __sdcfduid={sdc}; locale=en-US',
        "Referer": 'https://discord.com/register',
        "Host": 'discord.com',
        "Sec-Fetch-Dest": 'empty',
        "Sec-Fetch-Mode": 'cors',
        "Sec-Fetch-Site": 'same-origin',
        "TE": 'trailers',
        "X-Track": 'eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6OTQuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC85NC4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTQuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNSIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5OTk5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0'
    }

    fingerprintreq = httpx.get("https://discord.com/api/v9/experiments", headers=header2, timeout=10)

    time.sleep(2)

    fingerprint = fingerprintreq.json()['fingerprint']

    f = fcs
    c = []

    c = f.generate(f, length=32, cbank="a0", amount=1)

    cookiesample = '__dcfduid=656992ffd148676671de4e048a4dc5c5; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Wed+Jul+21+2021+16%3A30%3A27+GMT%2B0300&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _gcl_au=1.1.39545198.1626873646'
    randomcookiec = cookiesample.replace("656992ffd148676671de4e048a4dc5c5", c)
    months = ['May', 'Apr', 'Mar', 'Jan', 'Feb']
    days = ['Sun', 'Mon', 'Tue', 'Wed']
    daynum = ['10', '12', '13', '14', '20', '21']
    replaceday = randomcookiec.replace("Wed", random.choice(days))
    replacedate = replaceday.replace("21", random.choice(daynum))
    cookie = replacedate.replace("Jul", random.choice(months))

    headerforphone = {
        "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkRpc2NvcmQgQ2xpZW50IiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X3ZlcnNpb24iOiIwLjAuMjYzIiwib3NfdmVyc2lvbiI6IjE5LjYuMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NDU0MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
        "X-Fingerprint": fingerprint,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.264 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "Authorization": acctoken,
        "Cookie": cookie
    }

    payload={

        "phone": str(phonenumber),
        'code': str(code),
    }

    submit = httpx.post('https://discord.com/api/v9/phone-verifications/verify', headers=headerforphone,
                        json=payload, timeout=20)


    tokenforphone = submit.json()['token']
    final = {
        'password': accpass,
        'phone_token': str(tokenforphone)
    }
    r = httpx.post('https://discord.com/api/v9/users/@me/phone',
                         headers=headerforphone,
                         json=final, timeout=20)







def handlephone(accpass,token):

    while True:
        number = buynumber()
        print("Using Number: ",number['number'])
        response = submitphone(token, number['number'])
        if response == 204:
            code = checkforsms(number['id'])

            if code == 'no':
                print("TIME LIMIT EXCEEDED TRYING NEW NUMBER")
                cancelorder(number['id'])
                continue
            if code != "no":
                print("Recieved SMS: ", code)
                submitrecievedcode(accpass,token,number['number'],code)
                finishorder(number['id'])
                return False
        else:
            print("INVALID NUMBER")
            cancelorder(number['id'])
            continue




                
