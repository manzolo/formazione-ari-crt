# Lezioni Radioamatori CRT Toscana - Piattaforma Web

Questa è una piattaforma web sviluppata con Django per la gestione e la visualizzazione di lezioni per radioamatori.

## Prerequisiti

Assicurati di avere installato sul tuo sistema:

* **Python 3:** (Versione raccomandata: 3.8 o superiore) - Puoi scaricarlo da [https://www.python.org/downloads/](https://www.python.org/downloads/)
* **pip:** Il gestore di pacchetti per Python (solitamente incluso con l'installazione di Python).
* **Git:** Per clonare il repository - Puoi scaricarlo da [https://git-scm.com/downloads](https://git-scm.com/downloads)

## Installazione e Configurazione

Segui questi passaggi per configurare ed eseguire l'applicazione sul tuo sistema locale:

1.  **Clona il Repository:**

    Apri il tuo terminale o prompt dei comandi e naviga nella directory in cui desideri clonare il progetto. Esegui il seguente comando:

    ```bash
    git clone https://github.com/manzolo/formazione-ari-crt
    cd formazione-ari-crt
    ```
    
2.  **Crea un Ambiente Virtuale (Raccomandato):**

    È buona pratica creare un ambiente virtuale Python isolato per questo progetto.

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Su Linux/macOS
    venv\Scripts\activate  # Su Windows
    ```

3.  **Installa le Dipendenze:**

    Naviga all'interno della directory del progetto (dove si trova il file `requirements.txt`) ed esegui il seguente comando per installare tutte le librerie necessarie, inclusa Django:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Effettua le Migrazioni:**

    Django utilizza le migrazioni per gestire le modifiche al modello del database. Esegui i seguenti comandi per creare e applicare le migrazioni iniziali:

    ```bash
    python3 manage.py makemigrations lezioni
    python3 manage.py migrate
    ```

    * `python3 manage.py makemigrations lezioni`: Questo comando cerca modifiche nel modello dell'app `lezioni` e crea nuovi file di migrazione.
    * `python3 manage.py migrate`: Questo comando applica tutte le migrazioni in sospeso a tutti i modelli delle tue app, creando le tabelle nel database (se non esistono già).

5.  **Crea un Superutente (Admin):**

    Per accedere all'interfaccia di amministrazione di Django (`/admin/`), devi creare un superutente:

    ```bash
    python3 manage.py createsuperuser
    ```

    Segui le istruzioni a schermo per inserire un nome utente, un indirizzo email e una password per l'utente amministratore.

6.  **Esegui il Server di Sviluppo:**

    Ora puoi avviare il server di sviluppo di Django per visualizzare l'applicazione nel tuo browser:

    ```bash
    python3 manage.py runserver
    ```

    Questo comando avvierà il server di sviluppo all'indirizzo `http://127.0.0.1:8000/`. Apri questo indirizzo nel tuo browser per visualizzare l'applicazione.

## Screenshot
![immagine](https://github.com/user-attachments/assets/7b64bd6e-f587-4137-acbb-7fa9f4a2dc34)

