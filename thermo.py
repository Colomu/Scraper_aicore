import ssl
from tkinter import Frame
from tracemalloc import start
from selenium import webdriver
import selenium
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
from typing import List

import os



from Scraper.Scraper.constants import BASE_URL
print('start')

class Scraper:
    def __init__(self):
        self.driver_path = "/Users/charlesolomu/Documents/chromedriver"
        self.service = Service(executable_path=self.driver_path)
        
        self.URL = BASE_URL
        chrome_options = Options()
        self.driver = webdriver.Chrome(self.driver_path, options=chrome_options)

    def land_first_page(self):
        self.driver.get(self.URL)

    

    class Scraper:
    
     def __init__(self):
        self.driver_path = "/Users/charlesolomu/Documents/chromedriver"
        self.service = Service(executable_path=self.driver_path)
        
        self.URL = BASE_URL
        chrome_options = Options()
        self.driver = webdriver.Chrome(self.driver_path, options=chrome_options)

    def land_first_page(self):
        self.driver.get(self.URL)

    

    def get_sequencing(self, xpath: str = '//a[@href="/uk/en/home/life-science/sequencing.html?icid=HPAB-C3C-sequencing-20150814-us"]'):
        sequencing = self.driver.find_element(By.XPATH, xpath)
        sequencing.click()
        
    def accept_cookies(self, xpath: str = '//a[@class="call"]'):
        '''
        Finds and clicks the "Accept" cookies button.

        parameters
        '''''''
        xpath: str
            The Xpath of the accept cookies button

        '''''''''
    
    
       
        self.driver.switch_to.frame(2) 
        
        
        accept_cookies = self.driver.find_element(By.XPATH, xpath)
        accept_cookies.click()


    def sanger_sequencing(self, xpath: str = '//a[text()="Sanger Sequencing "]'):
        sanger_sequencing = self.driver.find_element(By.XPATH, xpath)
        sanger_sequencing.click()




if __name__ == "__main__":
    print('start')
    bot = Scraper()
    bot.land_first_page()
    time.sleep(3)
    bot.accept_cookies()
    time.sleep(2)
    
    bot.get_sequencing()
    time.sleep(3)
    bot.sanger_sequencing()
    time.sleep(3)