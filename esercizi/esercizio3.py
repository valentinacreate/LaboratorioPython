#
#esercizio3.py
#Creato da Valentina Furlanis IN0501333
#Data:19 aprile 2026
#
#Descrizione codice
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

import argparse

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
    for nome, info in rubrica.items():
        print(f'{nome}:')
        for chiave,valore in info.items():
            print(f'    {chiave}:{valore}')
        print('\n')

def ordinamento_eta_crescente(rubrica):
    '''A partire dalla rubrica, costruisce la lista delle età, ordinata in ordine crescente e visualizza
       i nomi in ordine crescente di età'''
    lista_eta = []
    for nome,info in rubrica.items():
        lista_eta.append([info['età'], nome])
        lista_eta.sort()
    print('\nNomi in ordine crescente di età:\n')
    for eta , nome in lista_eta:
        print(f'{nome}: {eta} anni' + '\n')

def ordinamento_eta_decrescente(rubrica):
    '''Inverto la lista dei nomi in ordine decrescente'''
    lista_eta = []
    for nome,info in rubrica.items():
        lista_eta.append([info['età'], nome])
        lista_eta.sort()
    print('\nNomi in ordine decrescente di età:\n')
    for i in range(len(lista_eta)-1,-1,-1):
        eta , nome = lista_eta[i]
        print(f'{nome}: {eta} anni' + '\n')

def stampa_messaggio(rubrica):
    '''Per OGNI membro della rubrica, stampa il seguente messaggio:'''
    for nome, info in rubrica.items():
        if info['sesso']=='M':
            x='o'
        else:
            x='a'
        print(f'Car{x} {nome}, \nsei nat{x} il {info["giorno"]} di {info["mese"]} del {info["anno"]} e quindi a breve compirai {info["età"]} anni.\nTi manderemo gli auguri a {info["mail"]}')

parser = argparse.ArgumentParser()
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

args = parser.parse_args()

def visualizza_contenuto_chiave():
    '''Visualizza tutto il contenuto della rubrica (valori) che corrispondono a questa chiave'''
    k=args.chiave
    p=True
    while(p==True):
        if args.chiave:
            if k in ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']:
                print(f'Contenuto della rubrica per la chiave "{k}":')
                for nome, info in rubrica.items():
                    print(info[k])
                p=False
            else:
                print(f'La chiave "{k}" non è valida. Scegli tra "giorno", "mese", "anno", "età", "sesso", "mail".')
                p=False
        else:
            print('Nessuna chiave fornita. Utilizza l\'opzione -k o --chiave per specificare una chiave.')
            p=False

def visualizza_messaggio_nome_specifico():
    '''Visualizza il messaggio per un nome specifico nella rubrica'''
    nome =' '.join(args.nome_esteso)
    p=True
    while(p==True):
        if args.nome_esteso:
            if nome in rubrica:
                info = rubrica[nome]
                if info['sesso']=='M':
                    x='o'
                else:
                    x='a'
                print(f'Car{x} {nome}, \nsei nat{x} il {info["giorno"]} di {info["mese"]} del {info["anno"]} e quindi a breve compirai {info["età"]} anni.\nTi manderemo gli auguri a {info["mail"]}')
                p=False
            else:
                print(f'Il nome "{nome}" non è valido. Scegli tra i nomi presenti nella rubrica.')
                p=False
        else:
            print('Nessuna chiave fornita. Utilizza l\'opzione -k o --chiave per specificare una chiave.')
            p=False

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