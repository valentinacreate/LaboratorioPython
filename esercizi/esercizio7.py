
#esercizio7.py
#Creato da Valentina Furlanis IN0501333

# Data: 10 giugno 2026

# Descrizione del programmaesercizio7.py:
#Il programma deve:
#- contenere un generatore che, dato un numero (ad esempio 7), generi la tabellina corrispondente al numero selezionato (0x7 = 0; 1x7 = 7; 2x7 = 14; ecc…);
#- contenere un loop che chieda in modo interrattivo all’utente di indovinare il valore corrente nella tabellina selezionata;
#- gestire tutti i caratteri alfanumerici (non deve “rompersi” se l’utente sceglie una lettera);
#- gestire caretteri speciali o numeri decimali;
#- gestire la chiusura del gioco in modo personalizzato.

def generatore_tabellina(numero):
    '''Generatore che, dato un numero, genera la tabellina corrispondente al numero selezionato (0xnumero = 0; 1xnumero = numero; 2xnumero = 2*numero; ecc…)'''               
    for i in range(11):                     #ciclo for che genera la tabellina del numero selezionato, da 0 a 10
         yield i * numero                   #utilizzo il yield per generare i valori della tabellina uno alla volta, senza doverli memorizzare tutti in una lista

chiusura = False                            #variabile booleana che indica se il gioco deve continuare o meno
while chiusura == False:
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=~`[]{};':\",.<>?/\\|èéàòìù£€$°§ç"       #stringa contenente tutti i caratteri alfanumerici e speciali, per controllare se l'input dell'utente è un numero o meno
    print("Inserisci un numero per generare la tabellina:")                                 #stampa il messaggio per chiedere all'utente di inserire un numero
    numero = input()                                                                        #legge l'input dell'utente
    while numero in alfabeto:                                                               #controllo che l'input non sia un carattere alfanumerico
            print('Errore: devi inserire un numero. Riprova:')                              #se l'input non è un numero, stampa un messaggio di errore
            numero = input()                                                                #legge nuovamente l'input dell'utente
    tabellina = generatore_tabellina(float(numero))                                         #creo un generatore che genera la tabellina del numero selezionato dall'utente, convertito in float per gestire anche numeri decimali
    for i in range(11):
        valore_corrente = next(tabellina)                                                   #salvo il valore atteso prima di iniziare i tentativi, così non viene consumato di nuovo a ogni errore
        print(f"Indovina il valore della tabellina!\nQuanto fa {i} x {numero}?")            #stampa il messaggio per chiedere all'utente di indovinare il valore della tabellina, indicando il numero selezionato e l'indice corrente della tabellina
        risposta = input()                                                                  #legge l'input dell'utente
        while risposta in alfabeto:                                                         #controllo che l'utente abbia inserito un numero 
            print('Errore: devi inserire un numero. Riprova:')                              #se l'input non è un numero, stampa un messaggio di errore
            risposta = input()                                                              #legge nuovamente l'input dell'utente
        while float(risposta) != valore_corrente:                                            #controllo che l'input dell'utente sia uguale al valore corrente della tabellina
            print('Sbagliato! Riprova:')                                                    #stampa il messaggio di errore se l'input dell'utente non è uguale al valore corrente della tabellina
            risposta = input()                                                              #legge nuovamente l'input dell'utente
            while risposta in alfabeto:                                                     #controllo che l'input non sia un carattere alfanumerico
                print('Errore: devi inserire un numero. Riprova:')                          #se l'input non è un numero, stampa un messaggio di errore
                risposta = input()                                                          #legge nuovamente l'input dell'utente
        print('Bravo! Hai indovinato!')                                                     #stampa il messaggio di congratulazioni se l'input dell'utente è uguale al valore corrente della tabellina

    print("Vuoi continuare? (si/no)")                                                       #stampa il messaggio per chiedere all'utente se vuole continuare a giocare
    risposta = input()                                                                      #legge l'input dell'utente
    if risposta.lower() == "no":                                                            #se l'input dell'utente è "no"
        chiusura = True                                                                     #imposta la variabile booleana chiusura a True per terminare il gioco
        print("E' stato un piacere giocare con te! A presto! (^_^)")                        #stampa il messaggio di chiusura del gioco