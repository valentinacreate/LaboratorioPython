
#esercizio8.py
#Creato da Valentina Furlanis IN0501333

# Data: 10 giugno 2026

# Descrizione dell’esercizio8.py:
#Scrivete un programma per “il gioco dell’impiccato” in cui:
#-leggete una lista di parole da un file JSON
#-scegliete una parola a caso con cui giocare dalla lista letta, tramite random
#-chiedete continuamente all’utente di inserire una lettera o di indovinare la parola, fino al termine del gioco in cui si esauriscono i tentativi o si indovina la parola
#   La rappresentazione grafica del gioco è libera, così come il numero dei “tentativi” disponibili.

#   1- Scrivete il programma con un approccio totalmente LBYL
#   2- RI-scrivete il programma con un approccio totalmente EAFP
import random
import json
print("Benvenuto al gioco dell'impiccato!")                                 #stampa il messaggio di benvenuto
valore_scelta_parola = random.randint(0, 82)                                #scelta casuale di un numero da 0 a 82 per selezionare una parola dalla lista
tentativi_disponibili = 6                                                   #numero di tentativi disponibili per l'utente

with open('Parole_impiccato.json', 'r') as in_file:                         #apertura del file in modalità lettura
    parole = json.load(in_file)                                             #caricamento del contenuto del file JSON nel dizionario rubrica   
parola_da_indovinare = parole[valore_scelta_parola]                         #selezione della parola da indovinare dalla lista
print(f"La parola da indovinare ha {len(parola_da_indovinare)} lettere.")   #stampa il numero di lettere della parola da indovinare
print("Hai a disposizione 6 tentativi per indovinare la parola.")           #stampa il numero di tentativi disponibili
tentativi_effettuati = 0                                                    #inizializzazione del numero di tentativi effettuati
prova_utente = ""                                                           #inizializzazione della variabile per l'input dell'utente
parola_indovinata = parola_da_indovinare[0] + "_" * (len(parola_da_indovinare)-2) + parola_da_indovinare[-1]  #inizializzazione della variabile per la parola indovinata con underscore al posto delle lettere
print(parola_indovinata)                                                        #stampa la parola da indovinare con le lettere indovinate dall'utente
for i in range(tentativi_disponibili):                                      #ciclo for per stampare il numero di lettere della parola da indovinare
    print(f"Hai usato {i+1} tentativi.")                    #stampa il numero di tentativi effettuati e disponibili        
    print("Inserire una lettera o indovinare la parola:")                   #stampa il messaggio per l'input dell'utente
    prova_utente = input()                                                  #lettura dell'input dell'utente
    for lettera in prova_utente:                                            #ciclo for per controllare se la lettera inserita dall'utente è presente nella parola da indovinare
        if lettera in parola_da_indovinare:                                                 #controllo se la lettera inserita dall'utente è presente nella parola da indovinare
            print(f"La lettera '{lettera}' è presente nella parola da indovinare.")         #stampa il messaggio se la lettera è presente nella parola da indovinare
            for i in range(len(parola_indovinata)):                                         #ciclo for per stampare la parola da indovinare con le lettere indovinate dall'utente
                if parola_da_indovinare[i] in prova_utente:                                 #controllo se la lettera della parola da indovinare è presente nell'input dell'utente
                    parola_indovinata=parola_indovinata[:i] + parola_da_indovinare[i] + parola_indovinata[i+1:]  #sostituzione dell'underscore con la lettera indovinata dall'utente
            print(parola_indovinata)                                                        #stampa la parola da indovinare con le lettere indovinate dall'utente
        else:
            print(f"La lettera '{lettera}' non è presente nella parola da indovinare.")     #stampa il messaggio se la lettera non è presente nella parola da indovinare
    if parola_indovinata == parola_da_indovinare:                                         #controllo se la parola indovinata dall'utente è uguale alla parola da indovinare
        print(f"Complimenti! Hai indovinato la parola '{parola_da_indovinare}'!")  #stampa il messaggio di vittoria se la parola indovinata dall'utente è uguale alla parola da indovinare
        break                                                                                  #interruzione del ciclo for se la parola indovinata dall'utente è uguale alla parola da indovinare
        