
# esercizio6.py
# Creato da Valentina Furlanis IN0501333

# Data: 4 Maggio 2026

#Descrizione del Metodo di Archimede:
#Il seguente programma esegue l'algoritmo per il calcolo del pigreco
#il calcolo avviene mediante l'utiizzo di due poligoni con una circonferenza
#inscritta ad un poligono e circostritta dall'altro
#aumentando i lati del poligono la vicinanza alla circonferenza aumenta e 
#l'approssimazione di pigreco migliora
#https://trinket.io/library/trinkets/create?lang=pygame per la simulazione

import math
import turtle

class MetodoArchimede:
    def __init__(self):
        self.raggio = 200.0
        self.schermo = turtle.Screen()
        self.schermo.setup(900, 600)
        self.penna = turtle.Turtle()
        self.penna.hideturtle()
        self.penna.speed("fast")
    
    def disegna_iterazione(self, n, pi_min, pi_max):
        self.penna.clear()
        self.disegna_cerchio()
        self.disegna_poligono_inscritto(n, pi_max)
        self.disegna_poligono_circoscritto(n, pi_min)

    def disegna_cerchio(self):
        self.penna.penup()
        self.penna.goto(0, -self.raggio)
        self.penna.pendown()
        self.penna.circle(self.raggio)

    def disegna_poligono_inscritto(self, n, pi_max=None):
        angolo = 360 / n
        self.penna.penup()
        x = self.raggio * math.cos(math.radians(0))
        y = self.raggio * math.sin(math.radians(0))
        self.penna.goto(x, y)
        self.penna.pendown()
        for i in range(1, n + 1):
            x = self.raggio * math.cos(math.radians(i * angolo))
            y = self.raggio * math.sin(math.radians(i * angolo))
            self.penna.goto(x, y)

    def disegna_poligono_circoscritto(self, n, pi_min=None):
        raggio_circoscritto = self.raggio / math.cos(math.pi / n)
        angolo = 360 / n
        self.penna.penup()
        x = raggio_circoscritto * math.cos(math.radians(0))
        y = raggio_circoscritto * math.sin(math.radians(0))
        self.penna.goto(x, y)
        self.penna.pendown()
        for i in range(1, n + 1):
            x = raggio_circoscritto * math.cos(math.radians(i * angolo))
            y = raggio_circoscritto * math.sin(math.radians(i * angolo))
            self.penna.goto(x, y)

    def calcolo_pi(self, itera, grafica = False):
        n = 6
        perimetro_circoscritto = (n * 2 * self.raggio) / math.sqrt(3)
        perimetro_inscritto = n * self.raggio

        for i in range(itera):
            pi_min = perimetro_circoscritto / (2 * self.raggio)
            pi_max = perimetro_inscritto / (2 * self.raggio)
            print(f"\n{i+1}^ interazione")
            print('Il valore di pi greco è compreso tra:')
            print(f"{pi_min} data dal poligono circoscritto con {n} lati \n{pi_max} data dal poligono inscritto con {n} lati")
            
            if grafica:
                self.disegna_iterazione(n, pi_min, pi_max)
            
            perimetro_circoscritto = (2 * perimetro_circoscritto * perimetro_inscritto) / (perimetro_circoscritto + perimetro_inscritto)
            perimetro_inscritto = math.sqrt(perimetro_circoscritto * perimetro_inscritto)
            n *= 2
        if grafica:
            turtle.done()

arch = MetodoArchimede()
print('quante volte vuoi iterare l\'algoritmo?')
numero_iterazione=int(input())
arch.calcolo_pi(numero_iterazione, grafica=True)