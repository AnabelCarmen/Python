#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from tkinter import *    #  python 3.
except:
    from Tkinter import *    #  python 2.7    
def main():

        #Crear y configurar ventana principal
        window = Tk() 
        window.title("Entry")         
        #window.geometry('500x150')  # Si queremos un tamaño determinado de ventana

        #widgets
        titulo = Label(window, text="CÁLCULO DEL INDICE DE MASA CORPORAL") 
        titulo.grid(row=0,column=0)
        
        #Primer número 
        lbl_1 = Label(window, text=" Peso en kg")         
        lbl_1.grid(column=0, row=1)  
        numero_1 = Entry(window,width=10) # Introducir Primer número       
        numero_1.insert(0,0) # Colocar un cero como valor inicial en la primera posición
        numero_1.grid(column=1, row=1) 
         
        #Segundo número
        lbl_2 = Label(window, text="Altura en metros")         
        lbl_2.grid(column=0, row=2)
        numero_2 = Entry(window,width=10) # Introducir Segundo número   
        numero_2.insert(0,0) # Colocar un cero como valor inicial en la primera posición     
        numero_2.grid(column=1, row=2) 
         
        #Resultado
        label_resultado = Label(window, text='IMC')
        label_resultado.grid(column=0, row=3)
        resultado = Label(window, text='')
        resultado.grid(column=1, row=3)
        
        # FUNCION que realiza el cálculo,  es llamada por el BOTON 'calcular'  con     'command=media'
        def media():
            try:  # Comprobar que los números introducidos son válidos y no son letras
                n1= float( numero_1.get() .replace(",",".") )
                n2= float( numero_2.get() .replace(",",".") )
                solucion = float(  n1  / n2**2)      
                resultado.config(text = solucion) # Modificar el contenido del label 'resultado'
            except:
                resultado.config(text ='Debe introducir números válidos')
            
        #Botón que llama a la función 'media' definida arriba         
        calcular = Button(window,text='Calcular IMC',command=media)
        calcular.grid(column=0, row=4)        

        window.mainloop()  #Bucle principal de la ventana         
 
if __name__ == "__main__":       # averiguar si se está ejecutando o importando
        main()
