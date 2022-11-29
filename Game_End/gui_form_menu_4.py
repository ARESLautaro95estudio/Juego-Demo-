from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar

class FormMenu_04(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)

        #self.niveles= Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="C:/Users/Ares/Cursada Lab 1/Menu/Menu/Buttons/Achievements.png", on_click = self.on_click_boton1 ,on_click_param="Level", text = " Sonido " ,font="Stencil",font_size=25,font_color = RED)
        self.low_sound = Button(master = self, x=353,y=200,w=140,h=50, color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton ,on_click_param="Menu", text = "DOWN -" ,font="Castellar",font_size=25,font_color=BLUE)
        self.up_sound = Button(master = self, x=740,y=200,w=140,h=50, color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton ,on_click_param="Menu",text="UP ",font="Castellar",font_size=25,font_color=RED)        
        self.back_option = Button(master = self,x=0,y=540,w=100,h=50, color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton ,on_click_param="Menu",text="BACK ",font="Castellar",font_size=25,font_color=RED)        
        self.reanudar =Button(master = self,x=40,y=40,w=100,h=50, color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton ,on_click_param="LEVEL_1",text="REANUDAR ",font="Castellar",font_size=10,font_color=RED)  
        self.soudn_text = TextBox(master = self, x=500,y=120,w=240,h=50, color_background=BLUE,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png",text="SONIDO",font="Castellar",font_size=30,font_color=GREEN)
              
        #self.pb1 = ProgressBar(master=self,x=200,y=20,w=240,h=50,color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png",image_progress="C:/Users/Ares/Cursada Lab 1/Menu/Menu/Buttons/Achievements.png",value = 3, value_max=8)
        #self.niveles,self.soudn_text,self.pb1
        self.lista_widget = [self.back_option,self.up_sound,self.low_sound,self.soudn_text,self.reanudar ]

    def on_click_boton(self, parametro):
        
        self.set_active(parametro)
    
    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:  
            aux_widget.draw()