'''
FIle: turtle.py
Autore: valentinacreate
Data 12 marzo 2026
Descrizione: lo scopo è quello di disegnare su schermo, è stato eseguito su Trinket
'''
import turtle                   #importo il modulo turtle



def draw_rectangle(my_turtle,lunghezza,altezza):
  '''Disegno un rettangolo con la tartaruga''' #qusto tipo di stringa è importante per comprensione e portabilità del codice, 
#pass è una keeword che ci permette di definire funzione vuota senza che il codice dia errore
  for i in range(2): 
        my_turtle.forward(lunghezza)
        my_turtle.left(90)
        my_turtle.forward(altezza)
        my_turtle.left(90)
        
def draw_square(my_turtle, step):    #le funzioni le posso dichiarare dovunque io voglia nel codice
#my_turtle esiste solo alliniterno della funzione, sono variabili locali
    '''Disegno un quadrato con la tartaruga''' #Doc string: il commento multi linea esattamente posto sotto definizione di funzione  diventa una stringa di documentazione, quindi non è più trasparente nel codice ma crea codice
    '''   for i in [0,1,2,3]: #posso anche scrivere range(0, 4, 1),ma essendo 0 e 1 default posso ulterioremente demplificare con range(4)
    # le istruzioni dentro al 'blocco' da ripetere sono indentate
        my_turtle.forward(step)
        my_turtle.left(ang)  '''    
  #posso specializzare rettangolo rendendolo un quadrato chiamandolo nella funzione quadrato
  #risparmio così spazio
    draw_rectangle(my_turtle,step,step)
def somma (a, b) :      # header della funzione
  risultato = a + b   # risultato è variabile temporanea interna alla funzione
  return risultato    # restituisco risultato tramite la funzione
# fine della funzione, tutto ciò che metterò dopo all'interno della funzione verra' saltato
        
window = turtle.Screen()        #creo una finestra dove lavorare
window.bgcolor("lightgreen")    #aggiungo colore di sfondo

raffaello=turtle.Turtle()       #creo la prima tartaruga
raffaello.color('red')          #assegno un colore al percorso della tartaruga, mediante l'attributo colore

draw_square(raffaello,50) #ciamata della funzione
#assegno return ad una variabile altrimenti viene perso
ris=somma(7,6)

print(ris)
'''leonardo=turtle.Turtle()            #creo la seconda tartaruga
#voglio che faccia un percorso a forma di triangolo equilatero, attenzione ai gradi che inserisco for i in ['red', 'purple', 'BLUE']:
for i in ['red', 'purple', 'BLUE']:
  leonardo.color(i)
  leonardo.forward(50)      #sposto leonardo dal punto di partenza (che è lo stesso di raffaello) perchè non voglio che i 2 oercorsi si sormontino
  leonardo.forward(50)
  leonardo.left(120)'''
  
window.mainloop()           # Attende che l'utente chiuda la finestra di gioco o fermi il programma

#posso inserire il tutto dentro una funzione