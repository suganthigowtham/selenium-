
import pytest
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from Data import data
from Locator import locator


class Test_loginPage:
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data.Webdata().url)  # this code is used to get the url from the data
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)  # this code is used to for explicit wait
        yield
        self.driver.quit()

    def enterText(self, locator, textvalue):
        self.wait = WebDriverWait(self.driver, 10)
        element = self.wait.until(ec.presence_of_element_located((By.XPATH, locator)))
        element.clear()
        element.send_keys(textvalue)

    def clickButton(self, locator):
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()

    def test_login(self,boot):
        try:
            # Username = 2
            # Password = 3
            # Test Results = 7
            # Row = 2 to End

            for row in range(2, data.Webdata().rowCount()+1):
                username = data.Webdata().readData(row, 2)
                password = data.Webdata().readData(row, 3)
                self.enterText(locator.Weblocator().usernameLocator, username)
                self.enterText(locator.Weblocator().passwordlocator, password)
                self.clickButton(locator.Weblocator().loginlocator)
                if self.driver.current_url == data.Webdata().dashboardURL:
                    print("Logged in Successfully")
                    data.Webdata().writeData(row, 7, "Logged in Successfully")
                    # This code is used to write name of tester
                    data.Webdata().writeData(row, 6, "sugu")
                    curr = datetime.now().strftime("%H:%M:%S")
                    print(curr)
                    self.clickButton(locator.Weblocator().dropdrownlocator)
                    self.clickButton(locator.Weblocator().logoutlocator)
                else:
                    print(" Login Unsuccessful")
                    data.Webdata().writeData(row, 7, "Invalid Credentials")

        except NoSuchElementException as e:
            print(e)


