
# QuickSort.py
# Creato da Valentina Furlanis IN0501333

# Data: 22 Giugno 2026

#Descrizione di MergeSort:
#Il seguente programma esegue l'algoritmo di ordinamento MergeSort
#utilizza il paradigma di divide et impera per suddividere l'array in sottoarray di ugual dimensione, fino ad arrivare al caso base
#successivamente ricompone l'intero array confrontando ogni elemento
#l'algoritmo ha complessità O(nlogn)

class MergeSort:

    def merge_sort(array, inizio, fine):
        if fine > inizio:
            mediana = int( (inizio+fine) / 2)
            MergeSort.merge_sort(array, inizio, mediana)
            MergeSort.merge_sort(array, mediana + 1, fine)

            MergeSort.merge(array, inizio, mediana, fine)
    
    def merge(array, inizio, mediana, fine):
        S = array[inizio:mediana + 1]
        R = array[mediana + 1:fine + 1]
        i = 0
        j = 0
        k = inizio

        while i < len(S) and j < len(R):
            if S[i] <= R[j]:
                array[k] = S[i]
                i = i + 1
            else:
                array[k] = R[j]
                j = j + 1
            k = k + 1

        while i < len(S):
            array[k] = S[i]
            i = i + 1
            k = k + 1

        while j < len(R):
            array[k] = R[j]
            j = j + 1
            k = k + 1
