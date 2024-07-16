import sys
from cx_Freeze import setup, Executable

options = {
    'packages': [
        'os', 
        'pyhtml2pdf', 
        'datetime', 
        'time', 
        'PIL',
        'selenium',
        'urllib',
        "zipfile",
        'reportlab',
        'shutil',
        'pymsgbox',
        'subprocess',
    ], 
    'excludes': ['tkinter'],
    "include_files": ["icon2.ico", "lib/"],
    "include_msvcr": True,
    "optimize": 2
    }

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Geração de relatório de impressoras',
    version='1.3',
    description='Gerador de relatório automatico das impressoras de rede da marca HP. Desennvolvido por: Yasser Ibrahim Abdallah Vaz Condoluci.',
    options={'build.exe': options},
    executables=[Executable('impressoras_HP.py', base=base, icon="icon2.ico")]
)
