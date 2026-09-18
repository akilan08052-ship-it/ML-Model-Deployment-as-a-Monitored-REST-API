FROM python:3.11-slim


WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
#clarification for host 0.0.0.0
#if set it to 127.0.0.1 it only allows request from local server but if 0.0.0.0 enables the route for outside local server