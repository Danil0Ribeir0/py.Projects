import pygame, sys

pygame.init()
color = (44, 44, 127)

screen = pygame.display.set_mode((300, 600)) # tamanho da janela (grid)
pygame.display.set_caption("Python Tetris") # Título do jogo

clock = pygame.time.Clock() # inicia o loop para o jogo

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # checa quando o jogo é fechado
            pygame.quit()
            sys.exit()
    screen.fill(color) # preenche a tela com a cor escolhida
    pygame.display.update()
    clock.tick(60) # determina a velocidade de atualização do jogo
