from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import locale
import time

PATH = "C:\Program Files\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
data_hoje = datetime.now().strftime("%d de %B de %Y")

driver.get("https://www.tjmg.jus.br/portal-tjmg/")
driver.maximize_window()
time.sleep(3)

#Download do diario
try:

    caminhoDiarios = driver.find_element(By.XPATH, '//*[@id="submenu"]/div/div/div[1]/div/div/div/a')
    driver.execute_script("arguments[0].click();", caminhoDiarios)

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
        driver.switch_to.window(driver.window_handles[-1])
        driver.maximize_window()
        escolha = driver.find_element(By.ID, "tipoDiario")
        escolha.click()
        time.sleep(2)
        select = Select(escolha)
        diario = select.select_by_visible_text("2ª inst. Judicial")
        time.sleep(2)
        submit = driver.find_element(By.CLASS_NAME, "botao_vinho")
        submit.click()
        opcoes_data = driver.find_elements(By.XPATH, "/html/body/div[2]/table/tbody/tr/td/table/tbody")
        for opcao in opcoes_data:
            opcao.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr/td/table/tbody/tr/td/li/a/div")
            data_texto = opcao.text.strip()
            data_texto = data_texto.replace(data_texto.split()[1], data_texto.split()[1].capitalize())
            data_hoje = data_hoje.strip()
            str(data_texto)
            str(data_hoje)
            if data_texto == data_hoje:
                opcao.click()
                print(data_texto)
                print(data_hoje)
                break
            time.sleep(4)
finally:
    driver.quit

    
