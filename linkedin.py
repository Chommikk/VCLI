from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

chromedriver_path = "/nix/store/qjk1gkbjfm88c0kwr5lx32d4vpknn12i-chromedriver-unwrapped-137.0.7151.103/bin/chromedriver"
service = Service(executable_path=chromedriver_path)
options = Options()


driver = webdriver.Chrome(service=service, options=options)

url = "https://www.linkedin.com/feed/"
driver.get(url)
time.sleep(3)

