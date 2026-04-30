
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
# la classe rubrica deve inizializzarsi con un dizionario (come nell’esercizio 3)
# la classe rubrica deve avere un classmethod per inizializzarla con un file JSON
# la classe rubrica deve avere un classmethod per inizializzarla con un file testo
# Per “aggiungere un elemento”, bisogna aver prima aperto una rubrica, altrimenti si ottine un messaggio di errore “Prima apri una rubrica”
# Per “rimuivere un elemento”, deve esserci almeno un elemento nella rubrica altrimenti si ottine un messaggio di errore “La rubrica è vuota”. Se l’elemento da rimuovere non esiste, il messaggio di errore sarà “Il contatto NOME non esiste in rubrica”
# Per “stampare le informazioni”, deve esserci almeno un elemento nella rubrica altrimenti si ottine un messaggio di errore “La rubrica è vuota”. Se l’elemento da rimuovere non esiste, il messaggio di errore sarà “Il contatto NOME non esiste in rubrica”
# Per salvare la rubrica su file (JSON o txt deciso dall’estensione del nome del file), la rubrica non deve essere vuota, altrimenti si ottine un messaggio di errore “La rubrica è vuota”
# In un file separato importate la classe rubrica appena creata e scrivete un programma che in modo interattivo chieda all’utente di quale delle 5 operazioni della classe rubrica svolgere. Se l’azione richiesta non esiste, il programma continua a chiedere l’azione da svolgere finchè non viene indicata la stringa “EXIT”.

import Rubrica

def main():
    rubrica = Rubrica.Rubrica()
    print('\nInserire il nome della rubrica da aprire incluso di estensione (.json o .txt):')
    nome_file = input().strip()
    dati = rubrica.apri(nome_file)
    print('\nFile aperto:', bool(dati))

    while True:
        print('\nScegliere un\'azione da svolgere: AGGIUNGI, RIMUOVI, SALVA, STAMPA')
        print('Per uscire digitare EXIT')
        azione = input().strip().upper()

        if azione == 'AGGIUNGI':
            rubrica.aggiungi()
            print('\nContatto aggiunto:', bool(rubrica.info))
            print(rubrica.info)
        elif azione == 'RIMUOVI':
            print('\nContatti attuali nella rubrica sono:')
            print([nome for nome in rubrica.info])
            print('\nInserire il nome del contatto da rimuovere:')
            nome_da_rimuovere = input().strip()
            rubrica.rimuovi(nome_da_rimuovere)
        elif azione == 'SALVA':
            print('\nInserire il nome del file in cui salvare la rubrica (con estensione .json o .txt):')
            nome_file = input().strip()
            rubrica.salva(nome_file)
        elif azione == 'STAMPA':
            print('\nContatti attuali nella rubrica sono:')
            print([nome for nome in rubrica.info])
            print('\nInserire il nome del contatto da stampare:')
            nome_da_stampare = input().strip()
            rubrica.stampa(nome_da_stampare)
        elif azione == 'EXIT':
            print('\nUscita dal programma.')
            break
        else:
            print('\nAzione non valida.')


main()






