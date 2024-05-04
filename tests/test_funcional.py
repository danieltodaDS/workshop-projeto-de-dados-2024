from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Iniciar streamlit em background
    process = subprocess.Popen(['streamlit', 'run', 'src/app.py'])
    options = Options()
    options.headless = True #Executar em modo headless
    driver = webdriver.Chrome(options=options)
    # Iniciar o Webdriver usando Geckodriver
    driver.set_page_load_timeout(5)
    yield driver 

    #Fechar o webdriver e o streamlit após o teste
    driver.quit()
    process.kill()

def test_app_opens(driver): 
    # Verificar se a pagina abre
    driver.get('http://localhost:8501')
    sleep(2)

# def test_check_title_is(driver): 
#     # Verificar se a pagina abre
#     driver.get('http://localhost:8501')
#     sleep(2)

#     # Captura o titulo da pagina
#     page_title = driver.title

#     # Verifica se o titulo da pagina é o esperado
#     expected_title = 'Validador de schema excel'

#     assert page_title == expected_title

# def test_check_streamlit_h1 (driver): 
#     # Verificar se a pagina abre
#     driver.get('http://localhost:8501')
#     sleep(2)   

#     # Captura primeiro elemento <h1> da pagina
#     h1_element = driver.find_element(By.TAG_NAME, 'h1')

#     # Verifica se o texto do elemento <h1> é o esperado
#     expected_text = 'Insira o seu excel para validação'

#     assert h1_element == expected_text
   