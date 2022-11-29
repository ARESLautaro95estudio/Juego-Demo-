# import json
# import re
# from Objetos import *
# from Enemy_1 import *
# from player import *
# from bullet import *



# class Manager_nivel_uno:

#     def __init__(self):
#         self.lista_plataformas = []
#         self.lista_loot = []
#         self.lista_player = []
#         self.lista_enemigos = []
#         self.lista_muros = []
#         self.lista_techos = []
#         self.lista_DRAW = []
#         self.diccionario = {}
#         nivel_uno=False

#     def importar_json(self,path):

#         with open(path,"r") as archivo:
#             self.diccionario = json.load(archivo)
#         return self.diccionario["Niveles"]

#         #self.diccionario = importar_json(r"C:\Users\Ares\Cursada Lab 1\Game_End\datas.json")
        
#     def creador(self):

#         nivel_uno = diccionario["Nivel_uno"]

#         for elemento in nivel_uno:

#             if elemento["plataformas"]:

#                 x=0
#                 y=0

#                 for plat in range(elemento["plataformas"]["cantidad"]):
            
#                     lista_plataformas.append(Block_1((elemento["plataformas"]["pos_x"])+x, (elemento["plataformas"]["pos_y"])+y,40,50,(elemento["plataformas"]["tipo"]))) 
#                     self.lista_DRAW.append(Block_1((elemento["plataformas"]["pos_x"])+x, (elemento["plataformas"]["pos_y"])+y,40,50,(elemento["plataformas"]["tipo"]))) 
#                     x+=40
#                     y+=0 

#             if elemento["loot"]:

#                 x=0
#                 y=0

#                 for loot in range(elemento["loot"]["cantidad"]):
                    
#                     self.lista_loot.append(Fruit((elemento["loot"]["pos_x"]),(elemento["loot"]["pos_y"]),34,25,1))
#                     self.lista_DRAW.append(Fruit((elemento["loot"]["pos_x"]),(elemento["loot"]["pos_y"]),34,25,1))
#                     x+=30
#                     y+=150
            
#             if elemento["Player"]:

#                 for pj in range (elemento["Player"]["cantidad"]):  

#                     self.lista_player.append(Player((elemento["Player"]["pos_x"]),(elemento["Player"]["pos_y"]),10,12,13,80,30,150,5))    
#                     self.lista_DRAW.append(Player((elemento["Player"]["pos_x"]),(elemento["Player"]["pos_y"]),10,12,13,80,30,150,5))    
                    
#             if elemento  ["Enemigo"]:

#                 for enemigo in range (elemento["Enemigo"]["cantidad"]):

#                     self.lista_enemigos.append(Enemy_02((elemento["Enemigo"]["pos_x"])))
#                     self.lista_DRAW.append(Enemy_02((elemento["Enemigo"]["pos_y"])))

#             if elemento  ["Muros"]:
#                 x=0
#                 y=0
#                 for muros in range (elemento["Muros"]["cantidad"]):

#                     self.lista_muros.append(Block_1())
#                     self.lista_DRAW.append(Block_1())
#                     y+=40

#             if elemento  ["Techos"]:
#                 x=0
#                 y=0

#                 for techos in range (elemento["Techos"]["cantidad"]):

#                     self.lista_techos.append(Block_2()) 
#                     self.lista_DRAW.append(Block_2()) 
#                     x+=40
            


    
    
    
# game = Manager_nivel_uno()
# game.importar_json(r"C:\Users\Ares\Cursada Lab 1\Game_End\datas.json")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #print(lista_plataformas)


#     try :
#         if elemento["tipos"]=="decoracion":
#             print("Tengo ",elemento["cantidad"])   
#     except: 
#         if elemento["tipo"]=="Enemigo":
#             diccionario_de_enemigos=elemento
#             print("Enemigos",elemento["cantidad"])
#         elif elemento["tipo"]=="loot":
#             print(elemento["pos_x"])
#         elif elemento["tipo"]=="plataformas":
#             print(elemento["pos_x"])
    
#Enemigo = Enemy_1(diccionario_de_enemigos)

#print(diccionario_de_enemigos)
#print(nivel[0]["Enemigo"])
#print(nivel_uno[0]["plataforma"])


















































# class Bush_6:
#     def __init__(self,x,y):
#         self.stay = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/Ares/Cursada Lab 1/PROYECTO MARTES/CLASE_19_inicio_juego/CLASE_19_inicio_juego/images/tile/sheet1.png",8,8)[3:4]
#         self.frame=0
#         self.animation=self.stay
#         self.image= self.animation[self.frame]
#         self.rect=self.image.get_rect()
#         self.position = (x,y)
#         self.colision_detected = False

#     def draw(self,screen,):
#         self.image = self.animation[self.frame]     
#         screen.blit(self.image,self.position)
    
#     def colision(self,pos_x_y):

#         if self.rect.colliderect(pos_x_y):
#             self.colision_detected = True
