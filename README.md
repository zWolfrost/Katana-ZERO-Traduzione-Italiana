# Katana ZERO Traduzione Italiana
Sono finalmente riuscito a tradurre gli oltre 2000 dialoghi di gioco di Katana ZERO in italiano usando il programma "exestringz" per sostituire le linee.
Detto francamente, il gioco è un capolavoro, e merita di essere localizzato in più lingue possibili. Inizio con quella che conosco.

**ATTENZIONE: Questa patch funziona solo sulla versione di gioco "v1.0.5", build "3889288", l'ultima disponibile**

Comunque, crearne una su altre versioni non è troppo complicato; in questa repository ci sono i file necessari per [crearla su qualsiasi build](#come-creare-una-patch-per-una-build-meno-recente). C'è solo quella dell'ultima versione per questioni di comodità. Se vorresti aiuto o hai domande riguardo le istruzioni, chiedi pure.

&nbsp;
## Come patchare il gioco con la traduzione
Scarica il programma "[exestringz](https://aluigi.altervista.org/mytoolz/exestringz.zip)", scarica "[stringz_patch.txt](https://raw.githubusercontent.com/zWolfrost/Katana-ZERO-Traduzione-Italiana/main/stringz_patch.txt)" (Ctrl+S) ed esegui questo comando:
```sh
"C:\percorso\di\exestringz.exe" 2 "C:\percorso\di\Katana ZERO.exe" "C:\percorso\di\stringz_patch.txt"
```
**ATTENZIONE**: Questo comando sovrascriverà il file eseguibile di gioco in modo irreversibile, quindi è consigliabile creare un backup. **Non** perderai i tuoi progressi in caso contrario, ma dovrai riscaricare il gioco per riportarlo da capo.

*PS: Puoi trascinare i file nel prompt dei comandi per inserire il loro percorso più velocemente.*

&nbsp;
## Come creare una patch per una build meno recente
Scarica il programma "[exestringz](https://aluigi.altervista.org/mytoolz/exestringz.zip)", scarica [questa repository](https://github.com/zWolfrost/Katana-ZERO-Traduzione-Italiana/archive/refs/heads/main.zip) ed esegui questi comandi all'interno della cartella "exestringz-translation-tools" della repository scaricata:
```sh
"C:\percorso\di\exestringz.exe" 1 -f "C:\percorso\di\Katana ZERO.exe" "stringz_full.txt"
```
```sh
py stringz_patch.py
```
**ATTENZIONE**: Il primo comando durerà molto di tempo (anche 30 minuti). Inoltre, per eseguire il secondo comando, devi avere Python installato sul tuo computer. Quello script creerà il file "stringz_patch.txt" nella "cartella parente", cioè quella che contiene "exestringz-translation-tools".

Dopo aver eseguito questi comandi, esegui il comando del [paragrafo precedente](#come-patchare-il-gioco-con-la-traduzione) per patchare il gioco.

&nbsp;
## FAQ
### Come posso aiutarti?
Se trovi delle frasi spagnole non tradotte, fai uno screenshot e crea un'issue su questa pagina allegando lo screenshot (o perfino un e-mail andrebbe bene). Questa traduzione è stata creata da relativamente poco tempo per cui una cosa del genere sarebbe completamente plausibile.

Un'altra cosa molto gentile che potresti fare per aiutarmi sarebbe rendere la traduzione attuale migliore, cioè trovare possibili errori grammaticali, di traduzione o anche semplicemente delle frasi che suonano male nel contesto del gioco, nel file "translation.json", e facendomi sapere.

Inoltre, puoi supportare il mio lavoro donandomi qualcosa [su questa pagina](https://paypal.me/zwolfrost) o [quest'altra](https://buymeacoffee.com/zwolfrost). Ne sarei estremamente grato.

### Non dovrai rifare tutto da capo una volta uscito il DLC?
È probabile che una volta uscito il DLC si dovranno reinserire le linee tradotte nel giusto punto, ma le linee tradotte non sono vincolate dalla loro posizione (nel file json), quindi ci vorrà veramente poco tempo per sistemare le cose. Ovviamente in tal caso dovrò tradurre anche i dialoghi del DLC, e ci vorrà circa una settimana, se sarà lungo quanto il gioco originale.

L'unica cosa che potrebbe vanificare i miei sforzi (e quelli di chi ha contribuito a questa traduzione) sarebbe se lo sviluppatore introducesse la lingua Italiana nel gioco effettivo. Ma non solo penso che sia improbabile, ma se mai dovesse succedere, renderebbe comunque tutti felici.

### Quanto è fedele questa traduzione?
Direi molto. Per chi lo stesse pensando, non ho tradotto dalla traduzione spagnola, ma dall'inglese, quella originale. Mi servo solo della traduzione spagnola per sostituirla con quella italiana.

Ho cercato il più possibile di non distorcere il significato delle frasi, tenendo presente del loro contesto nel gioco, e catturarne l'impatto, ma non assicuro nulla.

### Stai per caso rompendo il copyright del gioco?
No. Per usare questa traduzione devi essere necessariamente a disposizione del file eseguibile di gioco.

### *Hai una domanda non presente tra queste?*
Se hai qualche altra domanda apri un'issue a proposito, chiedila sul thread di steam o mandami un email, e proverò a risponderti in tempo utile.
