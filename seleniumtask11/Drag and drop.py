
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


# action chains
from selenium.webdriver import ActionChains




class DragAndDrop:


   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.action = ActionChains(self.driver)


   def boot(self):
       self.driver.get(self.url)
       sleep(3)
       self.driver.maximize_window()


   def quit(self):
       self.driver.quit()


   def findElementByID(self, id):
       return self.driver.find_element(by=By.ID, value=id)

   def findElementByTagName(self, value):
       return self.driver.find_element(by=By.TAG_NAME, value=value)

   def dragAndDrop(self):
       try:
           self.boot()
           self.driver.switch_to.frame(self.driver.find_element(by=By.TAG_NAME, value="iframe"))
           start = self.findElementByID("draggable")
           destination = self.findElementByID("droppable")
           self.action.drag_and_drop(start, destination).perform()
           sleep(3)
           self.findElementByTagName("Drop here")
           sleep(3)

           Droppable = self.findElementByTagName("Dropped!")
           if Droppable == "Dropped!":
               print("Success")
           else:
               print("Error")
       except NoSuchElementException as e:
           print(e)
       finally:
           self.driver.quit()

obj = DragAndDrop("https://jqueryui.com/droppable/")
obj.dragAndDrop()


