# Questo script permette di creare il file "stringz_filter.txt", partendo dal file "stringz_full.txt" (tutte le stringhe di gioco).
# Il file "stringz_filter.txt" conterrà solo le stringhe in lingua spagnola, utili per smistare le stringhe da tradurre velocemente.
from lingua import Language, LanguageDetectorBuilder
from utils import get_stringz_full, get_translation, clean_dialog


# Apri i file
TRANSLATION_FILEPATH = "./translation.json"
STRINGZ_FULL_FILEPATH = "./stringz_full.txt"
STRINGZ_FILTER_FILEPATH = "./stringz_filter.txt"

try:
	translation = get_translation(TRANSLATION_FILEPATH)[0]
	stringz_offsets, stringz_lines = get_stringz_full(STRINGZ_FULL_FILEPATH)
except FileNotFoundError as e:
	print(f"File '{e.filename}' non trovato.")
	exit(1)


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

	for stringz_index in range(len(stringz_lines)):
		line = stringz_lines[stringz_index]
		if line and line not in translation and all(ch in CHAR_WHITELIST for ch in line):
			confidence = detector.compute_language_confidence_values(clean_dialog(line))[0]
			if confidence.language == Language.SPANISH and confidence.value > 0.5:
				stringz_filter.write(f"\n{stringz_offsets[stringz_index]}___{confidence.value:.2f}\n{line}")

		print(round(stringz_index / len(stringz_lines) * 100), end='%\r')