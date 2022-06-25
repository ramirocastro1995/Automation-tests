from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd

#Pagina de la que vamos a sacar la informacion
web = 'https://www.google.com/'
#Localizamos donde esta instalado el chromedriver
path = "C:/Users/Ramiro/Downloads/chromedriver/chromedriver.exe" 

driver = webdriver.Chrome(path)
driver.get(web)
driver.implicitly_wait(0.5)

search_box = driver.find_element(by=By.NAME, value="q")
search_button = driver.find_element(by=By.NAME, value="btnK")

#ingresamos un input para elegir que buscar desde el cmd
search_box.send_keys(input('ingresa que buscar: '))
search_button.click()
#search_button.click()
