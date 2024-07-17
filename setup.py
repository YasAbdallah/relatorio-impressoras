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
    "include_files": "icon2.ico",
    "include_msvcr": True,
    "optimize": 2,
    
    }

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Geração de relatório de impressoras',
    version='1.3',
    description='Gerador de relatório automatico das impressoras de rede da marca HP. Desenvolvido por: Yasser Ibrahim Abdallah Vaz Condoluci.',
    options={'build.exe': options},
    executables=[
        Executable(
            'src/impressoras_HP.py', 
            base=base, 
            target_name="impressoras_HP.exe", 
            icon="img/icon2.ico", 
            shortcut_name='impressoras_HP', 
            shortcut_dir='Relatorio_impressoras')]
)
