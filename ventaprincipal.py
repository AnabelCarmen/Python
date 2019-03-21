#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from tkinter import *    #  python 3.
except:
    from Tkinter import *    #  python 2.7    
def main():
        #Crear y configurar ventana principal
        window = Tk()         
        window.title("Welcome to Tkinter")
        window.geometry("400x400+0+0")  # ancho x alto + offset posicion x + offset posicion y
        window.update_idletasks()       # actualizar valor width y height
        ancho = window.winfo_width()    # conocer el ancho de la ventana
        alto = window.winfo_height()    # conocer el alto de la ventana
        print(ancho,alto) # print
        #Widgets y Contenidos 
        lbl = Label(window, text = "Hola mundo")
        lbl.config(font = ("Courier",44))  #      sinónimo         lbl.configure()
        lbl.config(fg = "#0000FF")        #  otra forma de modificar una propiedad
                                                         #  lbl[‘fg’] = “#0000FF”
                                                         #  NombreWidget[‘propiedad’] = valor
                                                         #  para leer una propiedad   variable = NombreWidget.cget(‘propiedad’) 
        lbl.pack()  #Colocar y Mostrar widget
        
        '''Opciones de posicionamiento:
                lbl.grid( column = 0, row = 0)        TABLA
                lbl.pack(     )                                    BLOQUES  
                lbl.place( x = 150,y = 200)              POSICIÓN x,y
        '''        
       
        window.mainloop()    #Bucle principal de la ventana      
if __name__ == "__main__":       # averiguar si se está ejecutando o importando
        main()
