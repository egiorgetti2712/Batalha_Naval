def define_posicoes(linha,coluna,orientacao,tamanho) :
    lista_posicoes = []
    for i in range(tamanho) :
      if orientacao == 'vertical' :
         lista_posicoes.append([linha+i,coluna])
      elif orientacao == 'horizontal' :
         lista_posicoes.append([linha,coluna+i])
    return lista_posicoes
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho) :


  posicoes_navios = define_posicoes(linha,coluna,orientacao,tamanho)
  if nome_navio in frota :
    frota[nome_navio].append(posicoes_navios)
  else : 
    frota[nome_navio] = [posicoes_navios]

  return frota
def faz_jogada(tabuleiro,linha,coluna) :

  if tabuleiro[linha][coluna] == 1 :
    tabuleiro[linha][coluna] = 'X'
  else: 
    tabuleiro[linha][coluna] = '-'
  return tabuleiro
def posiciona_frota(frota) :
  grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
  for navios, posicao in frota.items() :
    for lista in posicao :
      for coordenadas in lista :
        linha = coordenadas[0]
        coluna = coordenadas[1]
        if grid[linha][coluna] == 0 :
          grid[linha][coluna] = 1
  return grid 
def afundados(frota,tabuleiro) :
  tot_afundado = 0 
  for tipo, navios in frota.items() :

    for navio in navios :
      afundado = True
      for posicoes in navio :
        linha = posicoes[0]
        coluna = posicoes[1]
        if tabuleiro[linha][coluna] != 'X' :
          afundado = False 
          break 
      if afundado : 
        tot_afundado += 1 
  return tot_afundado
def posicao_valida(frota,linha,coluna,orientacao,tamanho) :
  jogada = define_posicoes(linha,coluna,orientacao,tamanho)
  

