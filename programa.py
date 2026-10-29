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
                    preenche_frota(frota, linha, coluna, orientacao, tamanho)
                    break
                else :
                    print('Esta posição não está válida!')
print(frota)
