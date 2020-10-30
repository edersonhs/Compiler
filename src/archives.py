from colors import colors


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')    # Abre o arquivo para leitura de texto
        a.close()   # Fecha o arquivo
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        if nome == './archives/log.txt':
            a = open(nome, 'wt')
        else:
            a = open(nome, 'wt+')    # Escreve um arquigo de texto, e caso ele não exista, é criado (+).
        a.close()
    except Exception:
        if nome == './archives/log.txt':
            print(f'{colors["vermelho"]}Houve um ERRO ao criar o arquivo {nome}.')
        elif nome == './archives/codigo.txt':
            print(f'{colors["vermelho"]}Houve um ERRO na criação do arquivo {nome}!')
    else:
        if nome == './archives/log.txt':
            pass
        else:
            print(f'{colors["verde"]}Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception:
        print(f'{colors["vermelho"]}ERRO ao ler o arquivo!')
    else:
        dado = list()
        for linha in a:     # Para cada linha em arquivo
            dado.append(linha)
        a.close()
        return dado   # Retorna uma lista de cada linha do arquivo dentro de outra lista
