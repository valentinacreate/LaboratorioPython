'''
FIle: turtle.py
Autore: valentinacreate
Data 3 marzo 2026
Descrizione: lo scopo è quello di disegnare su schermo, è stato eseguito su Trinket
'''
import turtle                   #importo il modulo turtle
window = turtle.Screen()        #creo una finestra dove lavorare
window.bgcolor("lightgreen")    #aggiungo colore di sfondo

raffaello=turtle.Turtle()       #creo la prima tartaruga
raffaello.color('red')          #assegno un colore al percorso della tartaruga, mediante l'attributo colore
#primo metodo per far muovere la tartaruga:
#voglio che faccia un percorso che è un quadrato
'''
raffaello.forward(50)           # Dico a "raffaello" di andare avanti di 50 passi
raffaello.left(90)              # Dico a "raffaello" di GIRARE a sinistra di 90 gradi
raffaello.forward(50)
raffaello.left(90)
raffaello.forward(50)
raffaello.left(90)
raffaello.forward(50)
raffaello.left(90)
'''
#secondo metodo per muovere la tartaruga:
#(più compatto e chiaro), utilizza i loop control
for i in [0,1,2,3]: #posso anche scrivere range(0, 4, 1),ma essendo 0 e 1 default posso ulterioremente demplificare con range(4)
    # le istruzioni dentro al 'blocco' da ripetere sono indentate
  raffaello.forward(50)
  raffaello.left(90)

#è valida una qualsiasi sequenza di 4 elementi:
#se vogliamo che ogni lato sia colorato:
'''
for i in ['red', 'purple', 'yellow', 'blue']:
  raffaello.color(i)
  raffaello.forward(50)
  raffaello.left(90)
'''  
  
leonardo=turtle.Turtle()            #creo la seconda tartaruga
#voglio che faccia un percorso a forma di triangolo equilatero, attenzione ai gradi che inserisco 
#primo metodo per far muovere la tartaruga:
'''
leonardo.forward(60)
leonardo.left(120)
leonardo.forward(60)
leonardo.left(120)
leonardo.forward(60)
leonardo.left(120)
leonardo.forward(60)
'''
#secondo metodo per far muovere la tartaruga:
#mediante l'utilizzo di loop control
'''
for i in [0,1,2]:
  leonardo.forward(50)
  leonardo.forward(50)
  leonardo.left(120)
'''
for i in ['red', 'purple', 'BLUE']:
  leonardo.color(i)
  leonardo.forward(50)      #sposto leonardo dal punto di partenza (che è lo stesso di raffaello) perchè non voglio che i 2 oercorsi si sormontino
  leonardo.forward(50)
  leonardo.left(120)
  
window.mainloop()           # Attende che l'utente chiuda la finestra di gioco o fermi il programma

#posso inserire il tutto dentro una funzione
