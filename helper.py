import discum
import time
import random
import string
import json

with open("config.json") as data:
    config = json.load(data)



def connecttow2s(token):

    while True:
        try:
            bot = discum.Client(token=token,
                                log=False)

            # bot.sendMessage("238323948859439", "Hello :)")

            @bot.gateway.command
            def helloworld(resp):
                if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
                    user = bot.gateway.session.user
                    # print("Logged in as {}#{}".format(user['username'], user['discriminator']))

                time.sleep(3)

                bot.gateway.close()

            bot.gateway.run(auto_reconnect=False)
            break
        except:
            continue

def getusername():
    discord_usernames = []
    with open('usernames.txt', 'r', encoding='UTF-8',errors='ignore') as username_txt:
        lines = username_txt.readlines()
        for line in lines:
            discord_usernames.append(line.replace('\n', ''))


    return "!" + " "+ random.choice(discord_usernames)+ random_char(2)

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def savetokeninfile(registerdata):
    if config['saveformat'] == "token":
        f = open('tokens.txt', "a+")
        f.write(registerdata['token'])
        f.write("\n")
        f.close()
    if config['saveformat'] == "email:pass:token":
        f = open('tokens.txt', "a+")
        f.write(registerdata['email']+":"+registerdata['password']+":"+registerdata['token'])
        f.write("\n")
        f.close()
