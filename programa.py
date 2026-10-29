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
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
        linha = int(input())
        coluna = int(input())
        escolha = int(input())
        if escolha == 1:
            orientacao = 'vertical'
        else:
            orientacao = 'horizontal'
        if tamanho == 4 :
            navio = posicao_valida(frota,linha,coluna,orientacao,tamanho)
            if navio == False :
                print("Esta posição não está válida!")
            else : 
                posicao = define_posicoes(linha,coluna,orientacao,tamanho)
                preencher = preenche_frota(frota,'porta-avioes',linha,coluna,orientacao,tamanho)
        if tamanho == 3 :
                    navio = posicao_valida(frota,linha,coluna,orientacao,tamanho)
                    if navio == False :
                        print("Esta posição não está válida!")
                    else : 
                        posicao = define_posicoes(linha,coluna,orientacao,tamanho)
                        preencher = preenche_frota(frota,'porta-avioes',linha,coluna,orientacao,tamanho)
        if tamanho == 2 :
                    navio = posicao_valida(frota,linha,coluna,orientacao,tamanho)
                    if navio == False :
                        print("Esta posição não está válida!")
                    else : 
                        posicao = define_posicoes(linha,coluna,orientacao,tamanho)
                        preencher = preenche_frota(frota,'porta-avioes',linha,coluna,orientacao,tamanho)
        if tamanho == 1 :
                    navio = posicao_valida(frota,linha,coluna,orientacao,tamanho)
                    if navio == False :
                        print("Esta posição não está válida!")
                    else : 
                        posicao = define_posicoes(linha,coluna,orientacao,tamanho)
                        preencher = preenche_frota(frota,'porta-avioes',linha,coluna,orientacao,tamanho)
print(frota)


        

