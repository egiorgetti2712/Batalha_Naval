from funcoes import posicao_valida
from funcoes import preenche_frota

frota = {}
nomes_navios = [
    'porta-aviões',
    'navio-tanque',
    'contratorpedeiro',
    'submarino'
]
tamanhos = [4, 3, 2, 1]
quantidades = [1, 2, 3, 4]
for i in range(len(nomes_navios)):
    nome = nomes_navios[i]
    tamanho = tamanhos[i]
    quantidade = quantidades[i]
    for j in range(quantidade):
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
        linha = int(input())
        coluna = int(input())
        escolha = int(input())
        if escolha == 1:
            orientacao = 'vertical'
        else:
            orientacao = 'horizontal'
        while not posicao_valida(frota, linha, coluna, orientacao, tamanho):
            print('Posição inválida. Escolha outra posição.')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            escolha = int(input('Orientação (1 - vertical, 2 - horizontal): '))
            if escolha == 1:
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'
        frota = preenche_frota(frota,nome,linha,coluna,orientacao,tamanho)