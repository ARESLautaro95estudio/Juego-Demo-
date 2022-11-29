from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar

class FormMenu_05(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)

        self.opciones = Button(master=self,x=495,y=205,w=150,h=50,color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton ,on_click_param = "Sonido" , text = "OPCIONES" ,font="Castellar",font_size=25,font_color=BLUE)
        self.back_option = Button(master = self,x=0,y=540,w=100,h=50, color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton ,on_click_param="Menu",text="BACK ",font="Castellar",font_size=25,font_color=RED)   
        self.lista_widget = [ self.back_option,self.opciones ]

    def on_click_boton(self, parametro):
        
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:  
            aux_widget.draw()

