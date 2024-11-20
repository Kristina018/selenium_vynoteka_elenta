from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time
import re

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(20)

prekyte = 'alus'

driver.get("https://www.vynoteka.lt")

# amzius - veikia:
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[3]/div/div[1]/button').click()

# slapukai bandymas - su timesleep veikia
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()

# naujienlaiskio ilgai lauktas baneris
driver.find_element(By.ID, 'omnisend-form-63ff1f31b40d6530aba59a6d-form-close-icon').click()

# paieskos laukelis
driver.find_element(By.CLASS_NAME, 'form-control').send_keys(prekyte)


    
driver.find_element(By.CLASS_NAME, '/html/body/div[2]/div[1]/header/div[2]/div/div/div[3]/div/div/div/form/div[2]/div/div[1]/div[1]/div/div/a[13]/div/div[1]/div').click()
# driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/form/div[2]/div[1]/button/i").click()
#
