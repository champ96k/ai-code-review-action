FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install google-generativeai requests
ENTRYPOINT ["python", "review_code.py"]