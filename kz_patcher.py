# nuitka-project: --standalone
# nuitka-project: --onefile
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --nofollow-import-to=lingua
# nuitka-project: --nofollow-import-to=language_tool_python
# nuitka-project: --windows-console-mode=attach

# Questo è un semplice script automatico con GUI per patchare Katana ZERO con la traduzione italiana.
# I file di patch sono scaricati automaticamente da GitHub, perciò è necessario avere una connessione internet.
# Una volta che il DLC sarà uscito, ne rilascierò delle versioni compilate & eseguibili.

# Dipendenze: strindex, pyxdelta, pyside6 (installabili tramite pip)

import os, hashlib, urllib.request, pyxdelta
from PySide6.QtWidgets import QMessageBox
import strindex.strindex as strindex
from strindex.gui import StrindexGUI

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/zWolfrost/Katana-ZERO-Traduzione-Italiana"
KZ_PATCH_URL = DOWNLOAD_ROOT + "/main/kz_patch.gz"
XDELTA_URL_BY_MD5 = {
	"7503b55baf2632e3bc107c43ce696c39": DOWNLOAD_ROOT + "/main/datawin-steam.xdelta",
	"0de1af51000566fa8e0a9d23e34c14b4": DOWNLOAD_ROOT + "/main/datawin-gog.xdelta"
}

def get_file_md5(file):
	hash = hashlib.md5()
	with open(file, "rb") as f:
		while chunk := f.read(8192):
			hash.update(chunk)
	return hash.hexdigest()

def download_file(url):
	try:
		filepath, _ = urllib.request.urlretrieve(url)
	except Exception as e:
		raise ConnectionError(f'Errore durante il download del file all\'url "{url}": {e}')
	return filepath

class KatanaZeroPatchGUI(StrindexGUI):
	def patch(self, katanazero_filepath):
		# Controlla l'esistenza dei file di gioco
		if not os.path.exists(katanazero_filepath) or os.path.basename(katanazero_filepath) != "Katana ZERO.exe":
			raise FileNotFoundError('File "Katana ZERO.exe" errato o non trovato.')

		datawin_filepath = os.path.join(os.path.dirname(katanazero_filepath), "data.win")

		if not os.path.exists(datawin_filepath):
			raise FileNotFoundError('File "data.win" non trovato.')

		# Patcha Katana ZERO.exe
		strindex_filepath = download_file(KZ_PATCH_URL)
		strindex_gz_filepath = strindex_filepath + ".gz"
		os.rename(strindex_filepath, strindex_gz_filepath)
		strindex.patch(katanazero_filepath, strindex_gz_filepath, None)

		# Rileva il tipo di data.win, e scarica il file xdelta corretto
		datawin_bak_filepath = datawin_filepath + ".bak"
		datawin_md5 = get_file_md5(datawin_bak_filepath if os.path.exists(datawin_bak_filepath) else datawin_filepath)

		if datawin_md5 in XDELTA_URL_BY_MD5:
			datawin_xdelta_filepath = download_file(XDELTA_URL_BY_MD5[datawin_md5])
		else:
			self.show_message((
				"File data.win non valido. "
				"La traduzione è stata patchata ma alcune lettere potrebbero avere accenti sbagliati. "
				"Assicurati di avere la versione più recente del gioco."
			), QMessageBox.Warning)
			return

		if not os.path.exists(datawin_bak_filepath):
			os.rename(datawin_filepath, datawin_bak_filepath)

		# Patcha data.win
		pyxdelta.decode(datawin_bak_filepath, datawin_xdelta_filepath, datawin_filepath)

	def setup(self):
		self.create_file_selection(
			line_text="*Seleziona il file eseguibile di Katana ZERO",
			button_text="Seleziona file"
		)

		self.create_action_button(
			text="Esegui Patch",
			progress_text="Patch in corso... %p%",
			complete_text="Patch avvenuta con successo.",
			callback=self.patch,
		)
		self.create_padding(1)

		self.create_grid_layout(2).setColumnStretch(0, 1)

		self.set_window_properties(title="Katana ZERO - Traduzione Italiana")

if __name__ == "__main__":
	KatanaZeroPatchGUI()
