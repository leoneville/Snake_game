import pygame
from random import randrange

branco= (255,255,255)
preto= (0,0,0)
vermelho= (255,0,0)
verde= (0,255,0)
azul= (0,0,255)

def seticon(iconname): #Função para definir o icone do display
    icon= pygame.Surface((32,32))
    icon.set_colorkey((0,0,0))
    rawicon= pygame.image.load(iconname)
    for i in range(0,32):
        for j in range (0,32):
            icon.set_at((i,j), rawicon.get_at((i,j)))
    pygame.display.set_icon(icon)


try:
    pygame.init()
except:
    print('Não foi possivel inicializar o módulo "pygame"')
    
largura= 320
altura= 280
tamanho= 10
placar= 40


relogio= pygame.time.Clock()
fundo= pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Game Snake')
seticon('icon.png')


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1= font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])

def snake(SnakeXY):
    for XY in SnakeXY:
        pygame.draw.rect(fundo, preto, [XY[0],XY[1],tamanho,tamanho])

def apple(apple_x, apple_y):
    pygame.draw.rect(fundo, vermelho, [apple_x,apple_y,tamanho,tamanho])
    
    

def game_snake():
    sair= True
    fimdejogo= False
    pos_x= randrange(0,largura-tamanho,10)
    pos_y= randrange(0,altura-tamanho-placar,10)
    apple_x= randrange(0,largura-tamanho,10)
    apple_y= randrange(0,altura-tamanho-placar,10)
    velocidade_x = 0
    velocidade_y = 0
    SnakeXY= []
    SnakeComp= 1
    pontos= 0
    while sair:
        while fimdejogo:      
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair= False
                    fimdejogo= False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair= True
                        fimdejogo= False
                        pos_x= randrange(0,largura-tamanho,10)
                        pos_y= randrange(0,altura-tamanho-placar,10)
                        apple_x= randrange(0,largura-tamanho,10)
                        apple_y= randrange(0,altura-tamanho-placar,10)
                        velocidade_x = 0
                        velocidade_y = 0
                        SnakeXY= []
                        SnakeComp= 1
                        pontos= 0
                    if event.key == pygame.K_s:
                        sair= False
                        fimdejogo= False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 45 and y > 120 and x < 180 and y < 147:
                        sair= True
                        fimdejogo= False
                        pos_x= randrange(0,largura-tamanho,10)
                        pos_y= randrange(0,altura-tamanho-placar,10)
                        apple_x= randrange(0,largura-tamanho,10)
                        apple_y= randrange(0,altura-tamanho-placar,10)
                        velocidade_x = 0
                        velocidade_y = 0
                        SnakeXY= []
                        SnakeComp= 1
                        pontos= 0
                    elif x > 190 and y > 120 and x < 265 and y < 147:
                        sair= False
                        fimdejogo= False

                        
            fundo.fill(branco)
            texto('Fim de jogo', vermelho, 50, 65, 30)
            texto('Pontuação Final: '+str(pontos), preto, 30, 70, 80)
            pygame.draw.rect(fundo, preto, [45, 120, 135, 27])
            texto('Continuar(C)', branco, 30, 50, 125)
            pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
            texto('Sair(S)', branco, 30, 195, 125)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho or event.key == pygame.K_a and velocidade_x != tamanho:
                    velocidade_x = -tamanho
                    velocidade_y = 0
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho or event.key == pygame.K_d and velocidade_x != -tamanho:
                    velocidade_x = tamanho
                    velocidade_y = 0
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho or event.key == pygame.K_s and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho or event.key == pygame.K_w and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho

        if sair:

            fundo.fill(branco)
            pos_x+= velocidade_x
            pos_y+= velocidade_y

            if pos_x == apple_x and pos_y == apple_y:
                apple_x= randrange(0,largura-tamanho,10)
                apple_y= randrange(0,altura-tamanho-placar,10)
                SnakeComp+= 1
                pontos+= 1

            if pos_x + tamanho > largura:
                pos_x=0

            if pos_y + tamanho > altura - placar:
                pos_y=0

            if pos_y < 0:
                pos_y= altura-tamanho-placar

            if pos_x < 0:
                pos_x = largura-tamanho

    ##        if pos_x + tamanho > largura:
    ##            fimdejogo= True
    ##        if pos_x < 0:
    ##            fimdejogo= True
    ##        if pos_y + tamanho > altura:
    ##            fimdejogo= True
    ##        if pos_y < 0:
    ##            fimdejogo= True
                        
            
            SnakeHead= []
            SnakeHead.append(pos_x)
            SnakeHead.append(pos_y)
            SnakeXY.append(SnakeHead)
            if len(SnakeXY) > SnakeComp:
                del SnakeXY[0]

            if any(Bloco == SnakeHead for Bloco in SnakeXY[:-1]):
                fimdejogo= True


            pygame.draw.rect(fundo, preto, [0,altura-placar,largura,40])
            texto("Pontuação: "+str(pontos), branco, 20, 10, altura-30)

            snake(SnakeXY)                
            apple(apple_x, apple_y)
            relogio.tick(15)
            pygame.display.update()


if __name__ == '__main__':
    game_snake()
    pygame.quit()



    


