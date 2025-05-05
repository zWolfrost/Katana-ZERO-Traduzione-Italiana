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

# Dipendenze: strindex, pyxdelta, pyside6 (installabili tramite pip)

import os, sys, hashlib, urllib.request, pyxdelta
from PySide6 import QtWidgets
import strindex.strindex as strindex
from strindex.gui import StrindexGUI
from strindex.utils import PrintProgress

SELF_LOCATION = os.path.dirname(os.path.abspath(sys.argv[0]))

POSSIBLE_LOCATIONS = [
	"C:/Program Files (x86)/Steam/steamapps/common/Katana ZERO/Katana ZERO.exe",
	"~/.steam/steam/steamapps/common/Katana ZERO/Katana ZERO.exe"
]

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/zWolfrost/Katana-ZERO-Traduzione-Italiana/main/"
KZ_PATCH_URL = DOWNLOAD_ROOT + "kz_patch.gz"
XDELTA_URL_BY_MD5 = {
	"7503b55baf2632e3bc107c43ce696c39": DOWNLOAD_ROOT + "datawin_steam.xdelta",
	"0de1af51000566fa8e0a9d23e34c14b4": DOWNLOAD_ROOT + "datawin_gog.xdelta"
}

def get_file_md5(file):
	hash = hashlib.md5()
	with open(file, "rb") as f:
		while chunk := f.read(8192):
			hash.update(chunk)
	return hash.hexdigest()

def download_if_needed(url):
	filename = os.path.basename(url)
	filepath = os.path.join(SELF_LOCATION, filename)

	if os.path.isfile(filepath):
		print(f"File {filename} already there, skipping download.")
		return filepath

	try:
		return urllib.request.urlretrieve(url)[0]
	except Exception as e:
		raise ConnectionError(f'Errore durante il download del file all\'url "{url}": {e}')

class KatanaZeroPatchGUI(StrindexGUI):
	def start_action(self):
		for widget in self.findChildren(QtWidgets.QWidget):
			if isinstance(widget, QtWidgets.QProgressBar):
				PrintProgress.callback = lambda progress: widget.setValue(progress.percent)

	def patch(self, katanazero_filepath):
		# Controlla l'esistenza dei file di gioco
		if not os.path.isfile(katanazero_filepath) or os.path.basename(katanazero_filepath) != "Katana ZERO.exe":
			raise FileNotFoundError('File "Katana ZERO.exe" errato o non trovato.')

		datawin_filepath = os.path.join(os.path.dirname(katanazero_filepath), "data.win")

		if not os.path.isfile(datawin_filepath):
			raise FileNotFoundError('File "data.win" non trovato.')

		# Questo controllo non è per niente affidabile, infatti non bloccherà il processo.
		file_count = len(next(os.walk(os.path.dirname(katanazero_filepath)))[2])
		if file_count > 60:
			self.show_message((
				"Questo gioco è stato probabilmente piratato. "
				"La patch avverrà malgrado ciò, ma per favore considera di supportare gli sviluppatori ;)"
			), QtWidgets.QMessageBox.Warning)

		# Patcha Katana ZERO.exe
		strindex_filepath = download_if_needed(KZ_PATCH_URL)
		strindex_gz_filepath = strindex_filepath.rstrip(".gz") + ".gz"
		os.rename(strindex_filepath, strindex_gz_filepath)
		strindex.patch(katanazero_filepath, strindex_gz_filepath, None)

		# Rileva il tipo di data.win, e scarica il file xdelta corretto
		datawin_bak_filepath = datawin_filepath + ".bak"
		datawin_md5 = get_file_md5(datawin_bak_filepath if os.path.isfile(datawin_bak_filepath) else datawin_filepath)

		if datawin_md5 in XDELTA_URL_BY_MD5:
			datawin_xdelta_filepath = download_if_needed(XDELTA_URL_BY_MD5[datawin_md5])
		else:
			self.show_message((
				"File data.win non valido. "
				"La traduzione è stata patchata ma alcune lettere potrebbero avere accenti sbagliati. "
				"Assicurati di avere la versione più recente del gioco."
			), QtWidgets.QMessageBox.Warning)
			return

		if not os.path.isfile(datawin_bak_filepath):
			os.rename(datawin_filepath, datawin_bak_filepath)

		# Patcha data.win
		print("Decoding using data.win.xdelta...")
		pyxdelta.decode(datawin_bak_filepath, datawin_xdelta_filepath, datawin_filepath)

	def remove(self, katanazero_filepath):
		# Ripristina i file di gioco dai backup
		katanazero_bak_filepath = katanazero_filepath + ".bak"

		if not os.path.isfile(katanazero_bak_filepath) or os.path.basename(katanazero_bak_filepath) != "Katana ZERO.exe.bak":
			raise FileNotFoundError((
				'File di backup "Katana ZERO.exe.bak" non trovato. '
				'Non è possibile ripristinare il gioco (o è già allo stato originale).'
			))

		if os.path.isfile(katanazero_filepath):
			os.remove(katanazero_filepath)

		os.rename(katanazero_bak_filepath, katanazero_filepath)

		datawin_filepath = os.path.join(os.path.dirname(katanazero_filepath), "data.win")
		datawin_bak_filepath = datawin_filepath + ".bak"

		if os.path.isfile(datawin_filepath):
			os.remove(datawin_filepath)

		os.rename(datawin_bak_filepath, datawin_filepath)

	def update_buttons(self, katanazero_filepath):
		enabled = os.path.isfile(katanazero_filepath)
		self.__widgets__[-1].setEnabled(enabled)
		self.__widgets__[-2].setEnabled(enabled)

	def setup(self):
		line_edit = self.create_file_selection(
			line_text="*Seleziona il file eseguibile di Katana ZERO",
			button_text="Seleziona file"
		)[0]

		line_edit.textChanged.connect(self.update_buttons)

		self.create_action_button(
			text="Esegui Patch",
			progress_text="Patch in corso... %p%",
			complete_text="Patch avvenuta con successo.",
			callback=lambda filepath: (self.start_action(), self.patch(filepath)),
		)

		self.create_action_button(
			text="Rimuovi Patch",
			progress_text="Rimozione... %p%",
			complete_text="Rimozione patch avvenuta con successo.",
			callback=lambda filepath: (self.start_action(), self.remove(filepath)),
		)

		self.create_grid_layout(2).setColumnStretch(0, 1)

		self.set_window_properties(title="Katana ZERO - Traduzione Italiana")

		for path in POSSIBLE_LOCATIONS:
			path = os.path.expanduser(path)
			if os.path.isfile(path):
				line_edit.setText(path)
				self.update_buttons(path)
				break

if __name__ == "__main__":
	KatanaZeroPatchGUI()
