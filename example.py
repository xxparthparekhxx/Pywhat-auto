import os
from pywhat_auto import pywhat_auto

if __name__ == "__main__":   
    names = ["ADD YOUR Whatsapp contact name","name2","name3"]
    bot = pywhat_auto(waitingtime= 3) #add a delay that works on your machine
    for ele in names:
        bot.sendfile(ele,os.path.join(os.getcwd(),'example.txt'),count= 10) #sends files 

