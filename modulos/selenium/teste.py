from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Opções do Chrome
# https://peter.sh/experiments/chromium-command-line-switches/

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'driver' / 'chromedriver'


def criar_navegador_chrome(*opcoes: str) -> webdriver.Chrome:
    opcoes_chrome = webdriver.ChromeOptions()

    # opcoes_chrome.add_argument('--headless') # #Headless -> com essa opção adicionada, o navegador não será exibido
    if opcoes is not None:
        for opcao in opcoes:
            opcoes_chrome.add_argument(opcao)

    servico_chrome = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    navegador = webdriver.Chrome(
        service=servico_chrome,
        options=opcoes_chrome
    )

    return navegador


if __name__ == '__main__':
    TEMPO_ESPERA = 5
    # Exemplo de opções:
    # opcoes = '--headless', '--disable-gpu',
    opcoes = ()
    navegador = criar_navegador_chrome(*opcoes)

    # Abrir o Google
    navegador.get('https://www.google.com')

    # Aguardar até encontrar a caixa de pesquisa
    caixa_pesquisa = WebDriverWait(navegador, TEMPO_ESPERA).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')  # Alterei o ID para NAME, pois é o seletor correto para a caixa de pesquisa do Google
        )
    )

    try:
        caixa_pesquisa.send_keys('Olá mundo!')
        caixa_pesquisa.send_keys(Keys.ENTER)
        sleep(10)
        try:
            WebDriverWait(navegador, TEMPO_ESPERA).until(
                EC.presence_of_all_elements_located(
                    (By.TAG_NAME, 'a')
                )
            )
            resultados = navegador.find_element(By.ID, 'search')
            links = resultados.find_elements(By.TAG_NAME, 'h3')
            # Abrir o segundo link usando JavaScript
            navegador.execute_script("arguments[0].click();", links[3])

        except:
            print('Link não encontrado')
    except:
        print('Não foi possível encontrar o elemento')

    # Aguardar por 10 segundos
    sleep(30)
