from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class LoginAutomation:

    def __init__(self, url="https://www.instagram.com/guviofficial/"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(3)

    def quit(self):

        self.driver.quit()

  # def findElementByXpath(self,Xpath):

        
      #  return self.driver.find_element(by=By.XPATH,value=Xpath)

    def login(self):
        self.boot()

    def gotofollower(self):
        self.boot()
        sleep(3)
       # self.clickElementByXPATH('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[2]/div/div/div[1]/div/button/span').click()
       # self.wait()
        follower=self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span")        
        following=self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span")   
        print(follower.text)
        print(following.text)
        #var=Element.text
       # print(var)
       # print(Element1.text)
        self.driver.quit()

obj = LoginAutomation()
obj.gotofollower()        





