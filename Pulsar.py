#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from tkinter import *    #  python 3.
except:
    from Tkinter import *    #  python 2.7

import time  # módulo time    ver   diferencia con  " from time import * "
    
def main():

        #Crear y configurar ventana principal
        window = Tk()        
        window.title("Botones")
        window.geometry("400x400+0+0")  # ancho x alto + posicion x + posicion y
        #NOTA  print(window.config())   el método config() o configure() sin parámetros 
        #                               devuelve una lista con todas la propiedades de un widget
     
        
        #Widgets y Contenidos
        
        lbl = Label(window, text="PULSA")
        lbl.pack()  #Colocar y Mostrar widget
          
        def clicked():
            if lbl.cget('text') == "PULSA":  # cget('propiedad') leer el valor de una propiedad de un widget
                lbl.configure(text = "PULSADO")
            else:
                lbl.configure(text = "PULSA")                
              
        btn = Button(window, text = "PULSA", cursor = 'hand1' , activebackground="#11ff11" , command = clicked)
        btn.pack()  #Colocar y Mostrar widget

        def minimizando():
            window.iconify()   # minimizar ventana
            time.sleep(2)      # no hacer nada durante 2 segundos
            window.deiconify() # desminimizar
        
        btn2 = Button(window , text = 'Minimizar un rato' , command = minimizando)
        btn2.pack()  #Colocar y Mostrar widget
        
        #Bucle principal de la ventana 
        window.mainloop()
        
if __name__ == "__main__":       # averiguar si se está ejecutando o importando
        main()
