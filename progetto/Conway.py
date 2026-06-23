
# Conway.py
# Creato da Valentina Furlanis IN0501333

# Data: 23 Giugno 2026

#descrigione dell'algoritmo Conway:
#Il Gioco della Vita di Conway è un automa cellulare ideato da John Conway. 
#Si tratta di un modello semplice che simula l’evoluzione di celle su una griglia bidimensionale secondo regole specifiche, 
#senza intervento esterno dopo l’inizializzazione. Ogni cella può essere viva o morta (stato 1 o 0) 
#e l’evoluzione avviene in turni (generazioni).
#Regole del Gioco
#Sopravvivenza: Una cella viva con due o tre vicini vivi sopravvive alla generazione successiva.
#Morte: Una cella viva con meno di due vicini vivi muore per solitudine; con più di tre vicini vivi muore per sovrappopolazione.
#Nascita: Una cella morta con esattamente tre vicini vivi diventa viva.
#La "vicinanza" si calcola considerando le otto celle adiacenti orizzontalmente, verticalmente e diagonalmente

class ConWay:
    def __init__(self, righe, colonne, valore_iniziale=0):
        '''Inizializza una matrice di dimensione righe x colonne'''
        self.righe = righe
        self.colonne = colonne
        self.matrice = [[valore_iniziale for _ in range(colonne)] for _ in range(righe)]
    


    def conway(self, righe, colonne):
        self.__init__(self, righe, colonne)

