FROM python:3.10-slim

WORKDIR /app

COPY review_code.py requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "/app/review_code.py"]
