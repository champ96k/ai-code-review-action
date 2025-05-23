FROM python:3.10-slim

# Install dependencies
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Set the entrypoint to use the mounted workspace
ENTRYPOINT ["python", "review_code.py"]