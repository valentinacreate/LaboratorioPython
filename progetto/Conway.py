
# Conway.py
# Creato da Valentina Furlanis IN0501333

# Data: 23 Giugno 2026

#descrigione dell'algoritmo Conway:
#Il Gioco della Vita di Conway è un automa cellulare ideato da John Conway. 
#Si tratta di un modello semplice che simula l’evoluzione di celle su una griglia bidimensionale secondo regole specifiche, 
#senza intervento esterno dopo l’inizializzazione. Ogni cella può essere viva o morta (stato 1 o 0) e l’evoluzione avviene in turni (generazioni).

#Regole del Gioco
#Sopravvivenza: Una cella viva con due o tre vicini vivi sopravvive alla generazione successiva.
#Morte: Una cella viva con meno di due vicini vivi muore per solitudine; con più di tre vicini vivi muore per sovrappopolazione.
#Nascita: Una cella morta con esattamente tre vicini vivi diventa viva.
#La "vicinanza" si calcola considerando le otto celle adiacenti orizzontalmente, verticalmente e diagonalmente

import time                             #importo la libreria time per misurare il tempo impiegato a trovare le soluzioni
import random                           #importo la libreria random

class ConWay:
    def __init__(self, righe, colonne, valore_iniziale = 0):
        '''Inizializza una matrice di dimensione righe x colonne'''
        self.righe = righe                                                                      #inizializzazione della variabile righe
        self.colonne = colonne                                                                  #inizializzazione della variabile colonne
        self.matrice = [[valore_iniziale for _ in range(colonne)] for _ in range(righe)]        #inizializzazione della matrice con valore iniziale 0 (cella morta)

    def conta_vicini_vivi(self, x, y):
        '''Conta il numero di celle vive adiacenti alla cella in posizione (x, y)'''
        vivi = 0                                                                                #variabile per contare le celle vive adiacenti
        for i in range(x - 1, x + 2):                                                           #scorro le righe vicine alla cella in posiszione (x,y)
            for j in range(y - 1, y + 2):                                                       #scorro le colonne vicine alla cella in posiszione (x,y)
                if (i, j) != (x, y) and 0 <= i < self.righe and 0 <= j < self.colonne:          #verifico che la cella vicina non sia la cella stessa e che sia all'interno dei limiti della matrice
                    if self.matrice[i][j] == 1:                                                 #se la cella vicina è viva allora incremento il contatore delle celle vive
                        vivi += 1
        return vivi                                                                             #restituisco il numero delle celle vive adiacenti alla cella in posizione (x,y)

    def aggiorna_matrice(self):
        '''Aggiorna la matrice secondo le regole del Gioco della Vita di Conway'''
        nuova_matrice = [[0 for _ in range(self.colonne)] for _ in range(self.righe)]           #inizializzazione della numva matrice, di dimenzione uguale a quella originale, con tutte le celle morte
        for i in range(self.righe):                                                             #scorro le righe della matrice
            for j in range(self.colonne):                                                       #scorro le colonne della matrice
                vivi = self.conta_vicini_vivi(i, j)                                             #contyo il numero delle celle vive adiacenti alla cella in posizioni (i,j)
                if self.matrice[i][j] == 1:                                                     #se la cella in posizioni (i,j) è viva allora verifico le regole del gioco: se ha meno di 2 o più di 3 vicini vivi muore, altrimenti sopravvive
                    if vivi < 2 or vivi > 3:
                        nuova_matrice[i][j] = 0
                    else:
                        nuova_matrice[i][j] = 1
                else:                                                                           #se la cella in posizioni (i,j) è viva allora e ha esattamente 3 vicini vivi allora nasce
                    if vivi == 3:
                        nuova_matrice[i][j] = 1
        self.matrice = nuova_matrice                                                            #aggiorno la matrice originale con la nuova matrice appena creata


    def main():
        '''Funzione principale per eseguire il Gioco della Vita di Conway'''    
        while True:                                                                             #ciclo per verificare che l'input dell'utente sia corretto
            try:                                                                                #eseguo il blocco di codice e se l'input dell'utente non è corretto allora viene sollevata un'eccezione
                print("\ninserire la dimensione N della matrice NxN, scegliere un intero\n inserire un valore intero preferibilemnte di 20")
                dimensione=int(input())
                # Se l'input è valido, esci dal loop per proseguire con il gioco
                break
            except ValueError:                                                                   #se l'input dell'utente non è un intero allora viene sollevata un'eccezione e viene stampato un messaggio di errore, chiedendo all'utente di inserire un nuovo valore
                print("\nIl dato inserito non è corretto, usare un valore intero")
                continue
            except KeyboardInterrupt:                                                            #se l'input dell'utente viene interrotto allora viene sollevata un'eccezione e viene stampato un messaggio di errore, chiudendo il gioco
                print("\nErrore, chiusura gioco")
                break
        
        gioco = ConWay(dimensione, dimensione)                                                   #inizializzazione della matrice di dimensione NxN con tutte le celle morte
        #Inizializzazione casuale per rendere la simulazione più dinamica
        random.seed()                                                                            #Viene usato un seed basato sul tempo di sistema per variare i pattern
        print("scegli la probabilità che una cella sia viva all'inizio (valore tra 0.1 e 0.8)")  #chiedo all'utente di inserire un valore per la densità delle celle vive iniziali
        densita = float(input())                                                    
        while densita < 0.0 or densita > 1.0:                                                    #se il valore inserito dall'utente non è compreso tra 0.1 e 0.8 allora viene stampato un messaggio di errore, chiedendo all'utente di inserire un nuovo valore
            print("valore per la densità non appropriato, inserire un nuovo valore")
            densita = float(input())
        for i in range(gioco.righe):                                                             #scorro le righe della matrice
            for j in range(gioco.colonne):                                                       #scorro le colonne della matrice
                if  random.random() < densita:                                                   #se il numero casuale generato è minore della densità allora la cella in posizioni (i,j) è viva, altrimenti è morta
                    gioco.matrice[i][j] = 1  
                else:
                    gioco.matrice[i][j] = 0
        print(f"Inizializzazione casuale completata (densità {densita})")

        tempo_sim_start = time.time()                                                                   #Tempo di inizio della simulazione
        while True:                                                                                     #ciclo per eseguire la simulazione del gioco fino a quando la popolazione non si estingue o fino a quando non sono passati 25 secondi
            celle_vive = 0                                                                              #variabile per contare le celle vive
            celle_morte = 0                                                                             #variabile per contare le celle morte
            gioco.aggiorna_matrice()                                                                    #aggiorno la matrice invocando la funzione aggiorna_matrice()
            for i in range(gioco.righe):                                                                #per ogni cella della matrice conto le celle vive e le celle morte
                for j in range(gioco.colonne):
                    if gioco.matrice[i][j] == 1:
                        celle_vive += 1
                    else:
                        celle_morte += 1
            for i in range(gioco.righe):                                                                #stampo la matrice aggiornata per mostratla all'utente
                print(f"{gioco.matrice[i]}")                                                            
            print(f"le celle vive sono: {celle_vive}\nle celle morte sono: {celle_morte}")              #stampo il numero di celle vive e di celle morte
            tempo_attuale = time.time()                                                                 #salvo il tempo di terminazione della creazione della matrice aggiornata
            tempo_simulazione = tempo_attuale - tempo_sim_start                                         #calcolo il tempo di simulazione 
            if celle_vive == 0:                                                                         #se il numero di celle vive è 0 allora la popolazione si è estinta e viene stampato un messaggio di avviso, terminando la simulazione
                print(f"La popolazione si è estinta, è sopravvissuta per {tempo_simulazione} secondi")
                break
            if tempo_simulazione >= 25.0:                                                               #se il tempo di simulazione è maggiore o uguale a 25 secondi allora viene stampato un messaggio di avviso, terminando la simulazione                                                                
                print(f"La simulazione è terminata dopo {tempo_simulazione} secondi.\nLa popolazione è stabile e riuscirà a soppravvivere ancora per diverso tempo\nle celle vive sono: {celle_vive}\nle celle morte sono: {celle_morte}")
                break
            time.sleep(1)                                                                               #pausa di 1 secondo tra ogni generazione per rendere la simulazione più leggibile

