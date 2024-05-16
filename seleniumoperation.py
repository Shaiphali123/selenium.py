import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cService = webdriver.ChromeService(executable_path = 'C:/Users/91912/Documents/Driver/chromedriver.exe')
driver = webdriver.Chrome(service = cService)
driver.impicity_wait(5)
driver.get("https://demo.charanpahariapp.com")
driver.impicity_wait(5)
driver.quit()
