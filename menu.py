from scanner import *
from colors import colors
from time import sleep
from os import system, name   # Limpar a tela

colors = {
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
        system('cls' if name == 'nt' else 'clear')
        opcao = 0
        print(f'{colors["amarelo"]}Selecione uma opção:')
        for nro, conteudo in enumerate(opcoes):
            print(f'{colors["roxo"]}{nro+1:>2} - {colors["branco"]}{conteudo}.')
        try:
            while True:
                opcao = int(input(f'{colors["amarelo"]}>>> {colors["branco"]}Sua opção: '))
                if opcao > len(list(opcoes)) or opcao <= 0:
                    input(f'{colors["vermelho"]}ERRO: opção invalida. Digite uma opção existente!\n{colors["branco"]}'
                          f'Pressione enter para tentar novamente...')
                else:
                    break
        except Exception:
            input(f'{colors["vermelho"]}ERRO: opção invalida. Digite um número valido!\n{colors["branco"]} Pressione '
                  f'enter para tentar novamente...')

        if opcao == 1:
            system('cls' if name == 'nt' else 'clear')
            nome_arquivo = 'codigo.txt'
            criarArquivo('log.txt')  # Reescrevendo um arquivo de log vazio para não concatenar com o log anterior
            if arquivoExiste(nome_arquivo) and arquivoExiste(nome_arquivo_log):
                print(f'{colors["verde"]}{nome_arquivo} e {nome_arquivo_log} encontrados com sucesso!\n')
                analisador([word for word in lerArquivo(nome_arquivo)])
                print(f'\n{colors["branco"]}LOG DO ANALISADOR LÉXICO:')
                mostraLog()
                input(f'\n{colors["branco"]}Pressione ENTER para continuar...')
            else:
                print(f'{colors["vermelho"]}ERRO: arquivos não encontrados.')
                while True:
                    try:
                        opcao_temp = str(input(f'{colors["branco"]}Deseja criar o arquivo? [S/N] ')).upper()[0]
                        if opcao_temp == 'S':
                            print('\n')
                            criarArquivo(nome_arquivo)
                            input(f'{colors["branco"]}Pressione enter para continuar...')
                        else:
                            print(f'\n{colors["verde"]}Beleza! Retornando ao menu principal...')
                            sleep(2)
                    except Exception:
                        print(f'{colors["vermelho"]}ERRO: opção invalida. Digite uma opção valida!')
                    else:
                        break
        elif opcao == 2:
            system('cls' if name == 'nt' else 'clear')
            exit()
