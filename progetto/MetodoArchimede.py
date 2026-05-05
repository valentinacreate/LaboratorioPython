
# esercizio6.py
# Creato da Valentina Furlanis IN0501333

# Data: 4 Maggio 2026

#Descrizione del Metodo di Archimede:
#Il seguente programma esegue l'algoritmo per il calcolo del pigreco
#il calcolo avviene mediante l'utiizzo di due poligoni con una circonferenza
#inscritta ad un poligono e circostritta dall'altro
#aumentando i lati del poligono la vicinanza alla circonferenza aumenta e 
#l'approssimazione di pigreco migliora
import math
import turtle

class MetodoArchimede:
    def __init__(self):
        self.raggio = 1.0
        self.schermo = turtle.Screen()
        self.schermo.setup(800, 800)
        self.penna = turtle.Turtle()
        self.penna.hideturtle()
        self.penna.speed("fastest")
    
    def disegna_iterazione(n, pi_min, pi_max):
        self.disegna_cerchio()
        self.disegna_poligono_inscritto(n, pi_max)
        self.disegna_poligono_circoscritto(n, pi_min)
        pass


    def calcolo_pi(self, itera, grafica = False):
        n = 6
        perimetro_circoscritto = (n * 2 * self.raggio) / math.sqrt(3)
        perimetro_insritto = n * self.raggio

        for i in range(itera):
            pi_min = perimetro_circoscritto / (2 * self.raggio)
            pi_max = perimetro_inscritto / (2 * self.raggio)
            print(f"\n{i+1}^ interazione")
            print('Il valore di pi greco è compreso tra:')
            print(f"{pi_min} data dal poligono circoscritto con {n} lati \n{pi_max} data dal poligono inscritto con {n} lati")
            
            if grafica:
                self.disegna_iterazione(n, pi_min, pi_max )
            perimetro_circoscritto = (2 * perimetro_circoscritto * perimetro_insritto) / (perimetro_circoscritto + perimetro_insritto)
            perimetro_insritto = math.sqrt(perimetro_circoscritto * perimetro_insritto)
            n *= 2
        if grafica:
            turtle.done()

arch = MetodoArchimede()
print('quante volte vuoi iterare l\'algoritmo?')
numero_iterazione=int(input())
arch.calcolo_pi(numero_iterazione)
