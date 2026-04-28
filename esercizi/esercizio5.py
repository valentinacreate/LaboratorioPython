
#esercizio5.py
#Creato da Valentina Furlanis IN0501333

#Data:28 aprile 2026

#Descrizione dell’esercizio5.py:
#Trovate 10 soluzioni per il gioco delle regine con il metodo delle permutazioni: quanto è il tempo medio necessario a trovare una soluzione?
#Contate quanti tentativi fa il programma per trovare ogni soluzione del problema 8 regine
#Alcune soluzioni possono essere ripetute: fate in modo che le soluzioni siano “uniche”
#Se ci sono soluzioni ripetute, contate quante volte ogni soluzione è ripetuta
#Generalizzate il programma per risolvere una scacchiera di qualunque dimensione NxN
#Trovate quale è la scacchiera con lato N più grande possibile per cui si riesce a trovare 1 soluzione in meno di 15s
#Ogni soluzione è ‘simmetrica’ per rotazioni della scacchiera 8x8 di 90, 180 e 270 gradi. Scrivete delle funzioni che, una volta trovata una soluzione alla scacchiera, costruiscano le 4 soluzioni simmetriche per rotazione. Trovate 5 soluzioni “uniche” e le rispettive soluzioni simmetriche per rotazione per una scacchiera 8x8

posizioni = [3, 6, 2, 7, 1, 4, 0, 5]

def stessa_diagonale(x0, y0, x1, y1):
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"
    '''
    # distanza lungo y
    dy = abs(y1 - y0) 

    # distanza lungo x
    dx = abs(x1 - x0)   
    
    # se dx == dy , dx/dy == 1 e sono sulla stessa diagonale, boolean expression
    return dx == dy

def incrocia_colonne(posizioni, col):
    '''Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna 
      delle posizioni delle regine precedenti 
    '''
    # controllo tutte le precedenti fino a questa 'col'
    for c in range(col):     
        # la coordinata X (la riga) è indice (c) 
        # la coordinata Y,(la colonna) è valore lista nell'indice (c)
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            # stop se trovo problemi
            return True  
    # nessun incrocio, la posizione va bene e NON incrocia altre colonne        
    return False   

incrocia_colonne(posizioni, 7)
# modulo
import random
# oggetto Random
random_generator = random.Random()
# lista da mescolare
lista_soluzione = list(range(8))
# permutazione casuale della lista soluzione
random_generator.shuffle(lista_soluzione)