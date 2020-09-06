from log import *
from linguagem import *


def analisador(codigo):
    ignore = False
    for linha, conteudo in enumerate(codigo):
        palavras = conteudo.split(' ')
        palavras = [palavras.strip() for palavras in palavras]   # retirando os espaços do inicio e fim de cada palavra
        for palavra in palavras:
            if type(palavra) == str and palavra.strip() == comentario_fim:   # Fim comentario de mais de uma linha
                ignore = False
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
                    if len(palavra) != 0 and palavra not in palavras_reservadas and \
                            palavra not in delimitadores and palavra not in operadores:
                        escreveLog(linha, 'IDENTIFICADOR', palavra)
