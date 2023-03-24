import pymsgbox

def mensagem(titulo, texto, tempo=3000):
    criador = " Criado Por: Nome."
    return pymsgbox.alert(text=texto, title=titulo + criador, timeout=tempo)