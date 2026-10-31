from funcoes import *
import random 
frota = {}
nomes_navios = ['porta-aviões','navio-tanque','contratorpedeiro','submarino']
tamanhos = [4, 3, 2, 1]
quantidades = [1, 2, 3, 4]

for i in range(len(nomes_navios)):
    nome = nomes_navios[i]
    tamanho = tamanhos[i]
    quantidade = quantidades[i]

    for j in range(quantidade):
        while True :
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
            linha = int(input())
            coluna = int(input())

            if tamanho == 1 :
                orientacao = 'vertical'

                if posicao_valida(frota,linha,coluna,orientacao,tamanho) :
                    preenche_frota(frota,nome,linha,coluna,orientacao,tamanho)
                    break 
                else : 
                    print('Esta posição não está válida!')
            else : 
                escolha = int(input())
                if escolha == 1 :
                  orientacao = 'vertical'
                else : 
                    orientacao = 'horizontal'

                if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                    preenche_frota(frota,nome, linha, coluna, orientacao, tamanho)
                    break
                else :
                    print('Esta posição não está válida!')
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)
posicoes_atacadas = []
jogando = True
while jogando:
    monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    posicao_nova = False
    while posicao_nova == False:
        linha = int(input('Jogador, qual linha deseja atacar? '))
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Jogador, qual linha deseja atacar? '))
        coluna = int(input('Jogador, qual coluna deseja atacar? '))
        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Jogador, qual coluna deseja atacar? '))
        posicao = [linha, coluna]
        if posicao in posicoes_atacadas:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            posicao_nova = True
    posicoes_atacadas.append(posicao)
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
    quantidade_afundados = afundados(frota_oponente, tabuleiro_oponente)
    if quantidade_afundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False