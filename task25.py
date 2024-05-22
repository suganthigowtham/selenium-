# Common


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Form:


   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       # Explicit wait
       self.wait = WebDriverWait(self.driver, 10)


   def boot(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.wait.until(ec.url_to_be(self.url))


   def quit(self):
       self.driver.quit()


   def fillForm(self):
       self.boot()
       self.driver.execute_script('window.scrollBy(0, 500)')
         # This code is used to find the path and fill the  box
       expand_all_element = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button/span')
          # This code is used to Expand the page of  filling form
       self.driver.execute_script("arguments[0].click();",expand_all_element )

       self.driver.execute_script('window.scrollBy(0, 500)')

        # creating wait object
       
       name_element = self.wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[2]/div/div/div/div/div/div/input')))
       name_element.send_keys('suganthi')

       # birthdate 
       from_element = self.wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/input'))) 
       from_element.send_keys('10-01-1994') 
 
 
       to_element = self.wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/input'))) 
       to_element.send_keys('19-01-1994') 
        # This code is used to scroll the webpage
       self.driver.execute_script('window.scrollBy(0, 500)') 

       
       




obj = Form("https://www.imdb.com/search/name/")
obj.fillForm()

