import requests
import random
import string
import json
import captcha

host = ''
def setHost(_host):
    global host
    host = _host
    if not host.startswith('http://'):
        host = 'http://' + host
    
    if not host.endswith(':80'):
        host = host + ':80'
    
    print('Set URL to ' + host)

def randomSub(size):
    return ''.join(random.choice(string.ascii_letters) for i in range(size))

class MailAPI:
    def __init__(self, *args):
        if len(args) == 1:
            self.sub = args[0].split('@')[0]
            self.domain = args[0].split('@')[1]
        else:
            self.sub = randomSub(int(args[0]))
            self.domain = args[1]
        self.host = host

    def getEmails(self, limit):
        if limit == None or limit <= 0:
            limit = -1
        return json.loads(requests.get(self.host + '/getemail?sub=' + self.sub + '&domain=' + self.domain + '&limit=' + str(limit)).text)