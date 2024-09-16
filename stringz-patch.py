# Questo script permette di creare il file "stringz-patch.txt",
# partendo dal file "stringz-full.txt" (tutte le stringhe di gioco) e dal file "translation.json" (le traduzioni delle stringhe).
import json

translation_filename = './translation.json'
stringz_filename = './stringz-full.txt'
patch_filename = './stringz-patch.txt'

patch = open(patch_filename, 'a', encoding='utf-8', errors='ignore')
patch.truncate(0)

with open(translation_filename, 'r', encoding='utf-8', errors='ignore') as f:
    translation = json.loads(f.read())

with open(stringz_filename, 'r', encoding='utf-8', errors='ignore') as f:
    stringz_raw = f.read().split('\n')


# Split stringz into dialogue lines
stringz = []
for line in stringz_raw:
    if line.startswith('_' * 80) or stringz[-1].startswith('_' * 80):
        stringz.append(line)
    else:
        stringz[-1] += '\n' + line


# Check for repeated lines in the table
for line in translation:
    if line.startswith('#' * 3):
        continue
    occurrences = stringz.count(line)
    assert occurrences != 0, f"La stringa:\n{line}\nnon è presente nel file stringz."
    if occurrences > 1:
        print(f"La stringa:\n{line} ha {occurrences} occorrenze nel file stringz. Potrebbe creare problemi.")
print("Tutte le linee di dialogo sono state trovate.")


CHAR_REPLACE = {
    "Ì": "Í",
    "ì": "í",
    "Ò": "Ó",
    "ò": "ó",
}

patch.write('_' * 80 + "https://github.com/zWolfrost/Katana-ZERO-Traduzione-Italiana")

# Substitute lines
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
                patch.write('\n' + stringz[stringz_id_index])
            translated_line = translation[line]
            for char in CHAR_REPLACE:
                translated_line = translated_line.replace(char, CHAR_REPLACE[char])
            patch.write('\n' + translated_line)
            break
        stringz_index += 1
    assert stringz_index != len(stringz), f"Sostituzione non trovata alla stringa: {line}\nControlla di avere la versione corretta di gioco."

patch.close()

print("Tutte le linee di dialogo sono state sostituite. Patch completata.")