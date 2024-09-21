# Questo script permette di creare il file "stringz-patch.txt",
# partendo dal file "stringz-full.txt" (tutte le stringhe di gioco) e dal file "translation.json" (le traduzioni delle stringhe).
import json


# Apri i file
TRANSLATION_FILEPATH = "./translation.json"
STRINGZ_FULL_FILEPATH = "./stringz_full.txt"
STRINGZ_PATCH_FILEPATH = "../stringz_patch.txt"

try:
	with open(TRANSLATION_FILEPATH, 'r', encoding='utf-8') as f:
		translation: dict[str, str] = json.loads(f.read())
	with open(STRINGZ_FULL_FILEPATH, 'r', encoding='utf-8', errors='ignore') as f:
		stringz_full = f.read().split('\n')
except FileNotFoundError as e:
	print(f"File '{e.filename}' non trovato.")
	exit(1)


# Dividi i dialoghi in stringz
stringz_offsets: list[str] = []
stringz_lines: list[str] = []
for line in stringz_full:
	if line.startswith('_' * 80):
		stringz_offsets.append(line)
	elif len(stringz_lines) < len(stringz_offsets):
		stringz_lines.append(line)
	else:
		stringz_lines[-1] += '\n' + line


# Controlla se la traduzione contiene tutte le linee di dialogo una sola volta
translation_counter = {t: 0 for t in dict(translation)}
for line in stringz_lines:
	if line in translation:
		translation_counter[line] += 1
for line, count in translation_counter.items():
	if not line.startswith('#' * 3) and count != 1:
		if count == 0:
			print("La seguente linea è inesistente:\n" + line)
		else:
			print("La seguente linea è presente più di una volta:\n" + line)
		exit(1)


# Inserisci le stringhe in stringz-patch.txt
def replace_with_table(string: str, table: dict[str, str]) -> str:
	for key, value in table.items():
		string = string.replace(key, value)
	return string

with open(STRINGZ_PATCH_FILEPATH, 'a', encoding='utf-8') as stringz_patch:
	stringz_patch.truncate(0)
	stringz_patch.write('_' * 80 + "https://github.com/zWolfrost/Katana-ZERO-Traduzione-Italiana")

	stringz_index = 0
	for line in translation:
		if line.startswith('#' * 3):
			continue

		try:
			stringz_index = stringz_lines.index(line, stringz_index + 1)
		except ValueError:
			print("La seguente linea è fuori ordine:\n" + line)
			exit(1)

		offsets = replace_with_table(stringz_offsets[stringz_index], translation["###"]["offset_replace"])
		line_translated = replace_with_table(translation[line], translation["###"]["string_replace"])

		stringz_patch.write('\n' + offsets + '\n' + line_translated)

print("Tutte le linee di dialogo sono state correttamente sostituite.")