from selenium import webdriver #links up with the browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Path of chrome Driver
PATH = "C:\Program Files (x86)\chromedriver.exe"

cService = webdriver.ChromeService(executable_path=PATH)
driver = webdriver.Chrome(service = cService) 

# open a website

driver.get('https://umdearborn.edu/facilities-operations/campus-access/standard-building-hours')

# driver.get("https://google.com")


# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
# )

# input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# input_element.clear()
# input_element.send_keys("tech with tim")

# input_element.send_keys(Keys.ENTER)


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "text"))
)


text_element = driver.find_element(By.CLASS_NAME, "text")
link = text_element.find_element(By.LINK_TEXT, "Standard Building Hours")


link.click()

time.sleep(3)

all_text = driver.find_elements(By.CLASS_NAME, "_textbox_jifpk_15")

for text_info in all_text:
    print(text_info.text)


time.sleep(20)

driver.quit()
