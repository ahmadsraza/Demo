import time

import keyboard
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome()

driver.get("https://app.createsmart.io/login")
driver.maximize_window()

#driver.find_element(By.XPATH, "//input[@id='Email']").clear()
driver.find_element(By.XPATH, "//input[@id='mui-4']").send_keys("omar.moazzam@bssuniversal.com")
#driver.find_element(By.XPATH, "//input[@id='Password']").clear()
driver.find_element(By.XPATH, "//input[@id='mui-5']").send_keys("Omar@085")
#driver.find_element(By.XPATH("//input[@id='RememberMe']")).click()
#driver.find_element(By.XPATH("//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]"))
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='demo-customized-button']").click()
#driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//*[@id='basic-menu']/div[3]/ul/li[2]").click()
time.sleep(5)
'''
file_input = driver.find_element(By.XPATH,"//*[@id='modal']/div/div[3]/div/div/div/form/div[1]/div/div").click()
time.sleep(5)
#file_path = "C:/Users/Ahmad.Raza/OneDrive - Business Solutions & Services/latest.zip"

file_input.send_keys("C:/Users/Ahmad.Raza/OneDrive - Business Solutions & Services/Documents/latest.zip")
time.sleep(5)
'''
driver.find_element(By.XPATH,"//*[@id='modal']/div/div[3]/div/div/div/form/div[1]/div/div").click()
time.sleep(5)

Keyboard = Controller()

#Keyboard.type("C:\\Users\\Ahmad.Raza\\OneDrive - Business Solutions & Services\\Documents\\latest.zip")
Keyboard.type("C:\\Users\\Ahmad.Raza\\OneDrive - Business Solutions & Services\\Documents\\latest.zipp")
time.sleep(5)
keyboard.press('enter')  # Press the 'Enter' key
keyboard.release('enter')
time.sleep(10)
#driver.find_element(By.XPATH, "//*[@id='modal']/div/div[3]/div/div/div/form/div[1]/div/div").send_keys("C:/Users/Ahmad.Raza/OneDrive - Business Solutions & Services/test_auto/latest.zip")
submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]').click()

time.sleep(20)


driver.close()




