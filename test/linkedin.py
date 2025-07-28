from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import os
from dotenv import load_dotenv

#takes email password and initialized selenium driver and signs you in to linked in
def sign_to_linkedin(email, password, driver):
    url = "https://www.linkedin.com/login/"
    driver.get(url)
    time.sleep(2)
    email_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-litms-control-urn='login-submit']")
    email_input.send_keys(email)
    time.sleep(2)
    password_input.send_keys(password)
    time.sleep(2)
    sign_in_button.click()
    time.sleep(2)

#when signed in to linked in posts given text
def post_text(text, driver):
    post_button = driver.find_element(By.ID, "ember42")
    post_button.click()
    time.sleep(2)
    textbox = driver.find_element(By.CSS_SELECTOR, 'div[data-placeholder="What do you want to talk about?"]')
    textbox.send_keys(text)
    time.sleep(2)
    send_button = driver.find_element(By.XPATH, "//button[contains(@class, 'share-actions__primary-action')]")
    send_button.click()

#takes text and makes post of it in linked in 
def text_to_linkedin(text):
    load_dotenv()
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    chromedriver_path = "/nix/store/qjk1gkbjfm88c0kwr5lx32d4vpknn12i-chromedriver-unwrapped-137.0.7151.103/bin/chromedriver"
    service = Service(executable_path=chromedriver_path)
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    sign_to_linkedin(email, password, driver)
    post_text("Something big is about to happen!!!!", driver)
    time.sleep(10)