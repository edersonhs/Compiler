from log import *
from linguagem import *


def analisador(codigo):
    ignore = False
    for linha, conteudo in enumerate(codigo):
        palavras = conteudo.split(' ')
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
                if type(palavra) == str and palavra.strip() in palavras_reservadas:
                    escreveLog(linha, 'PALAVRA_RESERVADA', palavra.strip())
                if type(palavra) == str and palavra.strip() in operadores:
                    escreveLog(linha, 'OPERADOR', palavra.strip())
                if type(palavra) == str and palavra.strip() in delimitadores:
                    escreveLog(linha, 'DELIMITADOR', palavra.strip())
                if type(palavra) == str and palavra.strip() == comentario:   # comentario de uma linha
                    break
                if type(palavra) == str and palavra.strip() == comentario_inicio:   # Comentario de mais de uma linha
                    ignore = True
                if type(palavra) == str and len(palavra) != 0 and palavra.strip() not in palavras_reservadas and \
                        palavra.strip() not in delimitadores and palavra.strip() not in operadores:
                    escreveLog(linha, 'IDENTIFICADOR', palavra)
