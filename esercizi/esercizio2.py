#
#esercizio2.py
#
#Creato da Valentina Furlanis IN0501333
#Data:21 marzo 2026
#
#Descrizione di cosa fa il programma Esercizio 2.py:
#   Il programma analizza un testo (in questo caso, una poesia) e restituisce:
#       - Contate le righe non vuote che compongono l’estratto
#       - Contate le parole che compongono l’estratto
#       - Contate i caratteri alfanumerici che compongono l’estratto
#       - Chiedere all’utente una lettera e contate quante volte compare nel testo
#       - Sostituite tutte le parole day, water e about con la parola PYTHON in tutti i versi
#       - Riscrivete il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo
#       - Riscrivere il testo invertendo l’ordine delle frasi dal basso all’alto.
#       - Riscrivete il testo in modo che il secondo verso di ogni strofa sia scritto a specchio (cioè al contrario carattere per carattere: Ad esempio, questa frase’ –> ‘esarf atseuq ,oipmese dA’)
#       - Trovate eventuali parole che compaiono in tutte le strofe
#       - Create la lista univoca di tutte le parole che compaiono nel testo, ordinatela per lunghezza delle parole e visualizzatela
#       - Create un dizionario che mappi OGNI carattere (chiave) con la sua occorrenza nel testo (valore) e visualizzatelo
#       - Create un dizionario come il precedente per i soli caratteri alfanumerici (no caratteri speciali), ignorando maiuscole e minuscole


def conta_righe_non_vuote(testo): 
    '''Conta le righe non vuote che compongono l’estratto''' 
    righe=[i for i in testo.split('\n')]
    righe_non_vuote=0
    for i in righe:
        if len(i)>0:
            righe_non_vuote+=1
    tupla=(righe, righe_non_vuote)
    return tupla

def parole(testo):
    '''Conta le parole che compongono l’estratto'''
    parole=[i for i in testo.split()]
    num_parole=0
    for i in parole:
        if len(i)>0:
            num_parole+=1
    tupla=(parole, num_parole)
    return tupla

def caratteri(testo):
    '''Conta i caratteri alfanumerici che compongono l’estratto'''
    caratteri=list(testo)
    alfabeto='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    num_caratteri=0
    for i in caratteri:
        if i in alfabeto:
            num_caratteri+=1
    tupla=(caratteri, num_caratteri)
    return tupla

def conta_lettera(caratteri):
    '''Conta quante volte compare una lettera nel testo'''
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

def sostituisci_parole(parole_testo):
    '''Sostituisce tutte le parole day, water e about con la parola PYTHON in tutti i versi'''
    parole_da_sostituire=['day', 'water', 'about', 'Day', 'Water', 'About', 'day,', 'water,', 'about,', 'Day,', 'Water,', 'About,', ]
    testo_sostituito=[]
    for i in parole_testo:
        if i in parole_da_sostituire:
            testo_sostituito.append('PYTHON')
        else:
            testo_sostituito.append(i)
    return testo_sostituito

def maiuscolo_dispari(parole):
    '''Riscrive il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo'''
    testo_modificato=[]
    for i in range(len(parole)):
        if i % 2 == 1:  # Indici 1, 3, 5,... corrispondono a posizioni dispari
            testo_modificato.append(parole[i].upper())
        else:
            testo_modificato.append(parole[i])
    print('Il testo con le parole in maiuscolo in posizione dispari è: ')
    print(testo_modificato)

def inverti_frasi(frasi):
    '''Riscrive il testo invertendo l’ordine delle frasi dal basso all’alto'''
    testo_invertito=[]
    for i in range(len(frasi)-1,-1,-1):
        testo_invertito.append(frasi[i])
    print('\nIl testo con le frasi invertite è: ')
    print(testo_invertito)

def specchio(frasi):
    '''Riscrive il testo in modo che il secondo verso di ogni strofa sia scritto a specchio (cioè al contrario carattere per carattere)'''
    testo_specchiato=[]
    for i in range(len(frasi)):
        if i == 2 or i == 7 or i == 11:  # Il secondo verso di ogni strofa è l'indice 1, 5, 9,...
            caratteri = list(frasi[i])
            frase_specchiata=[]
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

def parole_comuni(testo):
    '''Trova eventuali parole che compaiono in TUTTE le strofe'''
    #creo 3 liste, una per ogni strofa
    lista_strofe=testo.split("\n\n")
    strofa1=set(lista_strofe[0].lower().split())
    strofa2=set(lista_strofe[1].lower().split())
    strofa3=set(lista_strofe[2].lower().split())
    strofa4=set(lista_strofe[3].lower().split())
    parole_comuni= strofa1 & strofa2 & strofa3 & strofa4
    if len(parole_comuni)==0:
        print('No ci sono parole comuni in tutte le strofe')
    else:
        print('\nLe parole comuni in tutte le strofe sono: ', parole_comuni)

def lista_univoca_parole(parole):
    '''Crea la lista univoca di tutte le parole che compaiono nel testo, ordinate per lunghezza delle parole'''
    parole_univoche=set(parole)
    parole_univoche=list(parole_univoche)
    parole_univoche.sort(key=len)
    print('\nLa lista univoca di tutte le parole che compaiono nel testo, ordinata per lunghezza è: ')
    print(parole_univoche)

def dizionario_caratteri(caratteri):
    '''Create un dizionario che mappi OGNI carattere (chiave) con la sua occorrenza nel testo (valore)'''
    dizionario={}
    for i in caratteri: 
        if i in dizionario:
            dizionario[i]+=1
        else:
            dizionario[i]=1
        
    print(dizionario)

def dizionario_caratteri_alfanumerici(caratteri):
    '''Crea un dizionario che mappi i soli caratteri alfanumerici (chiave) con la sua occorrenza nel testo (valore), 
    ignorando maiuscole e minuscole'''
    dizionario={}
    caratteri=[i.lower() for i in caratteri] #converto tutti i caratteri in minuscolo per ignorare la differenza tra maiuscole e minuscole
    for i in caratteri: 
        if i in dizionario:
            dizionario[i]+=1
        else:
            dizionario[i]=1
    for i in list(dizionario.keys()):
        if i not in 'abcdefghijklmnopqrstuvwxyz1234567890':
            del dizionario[i]

    print(dizionario)

#main program
def main():
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

    (righe, righe_non_vuote)=conta_righe_non_vuote(testo)
    print('Le righe non vuote sono: ', righe_non_vuote)
    (parole_testo, num_parole)=parole(testo)
    print('Le parole sono: ', num_parole)
    (caratteri_testo, num_caratteri)=caratteri(testo)
    print('I caratteri alfanumerici sono: ', num_caratteri)
    conta_lettera(caratteri_testo)
    print('Il testo con le parole sostituite è: ', sostituisci_parole(parole_testo))
    maiuscolo_dispari(parole_testo)
    inverti_frasi(righe)
    specchio(righe)
    parole_comuni(testo)
    lista_univoca_parole(parole_testo)
    dizionario_caratteri(caratteri_testo)
    dizionario_caratteri_alfanumerici(caratteri_testo)


main()




