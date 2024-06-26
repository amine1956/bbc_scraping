FROM python:3.11.4-buster


WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY . .

CMD ["python", "main.py"]
