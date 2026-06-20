
#esercizio7.py
#Creato da Valentina Furlanis IN0501333

# Data: 10 giugno 2026

# Descrizione dell’esercizio7.py:
#Il programma deve:
#-contenere un generatore che, dato un numero (ad esempio 7), generi la tabellina corrispondente al numero selezionato (0x7 = 0; 1x7 = 7; 2x7 = 14; ecc…);
#-contenere un loop che chieda in modo interrattivo all’utente di indovinare il valore corrente nella tabellina selezionata;
#-gestire tutti i caratteri alfanumerici (non deve “rompersi” se l’utente sceglie una lettera);
#-gestire caretteri speciali o numeri decimali;
#-gestire la chiusura del gioco in modo personalizzato.

def generatore_tabellina(numero):
    for i in range(11):
         yield i*numero

chiusura = False
while chiusura == False:
    alfabeto="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=~`[]{};':\",.<>?/\\|èéàòìù£€$°§ç"
    print("Inserisci un numero per generare la sua tabellina:")
    numero = input()
    while numero in alfabeto:                                                              #controllo che la lettera inserita sia una lettera dell'alfabeto (maiuscola o minuscola)
            print('Errore: devi inserire un numero. Riprova:')
            numero = input()
    tabellina = generatore_tabellina(float(numero))
    for i in range(11):
        print(f"Indovina il valore della tabellina!\nQuanto fa {i} x {numero}?")
        risposta = input()
        while risposta in alfabeto:                                                          #controllo che la lettera inserita sia una lettera dell'alfabeto (maiuscola o minuscola)
            print('Errore: devi inserire un numero. Riprova:')
            risposta = input()
        while float(risposta) != next(tabellina):
            print('Sbagliato! Riprova:')
            risposta = input()
            while risposta in alfabeto:                                                          #controllo che la lettera inserita sia una lettera dell'alfabeto (maiuscola o minuscola)
                print('Errore: devi inserire un numero. Riprova:')
                risposta = input()
        print('Bravo! Hai indovinato!')

    print("Vuoi continuare? (si/no)")
    risposta = input()
    if risposta.lower() == "no":
        chiusura = True
        print("E' stato un piacere giocare con te! A presto! (^_^)")