import pygame
import sys
from pygame.locals import *
from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormMenu_03(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)

        self.sonido_up= Button(master=self,x=50,y=90,w=140,h=50,color_background=None,color_border=None,image_background="set_gui_01/Comic_Border/Elements/Element01s.png", on_click = self.on_click_boton1 ,on_click_param="SUBIR", text = " UP " ,font="Castellar",font_size=25,font_color = RED)
        self.sonido_down= Button(master=self,x=200,y=90,w=140,h=50,color_background=None,color_border=None,image_background="set_gui_01/Comic_Border/Elements/Element02s.png", on_click = self.on_click_boton1 ,on_click_param="BAJAR", text = " DOWN " ,font="Castellar",font_size=25,font_color = RED)
        
        self.salir = Button(master=self,x=0,y=120,w=140,h=50,color_background=None,color_border=None,image_background="set_gui_01/Comic_Border/Elements/Element03s.png", on_click = self.on_click_boton3 ,on_click_param="Start",text="SALIR ",font="Castellar",font_size=25,font_color=RED)        
        
        self.txt1 = TextBox(master=self,x=25,y=50,w=240,h=50,color_background=BLUE,color_border=None,image_background="set_gui_01/Comic_Border/Elements/Element04s.png",text="SCORE",font="Castellar",font_size=30,font_color=BLUE)
        self.pb1 = ProgressBar(master=self,x=500,y=50,w=240,h=50,color_background=None,color_border=None,image_background="set_gui_01/Comic_Border/Elements/Element05s.png",image_progress="C:/Users/Ares/Cursada Lab 1/Menu/Menu/Buttons/Achievements.png",value = 3, value_max=8)
        
        self.lista_widget = [self.sonido_up,self.sonido_down,self.salir,self.txt1,self.pb1]

    def on_click_boton1(self, parametro):
        self.pb1.value += 1
        self.set_active(parametro)

    def on_click_boton2(self, parametro):
        self.pb1.value -= 1
        self.set_active(parametro)
    
    def on_click_boton3(self, parametro):
        pygame.quit()
        sys.exit() 

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:  
            aux_widget.draw()