import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class pywhat_auto:
    def __init__(self,waitingtime) -> None:
        self.waitingtime= waitingtime 
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://web.whatsapp.com/")
        input("Scan the qr code on the new crome window and press enter")
        
    def search(self,contactname):
        self.ele = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        self.ele.click()
        self.driver.implicitly_wait(self.waitingtime)
        self.ele.send_keys(contactname)
        self.ele.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(self.waitingtime)
    
    def sendfile(self,contactname,path) -> None:
        self.search(contactname)
        ele = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[1]/div[2]/div/div')
        ele.click()
        self.driver.implicitly_wait(self.waitingtime)
        self.ele = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[1]/div[2]/div/span/div[1]/div/ul/li[3]/button/span')
        self.ele = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[1]/div[2]/div/span/div[1]/div/ul/li[3]/button/input')
        self.driver.implicitly_wait(self.waitingtime)
        self.ele.send_keys(path)
        self.driver.implicitly_wait(self.waitingtime)
        self.ele = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div')
        self.ele.click()
        self.driver.implicitly_wait(self.waitingtime)

    def sendmessage(self,contactname,message,times = 1):
        self.search(contactname)
        self.driver.implicitly_wait(self.waitingtime)
        self.ele = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')        
        for i in range(times):
            self.ele.send_keys(message)
            self.driver.implicitly_wait(self.waitingtime)
            self.ele.send_keys(Keys.ENTER)


