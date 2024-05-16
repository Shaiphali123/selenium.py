import driver
import select
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from webdriver_manager.chrome import ChromeDriverManager
driver: WebDriver =webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver.get("https://www.bing.com/?toWww=1&redig=1B49B980E76E4F6AB5E8E734E0CC456C")
driver.impicity_wait(5)
driver.find_element("id",'sb_form_q').send_keys("Shaiphali Bhadani")
driver.impicity_wait(10)
driver.find_element(By.XPATH,"//label[@id ='search_icon']").click()
driver.impicity_wait(10)
time.sleep(2)
driver.quit()

