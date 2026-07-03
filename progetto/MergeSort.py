
# MergeSort.py
# Creato da Valentina Furlanis IN0501333

# Data: 22 Giugno 2026

#Descrizione di MergeSort:
#Il seguente programma esegue l'algoritmo di ordinamento MergeSort
#utilizza il paradigma di divide et impera per suddividere l'array in sottoarray di ugual dimensione, fino ad arrivare al caso base
#successivamente ricompone l'intero array confrontando ogni elemento
#l'algoritmo ha complessità O(nlogn)

class MergeSort:

    def mergesort(array, inizio, fine):
        '''Ordina ricorsivamente l'array usando MergeSort per poi ricombinare e orinare i 2 sottoarray usando il metodo merge'''
        if fine > inizio:                                                       #finché l'array ha più di un elemento, calcolo la mediana e divido l'array in 2 sottoarray, invocando ricorsivamente la funzione merge_sort() sui 2 sottoarray, per poi ricombinarli e ordinarli usando il metodo merge()
            mediana = int( (inizio+fine) / 2)
            MergeSort.mergesort(array, inizio, mediana)
            MergeSort.mergesort(array, mediana + 1, fine)
            MergeSort.merge(array, inizio, mediana, fine)
    
    def merge(array, inizio, mediana, fine):
        '''Unisce due sottosequenze ordinate dell'array in un unico segmento ordinato confrontando elemento con elemento'''
        S = array[inizio:mediana + 1]                                           #sottosequenza sinistra dell'array
        R = array[mediana + 1:fine + 1]                                         #sottosequenza destra dell'array
        i = 0                                                                   #inizializzazione dell'indice per la sottosequenza sinistra
        j = 0                                                                   #inizializzazione dell'indice per la sottosequenza destra
        k = inizio                                                              #inizializzazione dell'indice per l'array risultante

        while i < len(S) and j < len(R):                                        #finché entrambi gli indici sono minori della lunghezza delle rispettive sottosequenze, confronto gli elementi delle due sottosequenze e li inserisco nell'array risultante in ordine crescente         
            if S[i] <= R[j]:
                array[k] = S[i]
                i = i + 1
            else:
                array[k] = R[j]
                j = j + 1
            k = k + 1

        while i < len(S):                                                       #se la sottosequenza sinistra ha ancora elementi, li inserisco nell'array risultante
            array[k] = S[i]
            i = i + 1
            k = k + 1

        while j < len(R):                                                       #se la sottosequenza destra ha ancora elementi, li inserisco nell'array risultante             
            array[k] = R[j]
            j = j + 1
            k = k + 1
