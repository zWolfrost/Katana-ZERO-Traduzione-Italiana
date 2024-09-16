# Questo script permette di creare il file "stringz-filter.txt", partendo dal file "stringz-full.txt" (tutte le stringhe di gioco).
# Il file "stringz-filter.txt" conterrà solo le stringhe in lingua spagnola, utili per smistare le stringhe da tradurre velocemente.
import langid

CHAR_BLACKLIST = ['_', '\\']

stringz = './stringz-full.txt'
filter = './stringz-filter.txt'

with open(stringz, 'r', encoding='utf-8', errors='ignore') as f:
    stringz = f.read()

filter = open(filter, 'a', encoding='utf-8', errors='ignore')
filter.truncate(0)

total_line = ''
write_this = False

filter_index = 0
for line in stringz.split('\n'):
    if line.startswith('_' * 80):
        if write_this:
            write_this = False
            filter.write(total_line + '\n')
            filter_index += 1
        total_line = line
    elif not any([ch in line for ch in CHAR_BLACKLIST]):
        lang, probability = langid.classify(line)

        if write_this or lang == 'es':
            write_this = True
            total_line += '\n' + line

    print("\r" + str(filter_index), end='')

filter.close()