FROM python:3.10
WORKDIR /github/workspace
COPY . /github/workspace
RUN pip install google-generativeai requests
ENTRYPOINT ["python", "review_code.py"]