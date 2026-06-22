
#MainProgetto.py
#Creato da: Valentina Furlanis IN0501333

#Data: 15 maggio 2026

#Descrizione del file:
#il file server per utilizzare 

from MetodoArchimede import MetodoArchimede
from QuickSort import QuickSort
import time
print("Benvenuto nel progetto giochiamo con gli algoritmi!")
chiusura=False
while chiusura==False:
    try:
        print("Scegli quale algoritmo vuoi eseguire: \n1) Metodo di Archimede \n2) Quick Sort VS BubbleSort")
        scelta = int(input())
    except ValueError:
        print(f"Input non ammesso, sceglere uno degli indici elencati")
        continue

    if scelta == 1:
        print("Hai scelto il Metodo di Archimede")
        MetodoArchimede.main()
    elif scelta == 2:
        print("Hai scelto Quick Sort VS BubbleSort, che la sfida cominci!")
        print("Inserisci gli elementi dell'array separati da spazi:")
        array = list(map(int, input().split()))
        tempo_di_inizio_quicksort=time.time()
        QuickSort.quick_sort(array, 0, len(array) - 1)
        print(array)
        tempo_di_fine_quicksort=time.time()
        tempo_di_esecuzione_quick_sort = tempo_di_fine_quicksort - tempo_di_inizio_quicksort
        print(f"Quicksort ha impiegato: {tempo_di_esecuzione_quick_sort} secondi")
    else:
        print(f"l'opzione {scelta} non è in elenco")
    risposta = "s"                                                                              #inizializzazione della variabile per l'input dell'utente per giocare di nuovo
    try:
        print("Vuoi giocare di nuovo? (premi s per giocare nuovamente, un qualsiasi altro tasto per uscire)")     #stampa il messaggio per chiedere all'utente se vuole giocare di nuovo
        risposta_utente = input().lower()                                                       #lettura dell'input dell'utente e conversione in minuscolo
        risposta.index(risposta_utente)                                                         #lettura dell'input dell'utente
    except ValueError:                                                                          #gestione dell'eccezione se l'input dell'utente non è s, ciò significa che non vuole più giocare
        print("Grazie per aver giocato! Arrivederci!")                                          #stampa il messaggio di ringraziamento e arrivederci 
        chiusura=True