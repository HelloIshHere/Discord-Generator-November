import threading
import json
from multiprocessing import Process
import handler

with open("config.json") as data:
    config = json.load(data)



def main():

    print("1.EMAIL VERIFIED")
    print("2.FULLY VERIFIED")
    print("3.UNVERIFIED")

    #choice = int(input("ENTER: "))
    choice = 1
    


    #threads_to_start = int(input("Workers Amount: "))
    threads_to_start = 25
    if config['method'] == "pro":
        print('Using Processes')
        for i in range(threads_to_start):
            p = Process(target=handler.handler,args=(choice,))
            p.start()
    if config['method'] == "thread":
        print('Using Threads')
        for i in range(threads_to_start):
            t = threading.Thread(target=handler.handler,args=(choice,))
            t.start()

if __name__ == '__main__':

    main()



