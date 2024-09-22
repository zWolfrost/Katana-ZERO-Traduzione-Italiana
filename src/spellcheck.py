# Questo script permette di trovare errori di ortografia e grammatica nel file "translation.json".
from language_tool_python import LanguageTool
from utils import get_translation, clean_dialog
lang = LanguageTool('it')


# Apri i file
TRANSLATION_FILEPATH = "./translation.json"
SPELLCHECK_FILEPATH = "./spellcheck.txt"

try:
	translation = get_translation(TRANSLATION_FILEPATH)[0]
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
	for line in translation.values():
		for error in lang.check(clean_dialog(line)):
			if error.ruleId not in BLACK_LIST_RULEID:
				spellcheck.write('\n'.join(str(error).split('\n')[-3:]) + '\n')

		print(round(list(translation.values()).index(line) / len(translation) * 100), end='%\r')