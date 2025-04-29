import time
import os # добавляем импорт файла .env
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls
from dotenv import load_dotenv # дополнительно добавляем импорт
load_dotenv() # и это тоже дополнительно

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)
action = ActionChains(driver)
scrolls = Scrolls(driver, action)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

username_field = driver.find_element("xpath", "//input[@name='username']")
username_field.send_keys(os.environ["LOGIN"]) # с помощью этой команды заполняем поля уже защищёнными данными

password_field = driver.find_element("xpath", "//input[@name='password']")
password_field.send_keys(os.environ["PASSWORD"])

time.sleep(3)