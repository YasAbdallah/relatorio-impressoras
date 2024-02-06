import sys
from cx_Freeze import setup, Executable

options = {'packages': ['os'], 'excludes': ['tkinter']}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Geração de relatório de impressoras da Receita Federal de Mundo Novo-ms',
    version='1.2',
    description='Gerador de relatório automatico das impressoras de rede da marca OKI, no sistema PrintSuperVision',
    options={'build.exe': options},
    executables=[Executable('main.py', base='win32GUI', icon="icon.ico")]
)
