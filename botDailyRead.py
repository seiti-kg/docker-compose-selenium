from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://www.tjmg.jus.br/portal-tjmg/")
driver.maximize_window()
time.sleep(3)

#Download do diario
try:

    caminhoDiarios = driver.find_element(By.XPATH, '//*[@id="submenu"]/div/div/div[1]/div/div/div/a')
    caminhoDiarios.click()
    time.sleep(2)
    try:
        cookies = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "termo-uso-btn"))
        )
        cookies.click()
    finally:
        caminhoDJe = driver.find_element(By.XPATH, '//*//div[@class=\'introduction\'][contains(text(),\'Diário do Judiciário eletrônico do Tribunal de Justiça de MG\')]')

        caminhoDJe.click()
        time.sleep(1)
        
        edicoesAnteriores = driver.find_element(By.LINK_TEXT, "Edições Anteriores")
        edicoesAnteriores.click()
        download = driver.find_element(By.LINK_TEXT, "Diários disponíveis")
        download.click()
        time.sleep(2)
        escolha = driver.find_element(By.ID, "tipoDiario")
        escolha.click()
        time.sleep(2)
        diario = driver.find_element(By.CSS_SELECTOR, "option[value='2inst|si']")
        diario.click()
        time.sleep(2)
        submit = driver.find_element(By.CLASS_NAME, "botao_vinho")
        submit.click()
        time.sleep(2)
finally:
    driver.quit

    
