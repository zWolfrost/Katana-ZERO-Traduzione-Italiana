import json

table = '.\\translation.json'
stringz = '.\\stringz.txt'

with open(table, 'r', encoding='utf-8', errors='ignore') as f:
    table = json.loads(f.read())

with open(stringz, 'r', encoding='utf-8', errors='ignore') as f:
    stringz = f.read().split('\n')

# Check for repeated lines in the table
for line in table:
    if line.startswith('#' * 3):
        continue
    occurrences = stringz.count(line)
    assert occurrences != 0, f"Table line {line} not found in the stringz file."
    if occurrences > 1:
        print(f"Table line {line} has {occurrences} occurrences in the stringz file. (>1)")

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
    assert index != len(stringz), f"Missing substitutions at line {line}."

print("All good :)")