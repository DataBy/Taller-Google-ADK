FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY agents ./agents

EXPOSE 8000
CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8000", "agents"]
