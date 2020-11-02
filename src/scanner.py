from log import escreveLog
from language import *
from colors import colors

ignore = False
comment = False
count = 0   # Controle das aspas


def deep_analyzer(linha, palavra):   # Analisa caractere por caractere
    global ignore
    global comment
    global count

    aux = ''
    caractere = 0
    print(palavra)
    if comentario_fim in palavra:   # Fim comentario de mais de uma linha
        escreveLog(linha, 'DELIMITADOR', comentario_fim)
        caractere = palavra.find(comentario_fim) + 2

    for caractere in range(caractere, len(palavra)):
        
        if palavra[caractere].isalpha() or palavra[caractere].isdigit():
            aux += palavra[caractere]
        else:
            break

    if len(aux.split()) != 0:
        try:
            aux = int(aux)
            escreveLog(linha, 'INTEIRO', aux)
        except Exception:
            try:
                aux = float(aux)
                escreveLog(linha, 'REAL', aux)
            except Exception:
                if str(aux[0]).isnumeric():
                    escreveLog(linha, f'{colors["vermelho"]}INVALIDO', aux,
                            'O primeiro caractere de um identificador não pode ser um número.')
                elif aux in palavras_reservadas:
                    escreveLog(linha, 'PALAVRA_RESERVADA', aux)
                elif aux in operadores:
                    escreveLog(linha, 'OPERADOR', aux)
                else:
                    escreveLog(linha, 'IDENTIFICADOR', aux)

    if caractere >= len(palavra):   # Se o contador já tiver percorrido todo o indice da string, sai da função.
        return

    # ASPAS - Controle
    if (aspas in palavra[caractere] and count == 0) or (aspasSimples in palavra[caractere] and count == 0):
        escreveLog(linha, 'DELIMITADOR', aspas if aspas in palavra[caractere] else aspasSimples)
        # caractere = palavra.find(aspas if aspas in palavra[caractere] else aspasSimples) + 1
        count += 1
        ignore = True

    if (aspas in palavra[caractere] and count == 1) or (aspasSimples in palavra[caractere] and count == 1):
        escreveLog(linha, 'DELIMITADOR', aspas if aspas in palavra[caractere] else aspasSimples)
        # caractere = palavra.find(aspas if aspas in palavra[caractere] else aspasSimples) + 1
        ignore = False
        count -= 1

    # Comentarios - Controle
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
    global count

    for linha, conteudo in enumerate(codigo):
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
