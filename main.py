from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time
import re

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(20)

# prekyte = 'alus'

driver.get("https://www.vynoteka.lt")

# amzius - veikia:
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[3]/div/div[1]/button').click()

# slapukai - neveikia
# driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()

# slapukai bandymas
driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
# driver.find_element(By.ID, 'c-button--blue-inversed').click()
# driver.find_element(By.ID, 'searchKeyword').send_keys(prekyte)
# # driver.find_element(By.CLASS_NAME, 'fa-search').click()
# driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/form/div[2]/div[1]/button/i").click()
#
# time.sleep(1)