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
driver.maximize_window()
driver.impicity_wait(5)
driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f%3ftoWww%3d1%26redig%3d1B49B980E76E4F6AB5E8E734E0CC456C&FORM=O2HV65")
driver.impicity_wait(5)
p1= driver.find_element("id", 'enAS').is_selected()
print(p1)

if p1:
    print("Already Selected")

else:
    driver.find_element("id", 'enAS').click()
    print("Successfully Checked in")

time.sleep(5)
driver.quit()
