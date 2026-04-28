#esercizio5.py
#Creato da Valentina Furlanis IN0501333

#Data:28 aprile 2026

#Descrizione dell’esercizio5.py:
#   - Trovate 10 soluzioni per il gioco delle regine con il metodo delle permutazioni: quanto è il tempo medio necessario a trovare una soluzione?
#   - Contate quanti tentativi fa il programma per trovare ogni soluzione del problema 8 regine
#   - Alcune soluzioni possono essere ripetute: fate in modo che le soluzioni siano “uniche”
#   - Se ci sono soluzioni ripetute, contate quante volte ogni soluzione è ripetuta
#   - Generalizzate il programma per risolvere una scacchiera di qualunque dimensione NxN
#Trovate quale è la scacchiera con lato N più grande possibile per cui si riesce a trovare 1 soluzione in meno di 15s
#Ogni soluzione è ‘simmetrica’ per rotazioni della scacchiera 8x8 di 90, 180 e 270 gradi. Scrivete delle funzioni che, una volta trovata una soluzione alla scacchiera, costruiscano le 4 soluzioni simmetriche per rotazione. Trovate 5 soluzioni “uniche” e le rispettive soluzioni simmetriche per rotazione per una scacchiera 8x8



def stessa_diagonale(x0, y0, x1, y1):
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"
    '''
    dy = abs(y1 - y0) 

    dx = abs(x1 - x0)   
    
    if dx==dy:
        return True
    else:
        return False

def incrocia_colonne(posizioni):
    '''Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna 
      delle posizioni delle regine precedenti 
    '''
    
    for c in range(len(posizioni)):  
        for j in range(c+1, len(posizioni)):   
            if stessa_diagonale(c, posizioni[c], j, posizioni[j]):
                return True 
    return False   

import random
import time
random_generator = random.Random()

print('Indicare la dimensione della scacchiera (NxN):')
dimensionescacchiera= int(input())
while dimensionescacchiera==2 or dimensionescacchiera==3:
    print('Non esistono soluzioni per una scacchiera di dimensione 2 o 3.')
    print('Inserire nuovamente la dimensione della scacchiera (NxN):')
    dimensionescacchiera= int(input())

print('inserire il numero di soluzioni desiderate:')
numerosoluzioni = int(input())

def soluzioni_da_dati(dimensionescacchiera, numerosoluzioni):
    lista_soluzione = list(range(dimensionescacchiera))
    soluzioni_uniche = set()
    soluzioni_trovate = 0
    tentativi = 0
    soluzioni_ripetute = 0
    start = time.perf_counter()

    while soluzioni_trovate < numerosoluzioni:
        random_generator.shuffle(lista_soluzione)
        tentativi += 1
        while incrocia_colonne(lista_soluzione):
            random_generator.shuffle(lista_soluzione)
            tentativi += 1


        if tuple(lista_soluzione) not in soluzioni_uniche:
            soluzioni_uniche.add(tuple(lista_soluzione))
            soluzioni_trovate += 1
            print(lista_soluzione)
        else:
            soluzioni_ripetute += 1
            if soluzioni_ripetute > numerosoluzioni * 10:  # Se ci sono troppe soluzioni ripetute, interrompiamo per evitare un loop infinito
                print("Troppe soluzioni ripetute, interrompo la ricerca.")
                break
        
    end = time.perf_counter()

    print(f"Tentativi totali: {tentativi}")
    print(f"Numero soluzioni che potevano essere ripetute: {soluzioni_ripetute}")
    print(f"Tempo medio per soluzione: {(end - start) / numerosoluzioni:.4f} secondi")

def dimensione_massima_per_tempo_limite(tempo_limite=15):
    N = 1
    while True:
        
        while True:
            start = time.perf_counter()
            soluzioni_da_dati(N+1, 1)  # Trova una soluzione per una scacchiera NxN
            end = time.perf_counter()       
        if (end - start) > tempo_limite:
            print(f"Tempo impiegato per dimensione {N+1}: {end - start:.4f} secondi")
            return N - 1  # Restituisce l'ultima dimensione che ha rispettato il limite di tempo
        N += 1
soluzioni_da_dati(dimensionescacchiera, numerosoluzioni)
print(f"La dimensione massima della scacchiera per trovare una soluzione in meno di 15 secondi è: {dimensione_massima_per_tempo_limite()}")
