
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
import os
chiusura = False                                                            #inizializzazione della variabile per la chiusura del programma
print("Benvenuto al gioco dell'impiccato!")                                 #stampa il messaggio di benvenuto
while chiusura == False:                                                    #ciclo while per la chiusura del programma
    tentativi_disponibili = 6                                                   #numero di tentativi disponibili per l'utente

    file_parole = 'Parole_impiccato.json'                                       #controllo preventivo del file JSON
    if not os.path.exists(file_parole):
        print("Errore: il file Parole_impiccato.json non esiste.")
        chiusura = True
        break

    with open(file_parole, 'r') as in_file:                                     #apertura del file in modalità lettura
        parole = json.load(in_file)                                             #caricamento del contenuto del file JSON nel dizionario rubrica

    if not isinstance(parole, list) or len(parole) == 0:
        print("Errore: il file JSON non contiene una lista di parole valida.")
        chiusura = True
        break

    parola_da_indovinare = random.choice(parole)                                #selezione casuale della parola dalla lista
    print(f"La parola da indovinare ha {len(parola_da_indovinare)} lettere.")   #stampa il numero di lettere della parola da indovinare
    print("Hai a disposizione 6 tentativi per indovinare la parola.")           #stampa il numero di tentativi disponibili
    prova_utente = ""                                                           #inizializzazione della variabile per l'input dell'utente
    parola_indovinata = parola_da_indovinare[0] + "_" * (len(parola_da_indovinare)-2) + parola_da_indovinare[-1]  #inizializzazione della variabile per la parola indovinata con underscore al posto delle lettere
    print(parola_indovinata)                                                        #stampa la parola da indovinare con le lettere indovinate dall'utente
    lettere_usate = []                                                          #memorizzazione delle lettere già provate
    for i in range(tentativi_disponibili):                                      #ciclo for per stampare il numero di lettere della parola da indovinare
        print(f"Sei al {i+1}° tentativo.")                    #stampa il numero di tentativi effettuati e disponibili        
        print("Inserire una lettera o indovinare la parola:")                   #stampa il messaggio per l'input dell'utente
        prova_utente = input().strip().lower()                                                  #lettura dell'input dell'utente
        alfabeto = "abcdefghijklmnopqrstuvwxyz"                                      #inizializzazione della variabile per l'alfabeto
        if len(prova_utente) == 1 and prova_utente in alfabeto:                                                   #controllo se l'input dell'utente è una lettera valida
            while prova_utente in lettere_usate:                                                #controllo se la lettera inserita dall'utente è già stata provata
                print(f"Hai già provato la lettera '{prova_utente}'.")                        #stampa il messaggio se la lettera è già stata provata
                print("Inserire una lettera:")                   #stampa il messaggio per l'input dell'utente
                prova_utente = input().strip().lower()                                                  #lettura dell'input dell'utente

        if len(prova_utente) == 1:
            if prova_utente in alfabeto:
                lettere_usate.append(prova_utente)                                               #aggiunta della lettera inserita dall'utente alla lista delle lettere già provate
                if prova_utente in parola_da_indovinare:                                                 #controllo se la lettera inserita dall'utente è presente nella parola da indovinare
                    print(f"La lettera '{prova_utente}' è presente nella parola da indovinare.")         #stampa il messaggio se la lettera è presente nella parola da indovinare
                    for i in range(len(parola_indovinata)):                                         #ciclo for per stampare la parola da indovinare con le lettere indovinate dall'utente
                        if parola_da_indovinare[i] == prova_utente:                                 #controllo se la lettera della parola da indovinare è presente nell'input dell'utente
                            parola_indovinata=parola_indovinata[:i] + parola_da_indovinare[i] + parola_indovinata[i+1:]  #sostituzione dell'underscore con la lettera indovinata dall'utente
                    print(parola_indovinata)                                                        #stampa la parola da indovinare con le lettere indovinate dall'utente
                    print(f"Lettere già provate: {', '.join(lettere_usate)}")                                 #stampa le lettere già provate dall'utente
                else:
                    print(f"La parola '{prova_utente}' non è corretta.\n {parola_indovinata}")
                    print(f"Lettere già provate: {', '.join(lettere_usate)}")                                 #stampa le lettere già provate dall'utente
            else:
                print("Inserire una lettera valida.")
        
        elif len(prova_utente) == len(parola_da_indovinare):                                                   #controllo se l'input dell'utente è una parola valida
            if prova_utente == parola_da_indovinare.lower():
                parola_indovinata = parola_da_indovinare
            else:
                print("Parola errata.")
        else:
            print("Inserimento vuoto o non valido.")
        
        if parola_indovinata == parola_da_indovinare:                                         #controllo se la parola indovinata dall'utente è uguale alla parola da indovinare
            print(f"Complimenti! Hai indovinato la parola '{parola_da_indovinare}'!")  #stampa il messaggio di vittoria se la parola indovinata dall'utente è uguale alla parola da indovinare
            break                                                                                  #interruzione del ciclo for se la parola indovinata dall'utente è uguale alla parola da indovinare
        if i == tentativi_disponibili-1:                                         #controllo se il numero di tentativi effettuati è uguale al numero di tentativi disponibili
            print(f"Mi dispiace! Hai esaurito i tentativi. La parola da indovinare era '{parola_da_indovinare}'.")  #stampa il messaggio di sconfitta se il numero di tentativi effettuati è uguale al numero di tentativi disponibili
    
    print("Vuoi giocare di nuovo? (s/n)")                                                   #stampa il messaggio per chiedere all'utente se vuole giocare di nuovo
    risposta_utente = input()                                                  #lettura dell'input dell'utente
    if risposta_utente.lower() == "n":                                                   #controllo se l'utente non vuole giocare di nuovo
        chiusura = True                                                            #impostazione della variabile per la chiusura del programma a True
        print("Grazie per aver giocato! Arrivederci!")                                 #stampa il messaggio di ringraziamento e arrivederci 
    