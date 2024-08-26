Introduzione
==================

Credits
------------------------------------------

.. image:: img/Gter.png
https://www.gter.it/


Il Plugin QGIS **CDU Creator** e questo manuale sono stati sviluppati da Gter srl Innovazione in Geomatica GNSS e GIS.

Sia il Plugin che il manuale sono distribuiti con licenza Creative Commons Attribution 4.0 International License https://creativecommons.org/licenses/by/4.0/

Acknowledgements
------------------------------------------

La funzione di multi selezione delle particelle catastali per la compilazione utomatica del CDU è stata implementata grazie ai forndi raccolti con la campagna di crowdfunding (http://sostieni.link/23824) che si è conclusa con successo il 15 Marzo 2020. La funzione è ora disponibile grazie al contributo di tutti coloro che hanno supportato il progetto. **Gter vuole quindi ringraziare tutti i sostenitori del Plugin QGIS CDU Creator!** `CLICCA QUI <acknow.html#acknowledgement>`__  per vedere l'elenco completo dei sostenitori!

Scopo
------------------------------------------
E’ noto che una delle esigenze più diffuse, fra gli oltre 9200 Comuni italiani, è la realizzazione dei Certificati di Destinazione Urbanistica (CDU).

Sono disponibili molte soluzioni online che però comportano spesso un costo che non tutti i Comuni possono affrontare. Inoltre i dati catastali non sempre sono pronti all'uso, necessitano di continui aggiornamenti e possono richiedere un affinamento delle comuni trasformazioni ottenute con i punti fiduciali al fine di ottenere la corretta georeferenziazione dei dati stessi.

Per queste ragioni ancora oggi molti uffici tecnici per effettuare operazioni di intersezione tra il catasto terreni e i layer urbanistici (vincoli, zone, ecc.) continuano a privilegiare soluzioni per nulla automatizzate invece che servirsi di Sistemi Informativi Territoriali, nonostante l’uso di tali sistemi potrebbe rendere la compilazione del CDU decisamente più semplice, veloce e precisa.

A partire da queste considerazioni, Gter ha sviluppato il **Plugin QGIS CDU Creator** con lo scopo di agevolare le attività di compilazione del CDU agli uffici tecnici fornendo uno strumento semplice e Open Source che consente appunto di ottenere un CDU impostando solo pochi parametri.

Il **Plugin CDU Creator** genera un file .pdf, **e se specificato un file di testo modificabile .odt**, contenete tutte le informazioni necessarie per la validità del CDU a partire dai layers vettoriali dei terreni catastali e dello strumento urbanistico vigente (PUC, PRG, ecc.). I dati vettoriali dello strumento urbanistico, organizzati in gruppi e sottogruppi, vengono intersecati con le particelle catastali selezionate dall'utente, le informazioni relative alle aree del piano interessate vengono automaticamente recuperate e stampate nel file .pdf/.odt. 

L'output finale è un file .pdf/.odt contente il CDU generato automaticamente e personalizzato in base ai parametri definiti tramite l'interfaccia grafica dall'utente. Il CDU conterrà quindi, non solo le informazione relative alle aree dello strumento urbanistico interessate ma anche il titolo e logo del Comune definiti dall'utente e, se richiesti, anche un paragrafo di introduzione al documento contenete eventuali riferimenti normativi, diciture o altro che devono essere indicati nel CDU per renderlo valido a tutti gli effetti e la mappa con la visualizzazione delle particelle selezionate.

.. note:: Il dataset di esempio, già pronto per l'utilizzo del plugin, è stato realizzato da **Salvatore Fiandaca** (https://pigrecoinfinito.wordpress.com/) ed è scaricabile qui :download:`zip <dati/dati_test_CDU.zip>`. Il dataset è stato creato usando parte dei dati presenti nel plugin **CXF_in** (https://github.com/saccon/CXF_in) di **Fabio Saccon**.

.. seealso:: Di seguito la registrazione del webinar sul Plugin CDU Creator realizzato con **Paolo Corradeghini** di **3DMetrica** (https://3dmetrica.it).

.. raw:: html

	<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
		<iframe src="https://www.youtube.com/embed/Sb5u4Xos638" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
	</div>

"""""""""""""""""""""""""""""""""""""""""""""""

Glossario
------------------------------------------

* CDU: Certificato di Destinazione Urbanistica
* PUC: Piano Urbanistico Comunale
* PRG: Piano Regolatore Generale
* GIS: Geographic Information System
* SIT: Sistemi Informativi Territoriali









.. _Gter srl: https://www.gter.it
