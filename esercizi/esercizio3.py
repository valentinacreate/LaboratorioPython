#
#esercizio3.py
#Creato da Valentina Furlanis IN0501333
#Data:19 aprile 2026
#
#Descrizione di cosa fa il programma esercizio3.py:
#Partendo dal dizionario annidato rubrica
#   - Visualizzate il contenuto del dizionario stampando a schermo delle stringhe formattate che contengano la chiave ed il valor di ognuno degli elementi(Esempio: ‘Paolino Paperino’, ‘giorno’ 9, ‘mese’ ‘giugno’, …)
#   - A partire dalla rubrica, costruire la lista delle età, ordinata in ordine crescente e visualizzate i nomi in ordine crescente di età
#   - Invertire l’ordine della lista precedentemente costruita e visualizzatela
#   - Utilizzare la rubrica e scrivere su schermo per OGNI membro della rubrica, il seguente messaggio:
#       '''Car[o/a] [Nome],
#           sei nat[o/a] il [giorno] di [mese] del [anno] e quindi a breve compirai [età] anni.
#           Ti manderemo gli auguri a [mail]''' dove [o/a] deve essere adattato all’attributo [M/F]
#   - Utilizzando args passate in input al vostro programma una chiave [giorno, mese, anno, età, sesso, mail] e visualizzate tutto il contenuto della rubrica (valori) che corrispondono a questa chiave
#   - Utilizzando argparse visualizzate la stringa al punto 4 SOLO per il nome fornito come opzione al vostro programma (esempio: python esercizio_3.py –nome ‘Madoka Ayukawa’ –> esegue punto 4 solo per il nome indicato)
#   - Utilizzando argparse introducede delle opzioni al vostro programma per eseguire i punti 1, 2, 3, 4, 5 dell’esercizio (esempio: python esercizio_3.py –lista_ordinata –> esegue il punto 2 dell’esercizio)

import argparse                         #importo la libreria argparse per gestire gli argomenti da linea di comando

rubrica = {
    'Paolino Paperino': {'giorno': 9,
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 93,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
    'Ron Weasley': {'giorno': 1, 
                'mese': 'marzo', 
                'anno': 1980, 
                'età': 46, 
                'sesso': 'M', 
                'mail': 'ron_weasley80@hogwards.uk'},
    'Ramona Flowers': {'giorno': 19, 
                'mese': 'ottobre', 
                'anno': 2004, 
                'età': 22, 
                'sesso': 'F', 
                'mail': 'ramona.fls@gmail.com'},
    'Madoka Ayukawa': {'giorno': 25, 
                'mese': 'maggio', 
                'anno': 1969, 
                'età': 57, 
                'sesso': 'F', 
                'mail': 'madoka_sax@asahi_net.jp'}
}

def stampa_contenuto(rubrica):
    '''Visualizza il contenuto del dizionario stampando a schermo delle stringhe formattate che contengano la chiave ed il valor di ognuno degli elementi(Esempio: ‘Paolino Paperino’, ‘giorno’ 9, ‘mese’ ‘giugno’, …)'''
    print('Contenuto della rubrica:')
    for nome, info in rubrica.items():              #itero su ogni elemento del dizionario rubrica
        print(f'{nome}:')                           #stampo il nome del membro della rubrica
        for chiave,valore in info.items():          #itero su ogni chiave e valore del dizionario annidato info
            print(f'{chiave}: {valore}')            #stampo la chiave e il valore corrispondente
        print('\n')

def ordinamento_eta_crescente(rubrica):
    '''A partire dalla rubrica, costruisce la lista delle età, ordinata in ordine crescente e visualizza
       i nomi in ordine crescente di età'''
    lista_eta = []                                      #creo una lista vuota per memorizzare le età e i nomi
    for nome,info in rubrica.items():                   #itero su ogni elemento del dizionario rubrica
        lista_eta.append([info['età'], nome])           #aggiungo alla lista_eta una lista contenente l'età e il nome del membro della rubrica
        lista_eta.sort()                                #ordino la lista_eta in ordine crescente di età (il primo elemento della lista è l'età)
    print('\nNomi in ordine crescente di età:\n')       
    for eta , nome in lista_eta:                        #itero su ogni elemento della lista_eta
        print(f'{nome}: {eta} anni' + '\n')             #stampo il nome e l'età del membro della rubrica in ordine crescente di età

def ordinamento_eta_decrescente(rubrica):
    '''Inverto la lista dei nomi in ordine decrescente'''
    lista_eta = []                                      #creo una lista vuota per memorizzare le età e i nomi
    for nome,info in rubrica.items():                   #itero su ogni elemento del dizionario rubrica
        lista_eta.append([info['età'], nome])           #aggiungo alla lista_eta una lista contenente l'età e il nome del membro della rubrica
        lista_eta.sort()                                #ordino la lista_eta in ordine crescente di età (il primo elemento della lista è l'età)
    print('\nNomi in ordine decrescente di età:\n')
    for i in range(len(lista_eta)-1,-1,-1):             #itero sulla lista_eta in ordine inverso (partendo dall'ultimo elemento fino al primo)
        eta , nome = lista_eta[i]                       #assegno l'età e il nome del membro della rubrica alla variabile eta e nome
        
        print(f'{nome}: {eta} anni' + '\n')             #stampo il nome e l'età del membro della rubrica in ordine decrescente di età

def stampa_messaggio(rubrica):
    '''Per OGNI membro della rubrica, stampa il seguente messaggio:'''
    for nome, info in rubrica.items():                  #itero su ogni elemento del dizionario rubrica
        if info['sesso']=='M':                          #se il sesso è maschile
            desinenza='o'                               #la desinenza è 'o'
        else:                   
            desinenza='a'                               #altrimenti la desinenza è 'a'
      
        #stampo il messaggio formattato con le informazioni del membro della rubrica, adattando la desinenza in base al sesso
        print(f'Car{desinenza} {nome}, \nsei nat{desinenza} il {info["giorno"]} di {info["mese"]} del {info["anno"]} e quindi a breve compirai {info["età"]} anni.\nTi manderemo gli auguri a {info["mail"]}')

parser = argparse.ArgumentParser()                                          #creo un oggetto parser per gestire gli argomenti da linea di comando
#aggiungo gli argomenti al parser per eseguire le diverse funzionalità del programma in base agli argomenti forniti da linea di comando
parser.add_argument('--chiave', 
                    help='Chiave per filtrare i dati della rubrica')
parser.add_argument('--stampa_contenuto',
                    help='Stampa il contenuto della rubrica')
parser.add_argument('--lista_eta_crescente',
                    help='Visualizza i nomi in ordine crescente di età')
parser.add_argument('--lista_eta_decrescente',
                    help='Visualizza i nomi in ordine decrescente di età')
parser.add_argument('--nome_esteso', nargs='+',
                    help='Nome specifico per visualizzare il messaggio personalizzato')

args = parser.parse_args()                          #passo gli argomenti da linea di comando al parser e li memorizzo nella variabile args

def visualizza_contenuto_chiave():
    '''Visualizza tutto il contenuto della rubrica (valori) che corrispondono a questa chiave'''
    key=args.chiave                                                             #assegno alla variabile key il valore dell'argomento chiave fornito da linea di comando
    if args.chiave:                                                         #se è stata fornita una chiave da linea di comando
        if key in ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']:       #
            print(f'Contenuto della rubrica per la chiave "{key}":')
            for nome, info in rubrica.items():
                print(info[key])
            controllo=False
        else:
            print(f'La chiave "{key}" non è valida. Scegli tra "giorno", "mese", "anno", "età", "sesso", "mail".')
    else:
        print('Nessuna chiave fornita. Utilizza l\'opzione -k o --chiave per specificare una chiave.')                                                         #se non è stata fornita una chiave da linea di comando, stampo un messaggio di errore e termino il ciclo

def visualizza_messaggio_nome_specifico():
    '''Visualizza il messaggio per un nome specifico nella rubrica'''
    nome =' '.join(args.nome_esteso)
    controllo=True
    while(controllo==True):
        if args.nome_esteso:
            if nome in rubrica:
                info = rubrica[nome]
                if info['sesso']=='M':
                    desinenza='o'
                else:
                    desinenza='a'
                print(f'Car{desinenza} {nome}, \nsei nat{desinenza} il {info["giorno"]} di {info["mese"]} del {info["anno"]} e quindi a breve compirai {info["età"]} anni.\nTi manderemo gli auguri a {info["mail"]}')
                controllo=False
            else:
                print(f'Il nome "{nome}" non è valido. Scegli tra i nomi presenti nella rubrica.')
                controllo=False
        else:
            print('Nessuna chiave fornita. Utilizza l\'opzione -k o --chiave per specificare una chiave.')
            controllo=False

def main():
    if args.stampa_contenuto:
        stampa_contenuto(rubrica)
    if args.lista_eta_crescente:
        ordinamento_eta_crescente(rubrica)
    if args.lista_eta_decrescente:
        ordinamento_eta_decrescente(rubrica)
    if args.nome_esteso:
        visualizza_messaggio_nome_specifico()
    if args.chiave:
        visualizza_contenuto_chiave()
    else:
        print('ERRORE. Utilizza --help per vedere le opzioni disponibili.')

main()