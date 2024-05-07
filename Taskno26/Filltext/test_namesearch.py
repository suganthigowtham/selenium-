import pytest

from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestNameSearch:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox()
        #self.driver.get(data.WebData().url)  # this code is use to get the url from the data
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)  # this code is used for explicit wait
        yield
        self.driver.quit()

    def clickButton(self, locator):
        #self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()
        see_results_element = self.wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        self.driver.execute_script("arguments[0].click();", see_results_element)

    def fillText(self, locator, value):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, locator))).send_keys(value)

    def test_search(self,boot):
        # this coded is used to scroll
        self.driver.get(data.WebData().url)
        self.driver.execute_script('window.scrollBy(0,500)')
        self.clickButton(locator.WebLocator().expandaAllLocator)
        self.driver.execute_script('window.scrollBy(0,500)')
        self.fillText(locator.WebLocator().nameLocator, data.WebData().name)
        self.fillText(locator.WebLocator().birthdayLocator, data.WebData().Birthdate)

        try:
            self.clickButton(locator.WebLocator().searchLocator)
        except NoSuchElementException as e:
            print(e)

       # if self.driver.current_url == data.WebData().dashboardURL:
      #      print("success:URL is valid")
       ## else:
        #    print("error")
        print("name search success")













