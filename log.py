from arquivo import *

cores = {
    'amarelo': '\033[1;33m',
    'roxo': '\033[1;35m',
    'vermelho': '\033[1;31m',
    'azul': '\033[1;34m',
    'azulCiano': '\033[1;36m',
    'verde': '\033[1;32m',
    'branco': '\033[1;37m'
}


nome_arquivo_log = 'log.txt'
criarArquivo(nome_arquivo_log)


def escreveLog(linha, tipo, conteudo):
    try:
        log = open(nome_arquivo_log, 'at')
    except Exception:
        print(f'{cores["vermelho"]}Houve um ERRO ao abrir o arquivo de log!')
    else:
        try:
            log.writelines(f'{cores["roxo"]}LINHA {linha+1}: {cores["branco"]}({cores["amarelo"]}{tipo}'
                           f'{cores["branco"]}: {cores["azul"]}{conteudo}{cores["branco"]})\n')
        except Exception:
            print(f'{cores["vermelho"]}Houve um ERRO ao escrever os dados no arquivo de Log!')
        else:
            log.close()


def mostraLog():
    try:
        log = open(nome_arquivo_log, 'rt')
    except Exception:
        print(f'{cores["vermelho"]}ERRO ao ler o Log!')
    else:
        for linha in log:
            print(linha.replace('\n', ''))
        log.close()
