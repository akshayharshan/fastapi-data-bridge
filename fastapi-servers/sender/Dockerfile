FROM python:3.11-slim
WORKDIR /app
COPY sender.py .
RUN pip install fastapi uvicorn requests
CMD ["python3", "sender.py"]
