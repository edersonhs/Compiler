from log import escreveLog
from language import *
from colors import colors

quote = False
comment = False
quoteCount = 0   # Controle das aspas


def deep_analyzer(linha, conteudo):   # Analisa caractere por caractere
    global quoteCount   # Contador de controle das aspas
    global quote   # Aspas
    global comment

    aux = ''
    indice = 0

    while indice < len(conteudo):
        # Aspas
        if comment ==  False and aspas in conteudo[indice] or aspasSimples in conteudo[indice]:   # Começa a ignorar o conteudo dentro das aspas
            if quoteCount == 0:
                quote = True
                quoteCount = 1
                escreveLog(linha, 'DELIMITADOR', conteudo[indice])
            else:   # Para de ignorar o conteudo dentro das aspas
                quote = False
                quoteCount = 0

        # Bloco de comentario
        if conteudo[indice:indice+2] in comentario_inicio:
            comment = True   # Começando a ignorar conteudo dentro do bloco de comentario
            escreveLog(linha, 'DELIMITADOR', comentario_inicio)
        elif conteudo[indice:indice+2] in comentario_fim:
            comment = False   # Parando de ignorar conteudo dentro do bloco de comentario
        
        # Analise
        if not comment and not quote:     
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
                        if aux[0].isdigit():
                            escreveLog(linha, 'IDENTIFICADOR', aux, 'O primeiro caractere de um identificador não pode ser um número.')
                        else:
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
                    if comentario in conteudo[indice-2:indice+2]:   # Comentario de uma linha, passa a ignorar o restante da linha
                        break
                    else:
                        continue
                elif conteudo[indice] in delimitadores and conteudo[indice:indice+2] not in operadores:
                    escreveLog(linha, 'DELIMITADOR', conteudo[indice])
                
                if not conteudo[indice].isdigit() and not conteudo[indice].isalpha() and conteudo[indice] not in operadores and conteudo[indice] not in delimitadores and not conteudo[indice].isspace():
                    escreveLog(linha, 'CARACTERE_INVALIDO', conteudo[indice], 'Caractere não encontrado no alfabeto da linguagem')
        indice += 1
    
    if indice == len(conteudo) and len(aux) != 0 and not comment:
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
