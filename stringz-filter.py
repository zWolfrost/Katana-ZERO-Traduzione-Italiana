# Questo script permette di creare il file "stringz-filter.txt", partendo dal file "stringz-full.txt" (tutte le stringhe di gioco).
# Il file "stringz-filter.txt" conterrà solo le stringhe in lingua spagnola, utili per smistare le stringhe da tradurre velocemente.
import langid


STRINGZ_FILEPATH = './stringz-full.txt'
FILTER_FILEPATH = './stringz-filter.txt'


# Apri il file
try:
    with open(STRINGZ_FILEPATH, 'r', encoding='utf-8', errors='ignore') as f:
        stringz_raw = f.read().split('\n')
except FileNotFoundError as e:
    print(f"File '{e.filename}' non trovato.")
    exit(1)

filter = open(FILTER_FILEPATH, 'a', encoding='utf-8', errors='ignore')
filter.truncate(0)


# Dividi i dialoghi in stringz
stringz = []
for line in stringz_raw:
    if line.startswith('_' * 80) or stringz[-1].startswith('_' * 80):
        stringz.append(line)
    else:
        stringz[-1] += '\n' + line


# Filtra le stringhe in lingua spagnola
CHAR_BLACKLIST = ['_', '\\']

filter.write('_' * 80 + "https://github.com/zWolfrost/Katana-ZERO-Traduzione-Italiana")

stringz_id = ""
stringz_index = 0
for line in stringz:
    if line.startswith('_' * 80):
        stringz_id = line
    elif not any([ch in line for ch in CHAR_BLACKLIST]):
        if langid.classify(line)[0] == 'es':
            filter.write(f"\n{stringz_id}\n{line}")

    stringz_index += 1
    print(str(round(stringz_index / len(stringz) * 100)) + '%\r', end='')

filter.close()