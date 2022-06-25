from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

#Pagina de la que vamos a sacar la informacion
web = 'https://www.thesun.co.uk/sport/football/'
#Localizamos donde esta instalado el chromedriver
path = "C:/Users/Ramiro/Downloads/chromedriver/chromedriver.exe" 

# iniciamos el driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)

# Encontramos los elementos
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')


#definimos las listas para appendear la info
titulos = []
subtitulos = []
links = []
for container in containers:
    titulo = container.find_element(by='xpath', value='./a/h2').text
    subtitulo = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titulos.append(titulo)
    subtitulos.append(subtitulo)
    links.append(link)

# Exportamos la informacion a csv
my_dict = {'titulo': titulos, 'subtitulo': subtitulos, 'link': links}
df_headlines = pd.DataFrame(my_dict)
print(df_headlines)
df_headlines.to_csv('headline.csv')

driver.quit()