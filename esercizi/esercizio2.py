#
#esercizio2.py
#
#Creato da Valentina Furlanis IN0501333
#Data:21 marzo 2026
#
#Descrizione di cosa fa il programma esercizio2.py:
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
    righe=[i for i in testo.split('\n')]                        #creo una lista di tutte le righe del testo
    righe_non_vuote=0                                           #contatore per contare le righe non vuote
    for i in righe:                                             #scorro tutte le righe del testo
        if len(i)>0:                                            #se la lunghezza della riga è maggiore di 0, allora la riga non è vuota 
            righe_non_vuote+=1                                  #incremento il contatore delle righe non vuote   
    tupla=(righe, righe_non_vuote)                              #creo una tupla con la lista di tutte le righe del testo e il numero di righe non vuote

    return tupla                                                #restituisco la tupla

def parole(testo):
    '''Conta le parole che compongono l’estratto'''
    parole=[i for i in testo.split()]                           #creo una lista di tutte le parole del testo
    num_parole=0                                                #contatore per contare le parole del testo
    for i in parole:                                            #scorro tutte le parole del testo   
        if len(i)>0:                                            #se la lunghezza della parola è maggiore di 0, allora la parola non è vuota
            num_parole+=1                                       #incremento il contatore delle parole del testo
    tupla=(parole, num_parole)                                  #creo una tupla con la lista di tutte le parole del testo e il numero di parole del testo 

    return tupla                                                #restituisco la tupla

def caratteri(testo):
    '''Conta i caratteri alfanumerici che compongono l’estratto'''
    caratteri=list(testo)                                                           #creo una lista di tutti i caratteri del testo    
    alfabeto='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'       #creo una stringa con tutti i caratteri alfanumerici (maiuscole, minuscole e numeri)
    num_caratteri=0                                                                 #contatore per contare i caratteri alfanumerici del testo  
    for i in caratteri:                                                             #scorro tutti i caratteri del testo
        if i in alfabeto:                                                           #se il carattere è presente nella stringa dei caratteri alfanumerici, allora è un carattere alfanumerico
            num_caratteri+=1                                                        #incremento il contatore dei caratteri alfanumerici del testo
    tupla=(caratteri, num_caratteri)                                                #creo una tupla con la lista di tutti i caratteri del testo e il numero di caratteri alfanumerici del testo

    return tupla                                                                    #restituisco la tupla   

def conta_lettera(caratteri):
    '''Conta quante volte una lettera scelta dell'utente compare nel testo'''
    alfabeto='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'                             #creo una stringa con tutti i caratteri alfanumerici (maiuscole e minuscole)
    print('Inserisci una lettera da cercare: ')                                                 #chiedo all'utente di inserire una lettera da cercare nel testo
    lettera = input()
    while lettera not in alfabeto:                                                              #controllo che la lettera inserita sia una lettera dell'alfabeto (maiuscola o minuscola)
        print('Errore: devi inserire una lettera')
        lettera = input('Inserisci nuovamente la lettera: ')                                    #se non appartiene ad alfabeto, chiedo nuovamente all'utente di inserire una lettera da cercare nel testo
    conteggio = caratteri.count(lettera.lower()) + caratteri.count(lettera.upper())             #conto quante volte la lettera compare nel testo, considerando sia la minuscola che quella maiuscola
    
    print('La lettera', lettera, 'compare', conteggio, 'volte nel testo.\n')                    #stampo il risultato

def sostituisci_parole(parole_testo):
    '''Sostituisce tutte le parole day, water e about con la parola PYTHON in tutti i versi'''
    #creo una lista con tutte le parole da sostituire, considerando sia le minuscole che le maiuscole e le parole seguite da una virgola
    parole_da_sostituire=['day', 'water', 'about', 'Day', 'Water', 'About', 'day,', 'water,', 'about,', 'Day,', 'Water,', 'About,', ]       
    testo_sostituito=[]                             #creo una lista vuota per contenere il testo con le parole sostituite
    for i in parole_testo:                          #scorro tutte le parole del testo
        if i in parole_da_sostituire:               #se la parola è presente nella lista delle parole da sostituire eseguo la funzione if
            testo_sostituito.append('PYTHON')       #sostituisco la parola con PYTHON e appendo la parola sostituita alla lista del testo sostituito
        else:           
            testo_sostituito.append(i)              #se la parola non è presente nella lista delle parole da sostituire, appendo la parola originale alla lista del testo sostituito
    
    return testo_sostituito                         #restituisco il testo modificato

def maiuscolo_dispari(parole):
    '''Riscrive il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo'''
    testo_modificato=[]                                         #creo una lista vuota per contenere il testo con le parole in maiuscolo in posizione dispari
    for i in range(len(parole)):                                #scorro tutte le parole del testo, utilizzando l'indice per identificare la posizione della parola
        if i % 2 == 1:                                          #gli indici 1, 3, 5,... corrispondono a posizioni dispari
            testo_modificato.append(parole[i].upper())          #se la parola è in posizione dispari, la converto in maiuscolo e appendo la parola modificata alla lista del testo modificato
        else:
            testo_modificato.append(parole[i])                  #se la parola è in posizione pari, appendo la parola originale alla lista del testo modificato
    
    print('Il testo con le parole in maiuscolo in posizione dispari è: ')
    print(testo_modificato)                                     #stampo il testo modificato

def inverti_frasi(frasi):
    '''Riscrive il testo invertendo l’ordine delle frasi dal basso all’alto'''
    testo_invertito=[]                                  #creo una lista vuota per contenere il testo con le frasi invertite
    for i in range(len(frasi)-1,-1,-1):                 #scorro tutte le frasi del testo, partendo dall'ultima frase (indice len(frasi)-1) fino alla prima frase (indice 0)
        testo_invertito.append(frasi[i])                #appendo la frase corrente alla lista del testo invertito, in questo modo le frasi vengono appese in ordine inverso rispetto all'ordine originale
    
    print('\nIl testo con le frasi invertite è: ')
    print(testo_invertito)                              #stampo il testo con le frasi invertite

def specchio(frasi):
    '''Riscrive il testo in modo che il secondo verso di ogni strofa sia scritto a specchio (cioè al contrario carattere per carattere)'''
    testo_specchiato=[]                                 #creo una lista vuota per contenere il testo con il secondo verso di ogni strofa scritto a specchio
    for i in range(len(frasi)):                         #scorro tutte le frasi
        if i == 2 or i == 7 or i == 11:                 #il secondo verso di ogni strofa è l'indice 1, 5, 9,...
            caratteri = list(frasi[i])                  #creo una lista di tutti i caratteri della frase corrente
            frase_specchiata=[]                         #creo una lista vuota per contenere la frase con i caratteri invertiti    
            for j in range(len(caratteri)-1,-1,-1):     #scorro tutti i caratteri della frase, partendo dall'ultimo carattere (indice len(caratteri)-1) fino al primo carattere (indice 0)
                frase_specchiata.append(caratteri[j])   #appendo il carattere corrente alla lista della frase specchiata, in questo modo i caratteri vengono appesi in ordine inverso rispetto all'ordine originale
            testo_specchiato.append(frase_specchiata)   #appendo la frase specchiata alla lista del testo specchiato
        else:                                           #se la frase corrente non è il secondo verso di una strofa
            testo_specchiato.append(frasi[i])           #appendo la frase originale alla lista del testo specchiato
        
    print('\nIl testo con il secondo verso di ogni strofa scritto a specchio è: ')
    print(testo_specchiato)                             #stampo il testo modificato

def parole_comuni(testo):
    '''Trova eventuali parole che compaiono in TUTTE le strofe'''
    #creo 3 liste, una per ogni strofa
    #uso la funzione lower() su ogni strofa per ignorare la differenza tra maiuscole e minuscole
    lista_strofe=testo.split("\n\n")
    strofa1=set(lista_strofe[0].lower().split())
    strofa2=set(lista_strofe[1].lower().split())
    strofa3=set(lista_strofe[2].lower().split())
    strofa4=set(lista_strofe[3].lower().split())
    parole_comuni= strofa1 & strofa2 & strofa3 & strofa4            #utilizzo l'operatore & per trovare le parole comuni tra le 4 strofe
    if len(parole_comuni)==0:                                       #se non ci sono parole comuni
        print('No ci sono parole comuni in tutte le strofe')        #segnalo all'utente che non ci sono parole comuni in tutte le strofe
    else:
        print('\nLe parole comuni in tutte le strofe sono: ', parole_comuni)    #se ci sono parole comuni, le stampo

def lista_univoca_parole(parole):
    '''Crea la lista univoca di tutte le parole che compaiono nel testo, ordinate per lunghezza delle parole'''
    parole_univoche=set(parole)                             #creo un set con tutte le parole del testo, in questo modo ottengo solo le parole univoche (senza duplicati)
    parole_univoche=list(parole_univoche)                   #converto il set in una lista per poter ordinare le parole
    parole_univoche.sort(key=len)                           #ordino la lista delle parole univoche in base alla lunghezza delle parole, utilizzando la funzione sort() con il parametro key=len (len=lunghezza della parola)
    
    print('\nLa lista univoca di tutte le parole che compaiono nel testo, ordinata per lunghezza è: ')
    print(parole_univoche)                                  #stampo la lista univoca ordinata

def dizionario_caratteri(caratteri):
    '''Create un dizionario che mappi OGNI carattere (chiave) con la sua occorrenza nel testo (valore)'''
    dizionario={}                           #creo un dizionario vuoto per contenere i caratteri come chiavi e le loro occorrenze come valori
    for i in caratteri:                     #scorro tutti i caratteri del testo
        if i in dizionario:                 #se il carattere è già presente come chiave nel dizionario
            dizionario[i]+=1                #incremento il valore associato a quella chiave (carattere) di 1, in questo modo conto quante volte il carattere compare nel testo
        else:
            dizionario[i]=1                 #se il carattere non è presente come chiave nel dizionario, lo aggiungo al dizionario con valore 1, in questo modo conto la prima occorrenza del carattere nel testo
    
    print(dizionario)                       #stampo il dizionario

def dizionario_caratteri_alfanumerici(caratteri):
    '''Crea un dizionario che mappi i soli caratteri alfanumerici (chiave) con la sua occorrenza nel testo (valore), 
    ignorando maiuscole e minuscole'''
    dizionario={}                                               #creo un dizionario vuoto per contenere i caratteri alfanumerici come chiavi e le loro occorrenze come valori
    caratteri=[i.lower() for i in caratteri]                    #converto tutti i caratteri in minuscolo per ignorare la differenza tra maiuscole e minuscole
    for i in caratteri:                                         #scorro tutti i caratteri del testo
        if i in dizionario:                                     #se il carattere è già presente come chiave nel dizionario
            dizionario[i]+=1                                    #incremento il valore associato a quella chiave (carattere) di 1, in questo modo conto quante volte il carattere alfanumerico compare nel testo
        else:
            dizionario[i]=1                                     #se il carattere non è presente come chiave nel dizionario, lo aggiungo al dizionario con valore 1, in questo modo conto la prima occorrenza del carattere alfanumerico nel testo
    for i in list(dizionario.keys()):                           #scorro tutte le chiavi
        if i not in 'abcdefghijklmnopqrstuvwxyz1234567890':     #se la chiave (carattere) non è un carattere alfanumerico
            del dizionario[i]                                   #elimino la chiave (carattere) dal dizionario, cosí ottenendo un dizionario con solo i caratteri alfanumerici come chiavi e le loro occorrenze come valori
    
    print(dizionario)                                           #stampo il dizionario

#funzione main
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
    
    #chiamo tutte le funzioni e stampo i risultati
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




