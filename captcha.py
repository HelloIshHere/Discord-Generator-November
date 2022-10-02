import deathbycaptcha

from anticaptchaofficial.hcaptchaproxyless import *



with open("config.json") as data:
    config = json.load(data)



def anti():
    siteKey = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"
    clientKey = config['anticaptcha-apikey']

    data = {
        "clientKey": clientKey,
        "task":
            {
                "type":"HCaptchaTaskProxyless",
                "websiteURL":"https://discord.com/",
                "websiteKey":siteKey,
                "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
            }
    }

    resp = requests.post("https://api.anti-captcha.com/createTask", json=data)
    taskId = resp.json()["taskId"]

    response = {}
    while not "solution" in response:
        data = {"clientKey": clientKey, "taskId": taskId}
        resp = requests.post("https://api.anti-captcha.com/getTaskResult", json=data)
        response = resp.json()

    captcha_key = response["solution"]["gRecaptchaResponse"]
    return captcha_key


def death():
    proxy = config['proxy']

    # Put the proxy and hcaptcha data
    Captcha_dict = {
        'proxy': f'http://{proxy}',
        'proxytype': 'HTTP',
        'sitekey': 'f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34',
        'pageurl': 'https://discord.com/register'}

    # Create a json string
    json_Captcha = json.dumps(Captcha_dict)

    # to use socket client
    client = deathbycaptcha.SocketClient(config['dbc-username'],config['dbc-password'],config['deathbycaptcha-apikey'])
    # to use http client
    #client = deathbycaptcha.HttpClient(config['dbc-username'], config['dbc-password'],config['dbc-apikey'])

    try:
        #print(balance)

        # Put your CAPTCHA type and Json payload here:
        captcha = client.decode(type=7, hcaptcha_params=json_Captcha)
        if captcha:
            # The CAPTCHA was solved; captcha["captcha"] item holds its
            # numeric ID, and captcha["text"] item its list of "coordinates".
            return captcha["text"]

    except deathbycaptcha.AccessDeniedException:
        # Access to DBC API denied, check your credentials and/or balance
        print("error: Access to DBC API denied," +
              "check your credentials and/or balance")

def getcaptchakey():
    if config['captcha-service'] == "anticaptcha":
        return anti()
    if config['captcha-service'] == "deathbycaptcha":
        return death()


    else:
        print('You have not entered correct captcha service inside config.json. THE TWO OPTIONS TO CHOOSE FROM ARE anti and death')

