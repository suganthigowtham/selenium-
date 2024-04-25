       
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

#driver.get_cookies("https://www.saucedemo.com/")

#cookies= self.drive.get_cookies()
#for cookie in cookies:
#	print(cookie)

class LoginAutomation:

    def __init__(self, url="https://www.saucedemo.com/", username="standard_user", password="secret_sauce"):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def boot(self):
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()

    def quit(self):
       
        self.driver.quit()


    def login(self):
        self.boot()


       # This is to fill the username and the password
        self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
        sleep(3)
        self.driver.find_element(by=By.ID, value="password").send_keys(self.password)
        sleep(3)
        # find the login button and click on it
        self.driver.find_element(by=By.ID, value="login-button").click()
        sleep(3)


        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            print("Login Successfully")
        else:
            print("Error")

        cookies =self.driver.get_cookies()  
        for cookie in cookies:
	        print(cookie)
        
def findElementbyfullxpath(self , fulxpath):
     return self.driver.find_element(by=By.XPATH,value=fulxpath)

def gotomenubar(self):
     
    self.driver.find_element(by=By.xpath, value="/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button")

    self.driver.find_element(by=By.xpath,value= '//*[@id="logout_sidebar_link"]').click()     
    

obj = LoginAutomation()
obj.login()
#obj.gotomenubar()



