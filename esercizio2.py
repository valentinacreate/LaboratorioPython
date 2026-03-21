#
#Esercizio 2.py
#
#Creato da Valentina Furlanis IN0501333
#Data:21 marzo 2026
#
#Descrizione di cosa fa il programma Esercizio 2.py:
#   Il programma analizza un testo (in questo caso, una poesia) e restituisce:
#       Contate le righe non vuote che compongono l’estratto
#       Contate le parole che compongono l’estratto
#       Contate i caratteri alfanumerici che compongono l’estratto
#       Chiedere all’utente una lettera e contate quante volte compare nel testo
#       Sostituite tutte le parole day, water e about con la parola PYTHON in tutti i versi
#       Riscrivete il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo
#       Riscrivere il testo invertendo l’ordine delle frasi dal basso all’alto.
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
        if i != '':
            righe_non_vuote+=1
    
    return righe_non_vuote

def Parole(testo):
    parole=[i for i in testo.split()]
    return parole

def Caratteri(testo):
    caratteri=[i for i in testo if i.isalnum()]
    return (caratteri)

def Conta_lettera(caratteri):
    '''Contare quante volte compare una lettera nel testo, la funzione è case sensitive'''
    print('La lettera è case sensitive, quindi se vuoi cercare la lettera "a" devi inserire "a" e non "A".')
    print('Inserisci una lettera da cercare: ')
    lettera = input()
    print('La lettera', lettera, 'compare', caratteri.count(lettera), 'volte nel testo.\n')

def Sostituisci_parole(testo):
    '''Sostituisci tutte le parole day, water e about con la parola PYTHON in tutti i versi'''
    parole_da_sostituire=['day', 'water', 'about', 'Day', 'Water', 'About']
    for parola in parole_da_sostituire:
        testo=testo.replace(parola, 'PYTHON')
    return testo

def Maiuscolo_dispari(testo):
    '''Riscrivete il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo'''
    parole=Parole(testo)
    testo_modificato=[]
    for i in range(len(parole)):
        if i % 2 == 0:  # Indici 0, 2, 4,... corrispondono a posizioni dispari
            testo_modificato.append(parole[i].upper())
        else:
            testo_modificato.append(parole[i])
    return ' '.join(testo_modificato)


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
print('Le righe non vuote sono: ', Conta_righe_non_vuote(testo))
parole_testo=Parole(testo)
print('Le parole sono: ', len(parole_testo))
caratteri_testo=Caratteri(testo)
print('I caratteri alfanumerici sono: ', len(caratteri_testo))
Conta_lettera(caratteri_testo)
print('Il testo con le parole sostituite è: ', Sostituisci_parole(testo))
print('Il testo con le parole in maiuscolo in posizione dispari è: ', Maiuscolo_dispari(testo))
