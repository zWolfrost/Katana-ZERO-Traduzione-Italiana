# nuitka-project: --standalone
# nuitka-project: --onefile
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --nofollow-import-to=lingua
# nuitka-project: --nofollow-import-to=language_tool_python
# nuitka-project: --windows-console-mode=attach
# nuitka-project: --windows-icon-from-ico=icon.ico

# Questo è un semplice script automatico con GUI per patchare Katana ZERO con la traduzione italiana.
# I file di patch sono scaricati automaticamente da GitHub, perciò è necessario avere una connessione internet.
# È anche possibile includere i file di patch nella sua stessa cartella per usarlo offline.

# Dipendenze: strindex (git), pyxdelta, pyside6 (installabili tramite pip)

import os, sys, hashlib, urllib.request, pyxdelta
from urllib.error import HTTPError
from PySide6 import QtWidgets, QtCore
import strindex.strindex as strindex
from strindex.gui import StrindexGUI

POSSIBLE_LOCATIONS = [
	"%programfiles(x86)%/Steam/steamapps/common/Katana ZERO/Katana ZERO.exe",
	"~/.steam/steam/steamapps/common/Katana ZERO/Katana ZERO.exe"
]

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/zWolfrost/Katana-ZERO-Traduzione-Italiana/main/"
STRINDEX_URL = DOWNLOAD_ROOT + "kz_patch.gz"
DATAWIN_URL = DOWNLOAD_ROOT + "datawin_{md5}.xdelta"

class SignalWorker(QtCore.QObject):
	warning = QtCore.Signal(str)
signals = SignalWorker()

def get_file_md5(file):
	hash = hashlib.md5()
	with open(file, "rb") as f:
		while chunk := f.read(8192):
			hash.update(chunk)
	return hash.hexdigest()

def get_file_bak_filepath(file):
	return os.path.join(os.path.dirname(file), os.path.basename(file) + "_" + get_file_md5(file) + ".bak")

def download_if_needed(url):
	SELF_LOCATION = os.path.dirname(os.path.abspath(sys.argv[0]))

	filename = os.path.basename(url)
	filepath = os.path.join(SELF_LOCATION, filename)

	if os.path.isfile(filepath):
		print(f'File "{filename}" already there, skipping download.')
		return filepath

	try:
		print(f'Downloading "{filename}"...')
		return urllib.request.urlretrieve(url)[0]
	except Exception as e:
		if isinstance(e, HTTPError) and e.code == 404:
			raise FileNotFoundError()
		raise ConnectionError(f'Errore durante il download del file all\'url "{url}": {e}')

def patch(katanazero_filepath):
	# Controlla l'esistenza dei file di gioco
	if os.path.basename(katanazero_filepath) != "Katana ZERO.exe":
		raise FileNotFoundError('File "Katana ZERO.exe" errato.')

	datawin_filepath = os.path.join(os.path.dirname(katanazero_filepath), "data.win")

	if not os.path.isfile(datawin_filepath):
		raise FileNotFoundError('File "data.win" non trovato.')

	# Patcha Katana ZERO.exe
	strindex_filepath = download_if_needed(STRINDEX_URL)
	strindex_gz_filepath = strindex_filepath.rstrip(".gz") + ".gz"
	os.rename(strindex_filepath, strindex_gz_filepath)
	try:
		strindex.patch(katanazero_filepath, strindex_gz_filepath, None)
	except Exception as e:
		if ".strdex" in str(e):
			raise ValueError("La patch è già applicata in precedenza.")
		raise

	os.replace(katanazero_filepath + ".bak", get_file_bak_filepath(katanazero_filepath))

	# Rileva il tipo di data.win, e scarica il file xdelta corretto
	datawin_bak_filepath = datawin_filepath + ".bak"
	datawin_md5 = get_file_md5(datawin_filepath)
	try:
		datawin_xdelta_filepath = download_if_needed(DATAWIN_URL.format(md5=datawin_md5))
	except FileNotFoundError:
		signals.warning.emit(
			'File di patch per "data.win" non trovato. '
			'La traduzione è stata patchata ma alcune lettere potrebbero avere accenti sbagliati. '
			'Assicurati di avere la versione più recente del gioco.'
		)
		return

	os.replace(datawin_filepath, datawin_bak_filepath)

	# Patcha data.win
	print('Decoding with "data.win.xdelta"...')
	pyxdelta.decode(datawin_bak_filepath, datawin_xdelta_filepath, datawin_filepath)

	os.replace(datawin_bak_filepath, get_file_bak_filepath(datawin_filepath))

def remove(katanazero_filepath):
	# Controlla l'esistenza dei file di gioco
	if os.path.basename(katanazero_filepath) != "Katana ZERO.exe":
		raise FileNotFoundError('File "Katana ZERO.exe" errato.')

	datawin_filepath = os.path.join(os.path.dirname(katanazero_filepath), "data.win")

	# Ripristina i file di gioco dai backup
	katanazero_bak_filepath = get_file_bak_filepath(katanazero_filepath)

	if os.path.isfile(katanazero_bak_filepath):
		os.replace(katanazero_bak_filepath, katanazero_filepath)

	datawin_bak_filepath = get_file_bak_filepath(datawin_filepath)

	if os.path.isfile(datawin_bak_filepath):
		os.replace(datawin_bak_filepath, datawin_filepath)

class KatanaZeroPatchGUI(StrindexGUI):
	def setup(self):
		line_edit = self.create_file_selection(
			line_text="*Seleziona il file eseguibile di Katana ZERO",
			button_text="Seleziona file"
		)[0]

		self.create_action_button(
			text="Esegui Patch",
			progress_text="Patch in corso... %p%",
			complete_text="Patch avvenuta con successo.",
			callback=patch,
		)

		self.create_action_button(
			text="Rimuovi Patch",
			progress_text="Rimozione... %p%",
			complete_text="I file che avevano backup esistenti sono stati ripristinati.",
			callback=remove,
		)

		description = QtWidgets.QLabel(
			"Made with ♥ by <a href='https://github.com/zWolfrost'>Luca Russo</a>. "
			"Per dettagli aggiuntivi, riferirsi a <a href='https://github.com/zWolfrost/Katana-ZERO-Traduzione-Italiana'>questa pagina</a>."
		)
		description.setOpenExternalLinks(True)
		self.__widgets__.append(description)
		self.create_padding(1)

		self.create_grid_layout(2).setColumnStretch(0, 1)

		self.set_window_properties(title="Katana ZERO - Traduzione Italiana")

		for path in POSSIBLE_LOCATIONS:
			path = os.path.expandvars(os.path.expanduser(path)).replace(os.sep, "/")
			if os.path.isfile(path):
				line_edit.setText(path)
				break

		signals.warning.connect(lambda msg: self.show_message(msg, QtWidgets.QMessageBox.Warning))

if __name__ == "__main__":
	KatanaZeroPatchGUI()
