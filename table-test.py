import json

table = '.\\table.json'
stringz = '.\\kz.txt'

with open(table, 'r', encoding='utf-8', errors='ignore') as f:
    table = json.loads(f.read())

stringz = open(stringz, 'r', encoding='utf-8', errors='ignore').read().split('\n')

all_good = True

# Check for repeated lines in the table
for line in table:
    if line.startswith('#' * 3):
        continue
    occurrences = stringz.count(line)
    if occurrences != 1:
        all_good = False
        print(f"Table line {line} has {occurrences} occurrences in the stringz file.")

# Check for missing substitutions
id_index = 0
index = 0
for line in table:
    if line.startswith('#' * 3):
        continue
    while index < len(stringz):
        if stringz[index].startswith('_' * 80):
            id_index = index
        elif line == stringz[index]:
            break
        index += 1
    if index == len(stringz):
        all_good = False
        print(f"Missing substitutions at line {line}.")
        break

if all_good:
    print("All good :)")

f.close()