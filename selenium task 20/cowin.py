from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


class Cowin:
    """
    This method is used to get into the webpage using Google Chrome
    """

    def __init__(self, url="https://www.cowin.gov.in/"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
        This method to start up the url in the chrome driver and maximize the window
        :return:
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(3)

    def quit(self):
        """
        This method is used close the Chrome browser
        :return:
        """
        self.driver.quit()
        sleep(3)

    def findelementbyxpath(self,xpath):
        return self.driver.find_element(by=By.XPATH,value=xpath).click()

    def clickFAQandPARTNERS(self):
        self.boot()
        main_window_handle = self.driver.current_window_handle
        print(main_window_handle)
        FAQ = '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a'
        self.findelementbyxpath(FAQ)
        sleep(5)
        PARTNERS = '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a'
        self.findelementbyxpath(PARTNERS)
        sleep(5)

        all_window_handle = self.driver.window_handles
        print(all_window_handle)
        for handle in all_window_handle:
            if handle != main_window_handle:
                self.driver.switch_to.window(handle)
                self.driver.close()
                sleep(5)
        self.quit()
        print("Successfully closed all window except main window: ")


obj = Cowin()
obj.clickFAQandPARTNERS()










