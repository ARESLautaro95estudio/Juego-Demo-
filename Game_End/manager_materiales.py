from Objetos_actual import Fruit
from Objetos_actual import Portal
from Objetos_actual import Skull
from Objetos_actual import Bush_1

class Materiales:

    #, decoraciones_x,decoraciones_y,decoraciones_cantidad
    def __init__(self,loot_x,loot_y,loot_cantidad,portal_x,portal_y):
        '''
        Crea una lista para todos los objetos que cree y establece los parametros recibidos del json como props.
        '''
        self.lista_materiales = []
        
        self.loot_x = loot_x
        self.loot_y = loot_y
        self.loot_cantidad = loot_cantidad
       
        self.porta_x = portal_x
        self.porta_y = portal_y
        
        self.lista_loot= []
        self.lista_portal= []

        # self.decoraciones_x = decoraciones_x
        # self.decoraciones_y = decoraciones_y
        # self.decoraciones_cantidad = decoraciones_cantidad

        self.crea_loot()
        self.crea_portal()
        #self.crea_decoraciones()
           
    def crea_loot(self):
        '''
        Crea objetos loot con parametros de json y los agrega a la lista materiales
        '''
        x=30
        y=150

        for loot  in range(self.loot_cantidad):

            if loot < 4:

                self.lista_materiales.append(Fruit(self.loot_x+x,self.loot_y+y,34,25,1))
                self.lista_loot.append(Fruit(self.loot_x+x,self.loot_y+y,34,25,1))
                x+=50

            if loot > 4 and  6 < loot:            
                self.lista_materiales.append(Fruit(self.loot_x+x,self.loot_y+y+80,34,25,1))
                self.lista_loot.append(Fruit(self.loot_x+x,self.loot_y+y+200,34,25,1))
                x+=50

    def crea_portal(self):
        '''
        Crea objetos loot con parametros de json y los agrega a la lista materiales
        '''
        self.lista_materiales.append(Portal(self.porta_x,self.porta_y))
        self.lista_portal.append(Portal(self.porta_x,self.porta_y))
        self.portal = Portal(self.porta_x,self.porta_y)

     
    def update(self,pos_x_y):
        '''
        Llama a las funciones que crean objetos para obtener la lista final del objeto Materiales
        '''
        # for material in self.lista_materiales:
            
        #     material.draw()

        for loot in self.lista_loot:
            
            loot.colision(pos_x_y)


    # self.lista_loot.append(Portal(self.porta_x,self.porta_y))
    #self.crea_decoraciones()
    # def crea_decoraciones(self):
    #     '''
    #     Crea objetos loot con parametros de json y los agrega a la lista materiales
    #     '''
    #    for decoraciones  in range(self.decoracion_cantidad):
    #       self.lista_materiales.append(Skull())
    #   for decoraciones  in range(self.decoracion_cantidad):
    #           self.lista_materiales.append(Bush_1())