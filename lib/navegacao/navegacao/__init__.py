from selenium import webdriver
from selenium.webdriver.common.by import By
from downloads import Download
from time import sleep


class Navegar:
    def __init__(self, site, caminhoDriver, urlWebDriver, xpaths):
        self.site = site
        self.caminhoDriver = caminhoDriver
        self.urlWebDriver = urlWebDriver
        self.xpaths = xpaths

    def abreSite(self):
        try:
            opcoes = webdriver.EdgeOptions()
            driver = webdriver.Edge(executable_path=f'{self.caminhoDriver}\\msedgedriver.exe', options=opcoes)
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
