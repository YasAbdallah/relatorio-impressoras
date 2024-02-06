import pymsgbox

def mensagem(titulo, texto, tempo=3000):
    criador = " Desenvolvido por: Yasser Ibrahim."
    return pymsgbox.alert(text=texto, title=titulo + criador, timeout=tempo)