import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random

# Graphic cards URL
url = "https://www.coolmod.com/tarjetas-graficas/"

driver = driver = webdriver.Chrome()  # seleccionem un navegador
driver.get(url)  # indiquem la web a visitar
driver.maximize_window()  # (opcional) maximitzem
time.sleep(0.5)  # esperem mig segon

# anem fent scroll fins al final de la web
iter = 1
while True:
    # Què ens queda fins arribar baix de tot?
    scrollHeight = driver.execute_script("return document.documentElement.scrollHeight")
    # aleatori el bot cap avall, multiplicat per la iteració actual
    height = random.randint(300, 400) * iter
    # Ens situem en dita posició
    driver.execute_script("window.scrollTo(0, " + str(height) + ");")

    # Si ja hem arribat al final trenquem el bucle i eixim
    if height > scrollHeight:
        print("End of page")
        break
    time.sleep(0.5)
    iter += 1


# recuperem el interior del cos, quedant-nos amb el HTML
body = driver.execute_script("return document.body")
source = body.get_attribute("innerHTML")

# creem el DOM per a processar-lo amb BeautifulSoup
soup = BeautifulSoup(source, "html.parser")
print(soup)
# Fer scraping amb la "sopa"
