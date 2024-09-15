import json

CHAR_REPLACE = {
    "Ì": "Í",
    "ì": "í",
    "Ò": "Ó",
    "ò": "ó",
}

table = '.\\translation.json'
stringz = '.\\stringz.txt'
patch = '.\\stringz-patch.txt'

with open(table, 'r', encoding='utf-8', errors='ignore') as f:
    table = json.loads(f.read())

with open(stringz, 'r', encoding='utf-8', errors='ignore') as f:
    stringz = f.read().split('\n')

patch = open(patch, 'a', encoding='utf-8', errors='ignore')
patch.truncate(0)

all_good = True

# Check for missing substitutions
wrote_id = False
id_index = 0
index = 0
for line in table:
    if line.startswith('#' * 3):
        continue
    while index < len(stringz):
        if stringz[index].startswith('_' * 80):
            id_index = index
            wrote_id = False
        elif line == stringz[index]:
            if not wrote_id:
                wrote_id = True
                patch.write(stringz[id_index] + '\n')
            translation = table[line]
            for char in CHAR_REPLACE:
                translation = translation.replace(char, CHAR_REPLACE[char])
            patch.write(translation + '\n')
            break
        index += 1
    if index == len(stringz):
        all_good = False
        print(f"Missing substitutions at line {line}.")
        break

if all_good:
    print("All good :)")

patch.close()