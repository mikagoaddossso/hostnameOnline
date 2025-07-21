# hostnameOnline

Questo progetto è una semplice applicazione Flask che restituisce il nome host del server in formato HTML.

## Requisiti
- Python 3.x
- `pip` (gestore pacchetti Python)

## Istruzioni per l'esecuzione

1. **Creare un ambiente virtuale**:
   ```sh
   python -m venv venv
   ```

2. **Attivare l'ambiente virtuale**:
   - Su Windows:
     ```sh
     venv\Scripts\activate
     ```
   - Su macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

3. **Installare le dipendenze**:
   ```sh
   pip install

 flask


   ```

4. **Eseguire l'applicazione**:
   ```sh
   python py.py
   ```

5. **Accedere all'applicazione**:
   Aprire un browser e visitare `http://localhost:8080` per visualizzare il nome host del server.

## Eseguire con Docker

1. **Costruire l'immagine Docker**:
   Assicurarsi di trovarsi nella directory contenente il file `Dockerfile` e il file `py.py`, quindi eseguire:
   ```sh
   docker build -t hostnameonline .
   ```

2. **Eseguire il container**:
   ```sh
   docker run -p 8080:80 hostnameonline
   ```

3. **Accedere all'applicazione**:
   Aprire un browser e visitare `http://localhost:8080` per visualizzare il nome host del server.
```