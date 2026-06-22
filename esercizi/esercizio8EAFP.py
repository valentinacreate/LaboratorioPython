
#esercizio8.py
#Creato da Valentina Furlanis IN0501333

# Data: 22 giugno 2026

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
    
    try:
        with open(file_parole, 'r') as in_file:                                                 #apertura del file in modalità lettura
            parole = json.load(in_file)                                                         #caricamento del contenuto del file JSON nel dizionario rubrica                                                        
    except FileNotFoundError:                                                                   #gestione dell'eccezione se il file JSON non esiste 
        print("Errore: il file Parole_impiccato.json non esiste.")                              #stampa il messaggio di errore se il file JSON non esiste
        break                                                                                   #interruzione del ciclo while se il file JSON non esiste
    except json.JSONDecodeError:                                                                #gestione dell'eccezione se il file JSON non è valido
        print("Errore: il file JSON non contiene una lista di parole valida.")                  #stampa il messaggio di errore se il contenuto del file JSON non è una lista di parole valida
        break                                                                                   #interruzione del ciclo while se il contenuto del file JSON non è una lista di parole valida

    parola_da_indovinare = random.choice(parole)                                                #selezione casuale della parola dalla lista
    print(f"\nLa parola da indovinare ha {len(parola_da_indovinare)} lettere.")                   #stampa il numero di lettere della parola da indovinare
    print("Hai a disposizione 6 tentativi per indovinare la parola.")                           #stampa il numero di tentativi disponibili
    prova_utente = ""                                                                           #inizializzazione della variabile per l'input dell'utente
    parola_indovinata = parola_da_indovinare[0] + "_" * (len(parola_da_indovinare)-2) + parola_da_indovinare[-1]  #inizializzazione della variabile per la parola indovinata con underscore al posto delle lettere
    print(parola_indovinata)                                                                    #stampa la parola da indovinare con le lettere indovinate dall'utente
    lettere_usate = []                                                                          #memorizzazione delle lettere già provate
    while errori < 6:                                                                           #ciclo while per gestire i tentativi dell'utente
        
        try:
            print(f"Sei al {errori+1}° tentativo.")                                             #stampa il numero di tentativi effettuati
            print(f"Lettere già provate: {', '.join(lettere_usate)}")                           #stampa le lettere già provate dall'utente
            print("Inserire una lettera o indovinare la parola:")                               #stampa il messaggio per l'input dell'utente
            prova_utente = input().strip().lower()                                              #lettura dell'input dell'utente, rimozione degli spazi bianchi e conversione in minuscolo
        except EOFError:                                                                        #gestione dell'eccezione se l'input dell'utente viene interrotto
            print("Input terminato. Impossibile continuare il gioco.")                          #stampa il messaggio se l'input viene interrotto davvero
            break                                                                               #interruzione del ciclo se l'input non è più disponibile

        if prova_utente == "":                                                                  #controllo se l'utente ha inserito solo spazi o nulla
            print("Input vuoto. Inserire una lettera valida.")                                  #stampa il messaggio di errore se l'input è vuoto
            continue                                                                            #richiesta di un nuovo input senza contarlo come tentativo

        alfabeto = "abcdefghijklmnopqrstuvwxyz"                                                 #inizializzazione della variabile per l'alfabeto

        if len(prova_utente) == 1:                                                              #se l'input dell'utente è una singola lettera
            try:
                alfabeto.index(prova_utente)                                                    #controllo se l'input dell'utente è una lettera valida
            except ValueError:
                print("Ci deve essere un errore di input, inserire lettere valide.")            #stampa il messaggio di errore se l'input dell'utente non è una lettera valida
                continue                                                                        #richiesta di un nuovo input senza contare come tentativo

            try:
                lettere_usate.index(prova_utente)                                               #controllo se la lettera è già stata provata
            except ValueError:                                                                  
                pass                                                                            #se la lettera non è stata provata, quindi genera errore durante l'esecuzione di index, continua con il gioco
            else:
                print(f"Hai già provato la lettera '{prova_utente}'.")                          #stampa il messaggio se la lettera è già stata provata
                continue                                                                        #richiesta di una nuova lettera senza consumare un tentativo

            lettere_usate.append(prova_utente)                                                  #aggiunta della lettera inserita dall'utente alla lista delle lettere già provate
            
            if prova_utente in parola_da_indovinare:                                            #controllo se la lettera inserita dall'utente è presente nella parola da indovinare
                print(f"La lettera '{prova_utente}' è presente nella parola da indovinare.")    #stampa il messaggio se la lettera è presente nella parola da indovinare
                for i in range(len(parola_indovinata)):                                         #ciclo for per stampare la parola da indovinare con le lettere indovinate dall'utente
                    if parola_da_indovinare[i] == prova_utente:                                 #individuazione della posizione della lettera indovinata dall'utente nella parola da indovinare
                        parola_indovinata = parola_indovinata[:i] + parola_da_indovinare[i] + parola_indovinata[i+1:]  #sostituzione dell'underscore con la lettera indovinata dall'utente
                print(parola_indovinata)                                                        #stampa la parola da indovinare con le lettere indovinate dall'utente
            else:
                print(f"La parola '{prova_utente}' non è corretta.\n {parola_indovinata}")      #stampa il messaggio se la lettera inserita dall'utente non è presente nella parola da indovinare
                errori += 1                                                                     #incremento del numero di errori commessi dall'utente
                print(stati_impiccato[errori])                                                  #stampa lo stato dell'impiccato in base al numero di errori commessi dall'utente

        elif len(prova_utente) == len(parola_da_indovinare):                                    #controllo se l'input dell'utente è una parola completa e valida
            try:
                for lettera in prova_utente:                                                    #per ogni lettera dell'input dell'utente
                    alfabeto.index(lettera)                                                     #controllo se l'input dell'utente è una parola completa e valida
            except ValueError:
                print("Ci deve essere un errore di input, inserire lettere valide.")            #stampa il messaggio di errore se l'input dell'utente non è valido
                continue                                                                        #richiesta di un nuovo input senza contare come tentativo

            if prova_utente == parola_da_indovinare.lower():                                    #controllo se l'input dell'utente è uguale alla parola da indovinare
                parola_indovinata = parola_da_indovinare                                        #sostituzione della parola indovinata dall'utente con la parola da indovinare
            else:
                print("Parola errata.")                                                         #stampa il messaggio se l'input dell'utente è una parola completa ma non è uguale alla parola da indovinare
                errori += 1                                                                     #incremento del numero di errori commessi dall'utente
                print(stati_impiccato[errori])                                                  #stampa lo stato dell'impiccato in base al numero di errori commessi dall'utente

        if parola_indovinata == parola_da_indovinare:                                           #controllo se la parola indovinata dall'utente è uguale alla parola da indovinare
            print(f"Complimenti! Hai indovinato la parola '{parola_da_indovinare}'!")           #stampa il messaggio di vittoria
            break                                                                               #interruzione del ciclo se la parola indovinata dall'utente è uguale alla parola da indovinare
    if errori == 6:                                                                             #controllo se il numero di tentativi effettuati è uguale al numero di tentativi disponibili
        print(f"Mi dispiace! Hai esaurito i tentativi. La parola da indovinare era '{parola_da_indovinare}'.")  #stampa il messaggio di sconfitta

    risposta = "s"                                                                              #inizializzazione della variabile per l'input dell'utente per giocare di nuovo
    try:
        print("Vuoi giocare di nuovo? (premi s per giocare nuovamente, un qualsiasi altro tasto per uscire)")     #stampa il messaggio per chiedere all'utente se vuole giocare di nuovo
        risposta_utente = input().lower()                                                       #lettura dell'input dell'utente e conversione in minuscolo
        risposta.index(risposta_utente)                                                         #lettura dell'input dell'utente
    except ValueError:                                                                          #gestione dell'eccezione se l'input dell'utente non è s, ciò significa che non vuole più giocare
        print("Grazie per aver giocato! Arrivederci!")                                          #stampa il messaggio di ringraziamento e arrivederci 
        break