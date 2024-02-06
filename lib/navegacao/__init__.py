import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from lib.downloads import Download
from time import sleep


class Navegar:
    def __init__(self, site, caminhoDriver, xpaths):
        self.site = site
        self.caminhoDriver = caminhoDriver
        self.versaoDriver = [f for d, f, a in os.walk('C:\\Program Files (x86)\\Microsoft\\Edge\\Application')][0][0]
        self.urlWebDriver = f"https://msedgedriver.azureedge.net/{self.versaoDriver}/edgedriver_win64.zip"
        self.xpaths = xpaths

    def abreSite(self):
        try:
            opcoes = webdriver.EdgeOptions()
            driver = webdriver.Edge(options=opcoes)
        except Exception as e:
            print(e)
            download = Download(self.urlWebDriver, self.caminhoDriver, self.caminhoDriver)
            download.download()
            self.abreSite()
        else:
            driver.get(self.site)
            for xpath, texto in self.xpaths.items():
                sleep(3)
                if texto != '':
                    driver.find_element(By.XPATH, xpath).send_keys(texto)
                else:
                    driver.find_element(By.XPATH, xpath).click()
            driver.close()
