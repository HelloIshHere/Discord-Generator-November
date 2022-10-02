import json
import httpx
import helper
import random
import activate
import captcha
import fivesim
import logger
import emailverifer
import time
import base64
import os

with open("config.json") as data:
    config = json.load(data)



def gatherutilities_phone():
    proxy = {
        "all://": f"http://{config['proxy']}"
    }
    headers = {
        "User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
    }

    while True:
        try:
            getcookie = httpx.get("https://discord.com/ios/106.0/manifest.json", headers=headers,proxies=proxy).headers['set-cookie']
            break
        except:
            continue


    sep = getcookie.split(";")
    sx = sep[0]
    sx2 = sx.split("=")
    dfc = sx2[1]

    split = sep[6]
    split2 = split.split(",")
    split3 = split2[1]
    split4 = split3.split("=")
    sdc = split4[1]

    headers2 = {
        "user-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
        "Cookie": f"__dcfduid={dfc}; __sdcfduid={sdc}",
        "x-super-properties": "eyJvcyI6ImlPUyIsImJyb3dzZXIiOiJEaXNjb3JkIGlPUyIsImRldmljZSI6ImlQaG9uZTEzLDIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJjbGllbnRfdmVyc2lvbiI6IjEwNi4wIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiZGV2aWNlX2FkdmVydGlzZXJfaWQiOiIxN0MwNzg4MS0wOUEwLTQ3RjItQjM2RC1FODk2MUIzOTUyRTEiLCJkZXZpY2VfdmVuZG9yX2lkIjoiNUM1NUEzMUQtMDY2RS00NjAwLThGNEEtRTQyRjNCNjY3MjNBIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiIiwiYnJvd3Nlcl92ZXJzaW9uIjoiIiwib3NfdmVyc2lvbiI6IjE0LjEiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTU3NSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
    }

    while True:
        try:
            fingerprintreq = httpx.get("https://discord.com/api/v9/experiments", headers=headers2,
                                       timeout=10,proxies=proxy)
            break
        except:
            continue



    fingerprint = fingerprintreq.json()['fingerprint']

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    if config['username'] != "random":
        username = config['username']
    if config['username'] == "random":
        username = helper.getusername()

    if config['password'] != "random":
        password = config['password']
    if config['password'] == "random":
        password = helper.random_char(10)+str(random.choice(numbers))


    email = helper.random_char(13)+str(random.choice(numbers))+ "@" +config['domain']



    registeringdata = {
        'dfc':dfc,
        'sdc':sdc,
        'fingerprint':fingerprint,
        'username':username,
        'email':email,
        'password':password

    }

    return registeringdata


def submitphone(rdata):
    proxy = {
        "all://": f"http://{config['proxy']}"
    }
    dfc= rdata['dfc']
    sdc = rdata['sdc']

    cookiesample = f'OptanonConsent=isIABGlobal=false&datestamp=Thu+Dec+30+2022+00%3A45%3A47+GMT%2B0530+(India+Standard+Time)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _gcl_au=1.1.1954317774.1640805348; locale=en-US; _ga=GA1.2.1805929657.1640805348; _gid=GA1.2.1453957326.1640805348; _gat_UA-53577205-2=1; __dcfduid={dfc}; __sdcfduid={sdc}'
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    daynum = ['10', '12', '13', '14', '20', '21']
    replaceday = cookiesample.replace("Thu", random.choice(days))
    replacedate = replaceday.replace("30", random.choice(daynum))
    cookie = replacedate.replace("Dec", random.choice(months))
    rdata['cok'] = cookie



    registerheaders = {
        "Content-Type": "application/json",
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
        "Cookie": cookie,
        "x-super-properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6OTUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC85NS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTUuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNSIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg4MDcsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
    }






    registerpayload = {
        "phone": rdata['number']
    }

    while True:
        try:
            register = httpx.post("https://discord.com/api/v9/auth/register/phone", headers=registerheaders,
                                  json=registerpayload,
                                  timeout=20, proxies=proxy)

            return register.status_code
        except:
            continue






def submit_recievedcode(rdata):


    header = {
        "Content-Type": "application/json",
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
        "Cookie": rdata['cok'],
        "x-super-properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6OTUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC85NS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTUuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNSIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg4MDcsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
    }

    payload = {
        "phone": rdata['number'],
        "code": rdata['code']
    }

    while True:
        try:
            resp = httpx.post("https://discord.com/api/v9/phone-verifications/verify", headers=header, json=payload)
            rdata['phone-token'] = resp.json()['token']
            return rdata
        except:
            continue




def register_normal(rdata):

    dfc = rdata['dfc']
    sdc = rdata['sdc']
    proxy = {
        "all://": f"http://{config['proxy']}"
    }
    header3 = {
        "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85My4wLjQ1NzcuODIgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny44MiIsIm9zX3ZlcnNpb24iOiIxMC4xNS43IiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        "X-Fingerprint": rdata['fingerprint'],
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
        "Authorization": "undefined",
        "Cookie": f"__dcfduid={dfc}; __sdcfduid={sdc}"

    }

    payload = {
        "fingerprint": rdata['fingerprint'],
        "consent" : True,
        "captcha_key" : rdata['key'],
        "username" : rdata['username'],
    }

    while True:
        try:
            resp = httpx.post("https://discord.com/api/v9/auth/register", headers=header3, json=payload, proxies=proxy)
            token = resp.json()['token']
            break
        except:
            continue


    header1 = {
        'host': "discord.com",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
        'accept': "*/*",
        'accept-language': "en-US,en;q=0.5",
        'content-type': "application/json",
        'authorization': token,
        'x-super-properties': "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6OTUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC85NS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTUuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNSIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
        'x-fingerprint': rdata['fingerprint'],
        'x-discord-locale': "en-US",
        'x-debug-options': "bugReporterEnabled",
        'origin': "https://discord.com",
        'alt-used': "discord.com",
        'connection': "keep-alive",
        'referer': "https://discord.com/channels/@me",
        'cookie': f"__dcfduid={dfc}; __sdcfduid={sdc}; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Sat+Jan+01+2022+00%3A10%3A58+GMT%2B0530+(India+Standard+Time)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _gcl_au=1.1.1745667611.1640976059; _ga=GA1.2.1048474825.1640976060; _gid=GA1.2.1260035076.1640976060; _fbp=fb.1.1640976307006.828724092; _gat_UA-53577205-2=1",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-origin",
        'te': "trailers",
        'cache-control': "no-cache",
    }
    payload1 = {
        "date_of_birth": "1997-03-04"
    }

    while True:
        try:
            adddob = httpx.patch("https://discord.com/api/v9/users/@me", headers=header1,
                                 json=payload1, timeout=30)
            newtoken = adddob.json()['token']
            break
        except:
            continue

    header2 = {
        'host': "discord.com",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
        'accept': "*/*",
        'accept-language': "en-US,en;q=0.5",
        'content-type': "application/json",
        'authorization': newtoken,
        'x-super-properties': "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6OTUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC85NS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTUuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNSIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
        'x-fingerprint': rdata['fingerprint'],
        'x-discord-locale': "en-US",
        'x-debug-options': "bugReporterEnabled",
        'origin': "https://discord.com",
        'alt-used': "discord.com",
        'connection': "keep-alive",
        'referer': "https://discord.com/channels/@me",
        'cookie': f"__dcfduid={dfc}; __sdcfduid={sdc}; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Sat+Jan+01+2022+00%3A10%3A58+GMT%2B0530+(India+Standard+Time)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _gcl_au=1.1.1745667611.1640976059; _ga=GA1.2.1048474825.1640976060; _gid=GA1.2.1260035076.1640976060; _fbp=fb.1.1640976307006.828724092; _gat_UA-53577205-2=1",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-origin",
        'te': "trailers",
        'cache-control': "no-cache",
    }
    payload2 = {
        'email': rdata['email'],
        'password': rdata['password']
    }

    while True:
        try:
            addmail = httpx.patch("https://discord.com/api/v9/users/@me", headers=header2,
                                  json=payload2, timeout=30)

            rdata['token'] = addmail.json()['token']
            break
        except:
            continue



    return rdata






def register_phone(rdata):

    dfc = rdata['dfc']
    sdc = rdata['sdc']
    proxy = {
        "all://": f"http://{config['proxy']}"
    }
    header3 = {
        "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85My4wLjQ1NzcuODIgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny44MiIsIm9zX3ZlcnNpb24iOiIxMC4xNS43IiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        "X-Fingerprint": rdata['fingerprint'],
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
        "Authorization": "undefined",
        "Cookie": f"__dcfduid={dfc}; __sdcfduid={sdc}"

    }

    payload = {
        "fingerprint": rdata['fingerprint'],
        "password": rdata['password'],
        "consent" : True,
        "phone_token" : rdata['phone-token'],
        "captcha_key" : rdata['key'],
        "username" : rdata['username'],
    }

    while True:
        try:
            resp = httpx.post("https://discord.com/api/v9/auth/register", headers=header3, json=payload, proxies=proxy)

            token = resp.json()['token']
            break
        except:
            continue


    header4 = {
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/',
        'authorization': token,
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
        'X-Super-Properties': 'eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6OTQuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC85NC4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTQuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNSIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6Ind3dy5nb29nbGUuY29tIiwic2VhcmNoX2VuZ2luZV9jdXJyZW50IjoiZ29vZ2xlIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTk5OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
    }
    check = httpx.get("https://discord.com/api/v9/users/@me/affinities/users", headers=header4)

    message = "You need to verify your account in order to perform this action."

    if message in check.text:
        print("LOCKED ACC")
        exit()
    else:
        print("NOT LOCKED")
        header1 = {
            'host': "discord.com",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.5",
            'content-type': "application/json",
            'authorization': token,
            'x-super-properties': "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6OTUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC85NS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTUuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNSIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
            'x-fingerprint': rdata['fingerprint'],
            'x-discord-locale': "en-US",
            'x-debug-options': "bugReporterEnabled",
            'origin': "https://discord.com",
            'alt-used': "discord.com",
            'connection': "keep-alive",
            'referer': "https://discord.com/channels/@me",
            'cookie': f"__dcfduid={dfc}; __sdcfduid={sdc}; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Sat+Jan+01+2022+00%3A10%3A58+GMT%2B0530+(India+Standard+Time)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _gcl_au=1.1.1745667611.1640976059; _ga=GA1.2.1048474825.1640976060; _gid=GA1.2.1260035076.1640976060; _fbp=fb.1.1640976307006.828724092; _gat_UA-53577205-2=1",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'te': "trailers",
            'cache-control': "no-cache",
        }
        payload1 = {
            "date_of_birth": "1997-03-04"
        }

        while True:
            try:
                adddob = httpx.patch("https://discord.com/api/v9/users/@me", headers=header1,
                                     json=payload1, timeout=30)

                newtoken = adddob.json()['token']
                break
            except:
                continue

        header2 = {
            'host': "discord.com",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.5",
            'content-type': "application/json",
            'authorization': newtoken,
            'x-super-properties': "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6OTUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC85NS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTUuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNSIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
            'x-fingerprint': rdata['fingerprint'],
            'x-discord-locale': "en-US",
            'x-debug-options': "bugReporterEnabled",
            'origin': "https://discord.com",
            'alt-used': "discord.com",
            'connection': "keep-alive",
            'referer': "https://discord.com/channels/@me",
            'cookie': f"__dcfduid={dfc}; __sdcfduid={sdc}; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Sat+Jan+01+2022+00%3A10%3A58+GMT%2B0530+(India+Standard+Time)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _gcl_au=1.1.1745667611.1640976059; _ga=GA1.2.1048474825.1640976060; _gid=GA1.2.1260035076.1640976060; _fbp=fb.1.1640976307006.828724092; _gat_UA-53577205-2=1",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'te': "trailers",
            'cache-control': "no-cache",
        }
        payload2 = {
            'email': rdata['email'],
            'password': rdata['password']
        }


        while True:
            try:
                addmail = httpx.patch("https://discord.com/api/v9/users/@me", headers=header2,
                                      json=payload2, timeout=30)

                rdata['token'] = addmail.json()['token']
                break

            except:
                continue
        return rdata






def addavatar(rdata):
    def getRandomPicture():
        files = os.listdir('profiles')
        with open('profiles' + "/" + files[random.randrange(0, len(files))], "rb") as pic:
            return "data:image/png;base64," + base64.b64encode(pic.read()).decode('utf-8')

    imagePayload = {
        'avatar': getRandomPicture()
    }
    dfc = rdata['dfc']
    sdc = rdata['sdc']

    header3 = {
        'host': "discord.com",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
        'accept': "*/*",
        'accept-language': "en-US,en;q=0.5",
        'accept-encoding': "gzip, deflate, br",
        'content-type': "application/json",
        'authorization': rdata['token'],
        'x-super-properties': "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6OTUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC85NS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTUuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNSIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
        'x-discord-locale': "en-US",
        'x-debug-options': "bugReporterEnabled",
        'origin': "https://discord.com",
        'alt-used': "discord.com",
        'connection': "keep-alive",
        'referer': "https://discord.com/channels/@me",
        'cookie': f"__dcfduid={dfc}; __sdcfduid={sdc}; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Sat+Jan+01+2022+00%3A10%3A58+GMT%2B0530+(India+Standard+Time)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _gcl_au=1.1.1745667611.1640976059; _ga=GA1.2.1048474825.1640976060; _gid=GA1.2.1260035076.1640976060; _fbp=fb.1.1640976307006.828724092",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-origin",
        'te': "trailers",
        'cache-control': "no-cache",
    }
    try:
        httpx.patch('https://discord.com/api/v9/users/@me', headers=header3, json=imagePayload)
    except:
        httpx.patch('https://discord.com/api/v9/users/@me', headers=header3, json=imagePayload)



def handleregister_normal():
    finished = "Yes"
    logger.log("Gathering Utilities")
    rdata = gatherutilities_phone()
    logger.log("Gathering Utilities Done!")
    logger.log("Solving Captcha")
    rdata['key'] = captcha.getcaptchakey()
    logger.log("Captcha Solved")
    rdata = register_normal(rdata)
    helper.connecttow2s(rdata['token'])
    logger.log(f"Registered : {rdata['token']}")
    emailverifer.emailverify(rdata)
    logger.log(f"{rdata['token']} : EMAIL VERIFIED")
    if config['addavatar'] == "yes":
        addavatar(rdata)
        logger.log(f"{rdata['token']} : ADDED AVATAR")
    else:
        helper.savetokeninfile(rdata)
        return finished

def handleunverified():
    finished = "Yes"
    logger.log("Gathering Utilities")
    rdata = gatherutilities_phone()
    logger.log("Gathering Utilities Done!")
    logger.log("Solving Captcha")
    rdata['key'] = captcha.getcaptchakey()
    logger.log("Captcha Solved")

    rdata = register_normal(rdata)
    helper.connecttow2s(rdata['token'])
    logger.log(f"Registered : {rdata['token']}")
    if config['addavatar'] == "yes":
        addavatar(rdata)
        logger.log(f"{rdata['token']} : ADDED AVATAR")
        helper.savetokeninfile(rdata)
    else:
        helper.savetokeninfile(rdata)
        return finished










def handleregister_phone():
    if config['phone-service'] == "smsactivate":
        logger.log("Gathering Utilities")
        rdata = gatherutilities_phone()
        logger.log("Gathering Utilities Done!")
        while True:
            number = activate.buynumber()
            rdata['id'] = number['id']
            rdata['number'] = number['number']

            logger.log(f"Using Number:  {number['number']}")

            response = submitphone(rdata)
            if response == 204:
                logger.log("Waiting for SMS")

                code = activate.checkforsms(rdata)
                if code == 'no':
                    logger.log("Time Exceeded Trying new number.")
                    activate.cancel(rdata)
                    continue
                if code != "no":
                    rdata['code'] = code
                    logger.log(f"Recieved SMS  {rdata['code']}")
                    rdata = submit_recievedcode(rdata)
                    activate.finish(rdata)
                    logger.log("Solving Captcha")
                    rdata['key'] = captcha.getcaptchakey()
                    logger.log("Captcha Solved")
                    register_phone(rdata)
                    helper.connecttow2s(rdata['token'])
                    logger.log(f"Registered : {rdata['token']}")

                    emailverifer.emailverify(rdata)
                    if config['addavatar'] == "yes":
                        addavatar(rdata)
                        logger.log(f"{rdata['token']} : ADDED AVATAR")
                        helper.savetokeninfile(rdata)
                        return False
                    else:
                        helper.savetokeninfile(rdata)
                        return False
            else:
                logger.log("Invalid Number")
                activate.cancel(rdata)
                continue
    if config['phone-service'] == "fivesim":
        logger.log("Gathering Utilities")
        rdata = gatherutilities_phone()
        logger.log("Gathering Utilities Done!")
        while True:
            number = fivesim.buynumber()
            rdata['id'] = number['id']
            rdata['number'] = number['number']

            logger.log(f"Using Number:  {number['number']}")

            response = submitphone(rdata)
            if response == 204:
                logger.log("Waiting for SMS")

                code = fivesim.checkforsms(rdata)
                if code == 'no':
                    logger.log("Time Exceeded Trying new number.")
                    fivesim.cancelorder(rdata)
                    continue
                if code != "no":
                    rdata['code'] = code
                    logger.log(f"Recieved SMS  {rdata['code']}")
                    rdata = submit_recievedcode(rdata)
                    fivesim.finishorder(rdata)
                    logger.log("Solving Captcha")
                    rdata['key'] = captcha.getcaptchakey()
                    logger.log("Captcha Solved")
                    register_phone(rdata)
                    helper.connecttow2s(rdata['token'])
                    logger.log(f"Registered : {rdata['token']}")

                    emailverifer.emailverify(rdata)
                    if config['addavatar'] == "yes":
                        addavatar(rdata)
                        logger.log(f"{rdata['token']} : ADDED AVATAR")
                        helper.savetokeninfile(rdata)
                        return False
                    else:
                        helper.savetokeninfile(rdata)
                        return False
            else:
                logger.log("Invalid Number")
                fivesim.cancelorder(rdata)
                continue





