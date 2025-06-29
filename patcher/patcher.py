# nuitka-project: --standalone
# nuitka-project: --onefile
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --nofollow-import-to=lingua
# nuitka-project: --nofollow-import-to=language_tool_python
# nuitka-project: --windows-console-mode=hide
# nuitka-project: --windows-icon-from-ico=icon.ico
# nuitka-project: --include-data-file=icon.ico=./

# Questo è un semplice script automatico con GUI per patchare Katana ZERO con la traduzione italiana.
# I file di patch sono scaricati automaticamente da GitHub, perciò è necessario avere una connessione internet.
# È anche possibile includere i file di patch nella sua stessa cartella per usarlo offline.

import os, sys, pyxdelta, ssl
from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError
from PySide6 import QtWidgets, QtCore, QtGui
from strindex import strindex
from strindex.gui import MainStrindexGUI
from strindex.utils import FileBytearray

POSSIBLE_LOCATIONS = [
	"%programfiles(x86)%/Steam/steamapps/common/Katana ZERO/Katana ZERO.exe",
	"%programfiles(x86)%/GOG Galaxy/Games/Katana ZERO/Katana ZERO.exe",
	"~/.steam/steam/steamapps/common/Katana ZERO/Katana ZERO.exe"
]

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/zWolfrost/Katana-ZERO-Traduzione-Italiana/main/patches/"
KZ_EXE_STRINDEX_URL = DOWNLOAD_ROOT + "kz_exe.gz"
DATAWIN_XDELTA_URL = DOWNLOAD_ROOT + "datawin_{id}.xdelta"

class SignalWorker(QtCore.QObject):
	warning = QtCore.Signal(str)
signals = SignalWorker()

def get_file_md5_id(file):
	MD5_SLICE = 8
	return FileBytearray.read(file).md5[:MD5_SLICE]

def get_file_bak_filepath(file):
	return file + "_" + get_file_md5_id(file) + ".bak"

def download_if_needed(url):
	SELF_LOCATION = os.path.dirname(os.path.abspath(sys.argv[0]))

	filename = os.path.basename(url)
	filepath = os.path.join(SELF_LOCATION, filename)

	if os.path.isfile(filepath):
		print(f'File "{filename}" already there, skipping download.')
		return filepath

	print(f'Downloading "{filename}"...')

	try:
		return urlretrieve(url)[0]
	except Exception as e:
		msg = f'Errore durante il download del file all\'url "{url}": {e}'
		if isinstance(e, URLError) and isinstance(e.reason, ssl.SSLError):
			print(f'Error verifying SSL certificate; disabling SSL verification.')
			ssl._create_default_https_context = ssl._create_unverified_context
			return download_if_needed(url)
		elif isinstance(e, HTTPError):
			e.msg = msg
			raise e
		raise Exception(msg)

def check_game_files(katanazero_filepath):
	game_dir = os.path.dirname(katanazero_filepath)

	katanazero_filepath = os.path.join(game_dir, "Katana ZERO.exe")
	if not os.path.isfile(katanazero_filepath):
		raise FileNotFoundError('File "Katana ZERO.exe" non trovato.')

	datawin_filepath = os.path.join(game_dir, "data.win")
	if not os.path.isfile(datawin_filepath):
		raise FileNotFoundError('File "data.win" non trovato.')

	return katanazero_filepath, datawin_filepath

def patch(katanazero_filepath, datawin_filepath):
	# Patcha Katana ZERO.exe
	try:
		strindex.patch(katanazero_filepath, download_if_needed(KZ_EXE_STRINDEX_URL), None)
	except HTTPError as e:
		if e.code == 404:
			e.msg = (
				'File di patch per "Katana ZERO.exe" non trovato. '
				'Assicurati di avere la versione più recente del gioco E di questo programma.'
			)
		raise
	except ValueError as e:
		if ".strdex" in str(e):
			raise Exception(
				"La patch è stata già applicata in precedenza. "
				"Se credi sia un errore, per favore verifica i file di gioco tramite Steam, "
				"o reinstalla il gioco da capo."
			)
		raise

	# Rileva il tipo di data.win, e scarica il file xdelta corretto
	datawin_xdelta_url = DATAWIN_XDELTA_URL.format(id=get_file_md5_id(datawin_filepath))
	try:
		datawin_xdelta_filepath = download_if_needed(datawin_xdelta_url)
	except HTTPError as e:
		if e.code == 404:
			signals.warning.emit(
				'File di patch per "data.win" non trovato. '
				'La traduzione è stata applicata ma alcune lettere potrebbero avere accenti sbagliati. '
				'Assicurati di avere la versione più recente del gioco E di questo programma.'
			)
			return
		raise

	datawin_bak_filepath = datawin_filepath + ".bak"
	os.replace(datawin_filepath, datawin_bak_filepath)

	# Patcha data.win
	print('Decoding with "data.win.xdelta"...')
	pyxdelta.decode(datawin_bak_filepath, datawin_xdelta_filepath, datawin_filepath)

	os.replace(datawin_bak_filepath, get_file_bak_filepath(datawin_filepath))

def remove(*game_files):
	# Ripristina i file di gioco dai backup
	for filepath in game_files:
		bak_filepath = get_file_bak_filepath(filepath)
		if os.path.isfile(bak_filepath):
			os.replace(bak_filepath, filepath)

	# Rimuovi i file di backup rimanenti
	game_dir = os.path.dirname(game_files[0])
	for filename in os.listdir(game_dir):
		filepath = os.path.join(game_dir, filename)
		if os.path.isfile(filepath) and filename.endswith(".bak"):
			os.remove(filepath)

class KatanaZeroPatchGUI(MainStrindexGUI):
	def setup(self):
		line_edit = self.create_file_selection(
			line_text="*Seleziona il file eseguibile di Katana ZERO",
			button_text="Seleziona file"
		)[0]

		self.create_action_button(
			text="Esegui Patch",
			progress_text="Patch in corso... %p%",
			complete_text="Patch avvenuta con successo.",
			callback=lambda f: (remove(*check_game_files(f)), patch(*check_game_files(f))),
		)

		self.create_action_button(
			text="Rimuovi Patch",
			progress_text="Rimozione... %p%",
			complete_text="I file che avevano backup esistenti sono stati ripristinati, e i backup sono stati rimossi.",
			callback=lambda f: remove(*check_game_files(f)),
		)

		description = QtWidgets.QLabel(
			"Made with ♥ by <a href='https://github.com/zWolfrost'>Luca Russo</a>. "
			"Per dettagli aggiuntivi, riferirsi a "
			"<a href='https://github.com/zWolfrost/Katana-ZERO-Traduzione-Italiana'>questa pagina</a>."
		)
		description.setOpenExternalLinks(True)
		self.__widgets__.append(description)
		self.create_padding(1)

		self.create_grid_layout(2).setColumnStretch(0, 1)

		self.setWindowTitle("Katana ZERO - Traduzione Italiana")
		self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.abspath(os.path.dirname(__file__)), "icon.ico")))

		self.set_custom_appearance()

		for path in POSSIBLE_LOCATIONS:
			path = os.path.expandvars(os.path.expanduser(path)).replace(os.sep, "/")
			if os.path.isfile(path):
				line_edit.setText(path)
				break

		signals.warning.connect(lambda msg: self.show_message(msg, QtWidgets.QMessageBox.Icon.Warning))

if __name__ == "__main__":
	KatanaZeroPatchGUI()
