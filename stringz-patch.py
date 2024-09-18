# Questo script permette di creare il file "stringz-patch.txt",
# partendo dal file "stringz-full.txt" (tutte le stringhe di gioco) e dal file "translation.json" (le traduzioni delle stringhe).
import json


TRANSLATION_FILEPATH = './translation.json'
STRINGZ_FILEPATH = './stringz-full.txt'
PATCH_FILEPATH = './stringz-patch.txt'


# Apri i file
try:
    with open(TRANSLATION_FILEPATH, 'r', encoding='utf-8', errors='ignore') as f:
        translation = json.loads(f.read())

    with open(STRINGZ_FILEPATH, 'r', encoding='utf-8', errors='ignore') as f:
        stringz_raw = f.read().split('\n')

    patch = open(PATCH_FILEPATH, 'a', encoding='utf-8', errors='ignore')
    patch.truncate(0)
except FileNotFoundError as e:
    print(f"File '{e.filename}' non trovato.")
    exit(1)


# Dividi i dialoghi in stringz
stringz = []
for line in stringz_raw:
    if line.startswith('_' * 80) or stringz[-1].startswith('_' * 80):
        stringz.append(line)
    else:
        stringz[-1] += '\n' + line


# Controlla se la traduzione contiene linee ripetute o mancanti
translation_index = 0
for line in translation:
    if line.startswith('#' * 3):
        continue
    occurrences = stringz.count(line)
    assert occurrences != 0, f"La stringa:\n{line}\nnon è presente nel file stringz. Controlla di averla digitata correttamente."
    if occurrences > 1:
        print(f"La stringa:\n{line} ha {occurrences} occorrenze nel file stringz. Potrebbe creare problemi.")

    translation_index += 1
    print(str(round(translation_index / len(translation) * 100)) + '%\r', end='')
print("Tutte le linee di dialogo sono state trovate.")


# Eccezioni per la traduzione
OFFSET_BLACKLIST = [
    "-005b854a",
    "-004d339f-004ddf7f-004ddfab-005b483e"
]
CHAR_REPLACE = {
    "ì": "í",
    "Ì": "Í",
    "ò": "ó",
    "Ò": "Ó",
}

patch.write('_' * 80 + "https://github.com/zWolfrost/Katana-ZERO-Traduzione-Italiana")


# Inserisci le stringhe in stringz-patch.txt
wrote_id = False
stringz_id_index = 0
stringz_index = 0
for line in translation:
    if line.startswith('#' * 3):
        continue
    while stringz_index < len(stringz):
        if stringz[stringz_index].startswith('_' * 80):
            stringz_id_index = stringz_index
            wrote_id = False
        elif line == stringz[stringz_index]:
            if not wrote_id:
                wrote_id = True
                id_line = '\n' + stringz[stringz_id_index]
                for offset in OFFSET_BLACKLIST:
                    id_line = id_line.replace(offset, '')
                patch.write(id_line)
            translated_line = translation[line]
            for char in CHAR_REPLACE:
                translated_line = translated_line.replace(char, CHAR_REPLACE[char])
            patch.write('\n' + translated_line)
            break
        stringz_index += 1
    assert stringz_index != len(stringz), f"Sostituzione non trovata alla stringa:\n{line}\nControlla di avere la versione corretta di gioco."

patch.close()

print("Tutte le linee di dialogo sono state sostituite. Patch completata.")