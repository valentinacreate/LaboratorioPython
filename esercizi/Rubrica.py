
#Rubrica.py
#Creato da: Valentina Furlanis IN0501333
#Data: 29 aprile 2026

#La classe rubrica deve fare 5 azioni:
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
        self.info = {}           # inizializzazione del dizionario

    @classmethod
    def from_json(cls, filename):
        instance = cls()
        with open(filename, 'r', encoding='utf-8') as in_file:
            instance.info = json.load(in_file)
        return instance

    @classmethod
    def from_txt(cls, filename):
        instance = cls()
        with open(filename, 'r', encoding='utf-8') as in_file:
            for line in in_file:
                nome, giorno, mese, anno, eta, sesso, mail = line.strip().split(', ')
                instance.info[nome] = {
                    'giorno': int(giorno),
                    'mese': mese,
                    'anno': int(anno),
                    'età': int(eta),
                    'sesso': sesso,
                    'mail': mail
                }
        return instance

    def apri(self, rubrica):
        if rubrica.endswith('.json'):
            with open(rubrica, 'r', encoding='utf-8') as in_file:
                self.info = json.load(in_file)
        elif rubrica.endswith('.txt'):
            with open(rubrica, 'r', encoding='utf-8') as in_file:
                for line in in_file:
                    nome, giorno, mese, anno, eta, sesso, mail = line.strip().split(', ')
                    self.info[nome] = {
                        'giorno': int(giorno),
                        'mese': mese,
                        'anno': int(anno),
                        'età': int(eta),
                        'sesso': sesso,
                        'mail': mail
                    }
        else:
            print("Il file deve terminare con .json o .txt")
        return self.info

    def aggiungi(self):
        if not self.info:
            print("\nPrima apri una rubrica")
            return

        print("\nDati del nuovo contatto:")
        while True:
            print("\nInserire il nome completo da aggiungere:")
            nome = input().strip()
            if nome:
                nome = " ".join([parte.capitalize() for parte in nome.split()])
                break
            print("\nNome non valido. Inserire almeno un nome.")

        while True:
            print('\nInserire il giorno di nascita:')
            giorno = int(input())
            if 1 <= giorno <= 31:
                break
            print("Valore non valido. Inserire un giorno compreso tra 1 e 31.")

        while True:
            print('\nInserire il nome del mese di nascita:')
            mese = input().strip()
            if mese.capitalize() in ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']:
                mese = mese.capitalize()
                break
            print("Valore non valido. Inserire un mese valido (es. Gennaio, Febbraio, etc.).")
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

        while True:
            print('\nInserire l\'anno di nascita:')
            anno = int(input())
            if anno <= anno_oggi:
                break
            else:
                print("Valore non valido. L'anno non può essere nel futuro.")

        eta = anno_oggi - anno
        if (mese_oggi < mese_num) or (mese_oggi == mese_num and giorno_oggi < giorno):
            eta -= 1
        print("\nInserimento automatico dell'età:", eta)

        while True:
            print("\nInserire il sesso, M o F:")
            sesso = input().strip()
            if sesso.upper() in ['M', 'F']:
                sesso = sesso.upper()
                break
            print("Valore non valido. Inserire 'M' o 'F'.")

        print("\nInserire la mail:")
        mail = input().strip()

        self.info[nome] = {
            'giorno': giorno,
            'mese': mese,
            'anno': anno,
            'età': eta,
            'sesso': sesso,
            'mail': mail
        }

    def rimuovi(self, nome):
        nome = " ".join([parte.capitalize() for parte in nome.split()])
        if not self.info:
            print("\nLa rubrica è vuota")
            return

        while nome not in self.info:
            print(f"\nIl contatto {nome} non esiste in rubrica")
            print('Se hai sbagliato sezione digita NONE')
            print('\nInserire un nome valido:')
            nome = input().strip()
            if nome.upper() == 'NONE':
                return
            nome = " ".join([parte.capitalize() for parte in nome.split()])

        del self.info[nome]
        print(f"Contatto {nome} rimosso dalla rubrica.")

    def salva(self, nome_file):
        if not self.info:
            print("\nLa rubrica è vuota")
            return

        if nome_file.endswith('.json'):
            with open(nome_file, 'w', encoding='utf-8') as out_file:
                json.dump(self.info, out_file, indent=4)
            print('\nRubrica salvata con successo.')
        elif nome_file.endswith('.txt'):
            with open(nome_file, 'w', encoding='utf-8') as out_file:
                for nome, contatto in self.info.items():
                    line = f"{nome}, {contatto['giorno']}, {contatto['mese']}, {contatto['anno']}, {contatto['età']}, {contatto['sesso']}, {contatto['mail']}\n"
                    out_file.write(line)
            print('\nRubrica salvata con successo.')
        else:
            print("\nEstensione del file non valida. Scegliere .json o .txt.")

    def stampa(self, nome):
        nome = " ".join([parte.capitalize() for parte in nome.split()])
        if not self.info:
            print("\nLa rubrica è vuota")
            return

        while nome not in self.info:
            print(f"\nIl contatto {nome} non esiste in rubrica")
            print('Se hai sbagliato sezione digita NONE')
            print('\nInserire un nome valido:')
            nome = input().strip()
            if nome.upper() == 'NONE':
                return
            nome = " ".join([parte.capitalize() for parte in nome.split()])

        contatto = self.info[nome]
        print(f"\nNome: {nome}")
        print(f"Giorno di nascita: {contatto['giorno']}")
        print(f"Mese di nascita: {contatto['mese']}")
        print(f"Anno di nascita: {contatto['anno']}")
        print(f"Età: {contatto['età']}")
        print(f"Sesso: {contatto['sesso']}")
        print(f"Mail: {contatto['mail']}")
