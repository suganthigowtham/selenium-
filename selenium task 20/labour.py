from time import sleep
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Labour:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def findElementByXPath(self, xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath).click()

    def alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def boot(self):
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def gotoMonthlyProgress(self):
        try:
            # To start up the webpage
            # To find the path of the document from the menu bar
            documents = self.driver.find_element(by=By.XPATH, value='//*[@id="nav"]/li[7]/a')
            # Move the mouse to the element
            self.action.move_to_element(documents).perform()
            sleep(3)
            # to find the path of the Monthly Progress Report
            self.driver.find_element(by=By.XPATH, value='//*[@id="nav"]/li[7]/ul/li[2]/a').click()
            sleep(3)
            print(self.driver.current_url)

        except NoSuchElementException as e:
            print(e)
        finally:
            print("No error")

    def clickDownload(self):
        # This code is used to find the path of february month download link
        self.findElementByXPath(
            '//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div['
            '2]/table/tbody/tr[2]/td[2]/a')
        # This code is used to alert page
        self.alert()
        # This code is used to find the path of media
        self.findElementByXPath('//*[@id="nav"]/li[10]/a')
        self.findElementByXPath(
            '//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/p/b/a')
        # This code is used to click the Photo Gallery
        self.findElementByXPath('//*[@id="block-block-88"]/ul/li[2]/strong/a')

    def toDownload(self):
        self.boot()
        parent_window_handle = self.driver.current_window_handle
        print(parent_window_handle)
        #  url  to download the Monthly Progress Report
        url1 = "https://labour.gov.in/sites/default/files/mpr_february_2024.pdf"
        response = requests.get(url1)
        """
        HTTP Response Status Code
         1. (100-199) - Informational Responses
         2. (200 - 299) - Successful Response
         3. (300 - 399) - Redirection messages
         4. (400 - 499) - Client Error Response
         5. (500 - 599) - Server Error Response
         """
        if response.status_code == 200:
            file = open("MonthlyProgressReport.pdf", "wb")
            file.write(response.content)
            file.close()
        else:
            print("Error")
        all_window_handle = self.driver.window_handles
        print(all_window_handle)
        for handle in all_window_handle:
            if handle != parent_window_handle:
                self.driver.switch_to.window(handle)
                self.driver.close()
                sleep(3)
        self.quit()


obj = Labour("https://labour.gov.in/")
obj.boot()
obj.gotoMonthlyProgress()
obj.clickDownload()
obj.toDownload()
obj.quit()