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
        if conteudo[indice].isalpha() or conteudo[indice].isdigit():
            aux += conteudo[indice]
        else:
            try:
                inteiro = int(aux)
                escreveLog(linha, 'INTEIRO', aux)
            except:
                try:
                    real = float(aux)
                    escreveLog(linha, 'REAL', aux)
                except:
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

        # if indice == len(conteudo) and len(aux) != 0:
        #    print('ERRO')
                        

def analisador(codigo):
    for linha, conteudo in enumerate(codigo):
        deep_analyzer(linha, conteudo)


"""
        palavras = conteudo.split(' ')
        palavras = [palavras.strip() for palavras in palavras]   # retirando os espaços do inicio e fim de cada palavra
        
        for palavra in palavras:
            if type(palavra) == str and comentario_fim in palavra:   # Fim comentario de mais de uma linha
                ignore = False
            
            # ASPAS - Controle
            if (palavra == aspas and count == 0) or (palavra == aspasSimples and count == 0):
                count += 1
                ignore = True
            elif (palavra == aspas and count == 1) or (palavra == aspasSimples and count == 1):
                escreveLog(linha, 'DELIMITADOR', palavra)
                ignore = False
                count -= 1

            if not ignore:
                try:
                    palavra = int(palavra)
                    escreveLog(linha, 'INTEIRO', palavra)
                except Exception:
                    try:
                        palavra = float(palavra)
                        escreveLog(linha, 'REAL', palavra)
                    except Exception:
                        pass
                if type(palavra) == str:
                    if palavra in palavras_reservadas:
                        escreveLog(linha, 'PALAVRA_RESERVADA', palavra)
                    if palavra in operadores:
                        escreveLog(linha, 'OPERADOR', palavra)
                    if palavra in delimitadores:
                        escreveLog(linha, 'DELIMITADOR', palavra)
                    if palavra == comentario:   # comentario de uma linha
                        break
                    if palavra == comentario_inicio:   # Comentario de mais de uma linha
                        ignore = True
                    if len(palavra) != 0 and palavra not in palavras_reservadas and palavra not in delimitadores and palavra not in operadores:   # Identificador
                        deep_analyzer(linha, palavra)
                        if comment:
                            comment = False   # Controle de comentario de uma linha dentro do deep_analyzer
                            break
"""