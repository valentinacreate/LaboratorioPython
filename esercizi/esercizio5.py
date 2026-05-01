
#esercizio5.py
#Creato da Valentina Furlanis IN0501333

#Data:28 aprile 2026

#Descrizione dell’esercizio5.py:
#   - Trovate 10 soluzioni per il gioco delle regine con il metodo delle permutazioni: quanto è il tempo medio necessario a trovare una soluzione?
#   - Contate quanti tentativi fa il programma per trovare ogni soluzione del problema 8 regine
#   - Alcune soluzioni possono essere ripetute: fate in modo che le soluzioni siano “uniche”
#   - Se ci sono soluzioni ripetute, contate quante volte ogni soluzione è ripetuta
#   - Generalizzate il programma per risolvere una scacchiera di qualunque dimensione NxN
#   - Trovate quale è la scacchiera con lato N più grande possibile per cui si riesce a trovare 1 soluzione in meno di 15s
#   - Ogni soluzione è ‘simmetrica’ per rotazioni della scacchiera 8x8 di 90, 180 e 270 gradi. Scrivete delle funzioni che, una volta trovata una soluzione alla scacchiera, costruiscano le 4 soluzioni simmetriche per rotazione. 
#   - Trovate 5 soluzioni “uniche” e le rispettive soluzioni simmetriche per rotazione per una scacchiera 8x8


import random                                                   #importo la libreria random per generare permutazioni casuali
import time                                                     #importo la libreria time per misurare il tempo impiegato a trovare le soluzioni
random_generator = random.Random()                              #creo un'istanza di random.Random() per generare numeri casuali

def stessa_diagonale(x0, y0, x1, y1):                           
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"'''
    dy = abs(y1 - y0)                                           #calcolo la differenza assoluta tra le coordinate y
    dx = abs(x1 - x0)                                           #calcolo la differenza assoluta tra le coordinate x               
    
    if dx==dy:                                                  #se la differenza tra le coordinate x è uguale alla differenza tra le coordinate y
        return True                                             #allora le posizioni sono sulla stessa diagonale, quindi ritorno True
    else:
        return False                                            #altrimenti non sono sulla stessa diagonale, quindi ritorno False   

def incrocia_colonne(posizioni):
    '''Ritorna Vero se due regine si trovano sulla stessa colonna o sulla stessa diagonale'''
    
    for c in range(len(posizioni)):                                             #itero su ogni regina della lista posizioni, dove c rappresenta la colonna e posizioni[c] rappresenta la riga
        for j in range(c+1, len(posizioni)):                                    #itero su ogni regina successiva alla regina c, dove j rappresenta la colonna, che parte da c+1 e posizioni[j] rappresenta la riga
            if stessa_diagonale(c, posizioni[c], j, posizioni[j]):              #chiamo la funzione stessa_diagonale per verificare se le regine si trovano sulla stessa diagonale
                return True                                                     #se due regine si trovano sulla stessa diagonale, allora ritorno True
    return False                                                                #se nessuna coppia di regine si trova sulla stessa colonna o sulla stessa diagonale, allora ritorno False

def soluzioni_da_dati_utente(dimensionescacchiera, numerosoluzioni):
    '''Dati i dati inseriti dall'utente, trovo le soluzioni ammissibili per il problema delle regine e stampo a video:
        - le soluzioni uniche trovate
        - il numero di tentativi totali per trovare le soluzioni
        - il numero di soluzioni che potevano essere ripetute
        - il tempo totale impiegato per trovare le soluzioni
        - il tempo medio per soluzione'''
    
    lista_soluzione = list(range(dimensionescacchiera))                     #creo una lista che rappresenta la soluzione, dove l'ordine in cui appaiono i valori rappresenta la riga e il valore rappresenta la colonna in cui si trova la regina
    soluzioni_uniche = set()                                                #creo un set per memorizzare le soluzioni uniche trovate, in modo da evitare di contare soluzioni duplicate
    soluzioni_trovate = 0                                                   #creo una variabile che funge da contatore per il numero di soluzioni uniche trovate
    tentativi = 0                                                           #creo una variabile che funge da contatore per il numero di tentativi totali per trovare le soluzioni
    soluzioni_ripetute = 0                                                  #creo una variabile che funge da contatore per il numero di soluzioni che potevano essere ripetute, ovvero quelle soluzioni che sono state generate ma erano già presenti nel set delle soluzioni uniche
    start = time.perf_counter()                                             #registro il tempo di inizio della ricerca delle soluzioni, in modo da poter calcolare il tempo totale impiegato alla fine della ricerca

    while soluzioni_trovate < numerosoluzioni:                              #continuo a cercare soluzioni finché il numero di soluzioni uniche trovate è inferiore al numero di soluzioni desiderate inserito dall'utente
        random_generator.shuffle(lista_soluzione)                           #genero una permutazione casuale della lista_soluzione, che rappresenta una possibile disposizione delle regine sulla scacchiera, e incremento il contatore dei tanativi totali
        tentativi += 1                                                      #incremento il contatore dei tentativi totali, per tenere traccia di quante permutazioni sono state generate 
        while incrocia_colonne(lista_soluzione):                            #verifico se la permutazione generata è una soluzione valida per l'algoritmo delle n regine
            random_generator.shuffle(lista_soluzione)                       #se la permutazione non è una soluzione valida, genero una nuova permutazione casuale 
            tentativi += 1                                                  #incremento il contatore dei tentativi totali

        if tuple(lista_soluzione) not in soluzioni_uniche:                                  #se la permutazione generata è una soluzione valida e non è già presente nel set delle soluzioni uniche
            soluzioni_uniche.add(tuple(lista_soluzione))                                    #aggiungo la soluzione al set delle soluzioni uniche, convertendo la lista in una tupla per poterla memorizzare nel set
            soluzioni_trovate += 1                                                          #incremento il contatore delle soluzioni uniche trovate, per tenere traccia di quante soluzioni uniche sono state generate
            print(f"\nSoluzione {soluzioni_trovate}:\n{lista_soluzione}")                   #stampo a video la soluzione trovata, indicando il numero della soluzione trovata 
            print(f"\nSoluzioni per rotazione della scacchiera con la soluzione {soluzioni_trovate}:")          
            rotazione_90_gradi(lista_soluzione)                                             #chiamo la funzione rotazione_90_gradi per stampare la soluzione ruotata di 90 gradi in senso orario
            rotazione_180_gradi(lista_soluzione)                                            #chiamo la funzione rotazione_180_gradi per stampare la soluzione ruotata di 180 gradi in senso orario
            rotazione_270_gradi(lista_soluzione)                                            #chiamo la funzione rotazione_270_gradi per stampare la soluzione ruotata di 270 gradi in senso orario

        else:
            soluzioni_ripetute += 1                                                         #se la permutazione generata è una soluzione valida ma è già presente nel set delle soluzioni uniche, incremento il contatore delle soluzioni che potevano essere ripetute, per tenere traccia di quante soluzioni duplicate sono state generate
            if soluzioni_ripetute > numerosoluzioni * 10:                                   #se ci sono troppe soluzioni ripetute, interrompiamo per evitare un loop infinito
                print("Troppe soluzioni ripetute, interrompo la ricerca.")                  #avviso l'utente che ci sono troppe soluzioni ripetute e interrompo la ricerca, per evitare un loop infinito in cui vengono generate solo soluzioni duplicate senza trovare nuove soluzioni uniche
                break
        
    end = time.perf_counter()                                                               #registro il tempo di fine della ricerca delle soluzioni, in modo da poter calcolare il tempo totale impiegato alla fine della ricerca

    print(f"\nTentativi totali: {tentativi}")                                               #stampo il numero di tentativi totali per trovare le soluzioni, che corrisponde al numero di permutazioni generate durante la ricerca
    print(f"Numero soluzioni che potevano essere ripetute: {soluzioni_ripetute}")           #stampo il numero di soluzioni che potevano essere ripetute
    print(f"Tempo totale: {end - start:.4f} secondi")                                       #stampo il tempo totale impiegato per trovare le soluzioni, cioè la differenza tra il tempo di fine e il tempo di inizio della ricerca
    print(f"Tempo medio per soluzione: {(end - start) / numerosoluzioni:.4f} secondi")      #stampo il tempo medio per soluzione, calcolato come il tempo totale diviso per il numero di soluzioni uniche trovate, 
                                                                                            #così da avere un'indicazione del tempo medio per trovare una soluzione unica

def dimensione_massima_per_tempo_limite():
    '''Trova la dimensione massima della scacchiera per cui si riesce a trovare una soluzione in meno di 15 secondi'''
    tempo_limite = 15                                                                       #definisco il tempo limite in secondi, che rappresenta il tempo massimo che vogliamo impiegare per trovare una soluzione
    N = 4                                                                                   #partiamo da 4, poiché per N=2 e N=3 non esistono soluzioni
    start = time.perf_counter()                                                             #registro il tempo di inizio della ricerca della soluzione               
    lista_soluzione = list(range(N))                                                        #creo una lista che rappresenta la soluzione, dove l'ordine degli elementi rappresenta la riga e il valore rappresenta la colonna in cui si trova la regina

    while incrocia_colonne(lista_soluzione):                                                #verifico se la soluzione iniziale è valida 
        random_generator.shuffle(lista_soluzione)                                           #se non lo è genero permutazioni casuali finché non trovo una soluzione valida
    end = time.perf_counter()                                                               #registro il tempo di fine della ricerca della soluzione, in modo da poter calcolare il tempo impiegato per trovare la soluzione    
    print(f"\nTempo impiegato per dimensione {N}:{end - start:.4f} secondi")                #stampo il tempo impiegato per trovare una soluzione valida
    #la stampa a video è utile per avvisare l'utente che la ricerca sta procedendo, soprattutto per dimensioni più grandi della scacchiera, dove la ricerca potrebbe richiedere più tempo, così da evitare che l'utente pensi che il programma si sia bloccato
    
    while (end - start) < tempo_limite:                                                     #se il tempo impiegato è < di 15s
        start = time.perf_counter()                                                         #registro il tempo di inizio della ricerca della soluzione per la dimensione successiva      
        N += 1                                                                              #incremento la dimensione della scacchiera di 1
        lista_soluzione = list(range(N))                                                    #creo una nuova lista per la scacchiera con la nuova dimensione
        while incrocia_colonne(lista_soluzione):                                            #verifico se la soluzione iniziale è valida per la nuova dimensione della scacchiera
            random_generator.shuffle(lista_soluzione)                                       #se non lo è genero permutazioni casuali finché non trovo una soluzione valida per la nuova dimensione della scacchiera
        end = time.perf_counter()                                                           #registro il tempo di fine della ricerca della soluzione per la nuova dimensione
        print(f"Tempo impiegato per dimensione {N}:{end - start:.4f} secondi")              #stampo il tempo impiegato per trovare una soluzione valida per la nuova dimensione della scacchiera
        if (end - start) >= tempo_limite:                                                   #se il tempo impiegato per trovare una soluzione valida per la nuova dimensione è >= al tempo limite
            #avviso l'utente che il tempo ha superato il limite per la nuova dimensione della scacchiera
            print(f"\nIl tempo ha superato il limite di {tempo_limite} secondi per dimensione {N}.") 
            #stampo la dimensione massima della scacchiera con cui è stata trovata una soluzione in meno di 15 secondi                                       
            print(f"La dimensione massima della scacchiera per trovare una soluzione in meno di {tempo_limite} secondi è: {N - 1}")         
            break                                                                           #interrompo la ricerca, poiché abbiamo trovato la risposta alla domanda

def rotazione_90_gradi(soluzione):
    '''Ritorna la soluzione ruotata di 90 gradi in senso orario'''
    print('Rotazione di 90 gradi: ')                                           #avviso che successivamente verrà stampata la soluzione ruotata di 90 gradi in senso orario
    soluzione90=[0]*len(soluzione)                                             #inizializzo una lista vuota per memorizzare la soluzione 
    for r, c in enumerate(soluzione):                                          #itero su ogni elemento della soluzione, dove r rappresenta la riga e c rappresenta la colonna in cui si trova la regina, la funzione enumerate mi permette di ottenere sia l'indice r che il valore c per ogni elemento della soluzione
        soluzione90[c] = (len(soluzione)-1)-r                                  
        #con una rotazione di 90 gradi in senso orario, colonne e righe si scambiano, 
        #   quindi la regina che era alla riga r e colonna c, dopo la rotazione sarà alla riga c e colonna n-1-r, dove n è la dimensione della scacchiera
    print(soluzione90)                                                         #stampo a video la soluzione 

def rotazione_180_gradi(soluzione):
    '''Ritorna la soluzione ruotata di 180 gradi in senso orario'''
    print('Rotazione di 180 gradi: ')                                       #avviso che successivamente verrà stampata la soluzione ruotata di 180 gradi in senso orario
    n=len(soluzione)                                                        #calcolo la dimensione della scacchiera
    soluzione180 = [0] * n                                                  #inizializzo una lista vuota per memorizzare la soluzione             
    for col in range(n):                                                    #itero su ogni colonna della soluzione, dove col rappresenta la colonna in cui si trova la regina
        soluzione180[(n-1) - col] = (n-1) - soluzione[col]                  
        #soluzione180[(n-1) - col]: Assegna la regina alla nuova colonna 
        #   (se era in colonna col, dopo una rotazione di 180 gradi sarà in colonna n-1-col)
        #soluzione[col]: Recupera il valore della riga dove si trova la regina nella colonna col
        #(n-1) - soluzione[col]: Calcola la nuova riga dopo la rotazione,
        #   (se la regina era alla riga r, dopo una rotazione di 180 gradi sarà alla riga n-1-r)
    print(soluzione180)                                                     #stampo a video la soluzione ruotata di 180 gradi in senso orario

def rotazione_270_gradi(soluzione):
    '''Ritorna la soluzione ruotata di 270 gradi in senso orario'''
    print('Rotazione di 270 gradi: ')                                       #avviso che successivamente verrà stampata la soluzione ruotata di 270 gradi in senso orario
    soluzione270=[0]*len(soluzione)                                         #inizializzo una lista vuota per memorizzare la soluzione
    for r,c in enumerate(soluzione):                                        #itero su ogni elemento della soluzione, dove r rappresenta la riga e c rappresenta la colonna in cui si trova la regina
        soluzione270[(len(soluzione)-1)-c]=r                                
        #con una rotazione di 270 gradi in senso orario, colonne e righe si scambiano, come se la scacchiera venisse ruotata di 90 gradi in senso antiorario,
        #   quindi la regina che era alla riga r e colonna c, dopo la rotazione sarà alla riga n-1-c e colonna r, dove n è la dimensione della scacchiera
    print(soluzione270)                                                     #stampo a video la soluzione ruotata di 270 gradi in senso orario

def main():
    '''Funzione principale main'''

    print('Indicare la dimensione della scacchiera (NxN):')                         #chiedo all'utente di inserire la dimensione della scacchiera
    dimensionescacchiera= int(input())                                              #memorizzo la dimensione della scacchiera inserita dall'utente in una variabile di tipo intero

    while dimensionescacchiera==2 or dimensionescacchiera==3:                       #se la dimensione della scacchiera è 2 o 3
        print('Non esistono soluzioni per una scacchiera di dimensione 2 o 3.')     #avviso l'utente che non esistono soluzioni per una scacchiera di dimensione 2 o 3
        print('Inserire nuovamente la dimensione della scacchiera (NxN):')          #chiedo nuovamente all'utente di inserire la dimensione della scacchiera, finché non viene inserita una dimensione valida (diversa da 2 e 3)
        dimensionescacchiera = int(input())                                         #memorizzo la dimensione della scacchiera inserita dall'utente in una variabile di tipo intero

    print('inserire il numero di soluzioni desiderate:')                            #chiedo all'utente di inserire il numero di soluzioni desiderate
    numerosoluzioni = int(input())                                                  #memorizzo il numero di soluzioni desiderate inserito dall'utente in una variabile di tipo intero

    soluzioni_da_dati_utente(dimensionescacchiera, numerosoluzioni)                 #chiamo la funzione soluzioni_da_dati_utente, passando come argomenti i dati inseriti dall'utente
    dimensione_massima_per_tempo_limite()                                           #chiamo la funzione dimensione_massima_per_tempo_limite per trovare la dimensione massima della scacchiera per cui si riesce a trovare una soluzione in meno di 15 secondi
    print("\nSoluzioni uniche e rispettive soluzioni simmetriche per rotazione per una scacchiera 8x8:\n")
    soluzioni_da_dati_utente(8, 5)                                                  #chiamo la funzione soluzioni_da_dati_utente, passando come argomenti la dimensione della scacchiera (8) e il numero di soluzioni desiderate (5), per trovare 5 soluzioni uniche e le rispettive soluzioni simmetriche per rotazione per una scacchiera 8x8

main()