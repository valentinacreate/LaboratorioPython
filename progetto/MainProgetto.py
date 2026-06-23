
#MainProgetto.py
#Creato da: Valentina Furlanis IN0501333

#Data: 15 maggio 2026

#Descrizione del file:
#il file server per utilizzare 

from MetodoArchimede import MetodoArchimede
from QuickSort import QuickSort
from MergeSort import MergeSort
from Conway import ConWay
import time

print("Benvenuto nel progetto 'Giochiamo con gli algoritmi!' ")
chiusura=False
while chiusura==False:
    try:
        print("\n ATTENZIONE: per ogni errore di digitazione si ritorna alla schermata di selezione")
        print("             per ogni interruzione da stastiera il gioco verrà chiuso")
        print("\nScegli quale algoritmo vuoi eseguire: \n1) Metodo di Archimede \n2) Quick Sort VS MergeSort \n3) Gioco della Vita di Conway")
        scelta = int(input())
    except ValueError:
        print(f"Input non ammesso, sceglere uno degli indici elencati")
        continue
    except KeyboardInterrupt:
        print("\nErrore, chiusura gioco")
        break

    if scelta == 1:
        print("\nHai scelto il Metodo di Archimede")
        print("Il seguente programma esegue l'algoritmo per il calcolo del pigreco, \nil calcolo avviene mediante l'utilizzo di due poligoni e una circonferenza, \nquest'ultima è inscritta ad un poligono e circostritta all'altro,")
        print("aumentando i lati del poligono la vicinanza tra i poligoni e circonferenza aumenta e l'approssimazione di pigreco migliora")
        MetodoArchimede.main()
    elif scelta == 2:
        print("\nHai scelto Quick Sort VS MergeSort, che la sfida cominci!")
        print("Entrambi sono algoritmi di ordinamento di un array che utizzano il metodo Divide et Impera con complessita O(nlogn)")
        print("QuickSort utilizza un pivot random e vengono confrontati tutti gli elementi dell'array con il pivot,\nsi generano così due sottoarray, uno con elementi minori del pivot l'altro con quelli maggiori, \niterando l'algoritmo in modo ricorsivo sui sottoarray ottengo l'array completo ordinato.")
        print("MergeSort suddivide l'arrray in sottoarray base per poi ricomporlo confrontando ogni singolo elemento\ndell'array di sinistra con quelli di destra, ottenendo così l'array completo")
        try:
            print("\nInserisci gli elementi dell'array separati da spazi:")
            array1 = list(map(int, input().split()))
        except ValueError:
            print("\nIl dato inserito non è corretto, usare un valore intero")
            continue
        except KeyboardInterrupt:
            print("\nErrore, chiusura gioco")
            break
        array2 = array1
        tempo_di_inizio_quicksort=time.time()
        QuickSort.quick_sort(array1, 0, len(array1) - 1)
        tempo_di_fine_quicksort=time.time()
        tempo_di_esecuzione_quick_sort = tempo_di_fine_quicksort - tempo_di_inizio_quicksort
        print(f"\nQuicksort ha impiegato: {tempo_di_esecuzione_quick_sort} secondi")
        print(array1)
        tempo_di_inizio_mergesort=time.time()
        MergeSort.merge_sort(array2, 0, len(array2) - 1)
        tempo_di_fine_mergesort=time.time()
        tempo_di_esecuzione_merge_sort = tempo_di_fine_mergesort - tempo_di_inizio_mergesort
        print(f"\nMergesort ha impiegato: {tempo_di_esecuzione_merge_sort} secondi")
        print(array2)
        if tempo_di_esecuzione_merge_sort > tempo_di_esecuzione_quick_sort:
            print(f"\nQuickSort ha vinto con una differenza nel tempo di esecuzione di {tempo_di_esecuzione_quick_sort - tempo_di_esecuzione_merge_sort} secondi")
        else:
            print(f"\nMergeSort ha vinto con una differenza nel tempo di esecuzione di {tempo_di_esecuzione_merge_sort - tempo_di_esecuzione_quick_sort} secondi")
    elif scelta == 3:
        print("\nHai scelto Il gioco della vita di Conway")
        print("Il Gioco della Vita di Conway è un automa cellulare ideato da John Conway.\nSi tratta di un modello semplice che simula l’evoluzione di celle su una griglia bidimensionale secondo regole specifiche, \nsenza intervento esterno dopo l’inizializzazione. Ogni cella può essere viva o morta (stato 1 o 0) \ne l’evoluzione avviene in turni (generazioni).")
        print("Regole del Gioco:")
        print("Sopravvivenza: Una cella viva con due o tre vicini vivi sopravvive alla generazione successiva.")
        print("Morte: Una cella viva con meno di due vicini vivi muore per solitudine; con più di tre vicini vivi muore per sovrappopolazione.")
        print("Nascita: Una cella morta con esattamente tre vicini vivi diventa viva.")
        print("La 'vicinanza' si calcola considerando le otto celle adiacenti orizzontalmente, verticalmente e diagonalmente.")
        
    else:
        print(f"\nL'opzione {scelta} non è in elenco")
    
    risposta = "s"                                                                              #inizializzazione della variabile per l'input dell'utente per giocare di nuovo
    try:
        print("\nVuoi giocare di nuovo? (premi s per giocare nuovamente, un qualsiasi altro tasto per uscire)")     #stampa il messaggio per chiedere all'utente se vuole giocare di nuovo
        risposta_utente = input().lower()                                                       #lettura dell'input dell'utente e conversione in minuscolo
        risposta.index(risposta_utente)                                                         #lettura dell'input dell'utente
    except ValueError:                                                                          #gestione dell'eccezione se l'input dell'utente non è s, ciò significa che non vuole più giocare
        print("Grazie per aver giocato! Arrivederci!")                                          #stampa il messaggio di ringraziamento e arrivederci 
        chiusura=True
    except KeyboardInterrupt:
        print("\nErrore, chiusura gioco")
        break