from fastapi import FastAPI, Request
import json, atexit
from datetime import datetime

app = FastAPI()
received_data = []

@app.post("/receive")
async def receive_data(request: Request):
    data = await request.json()
    received_data.append(data)
    return {"status": "received", "count": len(received_data)}

def write_to_file():
    filename = f"/data/received_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wdb"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(received_data, f, indent=2)
    print(f"🧾 Data written to {filename}")

atexit.register(write_to_file)
