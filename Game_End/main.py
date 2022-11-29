import pygame
import sys
from constantes import *
from manager_nivel_1 import *
from leer_json import Lector_json
from pygame.locals import *
from constantes_gui import *
from manager_gui import Manager_do_formularios
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()
json_full = Lector_json((r"C:\Users\Ares\Cursada Lab 1\Game_End\datas.json"))
data_lvl_one = json_full.importar_json()
imagen_fondo = pygame.image.load(data_lvl_one["nivel_uno"][0]["imagen_fondo"]).convert_alpha()
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
level_01 = Nivel_uno(data_lvl_one,screen)
game = Manager_do_formularios(screen,level_01)
while True:
    keys = pygame.key.get_pressed()
    lista_eventos = pygame.event.get()
    for event in pygame.event.get():                                                                              
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    game.update(screen,delta_ms,keys,lista_eventos)
    pygame.display.flip()