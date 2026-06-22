
# QuickSort.py
# Creato da Valentina Furlanis IN0501333

# Data: 22 Giugno 2026

#Descrizione di QuickSort:
#Il seguente programma esegue l'algoritmo di ordinamento QuickSort
#utilizza il paradigma di divide et impera per suddividere l'array in sottoarray basandosi sull'elemento pivot (scelto in modo casuale) 
#ordinare ciascuno dei sottoarray in modo ricorsivo 
#il pivot è scelto in modo casuale in modo da evitare il caso peggiore di complessità O(n^2) che si verifica quando 
#l'array è già ordinato o quasi ordinato, in questo modo si garantisce una complessità media di O(n log n) con n numero di elementi nell'array.

import random
class QuickSort:
    
    def partition(array, p, r):
        '''partiziona l'array in base al pivot scelto in modo casuale e restituisce l'indice delpivot'''
        indice_pivot = random.randint(p, r)
        pivot=array[indice_pivot]
        array[indice_pivot], array[r] = array[r], array[indice_pivot]
        ultimo_valore_minore = p - 1
        for j in range(p, r):
            if array[j] < pivot:
                ultimo_valore_minore += 1
                array[ultimo_valore_minore], array[j] = array[j], array[ultimo_valore_minore]
        array[ultimo_valore_minore + 1], array[r] = array[r], array[ultimo_valore_minore +1]
        return ultimo_valore_minore + 1
    
    def quick_sort(array, p, r):
        '''ordina l'array in modo ricorsivo'''
        if p < r:
            q = QuickSort.partition(array, p, r)
            QuickSort.quick_sort(array, p, q-1)
            QuickSort.quick_sort(array, q+1, r)

        

