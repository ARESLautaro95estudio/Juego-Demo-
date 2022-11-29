from manager_terreno import Terreno
from manager_materiales import Materiales
from manager_bullet import Manager_Bala
from player import Player
from Enemy_1 import Enemy_02
from Enemy_1 import Enemy_1
import pygame
from constantes import *
from gui_button import Button
class Nivel_uno:

    def __init__(self,json_data,screen):

        self.json = json_data
        self.screen = screen
        self.terreno = []
        self.materiales = []
        self.enemigos = []
        self.scenario= []
        self.portales = []
        self.bala= 0
        self.armado_de_materiales()
        self.armado_de_terreno()
        self.armado_de_menu()
        self.player = self.armado_de_personaje()
        self.armado_de_enemigos()
        self.el_unificador()
        self.armado_de_balas()
        
    def armado_de_terreno(self):
        '''
        Llama a objeto Terreno creando una lista estos objetos tienen metodo(draw/update/colicion)
        Incluye(Muros/plataformas/Techos)
        '''
        self.terreno = Terreno(self.json["nivel_uno"][0]["plataformas"]["pos_x"],self.json["nivel_uno"][0]["plataformas"]["pos_y"],self.json["nivel_uno"][0]["plataformas"]["cantidad"],self.json["nivel_uno"][0]["Muros"]["pos_x"],self.json["nivel_uno"][0]["Muros"]["pos_y"],self.json["nivel_uno"][0]["Muros"]["cantidad"],self.json["nivel_uno"][0]["Techos"]["pos_x"],self.json["nivel_uno"][0]["Techos"]["pos_y"],self.json["nivel_uno"][0]["Techos"]["cantidad"],self.screen)

    def armado_de_materiales(self):
        '''
        Llama a objeto Materiales creando una lista estos objetos tienen metodo(draw/update/colicion)
        Incluye(Fruits/Portal)
        ''' 
        loot_x = self.json["nivel_uno"][0]["loot"]["pos_x"]
        loot_y = self.json["nivel_uno"][0]["loot"]["pos_y"]
        loot_cantidad = self.json["nivel_uno"][0]["loot"]["cantidad"]
        portal_x = self.json["nivel_uno"][0]["portal"]["pos_x"]
        portal_y = self.json["nivel_uno"][0]["portal"]["pos_y"]

        self.materiales = Materiales(loot_x,loot_y,loot_cantidad,portal_x,portal_y)

    def armado_de_menu(self):
        # lifecont = pygame.font.Font(None,30)
        # score = pygame.font.Font(None,30)
        # end_score = pygame.font.Font(None,100)


        # lista_balas= []
        # objetivo2=0
        # objetivo1=0
        pass
    
    def update(self,screen,delta_ms,keys,objetivos):
        '''
        Recibe el screen , delta(tiempo),teclas(get_presed) desde el main
        Mantiene actualizado el objeto llamando a los metodos de los objetos involucrados.
        Ejecuta el metodo .draw y busca coliciones.
        '''
        self.player.draw(screen)      
        self.player.events(keys)
        self.player.update(delta_ms , self.terreno.plataformas_lista , self.terreno.muros_lista , self.terreno.techos_lista ,self.enemigos,self.enemigos,self.materiales.lista_loot)   
        self.bala.update(delta_ms,screen)  
          
        for enemy in self.enemigos:
            enemy.draw(screen)  
            enemy.update(delta_ms,self.terreno.plataformas_lista,self.player.rect)
            enemy.move()

        for things in self.scenario:
            things.draw(screen)

        for fruta in self.materiales.lista_loot:
            fruta.draw(screen)
            fruta.colision(self.player.rect_pick_up_collition,fruta)


        self.score(screen)
   
    def el_unificador(self):
        '''
        Unifica todos los objetos en una sola lista para iterarla con .draw(screen)
        '''
        self.scenario+=self.terreno.plataformas_lista
        self.scenario+=self.terreno.techos_lista
        self.scenario+=self.terreno.muros_lista
        self.scenario+=self.materiales.lista_portal
            
    def armado_de_balas (self):
        '''
        Unifica objetos materiales,terrenos,enemigos y personaje
        (SUMA LISTAS Y LA DUPLICO UNA PARA DIBUJAR Y OTRA PARA RASTREAR COORDENADAS)
        '''
        self.bala = Manager_Bala(self.player,self.enemigos)
        
    def exportarJson(self):
        '''
        Guardar puntaje
        '''

    def armado_de_personaje(self):

        return Player(x=50,y=400,speed_walk=6,gravity=8,jump_power=30,frame_rate_ms=40,move_rate_ms=10,jump_height=110,vidas=5)
        
    def armado_de_enemigos(self):
        x=1
        cantidad=self.json["nivel_uno"][0]["Enemigo"]["lagarto"]["cantidad"]
        for crear in range(cantidad):
            if x < ANCHO_VENTANA-300:
                self.enemigos.append(Enemy_1 (50+x,50,9,10,12,20))
            else:
                if x == 1001:
                    x = 80
                elif x ==1080:
                    x = cantidad*3
            x+=250
        t=1
        for crear in range(self.json["nivel_uno"][0]["Enemigo"]["pork"]["cantidad"]):
            if t < ANCHO_VENTANA-300:
                self.enemigos.append(Enemy_02 (50+t,250,25,22,12))
            else:
                if t == 1001:
                    t=25
            t+=180
        
    def you_win(self,screen):
        
        if self.materiales.portal.habilitado:
            if self.player.rect_pick_up_collition.colliderect(self.materiales.portal.rect_colition):
                win = pygame.image.load("you win.jpg")
                win = pygame.transform.scale(win,(ANCHO_VENTANA,ALTO_VENTANA))
                screen.blit(win,win.get_rect())
                puntos = puntos.render("SCORE FINAL  {0} ".format(self.player.puntos),0,(200,200,200))
                screen.blit(puntos,(10,10))

    def you_lose(self,screen):

        if not(self.player.status_life):

            lose=pygame.image.load("game over.jpg")
            lose = pygame.transform.scale(lose,(ANCHO_VENTANA,ALTO_VENTANA))
            screen.blit(lose,lose.get_rect())
            puntos = puntos.render("SCORE  FINAL {0} ".format(self.player.puntos),0,(200,200,200))
            screen.blit(puntos,(10,10))
             
    def score(self,screen):
        '''LLeva la cuenta '''
        lifecont = pygame.font.Font(None,30)
        score = pygame.font.Font(None,30)
        life = lifecont.render("Vidas: {0}".format(self.player.vidas),0,(200,200,200))
        screen.blit(life,(1100,10))
        puntos = score.render("SCORE: {0}".format(self.player.puntos),0,(200,200,200))
        screen.blit(puntos,(10,10))

    # def pausa(self,screen):
    #     self.pause = Button(master=screen,x=0,y=0,w=100,h=100,color_background=None,color_border=None,image_background="C:/Users/Ares/Cursada Lab 1/set_gui_01/Data_Border/Buttons/settings.png", on_click = self.on_click_boton ,on_click_param="Sonido",text="Pausa",font="Castellar",font_size=25,font_color=RED)  
    #     self.lista_widget = [self.pause]
