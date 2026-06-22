
#esercizio8.py
#Creato da Valentina Furlanis IN0501333

# Data: 10 giugno 2026

# Descrizione dell’esercizio8.py:
#Scrivete un programma per “il gioco dell’impiccato” in cui:
#- leggete una lista di parole da un file JSON
#- scegliete una parola a caso con cui giocare dalla lista letta, tramite random
#- chiedete continuamente all’utente di inserire una lettera o di indovinare la parola, fino al termine del gioco in cui si esauriscono i tentativi o si indovina la parola
#- La rappresentazione grafica del gioco è libera, così come il numero dei “tentativi” disponibili.

#- 1- Scrivete il programma con un approccio totalmente LBYL
#   2- RI-scrivete il programma con un approccio totalmente EAFP

import random                                                              
import json
import os

stati_impiccato = [                                                         

    """
      +---+
      |   |
      |   
      |
      |
      |
    =========
    """,
    """
      +---+
      |   |
      |   O
      |
      |
      |
    =========
    """,
    """
      +---+
      |   |
      |   O
      |   |
      |
      |
    =========
    """,
    """
      +---+
      |   |
      |   O
      |  /|
      |
      |
    =========
    """,
    """
      +---+
      |   |
      |   O
      |  /|\\
      |
      |
    =========
    """,
    """
      +---+
      |   |
      |   O
      |  /|\\
      |  / 
      |
    =========
    """,
        """
      +---+
      |   |
      |   O
      |  /|\\
      |  / \\
      |
    =========
    """,    
]
chiusura = False                                                                                #inizializzazione della variabile per la chiusura del programma
print("Benvenuto al gioco dell'impiccato!")                                                     #stampa il messaggio di benvenuto
while chiusura == False:                                                                        #ciclo while per la chiusura del programma
    errori=0                                                                                    #numero di errori commessi dall'utente
    file_parole = 'Parole_impiccato.json'                                                       #controllo preventivo del file JSON
    if not os.path.exists(file_parole):                                                         #controllo se il file JSON esiste
        print("Errore: il file Parole_impiccato.json non esiste.")                              #stampa il messaggio di errore se il file JSON non esiste
        chiusura = True                                                                         #impostazione della variabile per la chiusura del programma a True
        break                                                                                   #interruzione del ciclo while se il file JSON non esiste

    if os.path.getsize(file_parole) == 0:                                                       #controllo se il file JSON è vuoto
        print("Errore: il file Parole_impiccato.json è vuoto.")                                #stampa il messaggio di errore se il file JSON è vuoto
        chiusura = True                                                                         #impostazione della variabile per la chiusura del programma a True
        break                                                                                   #interruzione del ciclo while se il file JSON è vuoto

    with open(file_parole, 'r') as in_file:                                                     #apertura del file in modalità lettura
        parole = json.load(in_file)                                                             #caricamento del contenuto del file JSON nel dizionario rubrica
        
    parola_da_indovinare = random.choice(parole)                                                #selezione casuale della parola dalla lista
    print(f"La parola da indovinare ha {len(parola_da_indovinare)} lettere.")                   #stampa il numero di lettere della parola da indovinare
    print("Hai a disposizione 6 tentativi per indovinare la parola.")                           #stampa il numero di tentativi disponibili
    prova_utente = ""                                                                           #inizializzazione della variabile per l'input dell'utente
    parola_indovinata = parola_da_indovinare[0] + "_" * (len(parola_da_indovinare)-2) + parola_da_indovinare[-1]  #inizializzazione della variabile per la parola indovinata con underscore al posto delle lettere
    print(parola_indovinata)                                                                    #stampa la parola da indovinare con le lettere indovinate dall'utente
    lettere_usate = []                                                                          #memorizzazione delle lettere già provate
    while errori < 6:                                                                           #ciclo while per stampare il numero di lettere della parola da indovinare
        print(f"Sei al {errori+1}° tentativo.")                                                 #stampa il numero di tentativi effettuati
        print(f"Lettere già provate: {', '.join(lettere_usate)}")                               #stampa le lettere già provate dall'utente
        print("Inserire una lettera o indovinare la parola:")                                   #stampa il messaggio per l'input dell'utente
        prova_utente = input().strip().lower()                                                  #lettura dell'input dell'utente, rimozione degli spazi bianchi e conversione in minuscolo
        alfabeto = "abcdefghijklmnopqrstuvwxyz"                                                 #inizializzazione della variabile per l'alfabeto
        while prova_utente == "":                                                               #controllo se l'input dell'utente è vuoto o non è una lettera valida
            print("Input non valido. Inserire una lettera.")                                    #stampa il messaggio di errore se l'input dell'utente non è valido
            prova_utente = input().strip().lower()                                              #lettura dell'input dell'utente
        
        if len(prova_utente) == 1 and prova_utente in alfabeto:                                 #controllo se l'input dell'utente è 1 lettera e che sia valida
            while prova_utente in lettere_usate:                                                #controllo se la lettera inserita dall'utente è già stata provata
                print(f"Hai già provato la lettera '{prova_utente}'.")                          #stampa il messaggio se la lettera è già stata provata, ciò non vale come tentativo, quindi richiedo una lettera
                print("Inserire una lettera:")                                                  #stampa il messaggio per l'input dell'utente
                prova_utente = input().strip().lower()                                          #lettura dell'input dell'utente

        if len(prova_utente) == 1:                                                              #controllo se l'input dell'utente è 1 lettera
            if prova_utente in alfabeto:                                                        #controllo se l'input dell'utente è una lettera valida
                lettere_usate.append(prova_utente)                                              #aggiunta della lettera inserita dall'utente alla lista delle lettere già provate
                if prova_utente in parola_da_indovinare:                                        #controllo se la lettera inserita dall'utente è presente nella parola da indovinare
                    print(f"La lettera '{prova_utente}' è presente nella parola da indovinare.")    #stampa il messaggio se la lettera è presente nella parola da indovinare
                    for i in range(len(parola_indovinata)):                                     #ciclo for per stampare la parola da indovinare con le lettere indovinate dall'utente
                        if parola_da_indovinare[i] == prova_utente:                             #individuazione della posizione della lettera indovinata dall'utente nella parola da indovinare
                            parola_indovinata=parola_indovinata[:i] + parola_da_indovinare[i] + parola_indovinata[i+1:]  #sostituzione dell'underscore con la lettera indovinata dall'utente
                    print(parola_indovinata)                                                    #stampa la parola da indovinare con le lettere indovinate dall'utente
                else:
                    print(f"La parola '{prova_utente}' non è corretta.\n {parola_indovinata}")  #stampa il messaggio se la lettera inserita dall'utente non è presente nella parola da indovinare e mostra la parola da indovinare con le lettere indovinate dall'utente
                    errori += 1                                                                 #incremento del numero di errori commessi dall'utente
                    print(stati_impiccato[errori])                                              #stampa lo stato dell'impiccato in base al numero di errori commessi dall'utente
            else:
                print("Inserire una lettera valida.")                                           #stampa il messaggio se l'input dell'utente non è una lettera valida
        
        elif len(prova_utente) == len(parola_da_indovinare):                                    #controllo se l'input dell'utente è una parola completa e valida                                    
            while not all(lettera in alfabeto for lettera in prova_utente):                     #controllo se anche solo una lettera della parola contiene simboli o numeri
                print("Ci deve essere un errore di digitazione.")                               #stampa il messaggio se l'input dell'utente non è una parola valida
                print("Inserire la parola corretta:")                                           #stampa il messaggio per l'input dell'utente
                prova_utente = input().strip().lower()                                          #lettura dell'input dell'utente
            if prova_utente == parola_da_indovinare.lower():                                    #controllo se l'input dell'utente è uguale alla parola da indovinare
                parola_indovinata = parola_da_indovinare                                        #sostituzione della parola indovinata dall'utente con la parola da indovinare
            else:
                print("Parola errata.")                                                         #stampa il messaggio se l'input dell'utente è una parola completa ma non è uguale alla parola da indovinare        
                errori += 1                                                                     #incremento del numero di errori commessi dall'utente
                print(stati_impiccato[errori])                                                  #stampa lo stato dell'impiccato in base al numero di errori commessi dall'utente                       
        else:
            print("Input non valido. Inserire una lettera o una parola completa.")             #stampa il messaggio se la lunghezza dell'input non è valida
        if parola_indovinata == parola_da_indovinare:                                           #controllo se la parola indovinata dall'utente è uguale alla parola da indovinare
            print(f"Complimenti! Hai indovinato la parola '{parola_da_indovinare}'!")           #stampa il messaggio di vittoria 
            break 
                                                                                                #interruzione del ciclo for se la parola indovinata dall'utente è uguale alla parola da indovinare
    if errori == 6:                                                                             #controllo se il numero di tentativi effettuati è uguale al numero di tentativi disponibili
        print(f"Mi dispiace! Hai esaurito i tentativi. La parola da indovinare era '{parola_da_indovinare}'.")  #stampa il messaggio di sconfitta

    print("Vuoi giocare di nuovo? (s/n)")                                                       #stampa il messaggio per chiedere all'utente se vuole giocare di nuovo
    risposta_utente = input()                                                                   #lettura dell'input dell'utente
    while risposta_utente.lower() not in ["s", "n"]:                                            #controllo se l'input dell'utente è diverso da "s" o "n"
        print("Input non valido. Inserire 's' per giocare di nuovo o 'n' per uscire.")          #stampa il messaggio di errore se l'input dell'utente non è valido
        risposta_utente = input()                                                               #lettura dell'input dell'utente
    if risposta_utente.lower() == "n":                                                          #controllo se l'utente non vuole giocare di nuovo
        chiusura = True                                                                         #impostazione della variabile per la chiusura del programma a True
        print("Grazie per aver giocato! Arrivederci!")                                          #stampa il messaggio di ringraziamento e arrivederci 
    