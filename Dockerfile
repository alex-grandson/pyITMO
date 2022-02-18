FROM python:3.9-alpine

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app
WORKDIR /app

COPY . .

CMD ["python3", "server.py"]