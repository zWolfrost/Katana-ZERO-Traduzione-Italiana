# Questo script permette di creare il file "stringz_patch.txt",
# partendo dal file "stringz_full.txt" (tutte le stringhe di gioco) e dal file "translation.json" (le traduzioni delle stringhe).
from utils import get_stringz_full, get_translation, replace_with_table


# Apri i file
TRANSLATION_FILEPATH = "./translation.json"
STRINGZ_FULL_FILEPATH = "./stringz_full.txt"
STRINGZ_PATCH_FILEPATH = "../stringz_patch.txt"

try:
	translation, translation_settings = get_translation(TRANSLATION_FILEPATH)
	stringz_offsets, stringz_lines = get_stringz_full(STRINGZ_FULL_FILEPATH)
except FileNotFoundError as e:
	print(f"File '{e.filename}' non trovato.")
	exit(1)


# Controlla se la traduzione contiene tutte le linee di dialogo una sola volta
translation_counter = {l: 0 for l in translation}
for line in stringz_lines:
	if line in translation:
		translation_counter[line] += 1
for line, count in translation_counter.items():
	if count == 0:
		print(f"La seguente linea è inesistente:\n{line}\n")
		del translation[line]
	elif count >= 2:
		print(f"La seguente linea è presente più di una volta:\n{line}\n")


# Inserisci le stringhe in stringz-patch.txt
with open(STRINGZ_PATCH_FILEPATH, 'a', encoding='utf-8') as stringz_patch:
	stringz_patch.truncate(0)
	stringz_patch.write('_' * 80 + "https://github.com/zWolfrost/Katana-ZERO-Traduzione-Italiana")

	stringz_index = 0
	for line in translation:
		try:
			stringz_index = stringz_lines.index(line, stringz_index + 1)
		except ValueError:
			print(f"La seguente linea è fuori ordine:\n{line}\n")
			continue

		offsets = replace_with_table(stringz_offsets[stringz_index], translation_settings["offset_replace"])
		line_translated = replace_with_table(translation[line], translation_settings["string_replace"])

		stringz_patch.write('\n' + offsets + '\n' + line_translated)

print("Sostituzione completata.")