
# esercizio6.py
# Creato da Valentina Furlanis IN0501333

# Data: 29 aprile 2026

# Descrizione dell’esercizio6.py:
#   - Riscrivete l’esercizio 3 della rubrica sotto forma di “classe”:
#       - in un file separato, create una classe rubrica la classe rubrica deve fare 5 azioni:
#       - aprire una rubrica leggendola da un file (JSON oppure testo) - APRI
#       - aggiungere un elemento alla rubrica - AGGIUNGI
#       - rimuovere un elemento dalla rubrica (dato il nome) - RIMUOVI
#       - salvare la rubrica su un file (JSON o testo) - SALVA
#       - stampare tutte le informazioni di un contatto (data il nome), come nell’eserczio 3 - STAMPA
#   - la classe rubrica deve inizializzarsi con un dizionario (come nell’esercizio 3)
#   - la classe rubrica deve avere un classmethod per inizializzarla con un file JSON
#   - la classe rubrica deve avere un classmethod per inizializzarla con un file testo
#   - Per “aggiungere un elemento”, bisogna aver prima aperto una rubrica, altrimenti si ottine un messaggio di errore “Prima apri una rubrica”
#   - Per “rimuivere un elemento”, deve esserci almeno un elemento nella rubrica altrimenti si ottine un messaggio di errore “La rubrica è vuota”. Se l’elemento da rimuovere non esiste, il messaggio di errore sarà “Il contatto NOME non esiste in rubrica”
#   - Per “stampare le informazioni”, deve esserci almeno un elemento nella rubrica altrimenti si ottine un messaggio di errore “La rubrica è vuota”. Se l’elemento da rimuovere non esiste, il messaggio di errore sarà “Il contatto NOME non esiste in rubrica”
#   - Per salvare la rubrica su file (JSON o txt deciso dall’estensione del nome del file), la rubrica non deve essere vuota, altrimenti si ottine un messaggio di errore “La rubrica è vuota”
#   - In un file separato importate la classe rubrica appena creata e scrivete un programma che in modo interattivo chieda all’utente di quale delle 5 operazioni della classe rubrica svolgere. Se l’azione richiesta non esiste, il programma continua a chiedere l’azione da svolgere finchè non viene indicata la stringa “EXIT”.

import Rubrica                                                                  #importazione della classe Rubrica dal file Rubrica.py

def main():
    '''Funzione principale del programma per poter interagire con la rubrica e apportare le modifiche APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA'''
    rubrica = Rubrica.Rubrica()                                                 #creazione di un'istanza della classe Rubrica
    
    while True:                                                                                             #ciclo infinito che continua a chiedere all'utente quale azione svolgere finché non viene digitata la stringa "EXIT"
        print('\nScegliere un\'azione da svolgere: APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA')                 #stampa le opzioni disponibili per l'utente
        print('Per uscire digitare EXIT')                                                                   #stampa l'opzione per uscire dal programma
        azione = input().upper()                                                                            #legge l'input dell'utente e converte la stringa in maiuscolo per facilitare il confronto con le opzioni disponibili           

        if azione == 'APRI':                                                                                #se l'utente inserisce "APRI"
            print('\nInserire il nome della rubrica da aprire, inclusa la sua estensione (.json o .txt):')  #stampa un messaggio che chiede all'utente di inserire il nome del file da aprire, inclusa l'estensione
            nome_file = input()                                                                             #legge l'input dell'utente per il nome del file da aprire
            dati = rubrica.apri(nome_file)                                                                  #chiama il metodo "apri" della classe Rubrica, passando il nome del file da aprire, e memorizza i dati restituiti nella variabile "dati"
            print('\nFile aperto:', bool(dati))                                                             #stampa un messaggio che indica se il file è stato aperto correttamente (True) o meno (False) in base al valore di "dati"       
        elif azione == 'AGGIUNGI':                                                                          #se l'utente inserisce "AGGIUNGI"
            rubrica.aggiungi()                                                                              #chiama il metodo "aggiungi" della classe Rubrica per aggiungere un nuovo contatto alla rubrica                                         
            print('\nContatto aggiunto:', bool(rubrica.info))                                               #stampa un messaggio che indica se il contatto è stato aggiunto correttamente (True) o meno (False)
        elif azione == 'RIMUOVI':                                                                           #se l'utente inserisce "RIMUOVI"                                    
            print('\nContatti attuali nella rubrica sono:')                                                 #stampa un messaggio che specifica all'utente che successivamente verrà mostrata una lista dei nomi dei contatti
            print([nome for nome in rubrica.info])                                                          #stampa una lista dei nomi dei contatti attualmente presenti nella rubrica                                        
            print('\nInserire il nome del contatto da rimuovere:')                                          #stampa un messaggio che chiede all'utente di inserire il nome del contatto da rimuovere   
            nome_da_rimuovere = input().strip()                                                             #legge l'input dell'utente per il nome del contatto da rimuovere e rimuove eventuali spazi bianchi all'inizio o alla fine del nome                  
            rubrica.rimuovi(nome_da_rimuovere)                                                              #chiama il metodo "rimuovi" della classe Rubrica, passando il nome del contatto da rimuovere
        elif azione == 'SALVA':                                                                             #se l'utente inserisce "SALVA"
            print('\nInserire il nome del file in cui salvare la rubrica (con estensione .json o .txt):')   #stampa un messaggio che chiede all'utente di inserire il nome del file in cui salvare la rubrica, inclusa l'estensione
            nome_file = input().strip()                                                                     #legge l'input dell'utente per il nome del file in cui salvare la rubrica e rimuove eventuali spazi bianchi all'inizio o alla fine del nome
            rubrica.salva(nome_file)                                                                        #chiama il metodo "salva" della classe Rubrica, passando il nome del file in cui salvare la rubrica
        elif azione == 'STAMPA':                                                                            #se l'utente inserisce "STAMPA"
            print('\nContatti attuali nella rubrica sono:')                                                 #stampa un messaggio che specifica all'utente che successivamente verrà mostrata una lista dei nomi dei contatti
            print([nome for nome in rubrica.info])                                                          #stampa una lista dei nomi dei contatti attualmente presenti nella rubrica                                            
            print('\nInserire il nome del contatto da stampare:')                                           #stampa un messaggio che chiede all'utente di inserire il nome del contatto di cui stampare le informazioni
            nome_da_stampare = input().strip()                                                              #legge l'input dell'utente per il nome del contatto di cui stampare le informazioni e rimuove eventuali spazi bianchi all'inizio o alla fine del nome
            rubrica.stampa(nome_da_stampare)                                                                #chiama il metodo "stampa" della classe Rubrica, passando il nome del contatto di cui stampare le informazioni
        elif azione == 'EXIT':                                                                              #se l'utente inserisce "EXIT"                                   
            print('\nUscita dal programma.')                                                                #stampa un messaggio che indica all'utente che sta uscendo dal programma
            break                                                                                           #esce dal ciclo infinito, terminando il programma                                    
        else:                                                                                       
            print('\nAzione non valida.')                                                                   #se l'utente inserisce un'azione non valida, stampa un messaggio di errore e continua a chiedere l'azione da svolgere


main()






