#la classe rubrica deve fare 5 azioni:
#   - aprire una rubrica leggendola da un file (JSON oppure testo) - APRI
#   - aggiungere un elemento alla rubrica - AGGIUNGI
#   - rimuovere un elemento dalla rubrica (dato il nome) - RIMUOVI
#   - salvare la rubrica su un file (JSON o testo) - SALVA
#   - stampare tutte le informazioni di un contatto (data il nome), come nell’eserczio 3 - STAMPA
import json
import datetime
giorno_oggi = datetime.datetime.now().day
mese_oggi = datetime.datetime.now().month
anno_oggi = datetime.datetime.now().year

class Rubrica:
    def __init__(self):
        self.info= {}   

    def apri(self, rubrica):
        if rubrica.endswith('.json'):
            with open(rubrica, 'r', encoding='utf-8') as in_file:       # encoding='utf-8' serve a gestire correttamente lettere accentate e caratteri speciali nei file di testo
                self.info = json.load(in_file)                                # caricamento del contenuto del file JSON nel dizionario rubrica
        elif rubrica.endswith('.txt'):
            with open(rubrica, 'r', encoding='utf-8') as in_file:                      # apertura del file in modalità lettura
                for line in in_file:                                      # iterazione su ogni riga del file di testo
                    nome, giorno, mese, anno, eta, sesso, mail = line.strip().split(', ')  # separazione delle informazioni della riga usando la virgola come delimitatore
                    self.info[nome] = {'giorno': int(giorno), 'mese': mese, 'anno': int(anno), 'eta': int(eta), 'sesso': sesso, 'mail': mail}  # creazione di un nuovo elemento nel dizionario rubrica con le informazioni estratte dalla riga del file di testo
        else:
            print("Il file deve terminare con .json o .txt")
        return self.info

    def aggiungi(self):
        if not self.info:
            print("\nPrima apri una rubrica")
        else:
            print("\nDati del nuovo contatto:")
            while True:  # ciclo per assicurarsi che l'utente inserisca un nome completo valido
                print("\nInserire il nome completo da aggiungere:")
                nome = input().strip()
                if nome:
                    nome = " ".join([parte.capitalize() for parte in nome.split()])
                    break
                else:
                    print("\nNome non valido. Inserire almeno un nome.")

            while True:  # ciclo per assicurarsi che l'utente inserisca un giorno di nascita valido
                print('\nInserire il giorno di nascita:')
                giorno = int(input())
                if 1 <= giorno <= 31:
                    break
                else:
                    print("Valore non valido. Inserire un giorno compreso tra 1 e 31.")
                    giorno = int(input())
            while True:  # ciclo per assicurarsi che l'utente inserisca un valore valido per il mese
                print('\nInserire il mese di nascita:')
                mese = input()
                if mese.capitalize() in ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']:
                    mese = mese.capitalize()
                    break
                else:
                    print("Valore non valido. Inserire un mese valido (es. Gennaio, Febbraio, etc.).")
            while True:  # ciclo per assicurarsi che l'utente inserisca un valore valido per l'anno
                print('\nInserire l\'anno di nascita:')
                anno = int(input())
                if anno <= anno_oggi:
                    break            
            eta = anno_oggi - anno
            print("\nInserimento automatico dell'età:", eta)

            while True:  # ciclo per assicurarsi che l'utente inserisca un valore valido per il sesso
                print("\nInserire il sesso:")
                sesso = input()
                if sesso.upper() in ['M', 'F']:
                    sesso = sesso.upper()
                    break
                else:
                    print("Valore non valido. Inserire 'M' o 'F'.")

            print("\nInserire la mail:")
            mail = input()

            self.info[nome] = {'giorno': giorno, 'mese': mese, 'anno': anno, 'eta': eta, 'sesso': sesso, 'mail': mail}  # creazione di un nuovo elemento nel dizionario rubrica con le informazioni inserite dall'utente
            with open("rubrica.json", "w") as write_file:                   #apertura del file in modalità scrittura
               json.dump(self.info, write_file, indent=4)                    #scrittura del dizionario rubrica nel file JSON con indentazione di 4 spazi per una migliore leggibilità

    def rimuovi(self, nome):
        nome = " ".join([parte.capitalize() for parte in nome.split()])
        if not self.info:
            print("\nLa rubrica è vuota")
        while nome not in self.info:
            print(f"\nIl contatto {nome} non esiste in rubrica")
            print('Se hai sbagliato sezione digita NONE')
            print('\nInserire un nome valido:')
            nome = input()
            if nome.upper() == 'NONE':
                return
            nome = " ".join([parte.capitalize() for parte in nome.split()])
        del self.info[nome]  # rimozione dell'elemento dal dizionario rubrica
        with open("rubrica.json", "w") as write_file:  # apertura del file in modalità scrittura
            json.dump(self.info, write_file, indent=4)  # scrittura del dizionario rubrica aggiornato nel file JSON con indentazione di 4 spazi per una migliore leggibilità
            print(f"Contatto {nome} rimosso dalla rubrica.")
    
    def salva(self, nome_file):
        if not self.info:
            print("\nLa rubrica è vuota")
        elif nome_file.endswith('.json'):
            with open(nome_file, 'w', encoding='utf-8') as out_file:  # apertura del file in modalità scrittura
                json.dump(self.info, out_file, indent=4)  # scrittura del dizionario rubrica nel file JSON con indentazione di 4 spazi per una migliore leggibilità
            print('\nRubrica salvata con successo.')
        elif nome_file.endswith('.txt'):
            with open(nome_file, 'w', encoding='utf-8') as out_file:  # apertura del file in modalità scrittura
                for nome, contatto in self.info.items():  # iterazione su ogni elemento del dizionario rubrica
                    line = f"{nome}, {contatto['giorno']}, {contatto['mese']}, {contatto['anno']}, {contatto['età']}, {contatto['sesso']}, {contatto['mail']}\n"  # creazione di una stringa formattata con le informazioni del contatto
                    out_file.write(line)  # scrittura della stringa nel file di testo
            print('\nRubrica salvata con successo.')
        else:
            print("\nEstensione del file non valida. Scegliere .json o .txt.")

    def stampa(self, nome):
        nome = " ".join([parte.capitalize() for parte in nome.split()])
        if not self.info:
            print("\nLa rubrica è vuota")
        while nome not in self.info:
            print(f"\nIl contatto {nome} non esiste in rubrica")
            print('Se hai sbagliato sezione digita NONE')
            print('\nInserire un nome valido:')
            nome = input()
            if nome.upper() == 'NONE':
                return
            nome = " ".join([parte.capitalize() for parte in nome.split()])

        contatto = self.info[nome]  # recupero delle informazioni del contatto dal dizionario rubrica
        print(f"\nNome: {nome}")
        print(f"Giorno di nascita: {contatto['giorno']}")
        print(f"Mese di nascita: {contatto['mese']}")
        print(f"Anno di nascita: {contatto['anno']}")
        print(f"Età: {contatto['età']}")
        print(f"Sesso: {contatto['sesso']}")
        print(f"Mail: {contatto['mail']}")
