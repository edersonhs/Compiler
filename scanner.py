from log import *
from linguagem import *

ignore = False
comment = False


def deep_analyzer(linha, palavra):   # Caracter por caracter
    global ignore
    global comment
    """
    if str(palavra[0]).isnumeric():
        escreveLog(linha, f'{cores["vermelho"]}INVALIDO', palavra,
                   'O primeiro caractere de um identificado não pode ser um número.')
    else:
        if str(palavra).isalpha():
            escreveLog(linha, 'IDENTIFICADOR', palavra)
    """
    aux = ''
    caractere = 0
    if comentario_fim in palavra:
        escreveLog(linha, 'DELIMITADOR', comentario_fim)
        caractere = palavra.find(comentario_fim) + 2

    for caractere in range(caractere, len(palavra)):
        if palavra[caractere].isalpha() or palavra[caractere].isdigit():
            aux += palavra[caractere]
        else:
            break

    if len(aux.split()) != 0:
        escreveLog(linha, 'IDENTIFICADOR', aux)

    if caractere >= len(palavra):   # Se já tiver percorrido todo o indice da string, sai da função.
        return
    if caractere+2 <= len(palavra):
        if palavra[caractere:caractere+2] == comentario:
            comment = True
            escreveLog(linha, 'DELIMITADOR', comentario)
            return
        if palavra[caractere:caractere+2] == comentario_inicio:
            ignore = True
            escreveLog(linha, 'DELIMITADOR', comentario_inicio)
            return


def analisador(codigo):
    global ignore
    global comment
    for linha, conteudo in enumerate(codigo):
        palavras = conteudo.split(' ')
        palavras = [palavras.strip() for palavras in palavras]   # retirando os espaços do inicio e fim de cada palavra
        for palavra in palavras:
            if type(palavra) == str and comentario_fim in palavra.strip():   # Fim comentario de mais de uma linha
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
                            palavra not in delimitadores and palavra not in operadores:   # Identificador
                        deep_analyzer(linha, palavra)
                        # escreveLog(linha, 'IDENTIFICADOR', palavra)
                        if comment:
                            comment = False   # Controle de comentario de uma linha dentro do deep_analyzer
                            break
