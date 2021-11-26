import os
from pywhat_auto import pywhat_auto

if __name__ == "__main__":   
    names = ["Chota Mannia"]
    #example 
    bot = pywhat_auto(waitingtime= 3)
    for ele in names:
        bot.sendfile(ele,os.path.join(os.getcwd(),'example.txt'),count= 10)

