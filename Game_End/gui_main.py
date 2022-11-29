import pygame
from pygame.locals import *
from constantes_gui import *
from manager_gui import Manager_do_formularios
flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
imagen_fondo = pygame.image.load("mountain/all.png").convert_alpha()
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
clock = pygame.time.Clock()
game = Manager_do_formularios(screen,1)
while True:     
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    game.update(screen,delta_ms,keys,lista_eventos)
    pygame.display.flip()