# import time
# from pathlib import Path
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# ROOT_FOLDER = Path(__file__).parent 
# CHROME_DRIVER_EXE = ROOT_FOLDER / 'driver' / 'chromedriver'

# # print(CHROME_DRIVER_EXE)

# chrome_options = webdriver.ChromeOptions()
# chrome_services = Service(executable_path=CHROME_DRIVER_EXE)
# chrome_browser = webdriver.Chrome(
#     service= chrome_services,
#     options= chrome_options,
# )

# chrome_browser.get('https://www.google.com.br/')
# time.sleep(30) 




# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'driver' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless') # #HEadless -> com essa opção adicionada, ele executa todo o comando sem abrir a tela do navegador
    if options is not None: 
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_WAIT = 10
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')

    #Espera para encontrar o input
    search_box = WebDriverWait(browser, TIME_WAIT).until(
        EC.presence_of_element_located(
            (By.ID, 'APjFqb')
        )

    )
    try:
        search_box.send_keys('HEllo world!')
        search_box.send_keys(Keys.ENTER)
        try:
            WebDriverWait(browser, TIME_WAIT).until(
                EC.presence_of_all_elements_located(
                    (By.TAG_NAME, 'a')
                )
            )
            results = browser.find_element(By.ID, 'search')
            links = results.find_elements(By.TAG_NAME, 'a')
            # print(links)
            links[0].click()
        except:
            print('LInk não encontrado')
    except:
        print('Não encontrado o elemento')
    # Dorme por 10 segundos
    sleep(TIME_WAIT)
    print(len(links))


