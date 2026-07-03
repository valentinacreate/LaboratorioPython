
# QuickSort.py
# Creato da Valentina Furlanis IN0501333

# Data: 22 Giugno 2026

#Descrizione di QuickSort:
#Il seguente programma esegue l'algoritmo di ordinamento QuickSort
#utilizza il paradigma di divide et impera per suddividere l'array in sottoarray basandosi sull'elemento pivot (scelto in modo casuale) 
#ordinare ciascuno dei sottoarray in modo ricorsivo 
#il pivot è scelto in modo casuale in modo da evitare il caso peggiore di complessità O(n^2) che si verifica quando 
#l'array è già ordinato o quasi ordinato, in questo modo si garantisce una complessità media di O(n log n) con n numero di elementi nell'array.

import random                           #importazione libreria random per la scelta casuale del pivot                                                      

class QuickSort:
    
    def partition(array, p, r):
        '''partiziona l'array in base al pivot scelto in modo casuale e restituisce l'indice delpivot'''
        indice_pivot = random.randint(p, r)                                                         #scelta casuale dell'indice del pivot tra p e r
        pivot=array[indice_pivot]                                                                   #assegnazione del valore del pivot scelto alla variabile pivot
        array[indice_pivot], array[r] = array[r], array[indice_pivot]                               #scambio del pivot con l'ultimo elemento dell'array  
        ultimo_valore_minore = p - 1                                                                #inizializzazione dell'indice dell'ultimo valore minore del pivot a p-1
        for j in range(p, r):                                                                       #per ogni elemento dell'array tra p e r, confronto l'elemento i-esimo con il pivot
            if array[j] < pivot:                                                                    #se è minore del pivot, incrementa l'indice dell'ultimo valore minore e scambia l'elemento i-esimo con l'ultimo elemento minore del pivot
                ultimo_valore_minore += 1
                array[ultimo_valore_minore], array[j] = array[j], array[ultimo_valore_minore]
        array[ultimo_valore_minore + 1], array[r] = array[r], array[ultimo_valore_minore +1]        #scambia il pivot con l'elemento successivo all'ultimo valore minore
        return ultimo_valore_minore + 1                                                             #restituisce l'indice del pivot
    
    def quick_sort(array, p, r):
        '''ordina l'array in modo ricorsivo'''
        if p < r:                                                                                   #finché p è minore di r, eseguo la partizione e poi richiamo la funzione quick_sort() sui due sottoarray generati dalla partizione
            q = QuickSort.partition(array, p, r)
            QuickSort.quick_sort(array, p, q-1)
            QuickSort.quick_sort(array, q + 1, r)

        

