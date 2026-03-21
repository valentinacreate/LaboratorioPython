#
#Esercizio 1.py
#
#Creato da Valentina Furlanis IN0501333
#Data:12 marzo 2026
#
#Descrizione di cosa fa il programma Esercizio 1.py:
#   L'utente inserisce un intero positivo
#   Viene verificato se esso è pari o dispari
#   Usando il numero scelto dall’utente, viene generata una lista seguendo questa regola: 
#       se il numero è pari, va diviso per 2; 
#       se è dispari, va moltiplicato per 3 e aggiunto 1.
#       Il processo va ripetuto finchè si arriva a 1 o la lista abbia piu’ di 100 numeri
#   La lista generata viene analizzata e vengono restituiti tre valori: 
#       il valore massimo raggiunto
#       la lunghezza della sequenza 
#       la somma di tutti i numeri
#   Vengono quindi stampati solo i numeri della sequenza che sono divisibili per 5
#       Se non ce ne sono, viene stampato un messaggio di avviso
#   Nel main program:
#       chiede all’inizio all’utente quanti numeri vuole testare. 
#       chiede all’utente i numeri da analizzare 
#       esegue le funzioni presenti per ogni numero. 
#   Alla fine stampa un riepilogo che mostri quale numero iniziale ha generato la sequenza più lunga.

def inserisci_numero():
    '''Inserimento numero'''
    
    n=int(input('Scrivi un numero intero positivo: '))          #chiedo all'utente di inserire un numero intero positivo
    while(n<=0):                                                #controllo che il numero inserito sia positivo                                             
        print('Errore: il valore inserito è < o = a 0')         #stampo messaggio di errore
        n=int(input('Scrivi un numero intero positivo: '))      #chiedo nuovamente all'utente di inserire un numero intero positivo
    return(n)                                                   #restituisco il numero inserito

def is_pari (n):
    '''Controllo se il numero inserito è pari'''

    return (n%2 == 0)                                           #restituisco True se il numero è pari, False se è dispari

def genera_lista(n):
    '''utilizzando il valore inserito genero una lista'''
  
    lista= []                                     #creo una lista vuota
    while (n>1 and len(lista)<100):               #continuo a generare numeri finchè n è maggiore di 1 e la lista ha meno di 100 numeri 
        if(n%2 == 0):                             #se n è pari, lo divido per 2    
            n=n/2
        else:                                     #se n è dispari, lo moltiplico per 3 e aggiungo 1    
            n=(n*3)+1

        lista.append(n)                           #aggiungo il numero generato alla lista
    return lista                                  #restituisco la lista generata

def analizza_sequenza(lista):
    '''riceve lista generata e restituisca tre valori: massimo, lunghezza sequenza e la somma di tutti i numeri'''
    
    massimo=max(lista)                                          #utilizzo la funzione max per trovare il massimo numero della lista
    lunghezza=len(lista)                                        #utilizzo la funzione len per trovare la lunghezza della lista    
    somma=sum(lista)                                            #utilizzo la funzione sum per trovare la somma di tutti i numeri della lista    
    tupla=(massimo, lunghezza, somma)                           #creo una tupla per salvare i tre valori da restituire
    return tupla                                                #restituisco i dati con una tupla

def ricerca(lista):
    '''scorre la lista e stampa solo i numeri della sequenza che sono divisibili per 5. Se non ce ne sono, stampa un messaggio dedicato'''
    
    k=0                                                                     #inizializzo una variabile contatore per contare quanti numeri della lista sono divisibili per 5
    print('I numeri dela sequenza che sono divisibili per 5 sono: ')        #stampo un messaggio per indicare che sto per stampare i numeri della lista che sono divisibili per 5
    for i in range(len(lista)):                                             #mediante un ciclo for scorro tutta la lista
        if(lista[i]%5==0):                                                  #mentre scorro la lista, controllo se il numero è divisibile per 5,
            print(lista[i])                                                 #se lo numero divisibile per 5, lo stampo
            k=k+1                                                           #se il numero è divisibile per 5, incremento il contatore di 1
    if(k==0):                                                               #se alla fine del ciclo for il contatore è ancora 0, significa che nella lista non ci sono numeri divisibili per 5
        print('Nella lista non ci sono numeri divisibiliper 5')             #stampo un messaggio di avviso per indicare che nella lista non ci sono numeri divisibili per 5
        

#inizio del main
#inizializzo due variabili per tenere traccia del numero che ha generato la lista più lunga (n_max) e della lunghezza massima della lista (len_max)
n_max=0
len_max=0
print('Quanti numeri vuoi testare? ')                       #chiedo all'utente quanti numeri vuole testare
n_test=int(input())                                         #leggo il numero di test che l'utente vuole fare
while(n_test<=0):                                           #controllo che il numero di test inserito sia positivo
    print('Errore: il valore inserito è < o = a 0')         #stampo un messaggio di errore
    n_test=int(input('Quanti numeri vuoi testare?   '))     #chiedo nuovamente all'utente di inserire un numero di test positivo

for i in range(n_test):                                     #mediante un ciclo for eseguo le funzioni per ogni numero che l'utente vuole testare    
    n=inserisci_numero()                                    #chiedo all'utente di inserire un numero intero positivo e lo leggo 
    print('Il numero inserito è pari?: ', is_pari(n))       #controllo se il numero inserito è pari o dispari e stampo il risultato
    lista=genera_lista(n)                                   #utilizzando il numero inserito genero una lista usando la funzione genera_lista e la salvo in una variabile
    print('La lista generata è: ', lista)                   #stampo la lista generata
    (massimo, lunghezza, somma)=analizza_sequenza(lista)    #analizzo la lista generata e restituisco il massimo, la lunghezza della sequenza e la somma di tutti i numeri
    print('Il massimo è: ', massimo)                        #restituisco il massimo numero della lista
    print('La lunghezza della sequenza è: ', lunghezza)     #restituisco la lunghezza della lista
    print('La somma di tutti i numeri è: ', somma)          #restituisco la somma di tutti i numeri della lista                      
    ricerca(lista)                                          #scorro la lista e stampo solo i numeri della sequenza che sono divisibili per 5, se non ce ne sono stampo un messaggio dedicato
    if(len(lista)>len_max):                                 #se la lunghezza della lista generata è maggiore della lunghezza massima finora registrata, aggiorno la lunghezza massima e il numero che ha generato la lista più lunga
        len_max=len(lista)
        n_max=n
print('il numero che ha generato lista di più lunga è: ', n_max)        #stampo il numero che ha generato la lista più lunga


