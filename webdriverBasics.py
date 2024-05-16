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
print(driver.title)
driver.find_element("id", 'HeaderMenu-combowise-demo').click()
time.sleep(5)
driver.find_element(By.XPATH,
                    "//a[@href = 'https://demo.charanpahariapp.com/products/bikini-sandnes-olive-green']").click()
time.sleep(5)

element=driver.find_element(By.CSS_SELECTOR,"combowise-mixmatch_select_wrap")
drp=Select(element)
drp.select_by_visible_txt('m')
