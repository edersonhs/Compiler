cores = {
    'amarelo': '\033[1;33m',
    'roxo': '\033[1;35m',
    'vermelho': '\033[1;31m',
    'azul': '\033[1;34m',
    'azulCiano': '\033[1;36m',
    'verde': '\033[1;32m',
    'branco': '\033[1;37m'
}


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
        if nome == 'log.txt':
            a = open(nome, 'wt')
        else:
            a = open(nome, 'wt+')    # Escreve um arquigo de texto, e caso ele não exista, é criado (+).
        a.close()
    except Exception:
        if nome == 'log.txt':
            print(f'{cores["vermelho"]}Houve um ERRO ao criar o arquivo {nome}.')
        elif nome == 'codigo.txt':
            print(f'{cores["vermelho"]}Houve um ERRO na criação do arquivo {nome}!')
    else:
        if nome == 'log.txt':
            pass
        else:
            print(f'{cores["verde"]}Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception:
        print(f'{cores["vermelho"]}ERRO ao ler o arquivo!')
    else:
        dado = list()
        for linha in a:     # Para cada linha em arquivo
            dado.append(linha)
        a.close()
        return dado   # Retorna uma lista de cada linha do arquivo dentro de outra lista
