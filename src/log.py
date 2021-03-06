from archives import criarArquivo
from colors import colors

nome_arquivo_log = './archives/log.txt'
criarArquivo(nome_arquivo_log)


def escreveLog(linha, tipo, conteudo, motivo=''):
    try:
        log = open(nome_arquivo_log, 'at')
    except Exception:
        print(f'{colors["vermelho"]}Houve um ERRO ao abrir o arquivo de log!')
    else:
        try:

            text = (f'{colors["branco"]}LINHA {linha+1}: {colors["branco"]}('
                    f'{colors["verde"] if len(motivo) == 0 else colors["vermelho"]}{tipo}'
                    f'{colors["branco"]}: {colors["branco"]}{conteudo}{colors["branco"]})')

            if len(motivo) == 0:
                log.writelines(f'{text:<91} {colors["verde"]} OK\n')
            else:
                log.writelines(f'{text:<91} {colors["vermelho"]}ERRO: {colors["branco"]}{motivo}\n')
        except Exception:
             print(f'{colors["vermelho"]}Houve um ERRO ao escrever os dados no arquivo de Log!')
        else:
            log.close()


def mostraLog():
    try:
        log = open(nome_arquivo_log, 'rt')
    except Exception:
        print(f'{colors["vermelho"]}ERRO ao ler o Log!')
    else:
        for linha in log:
            print(linha.replace('\n', ''))
        log.close()
