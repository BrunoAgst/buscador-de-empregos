#imports
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()

#config additional webdriver firefox
firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')

#setting config
driver = webdriver.Firefox(firefox_options=firefox_options, executable_path=rf'{os.getenv("DIRECTORY_WEBDRIVER")}')

def scraping_vagas(job, state):
    url = f'https://www.vagas.com.br/vagas-de-{job}-em-{state}?ordenar_por=mais_recentes'

    driver.get(url)
    sleep(5)

    try:
        while True:
            btn = driver.find_element_by_xpath('//*[@id="maisVagas"]')
            btn.click()
    except:
        pass

    jobs = driver.find_elements_by_class_name('informacoes-header')

    list_jobs = []
    
    for job in jobs:
        job_descript = {
            'cargo': f"{job.find_element_by_class_name('link-detalhes-vaga').text}",
            'empresa': f"{job.find_element_by_class_name('emprVaga').text}",
            'nivel': f"{job.find_element_by_class_name('nivelQtdVagas').text}"
        }

        list_jobs.append(job_descript)

    return list_jobs
