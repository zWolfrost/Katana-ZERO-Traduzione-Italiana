# Katana ZERO Traduzione Italiana
Ho finalmente affrontato la sfida monumentale di provare a tradurre gli oltre 2000 dialoghi di gioco di Katana ZERO in italiano usando il programma "exestringz.exe".
Detto francamente, il gioco è un capolavoro, e merita di essere localizzato in più lingue possibili. Inizio io.
Non dovrebbe essere troppo difficile in realtà. Sono attualmente al **40%** circa (linea 1400 di "kz-f.txt").

Per capirci riguardo i file di questa repository:
- "kz.txt": Tutte le stringhe di gioco, dialogo o non.
- "kz-f.txt": **La maggior parte** dei dialoghi di gioco spagnoli. Filtrati usando "langfilter.py".
- "kz-w.txt": La traduzione italiana di "kz-f.txt" + i dialoghi di testo in "kz.txt" non correttamente filtrati da "langfilter.py".

&nbsp;
## Come patchare il gioco con la traduzione
Scarica il programma "exestringz", scarica "kz-w.txt", rimuovi le linee che iniziano con "###" ed esegui questo comando sul file eseguibile di gioco:
```
.\exestringz.exe 2 'C:\percorso\di\Katana ZERO.exe' 'C:\percorso\di\kz-w.txt'
```
ATTENZIONE: questo comando sovrascriverà il file di gioco in modo irreversibile (o meglio, dovrai riscaricare il gioco per riportarlo da capo)

Renderò questo processo molto più semplice e carino una volta che la traduzione sarà completata (se sarà necessario)

&nbsp;
## FAQ
#### Come posso aiutarti?
Una cosa molto gentile che puoi fare per aiutarmi sarebbe rendere la traduzione attuale migliore, cioè trovare possibili errori grammaticali e/o di traduzione nel file "kz-w.txt", e farmi sapere tramite un issue o creare una pull request direttamente.
Puoi aiutarti a tradurre dallo spagnolo usando i dialoghi inglesi. Sono spesso circa 5 lingue straniere sopra quelle spagnole nel file "kz.txt".

#### Stai per caso rompendo il copyright del gioco?
Per niente. Per usare questa traduzione devi avere comunque a disposizione del gioco, e del file con tutte le stringhe non ci fai nulla, di per sè.

#### Non dovrai rifare tutto da capo una volta uscito il DLC?
È probabile che una volta uscito il DLC si dovranno reinserire le linee tradotte nel giusto punto, ma creare uno script python che traduce le giuste frasi e le sostituisce automaticamente partendo da questa traduzione sarebbe estremamente semplice.
Ovviamente in tal caso dovrò tradurre anche i dialoghi del DLC, e ci vorrà circa una settimana, se è lungo quanto il gioco originale.
L'unica cosa che potrebbe vanificare i miei sforzi (e possibilmente quelli dei contribuitori) sarebbe se lo sviluppatore introducesse la lingua Italiana nel gioco effettivo. Ma credo che ciò non solo è improbabile, ma renderebbe comunque tutti felici, in ogni caso.

#### *Hai una domanda non presente tra queste?*
Se hai qualche altra domanda apri un'issue, e proverò a risponderti in tempo utile.
