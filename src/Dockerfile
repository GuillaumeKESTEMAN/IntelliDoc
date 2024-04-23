FROM python:3.9.1

WORKDIR /app

COPY .env ./
COPY src/requirements.txt ./
COPY src/index_mapping.json ./
COPY src/search.py ./
COPY src/add_data.py ./
COPY src/import_wikipedia_data.py ./
COPY src/main.py ./
COPY src/build.py ./

RUN pip install -r requirements.txt
RUN echo "Téléchargement du modèle d'IA...";python build.py
RUN rm build.py

CMD echo "Exécutez 'python main.py'";tail -f /dev/null