# nuitka-project: --standalone
# nuitka-project: --onefile
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --nofollow-import-to=lingua
# nuitka-project: --nofollow-import-to=language_tool_python
# nuitka-project: --windows-console-mode=attach
# nuitka-project: --windows-icon-from-ico=icon.ico
# nuitka-project: --include-data-files=icon.ico=./
# nuitka-project: --include-data-files=*.png=./

# Questo è un semplice script automatico con GUI per patchare Katana ZERO con la traduzione italiana.
# I file di patch sono scaricati automaticamente da GitHub, perciò è necessario avere una connessione internet.
# È anche possibile includere i file di patch nella sua stessa cartella per usarlo offline.

import os, pyxdelta, hashlib, ssl
from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError
from PySide6 import QtWidgets, QtCore, QtGui
from strindex import strindex
from strindex.gui import MainStrindexGUI
from strindex.utils import PrintProgress

# Percorsi possibili per Katana ZERO.exe
POSSIBLE_LOCATIONS = [
	"%programfiles(x86)%/Steam/steamapps/common/Katana ZERO/Katana ZERO.exe",
	"%programfiles(x86)%/GOG Galaxy/Games/Katana ZERO/Katana ZERO.exe",
	"~/.steam/steam/steamapps/common/Katana ZERO/Katana ZERO.exe"
]

# URL dei file di patch
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/zWolfrost/Katana-ZERO-Traduzione-Italiana/main/patches/"
KZ_EXE_STRINDEX_URL = DOWNLOAD_ROOT + "kz_exe.gz"
DATAWIN_XDELTA_URL = DOWNLOAD_ROOT + "datawin_{id}.xdelta"

# Crea un worker per i segnali di avviso tra thread diversi.
class SignalWorker(QtCore.QObject):
	warning = QtCore.Signal(str)
signals = SignalWorker()

def get_file_md5_id(file: str) -> str:
	# Restituisci i primi 8 caratteri dell'ID md5 del file.
	MD5_SLICE = 8
	with open(file, "rb") as f:
		file_hash = hashlib.md5()
		while chunk := f.read(8192):
			file_hash.update(chunk)
	return file_hash.hexdigest()[:MD5_SLICE]

def get_file_bak_filepath(file: str) -> str:
	# Usa l'ID md5 del file per creare un filename di backup unico.
	return file + "_" + get_file_md5_id(file) + ".bak"

def download_if_needed(url: str) -> str:
	# Se non esiste già nella cartella attuale, scarica il file.
	filename = os.path.basename(url)
	filepath = os.path.abspath(filename)

	if os.path.isfile(filepath):
		print(f"Il file \"{filename}\" è già presente, salto il download.")
		return filepath

	print(f"Scaricando \"{filename}\"...")

	try:
		return urlretrieve(url)[0]
	except Exception as e:
		msg = f"Errore durante il download del file all'url \"{url}\": {e}"
		if isinstance(e, URLError) and isinstance(e.reason, ssl.SSLError):
			print("Errore durante la verifica del certificato SSL; verifica disattivata.")
			ssl._create_default_https_context = ssl._create_unverified_context
			return download_if_needed(url)
		elif isinstance(e, HTTPError):
			e.msg = msg
			raise e
		raise Exception(msg)

def check_game_files(katanazero_filepath: str) -> tuple[str, str]:
	# Controlla se i file di gioco da patchare esistono, e restituisci i loro percorsi.
	game_dir = os.path.dirname(katanazero_filepath)

	katanazero_filepath = os.path.join(game_dir, "Katana ZERO.exe")
	if not os.path.isfile(katanazero_filepath):
		raise FileNotFoundError("File \"Katana ZERO.exe\" non trovato.")

	datawin_filepath = os.path.join(game_dir, "data.win")
	if not os.path.isfile(datawin_filepath):
		raise FileNotFoundError("File \"data.win\" non trovato.")

	return katanazero_filepath, datawin_filepath

def patch(katanazero_filepath: str, datawin_filepath: str):
	print_progress = PrintProgress(8)
	print_progress(1)

	# Scarica il file di patch per Katana ZERO.exe
	try:
		katanazero_strindex_filepath = download_if_needed(KZ_EXE_STRINDEX_URL)
	except HTTPError as e:
		if e.code == 404:
			e.msg = (
				"File di patch per \"Katana ZERO.exe\" non trovato. "
				"Assicurati di avere la versione più recente di questo programma."
			)
		raise
	print_progress(2)

	# Patcha Katana ZERO.exe
	try:
		strindex.patch(katanazero_filepath, katanazero_strindex_filepath, None)
	except ValueError as e:
		if ".strdex" in str(e):
			raise Exception(
				"La patch è stata già applicata in precedenza. "
				"Se credi sia un errore, per favore verifica i file di gioco tramite Steam, "
				"o reinstalla il gioco da capo."
			)
		raise
	print_progress(3)

	# Rileva l'ID md5 di data.win
	datawin_xdelta_id = get_file_md5_id(datawin_filepath)
	print_progress(4)

	# Scarica il file xdelta giusto per data.win
	try:
		datawin_xdelta_filepath = download_if_needed(DATAWIN_XDELTA_URL.format(id=datawin_xdelta_id))
	except HTTPError as e:
		if e.code == 404:
			signals.warning.emit(
				"File di patch per \"data.win\" non trovato. "
				"La traduzione è stata applicata ma alcune lettere potrebbero avere accenti sbagliati. "
				"Assicurati di avere la versione più recente del gioco E di questo programma."
			)
			return
		raise
	print_progress(5)

	# Crea un backup di data.win
	datawin_bak_filepath = datawin_filepath + ".bak"
	os.replace(datawin_filepath, datawin_bak_filepath)
	print_progress(6)

	# Patcha data.win
	pyxdelta.decode(datawin_bak_filepath, datawin_xdelta_filepath, datawin_filepath)
	print("Il file \"data.win\" è stato patchato con successo.")
	print_progress(7)

	# Rinomina il backup di data.win
	os.replace(datawin_bak_filepath, get_file_bak_filepath(datawin_filepath))
	print_progress(8)

def remove(*game_files: str):
	# Ripristina i file di gioco dai backup
	for filepath in game_files:
		bak_filepath = get_file_bak_filepath(filepath)
		if os.path.isfile(bak_filepath):
			os.replace(bak_filepath, filepath)

	# Rimuovi i file di backup rimanenti per sicurezza
	game_dir = os.path.dirname(game_files[0])
	for filename in os.listdir(game_dir):
		filepath = os.path.join(game_dir, filename)
		if os.path.isfile(filepath) and filename.endswith(".bak"):
			os.remove(filepath)

class KatanaZeroPatchGUI(MainStrindexGUI):
	def setup(self):
		SELF_LOCATION = os.path.abspath(os.path.dirname(__file__))

		logo_pixmap = QtGui.QPixmap(os.path.join(SELF_LOCATION, "header.png"), "PNG")
		logo_pixmap = logo_pixmap.scaled(400, 200, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
		logo_label = QtWidgets.QLabel(pixmap=logo_pixmap, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
		self.__widgets__.append(logo_label)
		self.create_padding(1)

		line_edit = self.create_file_selection(
			line_text="Inserisci il percorso del file eseguibile di Katana ZERO (Katana ZERO.exe)",
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
		self.setWindowIcon(QtGui.QIcon(os.path.join(SELF_LOCATION, "icon.ico")))

		self.set_custom_appearance()

		for path in POSSIBLE_LOCATIONS:
			path = os.path.expandvars(os.path.expanduser(path)).replace(os.sep, "/")
			if os.path.isfile(path):
				line_edit.setText(path)
				break

		signals.warning.connect(lambda msg: self.show_message(msg, QtWidgets.QMessageBox.Icon.Warning))

if __name__ == "__main__":
	KatanaZeroPatchGUI()
