# Questo script permette di creare il file "stringz_filter.txt", partendo dal file "stringz_full.txt" (tutte le stringhe di gioco).
# Il file "stringz_filter.txt" conterrà solo le stringhe in lingua spagnola, utili per smistare le stringhe da tradurre velocemente.
import json, re
from lingua import Language, LanguageDetectorBuilder


# Apri i file
TRANSLATION_FILEPATH = "./translation.json"
STRINGZ_FULL_FILEPATH = "./stringz_full.txt"
STRINGZ_FILTER_FILEPATH = "./stringz_filter.txt"

try:
	with open(TRANSLATION_FILEPATH, 'r', encoding='utf-8') as f:
		translation = json.loads(f.read())
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


# Setup del classificatore di lingua
languages = [
	Language.ENGLISH, Language.JAPANESE, Language.KOREAN,
	Language.GERMAN, Language.FRENCH, Language.SPANISH,
	Language.PORTUGUESE, Language.RUSSIAN, Language.CHINESE
]
detector = LanguageDetectorBuilder.from_languages(*languages).build()


# Filtra le stringhe in lingua spagnola
CHAR_WHITELIST = """\n !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^`abcdefghijklmnopqrstuvwxyz{|}~ ¡ª¿ÀÁÂÃÄÆÇÈÉÊËÍÎÏÑÓÔÕÖÙÚÛÜßàáâãäæçèéêëíîïñóôõöùúûüŒœЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяёẞ‐‑‒–—―…⁃"""

with open(STRINGZ_FILTER_FILEPATH, 'a', encoding='utf-8') as stringz_filter:
	stringz_filter.truncate(0)
	stringz_filter.write('_' * 80 + "https://github.com/zWolfrost/Katana-ZERO-Traduzione-Italiana")

	stringz_index = 0
	for line in stringz_lines:
		if line not in translation and all(ch in CHAR_WHITELIST for ch in line):
			line_clean = re.sub(r'\[.*?\]|\*', '', line)
			confidence = detector.compute_language_confidence_values(line_clean)[0]
			if confidence.language == Language.SPANISH and confidence.value > 0.5:
				stringz_filter.write(f"\n{stringz_offsets[stringz_index]}_{confidence.value:.2f}\n{line}")

		stringz_index += 1
		print(round(stringz_index / len(stringz_lines) * 100), end='%\r')