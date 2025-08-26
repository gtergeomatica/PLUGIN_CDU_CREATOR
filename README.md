# CDU Creator

Plugin QGIS **CDU Creator** per la compilazione automatica del *Certificato di Destinazione Urbanistica (CDU)*.

Il plugin permette di generare automaticamente un file **PDF** contenente tutte le informazioni urbanistiche relative a una particella catastale selezionata, a partire dall'intersezione con i layer dello strumento urbanistico.  
L'output può essere personalizzato con logo, titolo e testo aggiuntivo (es. riferimenti normativi, note introduttive, ecc.).

---

## Installazione

Il plugin **CDU Creator** è disponibile nella [repository ufficiale dei plugin di QGIS](https://plugins.qgis.org/).  
È quindi possibile installarlo direttamente tramite il *Plugin Manager* di QGIS.  

In alternativa, è possibile installarlo manualmente utilizzando un file `.zip` creato da questa repository.

⚠️ **Nota importante**: lo zip scaricato direttamente da GitHub (*Download ZIP*) **non è installabile** come plugin QGIS, poiché la repository contiene anche il codice della documentazione.  

Per ottenere un pacchetto valido è necessario seguire la procedura sotto descritta.

---

## Creazione del pacchetto ZIP

### Requisiti

Assicurarsi di avere installato **make** e **zip** sul proprio sistema.  
   - Linux/macOS: generalmente già disponibili.  
   - Windows: disponibili tramite [Git for Windows](https://gitforwindows.org/) o [WSL](https://learn.microsoft.com/windows/wsl/).

1. Clonare la repository o scaricare il codice sorgente del plugin:  
   ```bash
   git clone https://github.com/gtergeomatica/PLUGIN_CDU_CREATOR.git
   cd PLUGIN_CDU_CREATOR
   ```

1. Lanciare il comando:
    ```bash
    make
    ```
    Verrà creato un archivio .zip nella root del progetto, ad esempio: `cdu_creator_v1.3.1.zip`
    Questo file contiene il plugin pronto per l'installazione.

### Installazione da ZIP in QGIS

1. QGIS.
2. Dal menu: Plugin → Gestisci e installa Plugin → Installa da ZIP.
3. Selezionare il file cdu_creator_<versione>.zip creato in precedenza.
4. Fare clic su Installa Plugin.

Al termine, il plugin CDU Creator sarà disponibile nell'elenco dei plugin installati e la sua icona comparirà nella barra degli strumenti di QGIS.

## Utilizzo

Il plugin consente di:

- selezionare una particella catastale;
- incrociare i dati con i layer del piano urbanistico;
- produrre un file PDF contenente tutte le informazioni urbanistiche della particella.

Per maggiori dettagli e procedure passo-passo consultare il manuale.

## Documentazione

📖 Il manuale d'uso del Plugin CDU Creator è disponibile al seguente link:
👉 [Manuale CDU Creator](https://manuale-cdu-creator.readthedocs.io/it/latest/index.html)

## Supporto e segnalazioni

Per segnalare errori, bug o proporre miglioramenti aprire una Issue su questa repository:
[Issue Tracker](https://github.com/gtergeomatica/PLUGIN_CDU_CREATOR/issues)

## Licenza
Il plugin è distribuito con [licenza GNU GPL v3](PLUGIN/LICENCE).