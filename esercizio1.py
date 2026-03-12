#
#Esercizio 1
#
#Creato da Valentina Furlanis IN0501333
#Data:12 marzo 2026
#
#Descrizione:
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
    
    n=int(input('Scrivi un numero intero positivo: '))
    while(n<=0):
        if (n<=0):
            print('Errore: il valore inserito è < o = a 0')
            n=int(input('Scrivi un numero intero positivo: '))
    return(n)

def is_pari (n):
    '''Controllo se il numero inserito è pari'''

    return (n%2 == 0)

def genera_lista(n):
    '''utilizzando il valore inserito genero una lista'''
  
    lista= []
    while (n>1 and len(lista)<100):
        if(n%2 == 0):
            n=n/2
        else:
            n=(n*3)+1
        
        lista.append(n)
    return lista

def analizza_sequenza(lista):
    '''riceve lista generata e restituisca tre valori: massimo, lunghezza sequenza e la somma di tutti i numeri'''
    
    massimo=max(lista)
    lunghezza=len(lista)
    somma=sum(lista)
    print('Il massimo è: ', massimo)
    print('La lunghezza della sequenza è: ', lunghezza)
    print('La somma di tutti i numeri è: ', somma)

def ricerca(lista):
    '''scorre la lista e stampa solo i numeri della sequenza che sono divisibili per 5. 
    Se non ce ne sono, stampa un messaggio dedicato'''
    
    k=0
    print('I numeri dela sequenza che sono divisibili per 5 sono: ')
    for i in range(len(lista)):
        if(lista[i]%5==0):
            print(lista[i])
            k=k+1
    if(k==0):
        print('Nella lista non ci sono numeri divisibiliper 5')
        

#inizio del main
n_max=0 
n_len_max=0
print('Quanti numeri vuoi testare? ')
n_test=int(input())
while(n_test<=0):
    if (n_test<=0):
        print('Errore: il valore inserito è < o = a 0')
        n_test=int(input('Quanti numeri vuoi testare?   '))

for i in range(n_test):
    n=inserisci_numero()
    print('Il numero inserito è pari?: ', is_pari(n))
    lista=genera_lista(n)
    print('La lista generata è: ', lista)
    analizza_sequenza(lista)
    ricerca(lista)
    if(len(lista)>n_max):
        n_max=len(lista)
        n_len_max=n
print('il numero che ha generato lista di più lunga è: ', n_len_max)


