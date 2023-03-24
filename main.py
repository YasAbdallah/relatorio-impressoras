from pdfkit import from_url
from datetime import datetime
from lib.funcoes import Navegar
from lib.funcoes import mensagem

mensagem('Iniciando Geração de relatório.', 'Aguarde uns instantes, qualquer coisa vamos te avisarei quando terminar.')

site = 'http://localhost:81/PrintSuperVision/LoginForm.aspx'
dirDriver = 'D:\\Temp\\scripts\\webdriver'
siteWebdriver = 'https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/' # Pagina de download do MS-Edge driver
urlRelatorio = 'http://localhost:81/PrintSuperVision/UsageReport.aspx?PG_ID=0&format=webNew&cmdReport=Exibir' # Url gerada depois de levantar os dados as impressoras.

pastaSalvarPDF = 'caminho da pasta de rede'
dataHoje = f"{datetime.today().day}-{datetime.today().month}-{datetime.today().year}"

xpath_passos = {
    # Se o parametro valor estiver vazio é um botão, se ele estiver com algum valor é campo de texto.
    '//input[@name="username"]': 'admin',
    '//input[@name="password"]': 'aaaaaa',
    '//input[@name="submit"]': '',
    '//*[@id="PSVmenu_2894"]/a': '', #Botão Serviços
    '/a[@href="DataCollect.aspx"]': '', #Botão de serviço de coleta de dados
    '//*[@id="btnCollect"]': '',
    '//input[@name="cmd"]': ''
}
nav = Navegar(site, dirDriver, siteWebdriver, xpath_passos)
nav.abreSite()

from_url(
    urlRelatorio,
    f'{pastaSalvarPDF}/relatorio_impressoras_{dataHoje}.pdf',
    options={'quiet': ''}
    )
nav.quit()

mensagem('Relatório concluido.', f'Confira a pasta: {pastaSalvarPDF}. Em sua rede.')
