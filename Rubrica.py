#la classe rubrica deve fare 5 azioni:
#   - aprire una rubrica leggendola da un file (JSON oppure testo) - APRI
#   - aggiungere un elemento alla rubrica - AGGIUNGI
#   - rimuovere un elemento dalla rubrica (dato il nome) - RIMUOVI
#salvare la rubrica su un file (JSON o testo) - SALVA
#stampare tutte le informazioni di un contatto (data il nome), come nell’eserczio 3 - STAMPA
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
            with open(rubrica, 'r', encoding='utf-8') as in_file:       #endcoding='utf-8'serve a gestire correttamente lettere accentate e caratteri speciali nei file di testo
                self.info = json.load(in_file)                                # caricamento del contenuto del file JSON nel dizionario rubrica
        elif rubrica.endswith('.txt'):    
            with open(rubrica, 'r', encoding='utf-8') as in_file:                      # apertura del file in modalità lettura
                for line in in_file:                                      # iterazione su ogni riga del file di testo
                    nome, giorno, mese, anno, eta, sesso, mail = line.strip().split(', ')  # separazione delle informazioni della riga usando la virgola come delimitatore
                    self.info[nome] = {'giorno': int(giorno), 'mese': mese, 'anno': int(anno), 'eta': int(eta), 'sesso': sesso, 'mail': mail}  # creazione di un nuovo elemento nel dizionario rubrica con le informazioni estratte dalla riga del file di testo
        else:
            raise ValueError("Il file deve terminare con .json o .txt")
        return self.info

    def aggiungi(self):
        if not self.info:
            raise ValueError("Prima apri una rubrica")
        else:
            print("Dati del nuovo contatto:")
            while True:  # ciclo per assicurarsi che l'utente inserisca un nome completo valido
                print(f"inserire il nome completo da aggiungere:")
                nome = input()
                nome = nome.split(" ")
                for i in range(len(nome)):
                    nome[i] = nome[i].capitalize()
                    nome = " ".join(nome)

            while True:  # ciclo per assicurarsi che l'utente inserisca un giorno di nascita valido
                print(f"inserire il giorno di nascita:")
                giorno = int(input())
                if 1 <= giorno <= 31:
                    break
                else:
                    print("Valore non valido. Inserire un giorno compreso tra 1 e 31.")
                    giorno = int(input())
            while True:  # ciclo per assicurarsi che l'utente inserisca un valore valido per il mese
                print(f"inserire il mese di nascita:")
                mese = input()
                if mese.capitalize() in ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']:
                    mese = mese.capitalize()
                    break
                else:
                    print("Valore non valido. Inserire un mese valido (es. Gennaio, Febbraio, etc.).")
            while True:  # ciclo per assicurarsi che l'utente inserisca un valore valido per l'anno
                print(f"inserire l'anno di nascita:")
                anno = int(input())
                if 1900 <= anno <= anno_oggi:
                    break
                else:
                    print("Valore non valido. Inserire un anno compreso tra 1900 e " + str(anno_oggi) + ".")
            while True:  # ciclo per assicurarsi che l'utente inserisca un valore valido per l'età
                print(f"inserire l'età:")
                eta = int(input())
                if eta == anno_oggi - anno:
                    break
                else:
                    print("Valore non valido. Inserire un'età compresa tra 0 e " + str(anno_oggi - anno) + ".")
            
            while True:  # ciclo per assicurarsi che l'utente inserisca un valore valido per il sesso
                print(f"inserire il sesso:")
                sesso = input()
                if sesso.upper() in ['M', 'F']:
                    sesso = sesso.upper()
                    break
                else:
                    print("Valore non valido. Inserire 'M' o 'F'.")

            print(f"inserire la mail:")
            mail = input()

            self.info[nome] = {'giorno': giorno, 'mese': mese, 'anno': anno, 'eta': eta, 'sesso': sesso, 'mail': mail}  # creazione di un nuovo elemento nel dizionario rubrica con le informazioni inserite dall'utente
            with open("rubrica.json", "w") as write_file:                   #apertura del file in modalità scrittura
               json.dump(self.info, write_file, indent=4)                    #scrittura del dizionario rubrica nel file JSON con indentazione di 4 spazi per una migliore leggibilità

def rimuovi(self, nome):
        if not self.info:
            raise ValueError("La rubrica è vuota")
        elif nome not in self.info:
            raise ValueError(f"Il contatto {nome} non esiste in rubrica")
        else:
            del self.info[nome]  # rimozione dell'elemento dal dizionario rubrica
            with open("rubrica.json", "w") as write_file:  # apertura del file in modalità scrittura
                json.dump(self.info, write_file, indent=4)  # scrittura del dizionario rubrica aggiornato nel file JSON con indentazione di 4 spazi per una migliore leggibilità

def salva(self, nome_file):
        if not self.info:
            raise ValueError("La rubrica è vuota")
        elif nome_file.endswith('.json'):
            with open(nome_file, 'w', encoding='utf-8') as out_file:  # apertura del file in modalità scrittura
                json.dump(self.info, out_file, indent=4)  # scrittura del dizionario rubrica nel file JSON con indentazione di 4 spazi per una migliore leggibilità

if __name__ == '__main__':
    rubrica = Rubrica()
    dati = rubrica.apri('rubrica.json')
    print('File aperto:', bool(dati))
    print(dati)
    azione = 'EXIT'
    while azione == 'EXIT':
        print('Scegliere un\'azione da svolgere: AGGIUNGI, RIMUOVI, EXIT')
        azione = input()
        if azione == 'AGGIUNGI':
            rubrica.aggiungi()
            print('Contatto aggiunto:', bool(rubrica.info))
            print(rubrica.info)
        elif azione == 'RIMUOVI':
            print('Inserire il nome del contatto da rimuovere:')
            nome_da_rimuovere = input()
            rubrica.rimuovi(nome_da_rimuovere)