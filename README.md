# Katana ZERO Traduzione Italiana
Ho finalmente affrontato la sfida monumentale di provare a tradurre gli oltre 2000 dialoghi di gioco di Katana ZERO in italiano usando il programma "exestringz.exe".

Detto francamente, il gioco è un capolavoro, e merita di essere localizzato in più lingue possibili. Inizio con quella che conosco.

Non dovrebbe essere troppo difficile in realtà. Sono attualmente al 75% circa (linea 2600 di "stringz-filter.txt").

Per capirci riguardo i file di questa repository:
- "stringz.txt": Tutte le stringhe di gioco, dialogo o non.
- "stringz-filter.txt": **La maggior parte** dei dialoghi di gioco spagnoli. Filtrati usando "stringz-filter.py". È solo per riferimento.
- "translation.json": La traduzione italiana di "stringz-filter.txt" + i dialoghi di testo in "stringz-filter.txt" non correttamente filtrati da "langfilter.py", in un file json.

&nbsp;
## Come patchare il gioco con la traduzione
Scarica il programma "exestringz", scarica "stringz-patch.txt" esegui questo comando sul file eseguibile di gioco:
```
.\exestringz.exe 2 'C:\percorso\di\Katana ZERO.exe' 'C:\percorso\di\stringz-patch.txt'
```
ATTENZIONE: questo comando sovrascriverà il file di gioco in modo irreversibile (o meglio, dovrai riscaricare il gioco per riportarlo da capo)

Renderò questo processo molto più semplice e carino una volta che la traduzione sarà completata (se sarà necessario)

&nbsp;
## FAQ
### Come posso aiutarti?
Se trovi delle frasi spagnole non tradotte, fai uno screenshot e crea un'issue su questa pagina allegando lo screenshot (o perfino un e-mail andrebbe bene). Questa traduzione è stata creata da poco per cui sarebbe completamente possibile.

Un'altra cosa molto gentile che puoi fare per aiutarmi sarebbe rendere la traduzione attuale migliore, cioè trovare possibili errori grammaticali, di traduzione o anche semplicemente delle frasi che suonano "male", nel file "translation.json", e facendomi sapere tramite un issue o creando una pull request che sistemi il problema direttamente.

Puoi aiutarti a tradurre dallo spagnolo usando i dialoghi inglesi. Sono spesso circa 5 lingue straniere sopra quelle spagnole nel file "stringz.txt".

### Stai per caso rompendo il copyright del gioco?
Per niente. Per usare questa traduzione devi avere comunque a disposizione del gioco, e del file con tutte le stringhe non ci fai nulla, di per sè.

### Non dovrai rifare tutto da capo una volta uscito il DLC?
È probabile che una volta uscito il DLC si dovranno reinserire le linee tradotte nel giusto punto, ma le linee tradotte non sono vincolate dalla loro posizione (nel file json), quindi ci vorrà veramente poco tempo per sistemare le cose. Ovviamente in tal caso dovrò tradurre anche i dialoghi del DLC, e ci vorrà circa una settimana, se sarà lungo quanto il gioco originale.

L'unica cosa che potrebbe vanificare i miei sforzi (e possibilmente quelli dei contribuitori) sarebbe se lo sviluppatore introducesse la lingua Italiana nel gioco effettivo. Ma credo che ciò non solo è improbabile, ma renderebbe comunque tutti felici, in ogni caso.

### Quanto è fedele questa traduzione?
Direi molto. Per chi lo stesse pensando, non ho tradotto dalla traduzione spagnola, ma dall'inglese, quella originale. Mi servo solo della traduzione spagnola per sostituirla con quella italiana. Ho cercato il più possibile di non distorcere il significato delle frasi, ma non assicuro nulla.

### *Hai una domanda non presente tra queste?*
Se hai qualche altra domanda apri un'issue a proposito, e proverò a risponderti in tempo utile.
