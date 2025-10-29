from fastapi import FastAPI
import requests
import uvicorn

app = FastAPI()

SERVER_RECEIVER_URL = "http://receiver:7000/receive"

@app.post("/send")
def send_data(data: dict):
    try:
        resp = requests.post(SERVER_RECEIVER_URL, json=data, timeout=5)
        return {"status": "sent", "server_receiver_response": resp.json()}
    except Exception as e:
        return {"error": str(e)}
if __name__ == "__main__":
    uvicorn.run(
            "sender:app",
            host = "0.0.0.0",
            port = 8000,
            reload = True
    )
