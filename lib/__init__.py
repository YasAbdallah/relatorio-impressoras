from time import sleep
from selenium import webdriver
from tkinter import messagebox, Tk
from _tkinter import TclError
from datetime import date


def abre_nav_chorme():
    """
    Função para abrir o navegador para automação
    :return: Retorna o navegado aberto
    """
    try:
        # Abrindo Navegador
        opcoes = webdriver.ChromeOptions()
        opcoes.add_argument('')
        nav = webdriver.Chrome(executable_path='lib\\chromedriver.exe')
        return nav
    except Exception as e:
        alerta('Houve um erro ao iniciar o aplicativo.',
               f'O arquivo chromedriver.exe não foi encontrado em seu computador. {e}')
        exit()


def abre_link(link=''):
    """
    O programador deve informar qual é o link para automação
    :param link: Informar o link
    :return: O site aberto
    """
    nav = abre_nav_chorme()
    try:
        nav.get(link)
        return nav
    except Exception as e:
        alerta('Houve um erro ao entrar no app das impressoras.',
               f'O link a qual foi informado anteriormente não está acessivel.{e}')
        nav.quit()
        exit()


def navegar_site(link, xpath):
    """
    função criada para clicar em botões do site.
    :param link: Deve informar a variavel que foi informado para abrir o site
    :param xpath: Passar uma lista de XPath dos botões em ordem que devem ser clicados. Caso haja forms para login
    informar o mesmo em Dicionario e fazer um if da posisão a qual esta este dict() e passar a def escreva_texto() para
    escrever nos inputs de texto.
    :return: Retorna a navegação no site clicando em botões
    """
    try:
        sleep(2)
        link.find_element_by_xpath(f'{xpath}').click()
        return link
    except Exception as e:
        alerta('Houve um erro ao navegar pelo app.', f'Não foi possivel encontrar os botões de navegação.{e}')
        link.quit()
        exit()


def escreva_texto(link, login):
    """
    Função criada para escrever textos em inputs que deseja automatizar.
    Para isso deve-se informar um dicionario à lista a qual foi indormado os botões na função navegar_site().
    :param link: Passar a variavel a qual foi declarada para abrir o site.
    :param login: passa o dicionario.
    :return: texto escrito no campo.
    """
    try:
        for k, v in login.items():
            sleep(0.9)
            link.find_element_by_name(f'{k}').send_keys(f'{v}')
        return link
    except Exception as e:
        alerta('Não foi possivel efetuar login.', f'Não consegui encontrar os campos para login. {e}')
        link.quit()
        exit()


def alerta(titulo, mensagem, espera=10000):
    root = Tk()
    root.withdraw()
    try:
        root.after(espera, root.destroy)
        return messagebox.Message(title=titulo, message=mensagem, master=root).show()
    except TclError:
        pass


def formata_data(data=date.today()):
    hoje = str(date.today())
    data = hoje.replace('-', ',').split(',')
    form_data = dict()
    form_data['dia'] = data[-1]
    form_data['mes'] = data[1]
    form_data['ano'] = data[0]
    return f'{form_data["dia"]}-{form_data["mes"]}-{form_data["ano"]}'