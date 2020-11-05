from log import escreveLog
from language import *
from colors import colors

ignore = False
comment = False
count = 0   # Controle das aspas


def deep_analyzer(linha, conteudo):   # Analisa caractere por caractere
    global ignore
    global comment
    global count

    aux = ''
    indice = 0

    while indice < len(conteudo):
        if conteudo[indice] == ',' and conteudo[indice-1].isdigit() and conteudo[indice+1].isdigit() or conteudo[indice].isalpha() or conteudo[indice].isdigit() or conteudo[indice] == '_':
            aux += conteudo[indice]
        else:
            try:
                aux = int(aux)
                escreveLog(linha, 'INTEIRO', aux)
                aux = ''
            except:
                pass
            try:
                if aux.count(',') == 1:
                    aux = aux.replace(',', '.')
                aux = float(aux)
                escreveLog(linha, 'REAL', aux)
                aux = ''
            except:
                pass
            if aux in palavras_reservadas:
                escreveLog(linha, 'PALAVRA_RESERVADA', aux)
                aux = ''
            else:
                if len(aux) != 0:
                    escreveLog(linha, 'IDENTIFICADOR', aux)
                    aux = ''
            if conteudo[indice:indice+2] in operadores:
                escreveLog(linha, 'OPERADOR', conteudo[indice:indice+2])
                indice += 2
                if conteudo[indice:indice-2] == comentario:
                    break
                continue
            elif conteudo[indice] in operadores and conteudo[indice:indice+2] not in delimitadores:
                escreveLog(linha, 'OPERADOR', conteudo[indice])
            if conteudo[indice:indice+2] in delimitadores:
                escreveLog(linha, 'DELIMITADOR', conteudo[indice:indice+2])
                indice += 2
                continue
            elif conteudo[indice] in delimitadores and conteudo[indice:indice+2] not in operadores:
                escreveLog(linha, 'DELIMITADOR', conteudo[indice])
        indice += 1
    
    if indice == len(conteudo) and len(aux) != 0:
        try:
            aux = int(aux)
            escreveLog(linha, 'INTEIRO', aux)
            aux = ''
        except:
            pass
        try:
            if aux.count(',') == 1:
                aux = aux.replace(',', '.')
            aux = float(aux)
            escreveLog(linha, 'REAL', aux)
            aux = ''
        except:
            pass
        if aux in palavras_reservadas:
            escreveLog(linha, 'PALAVRA_RESERVADA', aux)
            aux = ''
        else:
            if len(aux) != 0:
                escreveLog(linha, 'IDENTIFICADOR', aux)
                aux = ''
                        

def analisador(codigo):
    for linha, conteudo in enumerate(codigo):
        deep_analyzer(linha, conteudo)
