#
#esercizio4.py
#Creato da Valentina Furlanis IN0501333
#Data:26 aprile 2026
#
#Partendo dall’esercizio 3, aggiungete una opzione al programma per generare un file di testo rubrica.txt contenente tutti gli elmenti della rubrica, uno per linea, con tutte le informazioni separate da virgole.
#Create un file JSON che contiene la rubrica con la stessa struttura del dizionario interno al programma
#Leggete la rubrica salvata in un file formato JSON e visualizzate tutto il contenuto

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

#creazione file di testo
file_testo = open('rubrica.txt', 'w')
for nome, info in rubrica.items():     
    file_testo.write(f'{nome}, {info["giorno"]}, {info["mese"]},{info["anno"]}, {info["età"]}, {info["sesso"]}, {info["mail"]}\n') 
file_testo.close()

#creazione file JSON
import json
with open("rubrica.json", "w") as write_file:
    json.dump(rubrica, write_file, indent=4)

#lettura file JSON
with open('rubrica.json', 'r') as in_file:
    rubrica = json.load(in_file)
print(json.dumps(rubrica, indent=4))