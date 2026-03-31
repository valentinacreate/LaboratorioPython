#
#Esercizio 2.py
#
#Creato da Valentina Furlanis IN0501333
#Data:21 marzo 2026
#
#Descrizione di cosa fa il programma Esercizio 2.py:
#   Il programma analizza un testo (in questo caso, una poesia) e restituisce:
#       -Contate le righe non vuote che compongono l’estratto
#       -Contate le parole che compongono l’estratto
#       -Contate i caratteri alfanumerici che compongono l’estratto
#       -Chiedere all’utente una lettera e contate quante volte compare nel testo
#       -Sostituite tutte le parole day, water e about con la parola PYTHON in tutti i versi
#       -Riscrivete il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo
#       -Riscrivere il testo invertendo l’ordine delle frasi dal basso all’alto.
#       Riscrivete il testo in modo che il secondo verso di ogni strofa sia scritto a specchio (cioè al contrario carattere per carattere: Ad esempio, questa frase’ –> ‘esarf atseuq ,oipmese dA’)
#       Trovate eventuali parole che compaiono in tutte le strofe
#       Create la lista univoca di tutte le parole che compaiono nel testo, ordinatela per lunghezza delle parole e visualizzatela
#       Create un dizionario che mappi OGNI carattere (chiave) con la sua occorrenza nel testo (valore) e visualizzatelo
#       Create un dizionario come il precedente per i soli caratteri alfanumerici (no caratteri speciali), ignorando maiuscole e minuscole


#Contate le righe non vuote che compongono l’estratto
def Conta_righe_non_vuote(testo):  
    righe=[i for i in testo.split('\n')]
    righe_non_vuote=0
    for i in righe:
        if len(i)>0:
            righe_non_vuote+=1
    tupla=(righe, righe_non_vuote)
    return tupla

def Parole(testo):
    parole=[i for i in testo.split()]
    num_parole=0
    for i in parole:
        if len(i)>0:
            num_parole+=1
    tupla=(parole, num_parole)
    return tupla

def Caratteri(testo):
    caratteri=list(testo)
    alfabeto='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    num_caratteri=0
    for i in caratteri:
        if i in alfabeto:
            num_caratteri+=1
    tupla=(caratteri, num_caratteri)
    return tupla

def Conta_lettera(caratteri):
    '''Contare quante volte compare una lettera nel testo, la funzione è case sensitive'''
    #controllo lettera inserita
    alfabeto='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print('Inserisci una lettera da cercare: ')
    lettera = input()
    while lettera not in alfabeto:
        print('Errore: devi inserire una lettera')
        lettera = input('Inserisci nuovamente la lettera: ')
    #deve considerare sia maiuscola che minuscola, quindi se l'utente inserisce "a" deve contare sia "a" che "A"  
    conteggio = caratteri.count(lettera.lower()) + caratteri.count(lettera.upper())
    print('La lettera', lettera, 'compare', conteggio, 'volte nel testo.\n')

def Sostituisci_parole(testo):
    '''Sostituisci tutte le parole day, water e about con la parola PYTHON in tutti i versi'''
    parole_da_sostituire=['day', 'water', 'about', 'Day', 'Water', 'About']
    for parola in parole_da_sostituire:
        testo=testo.replace(parola, 'PYTHON')
    return testo

def Maiuscolo_dispari(parole):
    '''Riscrivete il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo'''
    testo_modificato=[]
    for i in range(len(parole)):
        if i % 2 == 0:  # Indici 0, 2, 4,... corrispondono a posizioni dispari
            testo_modificato.append(parole[i].upper())
        else:
            testo_modificato.append(parole[i])
    print('Il testo con le parole in maiuscolo in posizione dispari è: ')
    print(testo_modificato)

def Inverti_frasi(frasi):
    '''Riscrivere il testo invertendo l’ordine delle frasi dal basso all’alto'''
    testo_invertito=[]
    for i in range(len(frasi)-1,-1,-1):
        testo_invertito.append(frasi[i])
    print('\nIl testo con le frasi invertite è: ')
    print(testo_invertito)

def Specchio(frasi):
    '''Riscrivete il testo in modo che il secondo verso di ogni strofa sia scritto a specchio (cioè al contrario carattere per carattere)'''
    testo_specchiato=[]
    frase_specchiata=[]
    for i in range(len(frasi)):
        if i== 2:  # Il secondo verso di ogni strofa è l'indice 1, 5, 9,...
            #dividi per carattere
            caratteri = list(frasi[i])
            #inverti j caratteri dalla fine all'inizio
            #assemblo la frase invertita
            #appendo la frase invertita alla lista del testo specchiato
            for j in range(len(caratteri)-1,-1,-1):
                frase_specchiata.append(caratteri[j])
            testo_specchiato.append(frase_specchiata)
        else:
            testo_specchiato.append(frasi[i])
    print('\nIl testo con il secondo verso di ogni strofa scritto a specchio è: ')
    print(testo_specchiato)

#main program
testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''
(righe, righe_non_vuote)=Conta_righe_non_vuote(testo)
print('Le righe non vuote sono: ', righe_non_vuote)
(parole_testo, num_parole)=Parole(testo)
print('Le parole sono: ', num_parole)
(caratteri_testo, num_caratteri)=Caratteri(testo)
print('I caratteri alfanumerici sono: ', num_caratteri)
Conta_lettera(caratteri_testo)
print('Il testo con le parole sostituite è: ', Sostituisci_parole(testo))
Maiuscolo_dispari(parole_testo)
Inverti_frasi(righe)
Specchio(righe)

