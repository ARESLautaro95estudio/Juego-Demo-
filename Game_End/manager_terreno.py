from Objetos_actual import *

class Terreno:

    '''
    Es un objeto que crea una lista de objetos que forman parte del escenario. (No inlcuye objetos que interactuen mas alla de una coision)
    '''

    def __init__(self,plataformas_x,plataformas_y,plataformas_cantidad,muros_x,muros_y,muros_cantidad,techos_x,techos_y,techos_cantidad,screen):
        
        '''
        Props recibidas de un json 
        '''       
        self.plataformas_x = plataformas_x
        self.plataformas_y = plataformas_y
        self.plataformas_cantidad = plataformas_cantidad 
        self.muros_x = muros_x
        self.muros_y = muros_y
        self.muros_cantidad = muros_cantidad
        self.techos_x = techos_x
        self.techos_y = techos_y
        self.techos_cantidad = techos_cantidad
        self.screen = screen
        self.lista_terreno=[]
        self.muros_lista = []
        self.techos_lista = []
        self.plataformas_lista = []

        self.crea_muros()
        self.crea_techos()
        self.crea_plataforma()

    def crea_plataforma(self):
        '''
        Crea objetos con parametros recibidos de un json y los adiere a una lista final
        '''
        x=0
        for i in range(self.plataformas_cantidad):
            if i <= 2 :
                self.lista_terreno.append(Block_1(625, 419,40,50,1))
                self.plataformas_lista.append(Block_1(625, 419,40,50,1))
                self.lista_terreno.append(Block_1(508, 504,40,50,1))
                self.plataformas_lista.append(Block_1(508, 504,40,50,1))
            if i <= 6 :  
                self.lista_terreno.append(Block_1(10+x,400,40,50,1))        
                self.plataformas_lista.append(Block_1(10+x,400,40,50,1))        
            if i <= 7 :
                self.lista_terreno.append(Block_1(14+x,200,40,50,1))                 
                self.plataformas_lista.append(Block_1(14+x,200,40,50,1))                 
            if i <=5 :
                self.lista_terreno.append(Platform(950+x,220,50,50,1))  
                self.plataformas_lista.append(Platform(950+x,220,50,50,1))  
            if i <=10 :
                self.lista_terreno.append(Platform(480+x,300,50,50,6))   
                self.plataformas_lista.append(Platform(480+x,300,50,50,6))   
            x+=40
        self.lista_terreno.append(Block_1(350,380,40,50,1))
        self.plataformas_lista.append(Block_1(350,380,40,50,1))
        self.lista_terreno.append(Block_1(390,380,40,50,1))
        self.plataformas_lista.append(Block_1(390,380,40,50,1))
        self.lista_terreno.append(Block_1(390,280,40,50,1))
        self.plataformas_lista.append(Block_1(390,280,40,50,1))

    def crea_muros(self):
        '''
        Crea objetos con parametros recibidos de un json y los adiere a una lista final
        '''
        y=0
        for i in range(self.muros_cantidad):
            if i < 13:
                self.lista_terreno.append(Techos(self.muros_x,self.muros_y+y,40,50,25))
                self.muros_lista.append(Techos(self.muros_x,self.muros_y+y,40,50,25))
            if i < 26:
                self.lista_terreno.append(Techos(1160+self.muros_x,self.muros_y+y,40,50,25))
                self.muros_lista.append(Techos(1160+self.muros_x,self.muros_y+y,40,50,25))
            y += 50

    def crea_techos(self):
        '''
        Crea objetos con parametros recibidos de un json y los adiere a una lista final
        '''
        y=0
        x=0
        for i in range(self.techos_cantidad):
            self.lista_terreno.append(Techos(self.techos_x+x,self.techos_y,40,10,25))
            self.techos_lista.append(Techos(self.techos_x+x,self.techos_y,40,10,25))
            x+=40

    def update(self):
        '''
        Llama a las funciones que crean objetos para obtener la lista final del objeto Terreno
        '''
        for terreno in self.lista_terreno:
            terreno.draw(self.screen)

        