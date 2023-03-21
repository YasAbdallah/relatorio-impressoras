from pdfkit import from_url
from datetime import datetime
from lib.navegacao import Navegar

alerta('Iniciando Geração de relatório.', 'Aguarde uns instantes, qualquer coisa vamos te avisarei quando terminar.')

site = 'http://localhost:81/PrintSuperVision/LoginForm.aspx'
dirDriver = 'D:\\Temp\\scripts\\webdriver'
siteWebdriver = 'https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/'

pastaSalvarPDF = 'caminho da pasta de rede'
dia = datetime.today().day
mes = datetime.today().month
ano = datetime.today().year
dataHoje = f"{dia}-{mes}-{ano}"

xpath_passos = {
    '//input[@name="username"]': 'admin',
    '//input[@name="password"]': 'aaaaaa',
    '//input[@name="submit"]': '',
    '//*[@id="PSVmenu_2894"]/a': '', #Botão Serviços
    '/a[@href="DataCollect.aspx"]': '', #Botão de serviço de coleta de dados
    '//*[@id="btnCollect"]': '',
    '//input[@name="cmd"]': ''
}
nav = Navegar(site, dirDriver, siteWebdriver, xpath_passos)

options = {
    'quiet': ''
}


from_url('http://localhost:81/PrintSuperVision/UsageReport.aspx?PG_ID=0&format=webNew&cmdReport=Exibir',
         f'{pastaSalvarPDF}/relatorio_impressoras_{dataHoje}.pdf',
         options=options
         )
nav.quit()
alerta('Relatório concluido.', f'Confira a pasta: {pastaSalvarPDF}. Em sua rede.')
