# Questo script permette di trovare errori di ortografia e grammatica nel file "translation.json".
import json, re
from language_tool_python import LanguageTool
lang = LanguageTool('it')


# Apri i file
TRANSLATION_FILEPATH = "./translation.json"
SPELLCHECK_FILEPATH = "./spellcheck.txt"

try:
	with open(TRANSLATION_FILEPATH, 'r', encoding='utf-8') as f:
		translation = json.loads(f.read())
except FileNotFoundError as e:
	print(f"File '{e.filename}' non trovato.")
	exit(1)


# Trova errori di ortografia e grammatica
BLACK_LIST_RULEID = [
	"ITALIAN_WORD_REPEAT_RULE",
	"GR_09_003",
]

with open(SPELLCHECK_FILEPATH, 'a', encoding='utf-8') as spellcheck:
	spellcheck.truncate(0)
	for line_translated in translation.values():
		if not isinstance(line_translated, str) or line_translated.startswith('#' * 3):
			continue

		line_clean = re.sub(r'\[.*?\]|\*', '', line_translated)
		errors = lang.check(line_clean)
		for error in errors:
			if error.ruleId not in BLACK_LIST_RULEID:
				spellcheck.write(f"{error}\n\n")

		print(round(list(translation.values()).index(line_translated) / len(translation) * 100), end='%\r')