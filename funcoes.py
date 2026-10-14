def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_posicoes = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            lista_posicoes.append([linha + i, coluna])
        elif orientacao == 'horizontal':
            lista_posicoes.append([linha,coluna + i])
    return lista_posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes_navios = define_posicoes(linha,coluna,orientacao,tamanho)
    if nome_navio in frota :
        frota[nome_navio].append(posicoes_navios)
    else : 
        frota[nome_navio] = [posicoes_navios]
    
    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro 

def posiciona_frota(info_navios):
    lista_listas = []
    

        
    