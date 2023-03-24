import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['os'], 'includes': ['tkinter']}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Geração de relatorio de impressoras da Receita Federal de Mundo Novo-ms',
    version='1.1',
    description='Gerador de relatório automatico das impressoras de rede da marca OKI, no sistema PrintSuperVision',
    options={'build.exe': build_exe_options},
    executables=[Executable('main.py', base='win32GUI')]
)
