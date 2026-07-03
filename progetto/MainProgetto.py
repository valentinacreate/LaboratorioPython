
#MainProgetto.py
#Creato da: Valentina Furlanis IN0501333

#Data: 15 maggio 2026

#Descrizione del file:
#Il seguente programma permette di eseguire 3 algoritmi diversi, selezionabili dall'utente:
#1) Metodo di Archimede: calcolo del pi-greco
#2) QuickSort VS MergeSort
#3) Gioco della Vita di Conway

from MetodoArchimede import MetodoArchimede                                 #importazione della classe MetodoArchimede dal file MetodoArchimede.py
from QuickSort import QuickSort                                             #importazione della classe QuickSort dal file QuickSort.py
from MergeSort import MergeSort                                             #importazione della classe MergeSort dal file MergeSort.py
from Conway import ConWay                                                   #importazione della classe Conway dal file Conway.py
import time                                                                 #importo la libreria time per misurare il tempo impiegato a trovare le soluzioni

print("Benvenuto nel progetto 'Giochiamo con gli algoritmi!' ")
chiusura = False
while chiusura == False:
    try:                                                                    #esecuzione del blocco di codice per la selezione dell'algoritmo da eseguire che potrebbe generare un'eccezione
        print("\n ATTENZIONE: per ogni errore di digitazione si ritorna alla schermata di selezione")
        print("             per ogni interruzione da stastiera il gioco verrà chiuso")
        print("\nScegli quale algoritmo vuoi eseguire: \n1) Metodo di Archimede \n2) QuickSort VS MergeSort \n3) Gioco della Vita di Conway")
        scelta = int(input())
    except ValueError:                                                      #gestione dell'eccezione se l'input dell'utente non è un numero intero
        print(f"Input non ammesso, sceglere uno degli indici elencati")
        continue
    except KeyboardInterrupt:
        print("\nErrore, chiusura gioco")
        break

    if scelta == 1:
        #descrizione del metodo di Archimede
        print("\nHai scelto il Metodo di Archimede")
        print("Il seguente programma esegue l'algoritmo per il calcolo del pi-greco. \nIl calcolo avviene mediante l'utilizzo di due poligoni e una circonferenza, \nquest'ultima è inscritta ad un poligono e circostritta all'altro.")
        print("Si parte da un esagono successivamnete vengono raddoppiati i lati del poligono ad ogni iterazione.\nIn quesrto modo la vicinanza tra i poligoni e circonferenza aumenta e l'approssimazione di pigreco migliora")
        MetodoArchimede.main()                                                                              #invocazione del metodo main() della classe MetodoArchimede per eseguire il calcolo di pi-greco
    elif scelta == 2:
        #descrizione del gioco QuickSort VS MergeSort
        print("\nHai scelto QuickSort VS MergeSort, che la sfida cominci!")
        print("In questo gioco verrano confrontate le velocità di ordinamento di un array di 2 algoritmi e verrà premiato l'algoritmo più veloce.")
        print("Entrambi sono algoritmi di ordinamento di un array che utizzano il metodo Divide et Impera con complessita O(nlogn).")
        print("- QuickSort utilizza un pivot random e confrontata tutti gli elementi dell'array con il pivot,\nsi generano così due sottoarray, uno con elementi minori del pivot l'altro con quelli maggiori. \nIterando l'algoritmo in modo ricorsivo sui sottoarray si ottiene l'array completo ordinato.")
        print("- MergeSort suddivide l'arrray in sottoarray base per poi ricomporlo confrontando ogni singolo elemento\ndell'array di sinistra con quelli di destra, ottenendo così l'array completo.")
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
        tempo_di_inizio_quicksort = time.time()
        QuickSort.quick_sort(array1, 0, len(array1) - 1)
        tempo_di_fine_quicksort = time.time()
        tempo_di_esecuzione_quick_sort = tempo_di_fine_quicksort - tempo_di_inizio_quicksort
        print(f"\nQuicksort ha impiegato: {tempo_di_esecuzione_quick_sort} secondi")
        print(array1)
        tempo_di_inizio_mergesort = time.time()
        MergeSort.merge_sort(array2, 0, len(array2) - 1)
        tempo_di_fine_mergesort = time.time()
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
        ConWay.main()

    else:
        print(f"\nL'opzione {scelta} non è in elenco")
    
    risposta = "s"                                                                              #inizializzazione della variabile per l'input dell'utente per giocare di nuovo
    try:
        print("\nVuoi provare un nuovo algoritmo? (premi s per giocare nuovamente, un qualsiasi altro tasto per uscire)")     #stampa il messaggio per chiedere all'utente se vuole giocare di nuovo
        risposta_utente = input().lower()                                                       #lettura dell'input dell'utente e conversione in minuscolo
        risposta.index(risposta_utente)                                                         #lettura dell'input dell'utente
    except ValueError:                                                                          #gestione dell'eccezione se l'input dell'utente non è s, ciò significa che non vuole più giocare
        print("\nGrazie per aver giocato! Arrivederci!")                                        #stampa il messaggio di ringraziamento e arrivederci 
        chiusura = True
    except KeyboardInterrupt:                                                                   #gestione dell'eccezione se l'input dell'utente viene interrotto
        print("\nErrore, chiusura gioco")                                               #stampa messaggio di errore
        break                                                                           #interruzione del ciclo se l'input non è più disponibile
