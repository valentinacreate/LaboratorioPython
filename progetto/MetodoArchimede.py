
# MetodoArchimede.py
# Creato da Valentina Furlanis IN0501333

# Data: 4 Maggio 2026

#Descrizione del Metodo di Archimede:
#Il seguente programma esegue l'algoritmo per il calcolo del pigreco
#il calcolo avviene mediante l'utiizzo di due poligoni con una circonferenza
#inscritta ad un poligono e circostritta dall'altro
#aumentando i lati del poligono la vicinanza alla circonferenza aumenta e 
#l'approssimazione di pigreco migliora per la simulazione

import math
import webbrowser

class MetodoArchimede:

    def __init__(self):
        self.raggio = 1.0

    def calcolo_pi(self, itera):
        '''calcola il valore approssimato di pi-greco partende da poligoni dinlato 6 e 
        raddoppiandoli a ogni iterazione'''
        n = 6
        perimetro_circoscritto = (n * 2 * self.raggio) / math.sqrt(3)
        perimetro_inscritto = n * self.raggio

        for i in range(itera):
            pi_min = perimetro_circoscritto / (2 * self.raggio)
            pi_max = perimetro_inscritto / (2 * self.raggio)
            print(f"\n{i+1}^ interazione")
            print('Il valore di pi greco è compreso tra:')
            print(f"{pi_min} data dal poligono circoscritto con {n} lati \n{pi_max} data dal poligono inscritto con {n} lati")
            
            perimetro_circoscritto = (2 * perimetro_circoscritto * perimetro_inscritto) / (perimetro_circoscritto + perimetro_inscritto)
            perimetro_inscritto = math.sqrt(perimetro_circoscritto * perimetro_inscritto)
            n *= 2
    
    def main():
        risposte_possibili = ["SI", "NO"]
        arch = MetodoArchimede()
        while True:
            try:
                print("\nVuoi vedere l\'algoritmo graficamente? [SI/NO]")
                risposta = input().upper()
                risposte_possibili.index(risposta)
            except ValueError:
                print("Errore nell'input. Riprova.")
                continue
            except KeyboardInterrupt:
                print("\nErrore, chiusura gioco")
                break
            if risposta == "SI":
                '''apre una pagina trinked dov'è presente una versione del codice con un\'implementazione grafica 
                delle iterazioni e mostra visivamente l\'avvicinarsi dei poligoni alla circonferenza'''
                url = "https://trinket.io/pygame/0e0d0a5d314d"
                webbrowser.open(url)
            else:
                try:
                    print('\nQuante volte vuoi iterare l\'algoritmo?\n Inserire un valore intero positivo')
                    numero_iterazione=int(input())
                    arch.calcolo_pi(numero_iterazione)
                except ValueError:
                    print("Errore nell'input. Riprova.")
                    continue
                except KeyboardInterrupt:
                    print("\nErrore, chiusura gioco")
                    break
            break