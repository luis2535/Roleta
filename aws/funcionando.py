#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import padroes
import testebot

# Função para lidar com as mudanças na div
def handle_div_changes(mutations_list, observer, div_selector):
    for mutation in mutations_list:
        if mutation.type == 'childList':
            # A <div> foi modificada (elementos filho adicionados/alterados/removidos)
            div_text = driver.find_element(By.XPATH, div_selector).text
            print("Texto modificado na div:", div_text)


login = 'ana.julia.machaado@gmail.com'
senha = 'roulettenemesis'

# Set path Selenium
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
s = Service(CHROMEDRIVER_PATH)
WINDOW_SIZE = "1920,1080"

# Options
chrome_options = Options()
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=s, options=chrome_options)


def conect():
    # Abra a página de login
    driver.get('https://www.playpix.com/pb')
    # Aguarde até que o botão de login esteja visível (max 10 segundos)
    try:
        botao_entrar = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/header/div[1]/div[3]/button[1]'))
        )
        botao_entrar.click()
        # Localize os campos de usuário e senha pelo name
        time.sleep(2)
        campo_usuario = driver.find_element(By.NAME, 'username')
        campo_senha = driver.find_element(By.NAME, 'password')

        # Preencha os campos de login
        campo_usuario.send_keys(login)
        campo_senha.send_keys(senha)

        botao_login = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[6]/div/button'))
        )
        botao_login.click()


    except:
        print("O botão de login não foi encontrado")

    try:
        botao_exit = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[7]/div/div/i'))
        ) 
    except:
        print("cade ?")
    botao_exit.click()

def find_iframe():
    

    time.sleep(5)

    iframes = driver.find_elements(By.TAG_NAME, 'iframe')

    # Verifique se há pelo menos um iframe na página
    if len(iframes) > 0:
        # Acesse o primeiro iframe da lista
        primeiro_iframe = iframes[0]

        # Use JavaScript para obter o valor do atributo src do primeiro iframe
        iframe_src = driver.execute_script("return arguments[0].getAttribute('src');", primeiro_iframe)


    driver.get(iframe_src)

    driver.switch_to.default_content()

def main_loop():

    array_anterior = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    time.sleep(5)
    while(True):
        time.sleep(1)
        try:

            dados = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[9]/div[1]/div'))
            )
        except Exception as e:
            print("Erro ao localizar a div específica:", str(e))
        dados_text = dados.text

        # Divida a string em linhas e converta em inteiros
        int_array = [int(line) for line in dados_text.splitlines()]
        if(int_array != array_anterior):
        # Agora, int_array contém os inteiros como elementos de uma lista
            print(int_array)
            seis_primeiros = int_array[:6]
            oito_primeiros = int_array[:8]
            validationArray1 = padroes.testing12(padroes.bets12, oito_primeiros)
            validationArray2 = padroes.testing13(padroes.bets13, seis_primeiros)


            if(any(validationArray1)):
                label1 = dict(zip(padroes.label12, validationArray1))
                msg = testebot.tratamsg12(int_array, label1)
                testebot.send_msg(msg, testebot.url)
            if(any(validationArray2)):
                label2 = dict(zip(padroes.label13, validationArray2))
                msg = testebot.tratamsg13(int_array,label2)
                testebot.send_msg(msg, testebot.url)

            array_anterior = int_array
        try:
            element = driver.find_element(By.CLASS_NAME, "pause-session-layout")
            print(element)
            botao_ficar = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/button[2]'))
        )
            botao_ficar.click()

        except:
            print('Mantendo ativo')


try:        
    conect()
    driver.get('https://www.playpix.com/pb?openGames=40003094-real&gameNames=Roulette%20A')
    find_iframe()
    find_iframe()
    main_loop()
    print('Saiu do loop')
finally:
    print('Finalizando drivers')
    driver.close()
    driver.quit()