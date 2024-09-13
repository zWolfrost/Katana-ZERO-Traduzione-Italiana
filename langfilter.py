import langid

CHAR_BLACKLIST = ['_', '\\']

input = '.\kz.txt'
output = '.\kz-f.txt'

with open(input, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

f = open(output, 'a', encoding='utf-8', errors='ignore')
f.truncate(0)

total_line = ''
write_this = False

line_num = 0
for line in text.split('\n'):
    if line.startswith('_' * 80):
        if write_this:
            write_this = False
            f.write(total_line + '\n')
            line_num += 1
        total_line = line
    elif not any([ch in line for ch in CHAR_BLACKLIST]):
        lang, probability = langid.classify(line)

        if write_this or lang == 'es':
            write_this = True
            total_line += '\n' + line

    print("\r" + str(line_num), end='')

f.close()