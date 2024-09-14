# Katana ZERO Traduzione Italiana
Un uomo con tanto tempo libero affronta la sfida monumentale di provare a tradurre gli oltre 2000 dialoghi di gioco di Katana ZERO in italiano usando il programma "exestringz.exe".
Non dovrebbe essere troppo difficile in realtà. Sono attualmente al **20%** circa (linea 800 di "kz-f.txt").

- "kz.txt": Tutte le stringhe di gioco, dialogo o non.
- "kz-f.txt": **La maggior parte** dei dialoghi di gioco spagnoli. Filtrati usando "langfilter.py".
- "kz-w.txt": La traduzione italiana di "kz-f.txt" + i dialoghi di testo in "kz.txt" non correttamente filtrati da "langfilter.py".

&nbsp;
## Come patchare la traduzione nel gioco
Scarica "exestringz", scarica "kz-w.txt" ed esegui questo comando sul file eseguibile di gioco:
```
.\exestringz.exe 2 'C:\percorso\di\Katana ZERO.exe' 'C:\percorso\di\kz-w.txt'
```
ATTENZIONE: questo comando sovrascriverà il file di gioco in modo irreversibile (o meglio, dovrai riscaricare il gioco per riportarlo da capo)

Renderò questo processo molto più semplice una volta che la traduzione sarà completata.

&nbsp;
## Come puoi aiutarmi
Puoi aiutarmi traducendo il file "kz-f.txt" dallo spagnolo, portando le linee in italiano in "kz-w.txt" e aprendo una pull request quando ti sei rotto di tradurre, immagino.
Per favore inizia dalla fine del file così non dovremmo tradurre gli stessi dialoghi inutilmente.

Un altra cosa molto gentile sarebbe trovare possibili errori grammaticali e/o errori di traduzione nel file "kz-w.txt", e farmi sapere tramite un issue o creare una pull request direttamente.

Puoi aiutarti a tradurre dallo spagnolo usando i dialoghi inglesi. Sono spesso circa 5 lingue straniere sopra quelle spagnole nel file "kz.txt".

&nbsp;
## Domande
Se hai qualche domanda apri un'issue, e proverò a risponderti in tempo utile.
