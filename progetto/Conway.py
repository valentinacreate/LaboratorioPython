
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
        self.righe = righe
        self.colonne = colonne
        self.matrice = [[valore_iniziale for _ in range(colonne)] for _ in range(righe)]

    def conta_vicini_vivi(self, x, y):
        vivi = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i, j) != (x, y) and 0 <= i < self.righe and 0 <= j < self.colonne:
                    if self.matrice[i][j] == 1:
                        vivi += 1
        return vivi

    def aggiorna_matrice(self):
        nuova_matrice = [[0 for _ in range(self.colonne)] for _ in range(self.righe)]
        for i in range(self.righe):
            for j in range(self.colonne):
                vivi = self.conta_vicini_vivi(i, j)
                if self.matrice[i][j] == 1:
                    if vivi < 2 or vivi > 3:
                        nuova_matrice[i][j] = 0
                    else:
                        nuova_matrice[i][j] = 1
                else:
                    if vivi == 3:
                        nuova_matrice[i][j] = 1
        self.matrice = nuova_matrice


    def main():    
        while True:
            try:
                print("\ninserire la dimensione N della matrice NxN, scegliere un intero\n inserire un valore intero preferibilemnte di 20")
                dimensione=int(input())
                # Se l'input è valido, esci dal loop per proseguire con il gioco
                break
            except ValueError:
                print("\nIl dato inserito non è corretto, usare un valore intero")
                continue
            except KeyboardInterrupt:
                print("\nErrore, chiusura gioco")
                break
        
        gioco = ConWay(dimensione, dimensione)
        # Inizializzazione casuale per rendere la simulazione più dinamica
        # Viene usato un seed basato sul tempo di sistema per variare i pattern
        random.seed()
        print("scegli la probabilità che una cella sia viva all'inizio (valore tra 0.1 e 0.8)")
        densita = float(input())
        while densita < 0.0 or densita > 1.0:
            print("valore per la densità non appropriato, inserire un nuovo valore")
            densita = float(input())
        for i in range(gioco.righe):
            for j in range(gioco.colonne):
                if  random.random() < densita:
                    gioco.matrice[i][j] = 1  
                else:
                    gioco.matrice[i][j] = 0
        print(f"Inizializzazione casuale completata (densità {densita})")

        # Tempo di inizio della simulazione (misurato una sola volta)
        tempo_sim_start = time.time()
        while True:
            celle_vive = 0
            celle_morte = 0
            gioco.aggiorna_matrice()
            for i in range(gioco.righe):
                for j in range(gioco.colonne):
                    if gioco.matrice[i][j] == 1:
                        celle_vive += 1
                    else:
                        celle_morte += 1
            for i in range(gioco.righe):
                print(f"{gioco.matrice[i]}")
            print(f"le celle vive sono: {celle_vive}\nle celle morte sono: {celle_morte}")
            tempo_attuale = time.time()
            tempo_simulazione = tempo_attuale - tempo_sim_start
            if celle_vive == 0:
                print(f"La popolazione si è estinta, è sopravvissuta per {tempo_simulazione} secondi")
                break
            # Interrompi la simulazione dopo 30 secondi
            if tempo_simulazione >= 25.0:
                print(f"La simulazione è terminata dopo {tempo_simulazione} secondi.\nle celle vive sono: {celle_vive}\nle celle morte sono: {celle_morte}")
                break
            time.sleep(1)

