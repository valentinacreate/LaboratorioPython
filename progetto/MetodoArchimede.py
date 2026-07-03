
# MetodoArchimede.py
# Creato da Valentina Furlanis IN0501333

# Data: 4 Maggio 2026

#Descrizione del Metodo di Archimede:
#Il seguente programma esegue l'algoritmo per il calcolo del pigreco
#il calcolo avviene mediante l'utiizzo di due poligoni con una circonferenza
#inscritta ad un poligono e circostritta dall'altro
#aumentando i lati del poligono la vicinanza alla circonferenza aumenta e 
#l'approssimazione di pigreco migliora per la simulazione

import math                                         #importazione la libreria math per utilizzare la funzione sqrt()
import webbrowser                                   #importazione della libreria webbrowser per aprire la pagina trinket con l'implementazione grafica del metodo di Archimede

class MetodoArchimede:

    def __init__(self):
        '''inizializza il raggio della circonferenza a 1'''
        self.raggio = 1.0

    def calcolo_pi(self, itera):
        '''calcola il valore approssimato di pi-greco partende da poligoni dinlato 6 e raddoppiandoli a ogni iterazione'''
        n = 6                                                                                   #inizializzazione numero dei lati dei poligoni
        perimetro_circoscritto = (n * 2 * self.raggio) / math.sqrt(3)                           #calcolo del perimetro del poligono circoscritto 
        perimetro_inscritto = n * self.raggio                                                   #calcolo del perimetro del poligono inscritto 

        for i in range(itera):                                                                  #ciclo for che calcola pi-greco per il numero di iterazioni richieste dall'utente
            pi_min = perimetro_circoscritto / (2 * self.raggio)                                 #cacolo del valore minimo di pi-greco data dal poligono circoscritto
            pi_max = perimetro_inscritto / (2 * self.raggio)                                    #cacolo del valore minimo di pi-greco data dal poligono inscritto
            
            #stampo i risultati dell'terazione corrente
            print(f"\n{i+1}^ interazione")
            print('Il valore di pi greco è compreso tra:')
            print(f"{pi_min} data dal poligono circoscritto con {n} lati \n{pi_max} data dal poligono inscritto con {n} lati")
            
            perimetro_circoscritto = (2 * perimetro_circoscritto * perimetro_inscritto) / (perimetro_circoscritto + perimetro_inscritto)        #calcolo del nuovo perimetro del poligono circoscritto
            perimetro_inscritto = math.sqrt(perimetro_circoscritto * perimetro_inscritto)                                                       #calcolo del nuovo perimetro del poligono inscritto
            n *= 2
    
    def main():
        risposte_possibili = ["SI", "NO"]                                                   #lista delle risposte possibile
        arch = MetodoArchimede()                                                            #creazione di un oggetto della classe MetodoArchimede
        while True:
            try:                                                                            #esecuzione del blocco di codice per chiedere all'utente se vuole osservare l'algoritmo graficamnete che potrebbe generare un'eccezione 
                print("\nVuoi vedere l\'algoritmo graficamente? [SI/NO]")
                risposta = input().upper()
                risposte_possibili.index(risposta)
            except ValueError:                                                              #gestione dell'eccezione se l'input non è una delle risposte possibili: stampa un messaggio di errore e chiede all'utente di riprovare
                print("Errore nell'input. Riprova.")
                continue
            except KeyboardInterrupt:                                                       #gestione dell'eccezione se l'utente interrompe il programma da tastiera: stampa un messaggio d'errore e chiude il programma
                print("\nErrore, chiusura gioco")
                break
            if risposta == "SI":                                                            #se la risposta è sì apre una pagina trinked dov'è presente una versione del codice con un\'implementazione grafica delle iterazioni e mostra visivamente l\'avvicinarsi dei poligoni alla circonferenza
                url = "https://trinket.io/pygame/0e0d0a5d314d"
                webbrowser.open(url)
            else:                                                                           #altrimenti chiede all'utente quante iterazioni vuole eseguire e invoca il metodo calcolo_pi()
                try:                                                                        #esecuzione del blocco di codice per inserire il numero di iterazioni che potrebbe generare un'eccezione
                    print('\nQuante volte vuoi iterare l\'algoritmo?\n Inserire un valore intero positivo')
                    numero_iterazione=int(input())
                    arch.calcolo_pi(numero_iterazione)
                except ValueError:                                                          #gestione dell'eccezione se l'input non è un numero intero positivo: stampa un messaggio di errore e chiede all'utente di riprovare
                    print("Errore nell'input. Riprova.")
                    continue
                except KeyboardInterrupt:                                                   #gestione dell'eccezione se l'utente interrompe il programma da tastiera: stampa un messaggio d'errore e chiude il programma
                    print("\nErrore, chiusura gioco")
                    break
            break