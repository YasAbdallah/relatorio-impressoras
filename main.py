from lib import *
from pdfkit import configuration, from_url

alerta('Iniciando Geração de relatório.', 'Aguarde uns instantes, qualquer coisa vamos te avisarei quando terminar.')
nav = abre_link('http://localhost:81/PrintSuperVision/Default.htm')
xpath_passos = [
    '/html/body/table[1]/tbody/tr/td[4]/a/span',
    {
        'username': 'admin',
        'password': 'aaaaaa'
    },
    '/html/body/form/blockquote/table/tbody/tr[3]/td/input',
    '//*[@id="PSVmenu_2894"]/a',
    '/html/body/p/table/tbody/tr[1]/td[2]/a',
    '//*[@id="btnCollect"]',
    '/html/body/form/p[5]/input'
]
for k, v in enumerate(xpath_passos):
    if k == 1:
        escreva_texto(nav, v)
    else:
        navegar_site(nav, v)
options = {
    'quiet': ''
}
caminho = '//10.51.102.90/Roteiros/_CONTROLES/_Relatorios_impressorasOKI'
from_url('http://localhost:81/PrintSuperVision/UsageReport.aspx?PG_ID=0&format=webNew&cmdReport=Exibir',
         f'{caminho}/relatorio_impressoras_{formata_data()}.pdf',
         options=options
         )
nav.quit()
alerta('Relatório concluido.', f'Confira a pasta: {caminho}. Em sua rede.')
