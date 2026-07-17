
#Rubrica.py
#Creato da: Valentina Furlanis IN0501333
#Data: 29 aprile 2026

#La classe rubrica deve fare 5 azioni:
#   - aprire una rubrica leggendola da un file (JSON oppure testo) - APRI
#   - aggiungere un elemento alla rubrica - AGGIUNGI
#   - rimuovere un elemento dalla rubrica (dato il nome) - RIMUOVI
#   - salvare la rubrica su un file (JSON o testo) - SALVA
#   - stampare tutte le informazioni di un contatto (data il nome), come nell’eserczio 3 - STAMPA

import json                                                                     #importazione del modulo json per la gestione dei file JSON
import datetime                                                                 #importazione del modulo datetime per ottenere la data odierna e calcolare l'età dei contatti in base alla data di nascita

giorno_oggi = datetime.datetime.now().day                                       #ottenimento del giorno odierno utilizzando il metodo now() del modulo datetime e accedendo all'attributo day
mese_oggi = datetime.datetime.now().month                                       #ottenimento del mese odierno utilizzando il metodo now() del modulo datetime e accedendo all'attributo month
anno_oggi = datetime.datetime.now().year                                        #ottenimento dell'anno odierno utilizzando il metodo now() del modulo datetime e accedendo all'attributo year

class Rubrica:                                                                  #definizione della classe Rubrica che contiene i metodi per gestire la rubrica dei contatti
    '''Una classe che rappresenta e permette di operare con una Rubrica'''
    def __init__(self):  
        '''Inizializzazione della classe Rubrica con un dizionario vuoto per memorizzare le informazioni dei contatti'''                                                   
        self.info = {}                                                                  #inizializzazione del dizionario info come attributo della classe Rubrica

    @classmethod                                                        
    def from_json(cls, filename):                                               #classmethod che permette di creare un'istanza della classe Rubrica a partire da un file JSON
        instance = cls()                                                        #creazione di un'istanza della classe Rubrica   
        with open(filename, 'r', encoding='utf-8') as in_file:                  #apertura del file JSON in modalità lettura con codifica UTF-8
            instance.info = json.load(in_file)                                  #caricamento dei dati dal file JSON nel dizionario info dell'istanza della classe Rubrica
        return instance                                                         #restituzione dell'istanza della classe Rubrica con i dati caricati dal file JSON

    @classmethod
    def from_txt(cls, filename):                                                        #classmethod che permette di creare un'istanza della classe Rubrica a partire da un file di testo
        instance = cls()                                                                #creazione di un'istanza della classe Rubrica
        with open(filename, 'r', encoding='utf-8') as in_file:                          #apertura del file di testo in modalità lettura con codifica UTF-8
            for line in in_file:                                                        #lettura del file di testo riga per riga
                nome, giorno, mese, anno, eta, sesso, mail = line.strip().split(', ')   #suddivisione di ogni riga in base alla virgola e assegnazione dei valori alle variabili corrispondenti
                instance.info[nome] = {                                                 
                    'giorno': int(giorno),
                    'mese': mese,
                    'anno': int(anno),
                    'età': int(eta),
                    'sesso': sesso,
                    'mail': mail
                }
        return instance                                                                 #restituzione dell'istanza della classe Rubrica con i dati caricati dal file di testo

    def apri(self, rubrica): 
        '''Metodo per aprire una rubrica da un file, che può essere in formato JSON o testo, e caricare i dati nel dizionario info della classe Rubrica'''                                                           
        if rubrica.endswith('.json'):                                                           #controllo se il nome del file termina con l'estensione .json
            with open(rubrica, 'r', encoding='utf-8') as in_file:                               #apertura del file JSON in modalità lettura con codifica UTF-8
                self.info = json.load(in_file)                                                  #caricamento dei dati dal file JSON nel dizionario info della classe Rubrica      
        elif rubrica.endswith('.txt'):                                                          #controllo se il nome del file termina con l'estensione .txt
            with open(rubrica, 'r', encoding='utf-8') as in_file:                               #apertura del file di testo in modalità lettura con codifica UTF-8
                for line in in_file:                                                            #lettura del file di testo riga per riga
                    nome, giorno, mese, anno, eta, sesso, mail = line.strip().split(', ')       #suddivisione di ogni riga in base alla virgola e assegnazione dei valori alle variabili corrispondenti
                    self.info[nome] = {                                                         
                        'giorno': int(giorno),
                        'mese': mese,
                        'anno': int(anno),
                        'età': int(eta),
                        'sesso': sesso,
                        'mail': mail
                    }
        else:                                                                                   #se il nome del file non termina con l'estensione .json o .txt
            print("Il file deve terminare con .json o .txt")                                    #stampa un messaggio di errore indicando che il file deve avere un'estensione valida
        return self.info                                                                        #restituzione del dizionario info della classe Rubrica con i dati caricati dal file

    def aggiungi(self):                                                    
        '''Metodo per aggiungere un nuovo contatto alla rubrica, chiedendo all'utente di inserire le informazioni necessarie e calcolando automaticamente l'età in base alla data di nascita'''
        if not self.info:                                                                       #controllo se il dizionario info è vuoto
            print("\nPrima apri una rubrica")                                                   #stampa un messaggio di errore indicando che è necessario aprire una rubrica prima di aggiungere un contatto
            return                                                                              #esce dal metodo se la rubrica è vuota      

        print("\nDati del nuovo contatto:")                                                     #stampa un messaggio che indica all'utente che deve inserire i dati del nuovo contatto      
        while True:
            print("\nInserire il nome completo da aggiungere:")
            nome = input().strip()
            if nome:                                                                            #ciclo che continua a chiedere all'utente di inserire un nome completo finché non viene inserito un nome valido (non vuoto)
                nome = " ".join([parte.capitalize() for parte in nome.split()])                 #capitalizzazione di ogni parte del nome inserito dall'utente per garantire un formato uniforme dei nomi nella rubrica
                break                                                                           #esce dal ciclo while se un nome valido è stato inserito
            print("\nNome non valido. Inserire almeno un nome.")                                #stampa un messaggio di errore indicando che il nome inserito non è valido e chiede all'utente di inserire almeno un nome

        while True:                                                                             #ciclo che continua a chiedere all'utente di inserire un giorno di nascita finché non viene inserito un valore valido (compreso tra 1 e 31)
            print('\nInserire il giorno di nascita:')                                           #stampa un messaggio che chiede all'utente di inserire il giorno di nascita del nuovo contatto
            giorno = int(input())                                                               #legge l'input dell'utente per il giorno di nascita e lo converte in un intero  
            if 1 <= giorno <= 31:                                                               #verifica se il giorno inserito è compreso tra 1 e 31
                break                                                                           #esce dal ciclo while se un giorno valido è stato inserito
            print("Valore non valido. Inserire un giorno compreso tra 1 e 31.")                 #stampa un messaggio di errore indicando che il giorno inserito non è valido e chiede all'utente di inserire un giorno compreso tra 1 e 31

        while True:                                                                             #ciclo che continua a chiedere all'utente di inserire un mese di nascita finché non viene inserito un valore valido (uno dei 12 mesi dell'anno)
            print('\nInserire il nome del mese di nascita:')                                    #stampa un messaggio che chiede all'utente di inserire il nome del mese di nascita del nuovo contatto           
            mese = input().strip()                                                              #legge l'input dell'utente per il mese di nascita e rimuove eventuali spazi bianchi all'inizio o alla fine del nome del mese
            #se il nome del mese inserito è valido
            if mese.capitalize() in ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']:
                mese = mese.capitalize()                                                        #capitalizzazione del nome del mese inserito dall'utente per garantire un formato uniforme dei mesi nella rubrica
                break                                                                           #esce dal ciclo while se un mese valido è stato inserito
            print("Valore non valido. Inserire un mese valido (es. Gennaio, Febbraio, etc.).")  #stampa un messaggio di errore indicando che il mese inserito non è valido e chiede all'utente di inserire un mese valido (ad esempio, Gennaio, Febbraio, etc.)
        #per calcolare l'età, associo ad ogni mese il suo numero corrispondente (Gennaio=1, Febbraio=2, etc.) per poter confrontare correttamente la data di nascita con la data odierna e calcolare l'età in modo accurato
        if mese=='Gennaio':
            mese_num = 1
        elif mese=='Febbraio':
            mese_num = 2
        elif mese=='Marzo':     
            mese_num = 3
        elif mese=='Aprile':
            mese_num = 4
        elif mese=='Maggio':
            mese_num = 5
        elif mese=='Giugno':
            mese_num = 6
        elif mese=='Luglio':
            mese_num = 7
        elif mese=='Agosto':
            mese_num = 8
        elif mese=='Settembre':
            mese_num = 9
        elif mese=='Ottobre':
            mese_num = 10
        elif mese=='Novembre':      
            mese_num = 11
        else:
            mese_num = 12

        while True:                                                                 #ciclo che continua a chiedere all'utente di inserire un anno di nascita finché non viene inserito un valore valido (un anno che non sia nel futuro rispetto all'anno odierno)  
            anno = int(input('\nInserire l\'anno di nascita:'))                     #stampa un messaggio che chiede all'utente di inserire l'anno di nascita del nuovo contatto e legge l'input dell'utente per l'anno di nascita e lo converte in un intero 
            if anno <= anno_oggi:                                                   #verifica se l'anno inserito è minore o uguale all'anno odierno per assicurarsi che l'anno di nascita non sia nel futuro
                break                                                               #esce dal ciclo while se un anno valido è stato inserito
            else:                                                                   
                print("Valore non valido. L'anno non può essere nel futuro.")       #stampa un messaggio di errore indicando che l'anno inserito non è valido perché è nel futuro e chiede all'utente di inserire un anno valido

        #inserimento automatico dell'età
        eta = anno_oggi - anno                                                          #calcolo dell'età sottraendo l'anno di nascita dall'anno odierno
        if (mese_oggi < mese_num) or (mese_oggi == mese_num and giorno_oggi < giorno):  #se il mese odierno è minore del mese di nascita o se il mese odierno è uguale al mese di nascita ma il giorno odierno è minore del giorno di nascita, significa che il compleanno del contatto non è ancora passato nell'anno in corso
            eta -= 1                                                                    #in questo caso, sottraggo 1 all'età calcolata per ottenere l'età corretta del contatto 
        print("\nInserimento automatico dell'età:", eta)                                #stampa un messaggio che indica all'utente l'età calcolata automaticamente in base alla data di nascita inserita

        while True:                                                                     #ciclo che continua a chiedere all'utente di inserire un sesso finché non viene inserito un valore valido (M o F)
            print("\nInserire il sesso, M o F:")                                        #stampa un messaggio che chiede all'utente di inserire il sesso del nuovo contatto, specificando che deve essere M o F
            sesso = input().strip()                                                     #legge l'input dell'utente per il sesso e rimuove eventuali spazi bianchi all'inizio o alla fine del valore inserito
            if sesso.upper() in ['M', 'F']:                                             #se il maiuscolo del sesso inserito è M o F, il valore è valido
                sesso = sesso.upper()                                                   #conversione del sesso inserito in maiuscolo per garantire un formato uniforme dei valori di sesso nella rubrica        
                break                                                                   #esce dal ciclo while se un sesso valido è stato inserito        
            print("Valore non valido. Inserire 'M' o 'F'.")                             #altrimenti, se il sesso inserito non è M o F, stampa un messaggio di errore indicando che il valore inserito non è valido e chiede all'utente di inserire 'M' o 'F'

        print("\nInserire la mail:")                                                    #stampa un messaggio che chiede all'utente di inserire la mail del nuovo contatto
        mail = input().strip()                                                          #legge l'input dell'utente per la mail e rimuove eventuali spazi bianchi all'inizio o alla fine del valore inserito

        #aggiunta del nuovo contatto al dizionario info della classe Rubrica, utilizzando il nome come chiave e un dizionario con le informazioni del contatto come valore
        self.info[nome] = {
            'giorno': giorno,
            'mese': mese,
            'anno': anno,
            'età': eta,
            'sesso': sesso,
            'mail': mail
        }

    def rimuovi(self, nome):                                                        
        '''Metodo per rimuovere un contatto dalla rubrica, dato il nome del contatto da rimuovere, con controlli per verificare che la rubrica non sia vuota e che il contatto esista prima di tentare di rimuoverlo'''
        nome = " ".join([parte.capitalize() for parte in nome.split()])             #capitalizzazione di ogni parte del nome inserito dall'utente per garantire un formato uniforme dei nomi nella rubrica e facilitare il confronto con i nomi dei contatti presenti nella rubrica
        if not self.info:                                                           #controllo se il dizionario info è vuoto
            print("\nLa rubrica è vuota")                                           #stampa un messaggio di errore indicando che la rubrica è vuota e non è possibile rimuovere un contatto
            return                                                                  #esce dal metodo se la rubrica è vuota

        while nome not in self.info:                                                #ciclo che continua a chiedere all'utente di inserire un nome valido finché il nome inserito non corrisponde a un contatto presente nella rubrica
            print(f"\nIl contatto {nome} non esiste in rubrica")                    #stampa un messaggio di errore indicando che il contatto con il nome inserito non esiste nella rubrica
            print('Se hai sbagliato sezione digita NONE')                           #stampa un messaggio che indica all'utente che se ha sbagliato sezione può digitare "NONE" per uscire dal ciclo di inserimento del nome
            print('\nInserire un nome valido:')                                     #stampa un messaggio che chiede all'utente di inserire un nome valido (un nome che corrisponda a un contatto presente nella rubrica)
            nome = input().strip()                                                  #legge l'input dell'utente per il nome da rimuovere e rimuove eventuali spazi bianchi all'inizio o alla fine del nome
            if nome.upper() == 'NONE':                                              #se l'utente inserisce "NONE"
                return                                                              #esce dal metodo, interrompendo il processo di rimozione del contatto
            nome = " ".join([parte.capitalize() for parte in nome.split()])         #se il nome inserito non è "NONE", capitalizza ogni parte del nome per garantire un formato uniforme dei nomi nella rubrica e facilitare il confronto con i nomi dei contatti presenti nella rubrica

        del self.info[nome]                                                         #rimozione del contatto dal dizionario info della classe Rubrica utilizzando il nome come chiave        
        print(f"Contatto {nome} rimosso dalla rubrica.")                            #stampa un messaggio che indica all'utente che il contatto con il nome specificato è stato rimosso dalla rubrica    

    def salva(self, nome_file):                                 
        '''Metodo per salvare la rubrica su un file, che può essere in formato JSON o testo, con controlli per
        verificare che la rubrica non sia vuota prima di tentare di salvarla e per assicurarsi che il nome del file abbia un'estensione valida'''
        if not self.info:                                                           #controllo se il dizionario info è vuoto
            print("\nLa rubrica è vuota")                                           #stampa un messaggio di errore indicando che la rubrica è vuota e non è possibile salvarla su un file
            return                                                                  #esce dal metodo se la rubrica è vuota      

        if nome_file.endswith('.json'):                                             #controllo se il nome del file termina con l'estensione .json
            with open(nome_file, 'w', encoding='utf-8') as out_file:                #apertura del file JSON in modalità scrittura con codifica UTF-8
                json.dump(self.info, out_file, indent=4)                            #salvataggio dei dati della rubrica nel file JSON utilizzando la funzione dump del modulo json, con un'indentazione di 4 spazi per rendere il file più leggibile
            print('\nRubrica salvata con successo.')                                #stampa un messaggio che indica all'utente che la rubrica è stata salvata con successo su un file JSON
        elif nome_file.endswith('.txt'):                                            #controllo se il nome del file termina con l'estensione .txt
            with open(nome_file, 'w', encoding='utf-8') as out_file:                #apertura del file di testo in modalità scrittura con codifica UTF-8
                for nome, contatto in self.info.items():                            #iterazione sui contatti presenti nel dizionario info della classe Rubrica, ottenendo il nome del contatto e le informazioni corrispondenti
                    #creazione di una riga di testo per ogni contatto, formattata con i campi separati da una virgola e uno spazio, e scrittura della riga nel file di testo
                    line = f"{nome}, {contatto['giorno']}, {contatto['mese']}, {contatto['anno']}, {contatto['età']}, {contatto['sesso']}, {contatto['mail']}\n"
                    out_file.write(line)                                            #scrittura della riga nel file di testo
            print('\nRubrica salvata con successo.')                                #stampa un messaggio che indica all'utente che la rubrica è stata salvata con successo su un file di testo
        else:                                                                       #se il nome del file non termina con l'estensione .json o .txt  
            print("\nEstensione del file non valida. Scegliere .json o .txt.")      #stampa un messaggio di errore indicando che l'estensione del file non è valida e chiede all'utente di scegliere un'estensione valida (.json o .txt)

    def stampa(self, nome):
        '''Metodo per stampare tutte le informazioni di un contatto, dato il nome del contatto da stampare, con controlli per verificare che la rubrica non sia vuota e che il contatto esista prima di tentare di stampare le informazioni'''
        nome = " ".join([parte.capitalize() for parte in nome.split()])             #capitalizzazione di ogni parte del nome inserito dall'utente per garantire un formato uniforme dei nomi nella rubrica e facilitare il confronto con i nomi dei contatti presenti nella rubrica
        if not self.info:                                                           #controllo se il dizionario info è vuoto
            print("\nLa rubrica è vuota")                                           #stampa un messaggio di errore indicando che la rubrica è vuota e non è possibile stampare le informazioni di un contatto
            return                                                                  #esce dal metodo se la rubrica è vuota      

        while nome not in self.info:                                                #ciclo che continua a chiedere all'utente di inserire un nome valido finché il nome inserito non corrisponde a un contatto presente nella rubrica
            print(f"\nIl contatto {nome} non esiste in rubrica")                    #stampa un messaggio di errore indicando che il contatto con il nome inserito non esiste nella rubrica
            print('Se hai sbagliato sezione digita NONE')                           #stampa un messaggio che indica all'utente che se ha sbagliato sezione può digitare "NONE" per uscire dal ciclo di inserimento del nome
            print('\nInserire un nome valido:')                                     #stampa un messaggio che chiede all'utente di inserire un nome valido (un nome che corrisponda a un contatto presente nella rubrica)
            nome = input().strip()                                                  #legge l'input dell'utente per il nome da stampare e rimuove eventuali spazi bianchi all'inizio o alla fine del nome
            if nome.upper() == 'NONE':                                              #se l'utente inserisce "NONE"
                return                                                              #esce dal metodo, interrompendo il processo di stampa delle informazioni del contatto       
            nome = " ".join([parte.capitalize() for parte in nome.split()])         #se il nome inserito non è "NONE", capitalizza ogni parte del nome per garantire un formato uniforme dei nomi nella rubrica e facilitare il confronto con i nomi dei contatti presenti nella rubrica

        contatto = self.info[nome]                                                  #ottenimento delle informazioni del contatto dal dizionario info della classe Rubrica utilizzando il nome come chiave
        #stampa delle informazioni del contatto in un formato leggibile, con ogni campo su una nuova riga e con etichette per identificare ogni campo
        print(f"\nNome: {nome}")
        print(f"Giorno di nascita: {contatto['giorno']}")
        print(f"Mese di nascita: {contatto['mese']}")
        print(f"Anno di nascita: {contatto['anno']}")
        print(f"Età: {contatto['età']}")
        print(f"Sesso: {contatto['sesso']}")
        print(f"Mail: {contatto['mail']}")
