from fastapi import FastAPI
import requests

app = FastAPI()

SERVER_RECEIVER_URL = "http://receiver:8001/receive"

@app.post("/send")
def send_data(data: dict):
    try:
        resp = requests.post(SERVER_RECEIVER_URL, json=data, timeout=5)
        return {"status": "sent", "server_receiver_response": resp.json()}
    except Exception as e:
        return {"error": str(e)}
