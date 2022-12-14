import json

class Lector_json:

    def __init__(self,path):
        '''Recibe el path del json con la data del juego'''
        self.path= path
        self.diccionario = {}

    def importar_json(self):
            '''
            Trae el json con los datos del juego.
            Llamo a esta funcion en los archivos manager para obtener los parametros.
            '''
            with open(self.path,"r") as archivo:
                diccionario = json.load(archivo)
            return diccionario["Niveles"]


#Llevar estas 2 lineas al manager nivel!! y borrar el print+la duncion de abajo.
# print("Ejemplo: La data_lvl_one del personaje es",data_lvl_one["Nivel_uno"][0]["Player"])

# def importar_json(self):
#             '''
#             Trae el json con los datos del juego.
#             Llamo a esta funcion en los archivos manager para obtener los parametros.
#             '''
#             with open(self.path,"r") as archivo:
#                 diccionario = json.load(archivo)
#             return diccionario["Niveles"]