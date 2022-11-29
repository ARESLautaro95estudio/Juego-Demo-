from pygame.locals import *
from constantes_gui import *
from gui_form_menu_1 import FormMenu_01
from gui_form_menu_2 import FormMenu_02
from gui_form_menu_0 import Form_menu_0
from gui_form_menu_3 import FormMenu_03
from gui_form_menu_4 import FormMenu_04
from gui_form_menu_5 import FormMenu_05
from gui_form_menu_6 import FormMenu_06
from gui_form_menu_7 import FormMenu_07
from gui_widget import Widget
# ANCHO_VENTANA = 1200
# ALTO_VENTANA = 600
class Manager_do_formularios:
    '''
    Esto tiene que recibir screen,deltas,keys.
    Armar los formularios.
    Y llamar al nivel
    PERO POR SOBRE TODO TIENE QUE FUNCIONAR
    '''
    def __init__(self,screen,lvl_1):

        self.screen = screen
        self.lvl_one = lvl_1

        self.iniciador_de_levels()
        self.iniciador_de_formularios()

    def iniciador_de_formularios(self):
        #1
        self.start = Form_menu_0("Start" , self.screen, 0, 0, ANCHO_VENTANA, ALTO_VENTANA, None, None,image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg", active=True)
        #2
        self.menu = FormMenu_01 ("Menu" ,  self.screen , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False )
        #3
        self.level_opcion = FormMenu_02 ("Level" , self.menu.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)
        self.sonido = FormMenu_04 ("Sonido" , self.menu.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)
        #4
        self.opciones = FormMenu_03 ("Opciones" , self.menu.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(GREEN_PERS),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)
        self.salir = FormMenu_06 ("Salir", self.menu.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)
        #5 PAUSA DE NIVEL
        self.pausa = FormMenu_05 ("Pausa", self.menu.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)
        #
        #self.pause = Widget(self.screen,400,0,60,50,None,None,None,"PAUSA","CasteLlar",18,RED)
        
        self.nivel_uno = FormMenu_07("LEVEL_1",self.screen,x=ANCHO_VENTANA/2,y=0,w=90,h=40,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)

    def update(self,screen,delta_ms,keys,lista_eventos):

        if(self.menu.active):
            self.menu.update(lista_eventos)
            self.menu.draw()

        elif(self.level_opcion.active):   
            self.level_opcion.update(lista_eventos)
            self.level_opcion.draw()
        
        elif(self.start.active):
            self.start.update(lista_eventos)
            self.start.draw()

        elif(self.opciones.active):
            self.opciones.update(lista_eventos)
            self.opciones.draw()

        elif(self.sonido.active):
            self.sonido.update(lista_eventos)
            self.sonido.draw()

        elif(self.pausa.active):
            self.pausa.update(lista_eventos)
            self.pausa.draw()

        elif(self.salir.active):
            self.salir.update(lista_eventos)
            self.salir.draw()
            
        elif(self.nivel_uno.active):
            
            self.lvl_one.update(screen,delta_ms,keys,objetivos=0)
            self.nivel_uno.update(lista_eventos)
            self.nivel_uno.draw()
            #self.pause.draw()
            
            
        
    def iniciador_de_levels(self):
        self.lvl_one
    def draw(self):
        pass
