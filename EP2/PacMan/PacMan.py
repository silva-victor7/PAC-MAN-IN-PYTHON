######################################################
# Introdução a Programação (2023/2)
# EP2 - PacMan
# Integrante 1: Victor Rodrigues Silva
# Integrante 2: Breno Marcolino Cardoso
# Integrante 3: Jose Modesto de Carvalho Neto
# Integrante 4: Guilherme Cunha Viana De Oliveira
######################################################

#ATENÇÃO: você não pode importar o módulo PyGame neste arquivo. 
#Consequentemente, você não pode usar o métodos do módulo.
#Você pode, se precisar, importar o módulo math e/ou random.
from BaseParaJogo import *
import random

CORFUNDOJANELA = (0, 0, 0)
LARGURAJANELA = 800
ALTURAJANELA = 704
ICONE = "Recursos/Imagens/icone.png"

#Direção do movimento
PARADO = 0
CIMA = 1
BAIXO = 2
ESQUERDA = 3
DIREITA = 4

MAPA = [
[5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7],   
[9,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
[9,2,5,1,7,2,5,1,7,2,5,1,7,2,39,41,43,45,7,2,5,29,7,2,11],
[9,2,9,2,2,2,9,2,2,2,9,0,11,2,35,41,43,45,35,2,51,29,15,2,11],
[9,2,9,2,11,2,9,2,11,2,9,0,11,2,35,2,2,2,35,2,35,2,2,2,11],
[9,2,13,3,15,2,13,3,15,2,13,3,15,2,33,2,31,2,33,0,33,2,37,2,11],
[9,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,35,2,2,2,2,2,2,2,11],
[13,3,3,3,3,3,17,2,31,2,5,1,53,1,7,2,35,2,19,3,3,3,3,3,15],
[0,0,0,0,0,0,11,2,35,2,9,0,0,0,11,2,35,2,9,0,0,0,0,0,0],
[3,3,3,3,3,3,15,2,35,2,9,0,0,0,11,2,35,2,13,3,3,3,3,3,3],
[2,2,2,2,2,2,2,2,35,2,9,0,0,0,11,2,35,2,2,2,2,2,2,2,2],
[1,1,1,1,1,1,7,2,33,2,13,3,3,3,15,2,33,2,5,1,1,1,1,1,1],
[0,0,0,0,0,0,11,2,2,2,2,2,2,2,2,2,2,2,9,0,0,0,0,0,0],
[5,1,1,1,1,1,21,2,25,29,29,29,29,29,29,29,27,2,23,1,1,1,1,1,7],
[9,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
[9,2,25,29,29,29,29,27,2,37,2,37,2,37,2,37,2,25,29,29,29,29,27,2,11],
[9,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
[9,2,25,29,29,29,29,27,2,25,29,27,2,25,29,27,2,25,29,29,29,29,27,2,11],
[9,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
[13,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,15]
]

def desenhaMapa(parede, pilula):
    
    """
    Funçao reponsável por posicionar os objetos no mapa(paredes e pilulas).
    
    Parâmetros:
        parede: Recebe uma lista de imagens que é selecionada de acordo com a sua posição na lista e necessidade.
        pilula: Imagem contendo a pilula(objeto de pontuação) que será consumida pelo Pacman.
        
    retorno:
        none.
    """
    for l in range(len(MAPA)):
        for c in range(len(MAPA[l])):
            if MAPA[l][c] == 1:
                desenhaImagem(parede[0], c*32, l*32)
            elif MAPA[l][c] == 3:
                desenhaImagem(parede[1], c*32, l*32)
            elif MAPA[l][c] == 5:
                desenhaImagem(parede[2], c*32, l*32)
            elif MAPA[l][c] == 7:
                desenhaImagem(parede[3], c*32, l*32)
            elif MAPA[l][c] == 9:
                desenhaImagem(parede[6], c*32, l*32)
            elif MAPA[l][c] == 11:
                desenhaImagem(parede[7], c*32, l*32)
            elif MAPA[l][c] == 13:
                desenhaImagem(parede[4], c*32, l*32)
            elif MAPA[l][c] == 15:
                desenhaImagem(parede[5], c*32, l*32)
            elif MAPA[l][c] == 17:
                desenhaImagem(parede[8], c*32, l*32)
            elif MAPA[l][c] == 19:
                desenhaImagem(parede[9], c*32, l*32)
            elif MAPA[l][c] == 21:
                desenhaImagem(parede[10], c*32, l*32)
            elif MAPA[l][c] == 23:
                desenhaImagem(parede[11], c*32, l*32)
            elif MAPA[l][c] == 25:
                desenhaImagem(parede[12], c*32, l*32)
            elif MAPA[l][c] == 27:
                desenhaImagem(parede[13], c*32, l*32)
            elif MAPA[l][c] == 29:
                desenhaImagem(parede[14], c*32, l*32)
            elif MAPA[l][c] == 31:
                desenhaImagem(parede[15], c*32, l*32)
            elif MAPA[l][c] == 33:
                desenhaImagem(parede[16], c*32, l*32)
            elif MAPA[l][c] == 35:
                desenhaImagem(parede[17], c*32, l*32)
            elif MAPA[l][c] == 37:
                desenhaImagem(parede[18], c*32, l*32)
            elif MAPA[l][c] == 39:
                desenhaImagem(parede[19], c*32, l*32)
            elif MAPA[l][c] == 41:
                desenhaImagem(parede[20], c*32, l*32)
            elif MAPA[l][c] == 43:
                desenhaImagem(parede[21], c*32, l*32)
            elif MAPA[l][c] == 45:
                desenhaImagem(parede[22], c*32, l*32)
            elif MAPA[l][c] == 47:
                desenhaImagem(parede[23], c*32, l*32)
            elif MAPA[l][c] == 51:
                desenhaImagem(parede[24], c*32, l*32)
            elif MAPA[l][c] == 53:
                desenhaImagem(parede[25], c*32, l*32)
            elif MAPA[l][c] == 2:
                desenhaImagem(pilula, c*32, l*32)
                
def identificaParedes(x, y, direcao):
    
    """
    Funçao reponsável por identificar paredes pelo mapa, possibilitando, assim, que o programa identifique se o Pacman ou os fantasmas pode ir na direção escolhida.
    
    Parâmetros:
        x: Recebe a posição atual do eixo x do Pacman ou de algum dos fantasmas.
        y: Recebe a posição atual do eixo y do Pacman ou de algum dos fantasmas.
        direcao: recebe a direção escolhida, e verifica se é possivel ir naquele sentido.
        
    retorno:
        Retorna True caso seja parede, e false caso contrario.
    """
    if direcao == CIMA and ((MAPA[(y - 1)//32][x//32]) %2 == 0) and (MAPA[(y - 1)//32][(x + 31)//32] %2 == 0):
        return True
    elif direcao == BAIXO and (MAPA[(y + 32) //32][x//32] %2 == 0) and (MAPA[(y + 32) //32][(x + 31) //32] %2 == 0): 
        return True
    elif direcao == ESQUERDA and (MAPA[y//32][(x - 1)//32] %2 == 0) and (MAPA[(y + 31) //32][(x - 1)//32] %2 == 0): 
        return True
    elif direcao == DIREITA and (MAPA[y//32][(x + 32) //32] %2 == 0) and (MAPA[(y + 31) //32][(x + 32)//32] %2 == 0): 
        return True  
      
    return False

def ehPilula(xPacman, yPacman):
    
    """
    Funçao reponsável por identificar se há pilula na posição que o pacman está.
    
    Parâmetros:
        xPacman: Recebe a posição do Pacman no eixo x.
        yPacman: Recebe a posição do Pacman no eixo y.
        
    retorno:
        retorna 1(um) caso haja pilula na posição em questao, e 0(zero) caso contrario.
    """
    comendoPilula = carregaSom("Recursos/Sons/comendo-pilula.mp3")
    if MAPA[yPacman//32][xPacman//32] == 2:
        MAPA[yPacman//32][xPacman//32] = 0
        tocaSom(comendoPilula)
        return 1
    else:
        return 0

def fantasmaPerseguidor(xFantasma, yFantasma, xPacman, yPacman, intencaoDoFantasma):
    
    """
    Funçao reponsável pela movimentação dos fantasmas pelo mapa.

    Parâmetros:
        xFantasma: Recebe a posição do fantasma no eixo x.
        yFantasma: Recebe a posição do fantasma no eixo y.
        xPacman: Recebe a posição do Pacman no eixo x.
        yPacman: Recebe a posição do Pacman no eixo y.
        intencaoDoFantasma: Recebe a direção em que o fantasma pretende ir.
        
    retorno:
        Retorna a nova direção que o fantasma perseguidor irá assumir.
    """
    
    # Lógica de perseguição: o fantasma se move em direção ao Pac-Man
    intencaoDoFantasma
    
    # Lista de direções possíveis
    direcoesPossiveis = []

    # Adiciona as direções possíveis à lista
    if xFantasma < xPacman and identificaParedes(xFantasma, yFantasma, DIREITA):
        direcoesPossiveis.append(DIREITA)
    elif xFantasma > xPacman and identificaParedes(xFantasma, yFantasma, ESQUERDA):
        direcoesPossiveis.append(ESQUERDA)

    if yFantasma < yPacman and identificaParedes(xFantasma, yFantasma, BAIXO):
        direcoesPossiveis.append(BAIXO)
    elif yFantasma > yPacman and identificaParedes(xFantasma, yFantasma, CIMA):
        direcoesPossiveis.append(CIMA)

    # Escolhe uma direção aleatória entre as possíveis
    if direcoesPossiveis:
        intencaoDoFantasma = random.choice(direcoesPossiveis)
    return intencaoDoFantasma

def moveFantasmas(xFantasma, yFantasma, intencaoDoFantasma, fantasmaSelecionado, corDoFantasma, xPacman, yPacman, pilulasComidas):

    """
    Funçao reponsável pela movimentação dos fantasmas pelo mapa.

    Parâmetros:
        xFantasma: Recebe a posição do fantasma no eixo x.
        yFantasma: Recebe a posição do fantasma no eixo y.
        intencaoDoFantasma: Recebe a direção em que o fantasma pretende ir.
        fantasmaSelecionado: Recebe uma lista de imagens do fantasma que está sendo analisado, os quais são: vermelho, rosa, ciano e laranja.
        
    retorno:
        Retorna a posição x e y atualizada do fantasma e a imagem que será impressa na janela.
    """
    imagemFantasma = fantasmaSelecionado[0]
    # Lógica para que os fantasmas saiam da ala aprisionamento.
    if xFantasma == 384 and yFantasma == 256:
        yFantasma -= 40
        imagemFantasma = fantasmaSelecionado[0]
        return xFantasma, yFantasma, imagemFantasma
    
    # Caso os fantasmas forem para o portal.
    if xFantasma == 768 and yFantasma == 320:
        xFantasma = 24
        yFantasma = 320
        return xFantasma, yFantasma, imagemFantasma
    elif xFantasma == 24 and yFantasma == 320:
        xFantasma = 768
        yFantasma = 320
        return xFantasma, yFantasma, imagemFantasma
    
    if corDoFantasma == "vermelho" and pilulasComidas >= 0:
        intencaoDoFantasma = fantasmaPerseguidor(xFantasma, yFantasma, xPacman, yPacman, intencaoDoFantasma)
    elif corDoFantasma == "rosa" and pilulasComidas >= 100:
        intencaoDoFantasma = fantasmaPerseguidor(xFantasma, yFantasma, xPacman, yPacman, intencaoDoFantasma)
    elif corDoFantasma == "ciano" and (tempoExecutandoJogo()/1000) >= 40.00:
        intencaoDoFantasma = fantasmaPerseguidor(xFantasma, yFantasma, xPacman, yPacman, intencaoDoFantasma)
    elif corDoFantasma == "laranja" and pilulasComidas >= 180:
        intencaoDoFantasma = fantasmaPerseguidor(xFantasma, yFantasma, xPacman, yPacman, intencaoDoFantasma)
    
    if intencaoDoFantasma == CIMA and identificaParedes(xFantasma, yFantasma, intencaoDoFantasma) :
        yFantasma -= 2
        imagemFantasma = fantasmaSelecionado[0]
    elif intencaoDoFantasma == BAIXO and identificaParedes(xFantasma, yFantasma, intencaoDoFantasma):
        yFantasma += 2
        imagemFantasma = fantasmaSelecionado[1]
    elif intencaoDoFantasma == ESQUERDA and identificaParedes(xFantasma, yFantasma, intencaoDoFantasma):
        xFantasma -= 2
        imagemFantasma = fantasmaSelecionado[3]
    elif intencaoDoFantasma == DIREITA and identificaParedes(xFantasma, yFantasma, intencaoDoFantasma):
        xFantasma += 2
        imagemFantasma = fantasmaSelecionado[2]

    return xFantasma, yFantasma, imagemFantasma

def mouseDentroRetangulo(xRetangulo, yRetangulo, larguraRetangulo, alturaRetangulo, xMouse, yMouse):
    """Verifica se o cursor do mouse está "dentro" do retângulo"""
    return xRetangulo <= xMouse <= larguraRetangulo + xRetangulo and yRetangulo <= yMouse <= yRetangulo + alturaRetangulo

def menuInicial():
    """
    Funçao reponsável pela tela inicial do jogo.

    Parâmetros:
        N/A.
        
    retorno:
        None.
    """
    criaJanela(800, 640, "PAC-MAN", CORFUNDOJANELA, ICONE)
    larguraRetangulo = 500
    alturaRetangulo = 250
    xRetangulo = 128
    yRetangulo1 = 192
    opcaoEscolhida = 0
    
    musica_menu_inicial = carregaMusica("Recursos/Sons/musica-inicial.mp3")
    menu = carregaImagem("Recursos/Imagens/menu.png", (800, 640))
    tocaMusica(musica_menu_inicial)
    
    while True:   
        
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()
        
        desenhaImagem(menu, 0, 0)
        #Obtem as informções do clique do mouse
        xMouse, yMouse = posicaoCursorMouse() 
        opcaoEscolhida = 0
        
        #Define as cores dos retângulos
        if mouseDentroRetangulo(xRetangulo, yRetangulo1, larguraRetangulo, alturaRetangulo, xMouse, yMouse):
            opcaoEscolhida = 1
        botaoPressionado, botao, posicao = botaoMousePressionado()    
        
        #Verifica se o botão esquerdo foi pressionado dentro de uma das opções
        if botaoPressionado and botao == 1 and opcaoEscolhida != 0: 
            break
        
        atualizaTelaJogo()

def gameOver():
    """
    Funçao reponsável pela tela que aparecerá quando o PacMan é morto.

    Parâmetros:
        N/A.
        
    retorno:
        None.
    """
    
    game_over = carregaImagem("Recursos/Imagens/game-over.png", (800, 640))
    som_game_over = carregaSom("Recursos/Sons/game-over.mp3")
    paraMusica()
    tocaSom(som_game_over)
    criaJanela(800, 640, "PAC-MAN", CORFUNDOJANELA, ICONE)
      
    while True:   
    
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()
        
        desenhaImagem(game_over, 0, 0)
        
        atualizaTelaJogo()    

def voceGanhou():
    """
    Funçao reponsável pela tela que aparecerá quando o PacMan come todas as pílulas.

    Parâmetros:
        N/A.
        
    retorno:
        None.
    """
    vencedor = carregaImagem("Recursos/Imagens/tela-vencedor.png", (800, 640))
    som_vencedor = carregaSom("Recursos/Sons/venceu.mp3")
    paraMusica()
    tocaSom(som_vencedor)
    criaJanela(800, 640, "PAC-MAN", CORFUNDOJANELA, ICONE)
      
    while True:   
    
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()
        
        desenhaImagem(vencedor, 0, 0)
        
        atualizaTelaJogo()    
   
def main():
    """
    Funçao principal.
    
    Parâmetros:
        N/A.
        
    retorno:
        None.
    """
    menuInicial()
    
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Pac-Man", CORFUNDOJANELA, ICONE)
    
    # Atributos do MAPA
    paredes = [carregaImagem("Recursos/Imagens/parede-superior.png", (32, 32)), #0
               carregaImagem("Recursos/Imagens/parede-inferior.png", (32, 32)), #1
               carregaImagem("Recursos/Imagens/parede-canto-esquerdo-superior.png", (32, 32)), #2
               carregaImagem("Recursos/Imagens/parede-canto-direito-superior.png", (32, 32)), #3
               carregaImagem("Recursos/Imagens/parede-canto-esquerdo-inferior.png", (32, 32)), #4
               carregaImagem("Recursos/Imagens/parede-canto-direito-inferior.png", (32, 32)), #5
               carregaImagem("Recursos/Imagens/parede-lateral-esquerda.png", (32, 32)), #6
               carregaImagem("Recursos/Imagens/parede-lateral-direita.png", (32, 32)),#7
               carregaImagem("Recursos/Imagens/parede-curva-esquerda.png", (32, 32)),#8 
               carregaImagem("Recursos/Imagens/parede-curva-direita.png", (32, 32)), #9,
               carregaImagem("Recursos/Imagens/parede-curva-esquerda-inferior.png", (32, 32)), #10
               carregaImagem("Recursos/Imagens/parede-curva-direita-inferior.png", (32, 32)), #11
               carregaImagem("Recursos/Imagens/bloco-fecha-esquerda.png", (32, 32)), #12
               carregaImagem("Recursos/Imagens/bloco-fecha-direita.png", (32, 32)), #13
               carregaImagem("Recursos/Imagens/bloco-central.png", (32, 32)), #14
               carregaImagem("Recursos/Imagens/bloco-fecha-cima.png", (32, 32)), #15
               carregaImagem("Recursos/Imagens/bloco-fecha-baixo.png", (32, 32)), #16
               carregaImagem("Recursos/Imagens/bloco-central-vertical.png", (32, 32)), #17
               carregaImagem("Recursos/Imagens/quadrado.png", (32, 32)), #18
               carregaImagem("Recursos/Imagens/primeira-parte-doM.png", (32, 32)), #19
               carregaImagem("Recursos/Imagens/segunda-parte-doM.png", (32, 32)), #20
               carregaImagem("Recursos/Imagens/terceira-parte-doM.png", (32, 32)), #21
               carregaImagem("Recursos/Imagens/quarta-parte-doM.png", (32, 32)), #22
               carregaImagem("Recursos/Imagens/quinta-parte-doM.png", (32, 32)), #23
               carregaImagem("Recursos/Imagens/parte-do-P.png", (32, 32)), #24
               carregaImagem("Recursos/Imagens/fecha-ala-fantasmas.png", (32, 32))] #25    
    pilula = carregaImagem("Recursos/Imagens/pilula.png", (32, 32))
    
    #Atributos do Pacman
    pacman_baixo = [carregaImagem("Recursos/Imagens/pacman_baixo.png", (32, 32)),
                     carregaImagem("Recursos/Imagens/pacmanBF.png", (32, 32))]
    pacman_cima = [carregaImagem("Recursos/Imagens/pacman_cima.png", (32, 32)),
                    carregaImagem("Recursos/Imagens/pacmanBF.png", (32, 32))]
    pacman_esquerda = [carregaImagem("Recursos/Imagens/pacman_esquerda.png", (32, 32)),
                        carregaImagem("Recursos/Imagens/pacmanBF.png", (32, 32))]
    pacman_direita = [carregaImagem("Recursos/Imagens/pacman_direita.png", (32, 32)),
                       carregaImagem("Recursos/Imagens/pacmanBF.png", (32, 32))]
    
    imagemPacman = pacman_direita
    framePacman = 0
    xPacman = 384
    yPacman = 448
    pacmanVivo = True
    
    velocidadeAnimacaoPacman = 0.2
    direcao = PARADO
    irPara = PARADO
    pilulasComidas = 0
    tempoJogado = tempoExecutandoJogo()
    
    #Atributos dos fantasmas
    fantasma_vermelho = [carregaImagem("Recursos/Imagens/fantasma-vermelho-cima.png", (32, 32)),
                         carregaImagem("Recursos/Imagens/fantasma-vermelho-baixo.png", (32, 32)),
                         carregaImagem("Recursos/Imagens/fantasma-vermelho-direita.png", (32, 32)),
                         carregaImagem("Recursos/Imagens/fantasma-vermelho-esquerda.png", (32, 32))]
    fantasma_rosa = [carregaImagem("Recursos/Imagens/fantasma-rosa-cima.png", (32, 32)),
                         carregaImagem("Recursos/Imagens/fantasma-rosa-baixo.png", (32, 32)),
                         carregaImagem("Recursos/Imagens/fantasma-rosa-direita.png", (32, 32)),
                         carregaImagem("Recursos/Imagens/fantasma-rosa-esquerda.png", (32, 32))]
    fantasma_ciano = [carregaImagem("Recursos/Imagens/fantasma-ciano-cima.png", (32, 32)),
                         carregaImagem("Recursos/Imagens/fantasma-ciano-baixo.png", (32, 32)),
                         carregaImagem("Recursos/Imagens/fantasma-ciano-direita.png", (32, 32)),
                         carregaImagem("Recursos/Imagens/fantasma-ciano-esquerda.png", (32, 32))]
    fantasma_laranja = [carregaImagem("Recursos/Imagens/fantasma-laranja-cima.png", (32, 32)),
                         carregaImagem("Recursos/Imagens/fantasma-laranja-baixo.png", (32, 32)),
                         carregaImagem("Recursos/Imagens/fantasma-laranja-direita.png", (32, 32)),
                         carregaImagem("Recursos/Imagens/fantasma-laranja-esquerda.png", (32, 32))]
    
    imagemFantasmaVermelho = fantasma_vermelho
    imagemFantasmaRosa = fantasma_rosa
    imagemFantasmaCiano = fantasma_ciano
    imagemFantasmaLaranja = fantasma_laranja
    xFantasmaVermelho = 352
    yFantasmaVermelho = 192
    xFantasmaRosa = 352
    yFantasmaRosa = 320
    xFantasmaCiano = 384
    yFantasmaCiano = 320
    xFantasmaLaranja = 416
    yFantasmaLaranja = 320
    
    intencaoDoFantasmaVermelho = random.choice([CIMA, BAIXO, ESQUERDA, DIREITA])
    intencaoDoFantasmaRosa = random.choice([CIMA, BAIXO, ESQUERDA, DIREITA])
    intencaoDoFantasmaCiano = random.choice([CIMA, BAIXO, ESQUERDA, DIREITA])
    intencaoDoFantasmaLaranja = random.choice([CIMA, BAIXO, ESQUERDA, DIREITA])
    
    while True:   
               
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()
        
        if (xFantasmaVermelho == xPacman and yFantasmaVermelho == yPacman) or (xFantasmaRosa == xPacman and yFantasmaRosa == yPacman)\
            or (xFantasmaRosa == xPacman and yFantasmaRosa == yPacman) or(xFantasmaCiano == xPacman and yFantasmaCiano == yPacman)\
            or(xFantasmaLaranja == xPacman and yFantasmaLaranja == yPacman):
            pacmanVivo = False
        
        if pacmanVivo == False:
            gameOver()
            
        if pilulasComidas == 210:
            voceGanhou()
        
        #movimentaçao do Pacman
        if xPacman == 768 and yPacman == 320:
            xPacman= 24
            yPacman = 320
            imagemPacman = pacman_direita
        elif xPacman == 24 and yPacman == 320:
            xPacman = 768
            yPacman = 320
            imagemPacman = pacman_esquerda
            
        #Verifica se uma das teclas foi pressionada. Se sim, atualiza a posição do Pacman
        if teclaPressionada(K_UP):
            irPara = CIMA
            
        elif teclaPressionada(K_DOWN):
            irPara = BAIXO
            
        elif teclaPressionada(K_LEFT):
            irPara = ESQUERDA
        
        elif teclaPressionada(K_RIGHT):
            irPara = DIREITA
            
        if irPara == CIMA and identificaParedes(xPacman, yPacman, irPara):
            direcao = irPara
            imagemPacman = pacman_cima
    
        elif irPara == BAIXO and identificaParedes(xPacman, yPacman, irPara):
            direcao = irPara
            imagemPacman = pacman_baixo
    
        elif irPara == ESQUERDA and identificaParedes(xPacman, yPacman, irPara):
            direcao = irPara
            imagemPacman = pacman_esquerda
    
        elif irPara == DIREITA and identificaParedes(xPacman, yPacman, irPara):
            direcao = irPara
            imagemPacman = pacman_direita
        
        #Atualiza a posição do jogador
        if direcao == CIMA and identificaParedes(xPacman, yPacman, direcao):
            yPacman -= 2
            pilulasComidas += ehPilula(xPacman, yPacman)
        elif direcao == BAIXO and identificaParedes(xPacman, yPacman, direcao):
            yPacman += 2
            pilulasComidas += ehPilula(xPacman, yPacman)
        elif direcao == ESQUERDA and identificaParedes(xPacman, yPacman, direcao):
            xPacman -= 2
            pilulasComidas += ehPilula(xPacman, yPacman)
        elif direcao == DIREITA and identificaParedes(xPacman, yPacman, direcao):
            xPacman += 2
            pilulasComidas += ehPilula(xPacman, yPacman)
        else:
            direcao = PARADO
            
        #Movimentação dos fantasmas
        
        # Fantasma Vermelho
        if not(identificaParedes(xFantasmaVermelho, yFantasmaVermelho, intencaoDoFantasmaVermelho)):
            intencaoDoFantasmaVermelho = random.choice([CIMA, BAIXO, ESQUERDA, DIREITA])
        xFantasmaVermelho, yFantasmaVermelho, imagemFantasmaVermelho = moveFantasmas(xFantasmaVermelho, yFantasmaVermelho, intencaoDoFantasmaVermelho, fantasma_vermelho,
                                                                                     "vermelho", xPacman, yPacman, pilulasComidas)
        # Fantasma Rosa
        if not(identificaParedes(xFantasmaRosa, yFantasmaRosa, intencaoDoFantasmaRosa)):
            intencaoDoFantasmaRosa = random.choice([CIMA, BAIXO, ESQUERDA, DIREITA])
        xFantasmaRosa, yFantasmaRosa, imagemFantasmaRosa = moveFantasmas(xFantasmaRosa, yFantasmaRosa, intencaoDoFantasmaRosa, fantasma_rosa,
                                                                         "rosa", xPacman, yPacman, pilulasComidas)
        # Fantasma Ciano
        if not(identificaParedes(xFantasmaCiano, yFantasmaCiano, intencaoDoFantasmaCiano)) :
            intencaoDoFantasmaCiano = random.choice([CIMA, BAIXO, ESQUERDA, DIREITA])
        xFantasmaCiano, yFantasmaCiano, imagemFantasmaCiano = moveFantasmas(xFantasmaCiano, yFantasmaCiano, intencaoDoFantasmaCiano, fantasma_ciano,
                                                                            "ciano", xPacman, yPacman, pilulasComidas)
        # Fantasma Laranja
        if not(identificaParedes(xFantasmaLaranja, yFantasmaLaranja, intencaoDoFantasmaLaranja)):
            intencaoDoFantasmaLaranja = random.choice([CIMA, BAIXO, ESQUERDA, DIREITA])
        xFantasmaLaranja, yFantasmaLaranja, imagemFantasmaLaranja = moveFantasmas(xFantasmaLaranja, yFantasmaLaranja, intencaoDoFantasmaLaranja, fantasma_laranja,
                                                                                  "laranja", xPacman, yPacman, pilulasComidas)
        
        #Desenha o mapa
        desenhaMapa(paredes, pilula)
        
        #Desenha eventuais textos
        desenhaTexto(f"PONTOS: {pilulasComidas:2d}                    TEMPO: {(tempoExecutandoJogo()/1000):.2f}s", 200, 672, 20, (255, 255, 255), "Recursos/Fontes/Grand9K Pixel.ttf")
        
        #Desenha o jogador          
        if direcao != PARADO:
            framePacman += velocidadeAnimacaoPacman
            if framePacman >= 2:
                framePacman = 0
            desenhaImagem(imagemPacman[int(framePacman)], xPacman, yPacman)
        else:
            desenhaImagem(imagemPacman[0], xPacman, yPacman)
        
        #Desenha fantasmas
        desenhaImagem(imagemFantasmaVermelho, xFantasmaVermelho, yFantasmaVermelho)
        desenhaImagem(imagemFantasmaRosa, xFantasmaRosa, yFantasmaRosa)
        desenhaImagem(imagemFantasmaCiano, xFantasmaCiano, yFantasmaCiano)
        desenhaImagem(imagemFantasmaLaranja, xFantasmaLaranja, yFantasmaLaranja)
        
        #Atualiza os objetos na janela
        atualizaTelaJogo()
            
    finalizaJogo()

main()

