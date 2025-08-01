# Katana ZERO - Traduzione Italiana
[![Download](https://img.shields.io/github/downloads/zWolfrost/Katana-ZERO-Traduzione-Italiana/total?label=Download)](https://github.com/zWolfrost/Katana-ZERO-Traduzione-Italiana/releases/latest)
[![Versione](https://img.shields.io/github/v/release/zWolfrost/Katana-ZERO-Traduzione-Italiana?label=Versione)](https://github.com/zWolfrost/Katana-ZERO-Traduzione-Italiana/releases/latest)

Sono riuscito con non poche difficoltà a tradurre gli oltre 2000 dialoghi di Katana ZERO in italiano, e scrivere un programma apposito per sostituire il testo.

**ATTENZIONE: Questa patch è stata testata solo sulla versione di gioco "v1.0.5", build "3889288", l'ultima disponibile**

Comunque, dovrebbe funzionare su qualsiasi versione del gioco, ma con la possibilità che alcune linee non vengano tradotte.

<br>

## Come applicare la traduzione

Il programma per effettuare la patch automaticamente [si trova qui](https://github.com/zWolfrost/Katana-ZERO-Traduzione-Italiana/releases/latest). È necessaria una connessione a internet per poter scaricare le ultime patch (a meno che non si includano queste nella sua stessa cartella).

Inoltre, per sistemi Linux, è necessario installare la libreria `libxcb-cursor0` (usando il package manager della distribuzione installata) per poterlo eseguire.

Se il programma dovesse essere segnalato come malware, si consiglia di disabilitare temporaneamente Windows Defender, in quanto si tratta di un falso positivo (molto comune nei file compilati di python). Il codice sorgente completo è disponibile [qui](./patcher/patcher.py).

*Se il programma dovesse dare problemi, per favore segnalali aprendo un'issue, mandandomi un'email o scrivendo sul thread di steam.*

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
Attualmente le linee tradotte sono prese direttamente dalla traduzione italiana ufficiale (presente esclusivamente nella versione da telefono del gioco, pubblicata da Netflix), con solo alcune piccole modifiche fatte.

In futuro cercherò il più possibile di non distorcere il significato delle frasi, tenendo presente del loro contesto nel gioco, e catturarne l'impatto, ma non assicuro nulla.

### Cosa fa il programma esattamente?
Il programma:
- Crea un backup dei file originali, in modo da poterli ripristinare in qualsiasi momento;
- Patcha il file `Katana ZERO.exe` con il file di traduzioni [kz_exe.txt](./patches/kz_exe.txt), usando lo strumento [strindex](https://github.com/zWolfrost/strindex);
- Patcha il file `data.win` con uno dei file `datawin_*.xdelta` presenti [qui](./patches), usando lo strumento [xdelta](https://github.com/jmacd/xdelta).

### *Hai una domanda non presente tra queste?*
Se hai qualche altra domanda puoi aprire un'issue a proposito, chiederla sul thread di steam o mandarmi un email, e proverò a risponderti in tempo utile.

<br>

## Screenshots
![Katana ZERO](./assets/screenshot1.png)
![Katana ZERO](./assets/screenshot2.png)
