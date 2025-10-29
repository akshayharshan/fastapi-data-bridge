FROM python:3.11-slim
WORKDIR /app
COPY receiver.py .
RUN pip install fastapi uvicorn
# persistent volume for .wdb files
VOLUME ["/data"]
CMD ["python3", "receiver.py"]
