FROM python:3.13-slim

WORKDIR /app

COPY backend/requirements.txt ./backend/requirements.txt

RUN pip install --no-cache-dir -r backend/requirements.txt

COPY backend/ ./backend/
COPY index.html style.css script.js ./
COPY assets/ ./assets/

RUN useradd --create-home --shell /bin/bash larbod

RUN chown -R larbod:larbod /app

USER larbod

WORKDIR /app/backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
