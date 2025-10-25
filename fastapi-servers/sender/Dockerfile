FROM python:3.11-slim
WORKDIR /app
COPY sender.py .
RUN pip install fastapi uvicorn requests
CMD ["uvicorn", "sender:app", "--host", "0.0.0.0", "--port", "8000"]
