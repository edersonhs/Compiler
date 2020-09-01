from scanner import *
from time import sleep

cores = {
    'amarelo': '\033[1;33m',
    'roxo': '\033[1;35m',
    'vermelho': '\033[1;31m',
    'azul': '\033[1;34m',
    'azulCiano': '\033[1;36m',
    'verde': '\033[1;32m',
    'branco': '\033[1;37m'
}


def menu(*opcoes):
    while True:
        print("\x1b[2J\x1b[1;1H")
        opcao = 0
        print(f'{cores["amarelo"]}Selecione uma opção:')
        for nro, conteudo in enumerate(opcoes):
            print(f'{cores["roxo"]}{nro+1:>2} - {cores["branco"]}{conteudo}.')
        try:
            while True:
                opcao = int(input(f'{cores["amarelo"]}>>> {cores["branco"]}Sua opção: '))
                if opcao > len(list(opcoes)) or opcao <= 0:
                    input(f'{cores["vermelho"]}ERRO: opção invalida. Digite uma opção existente!\n{cores["branco"]}'
                          f'Pressione enter para tentar novamente...')
                else:
                    break
        except Exception:
            input(f'{cores["vermelho"]}ERRO: opção invalida. Digite um número valido!\n{cores["branco"]} Pressione '
                  f'enter para tentar novamente...')

        if opcao == 1:
            print("\x1b[2J\x1b[1;1H")
            nome_arquivo = 'codigo.txt'
            criarArquivo('log.txt')  # Reescrevendo um arquivo de log vazio para não concatenar com o log anterior
            if arquivoExiste(nome_arquivo) and arquivoExiste(nome_arquivo_log):
                print(f'{cores["verde"]}{nome_arquivo} e {nome_arquivo_log} encontrados com sucesso!\n')
                analisador([word.replace('\n', '') for word in lerArquivo(nome_arquivo)])
                print(f'{cores["branco"]}LOG DO ANALISADOR LÉXICO:')
                mostraLog()
                input(f'\n{cores["branco"]}Pressione ENTER para continuar...')
            else:
                print(f'{cores["vermelho"]}ERRO: arquivos não encontrados.')
                while True:
                    try:
                        opcao_temp = str(input(f'{cores["branco"]}Deseja criar o arquivo? [S/N] ')).upper()[0]
                        if opcao_temp == 'S':
                            criarArquivo(nome_arquivo)
                            input(f'{cores["branco"]}Pressione enter para continuar...')
                        else:
                            print(f'{cores["verde"]}Beleza! Retornando ao menu principal...')
                            sleep(2)
                    except Exception:
                        print(f'{cores["vermelho"]}ERRO: opção invalida. Digite uma opção valida!')
                    else:
                        break
        elif opcao == 2:
            print("\x1b[2J\x1b[1;1H")
            exit()
