# Katana ZERO - Traduzione Italiana
Sono finalmente riuscito a tradurre gli oltre 2000 dialoghi di Katana ZERO in italiano, e ho scritto un programma apposito per sostituire il testo.

**ATTENZIONE: Questa patch è stata testata solo sulla versione di gioco "v1.0.5", build "3889288", l'ultima disponibile**

Comunque, dovrebbe funzionare su qualsiasi versione del gioco, ma con la possibilità che alcune linee non vengano tradotte.

<br>

## Come patchare il gioco con la traduzione
Scarica "[kz_patch.gz](https://raw.githubusercontent.com/zWolfrost/Katana-ZERO-Traduzione-Italiana/main/kz_patch.gz)", scarica il programma "[strindex](https://github.com/zWolfrost/strindex/releases/tag/v3.7.1)", e avvialo. Una volta aperto, clicca il bottone "**Patch**" e, nella nuova finestra, seleziona prima il file eseguibile di gioco "**Katana ZERO.exe**" (presente nella cartella di installazione), e subito sotto il file "**kz_patch.gz**" scaricato (nessun bisogno di estrarlo). Infine, clicca il tasto "**Patch file**" e attendi che il programma finisca.

Se il programma dovesse essere segnalato come malware, si consiglia di disabilitare temporaneamente Windows Defender, in quanto si tratta di un falso positivo (molto comune nei file compilati di python). Per tua informazione, strindex è Open Source e, se non ti fidi, puoi sempre installare la versione command line e patchare il gioco con i seguenti comandi:

```sh
pip install strindex
strindex patch "C:\percorso\di\Katana ZERO.exe" "C:\percorso\di\kz_patch.gz"
```

*Se il programma dovesse dare problemi, per favore segnalali aprendo un'issue, mandandomi un'email o scrivendo sul thread di steam.*

<br>

## Come cambiare gli accenti di `ì`, `Ì`, `ò`, `Ò` in accenti acuti
Apri il sito [xdelta patcher](https://kotcrab.github.io/xdelta-wasm/) e inserisci come "**Source file**" il file "data.win" presente nella cartella di installazione di gioco, e come "**Patch file**" il file "[data.win.xdelta](https://raw.githubusercontent.com/zWolfrost/Katana-ZERO-Traduzione-Italiana/main/data.win.xdelta)" fornito. Infine, premi "Apply patch" e sostituisci il file "data.win" scaricato con quello di gioco. A differenza della patch descritta in precedenza, questo metodo **funzionerà esclusivamente sulla versione presente del gioco**.

<br>

## Come rimuovere la patch
Il programma usato, **strindex**, crea un file di backup del file eseguibile originale nella stessa cartella, con estensione "**.bak**". Per rimuovere la patch, puoi semplicemente rinominare il file di backup in "**Katana ZERO.exe**" e sovrascrivere il file eseguibile patchato.

In alternativa, puoi [verificare l'integrità dei file di gioco](https://help.steampowered.com/it/faqs/view/0C48-FCBD-DA71-93EB) tramite Steam, e il gioco verrà ripristinato allo stato originale.

<br>

## FAQ
### Come posso aiutarti?
Se trovi delle frasi spagnole non tradotte, ti prego di fare uno screenshot e creare un'issue su questa pagina allegando quest'ultimo (o perfino mandare un e-mail andrebbe bene).

Un'altra cosa che potresti fare per aiutarmi sarebbe rendere la traduzione attuale migliore, cioè trovare possibili errori grammaticali, di traduzione o anche semplicemente delle frasi che suonano male nel contesto del gioco, e facendomi sapere.

Inoltre, puoi supportare il mio lavoro donandomi qualcosa [su questa pagina](https://paypal.me/zwolfrost) o [quest'altra](https://buymeacoffee.com/zwolfrost). Ne sarei estremamente grato.

### Non dovrai rifare tutto da capo una volta uscito il DLC?
Fortunatamente le linee tradotte non sono vincolate dalla loro posizione, quindi ci vorrà veramente poco tempo per sistemare le cose. Ovviamente in tal caso dovrò tradurre anche i dialoghi del DLC, e ci vorrà circa una settimana, se sarà lungo quanto il gioco originale.

L'unico problema che potrebbe presentarsi sarebbe se lo sviluppatore dovesse cambiare il modo con cui vengono memorizzate le linee di testo, rendendo il mio programma inutile, e possibilmente rendendo il processo di traduzione molto più lungo e complicato.

### Quanto è fedele questa traduzione?
Direi molto. Per chi lo stesse pensando, non ho tradotto dalla traduzione spagnola, ma dall'inglese, quella originale. Mi servo solo della traduzione spagnola per sostituirla con quella italiana.

Ho cercato il più possibile di non distorcere il significato delle frasi, tenendo presente del loro contesto nel gioco, e catturarne l'impatto, ma non assicuro nulla.

### *Hai una domanda non presente tra queste?*
Se hai qualche altra domanda apri un'issue a proposito, chiedila sul thread di steam o mandami un email, e proverò a risponderti in tempo utile.

<br>

## Screenshots
![Katana ZERO](./screenshot1.png)
![Katana ZERO](./screenshot2.png)
