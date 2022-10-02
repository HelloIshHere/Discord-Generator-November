import httpx
import logger
import requests
from urlextract import URLExtract
import json
from imap_tools import MailBox,AND

with open("config.json") as data:
    config = json.load(data)



import httpx
import time
import requests
from urlextract import URLExtract
import json
from mail import MailAPI
import mail
import captcha

mail.setHost('192.53.122.249')

def imap(tofrom):
    mailbox = MailAPI(tofrom)
    emails = mailbox.getEmails(-1)
    print(len(emails))
    for msg in emails:
        body = msg

        extractor = URLExtract()
        urls = extractor.find_urls(body)
        geturltoken = requests.get(urls[0], allow_redirects=False, headers={
            'Referer': urls[0]
        })
        # s = geturltoken.url
        s = geturltoken.headers["Location"]
        splitted = s.split("#token=")
        verifytoken = splitted[1]
        return verifytoken


def verify(registerdata):

    dfc= registerdata['dfc']
    sdc = registerdata['sdc']
    token = registerdata['token']
    verifytoken = registerdata['verifytoken']
    headers = {
        'host': "discord.com",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
        'accept': "*/*",
        'accept-language': "en-US,en;q=0.5",
        'content-type': "application/json",
        'authorization': token,
        'x-super-properties': "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6OTUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC85NS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTUuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNSIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
        'x-discord-locale': "en-US",
        'x-debug-options': "bugReporterEnabled",
        'origin': "https://discord.com",
        'alt-used': "discord.com",
        'connection': "keep-alive",
        'referer': "https://discord.com/verify",
        'cookie': f"__dcfduid={dfc}; __sdcfduid={sdc}",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-origin",
        'te': "trailers",
        'cache-control': "no-cache",
    }
    verifypaylod = {
        "token": verifytoken,
    }

    s = httpx.post("https://discord.com/api/v9/auth/verify", headers=headers,
                               json=verifypaylod, timeout=100)
    










def emailverify(registerdata):
    while True:
        verifytoken = imap(registerdata['email'])
        if verifytoken == None:
            continue
        else:
            registerdata['verifytoken'] = verifytoken
            verify(registerdata)
            return logger.log(f"{registerdata['token']} : EMAIL VERIFIED")
