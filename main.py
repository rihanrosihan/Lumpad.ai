import os
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

VERIFY_TOKEN = "lumpad123"

@app.get("/")
def root():
    return {"status": "Lumpad running 🚀"}

# ✅ endpoint webhook GET (buat verifikasi Strava)
@app.get("/webhook")
def verify(mode: str = None, token: str = None, challenge: str = None):
    if token == VERIFY_TOKEN:
        return {"challenge": challenge}
    return {"error": "invalid"}

# ✅ endpoint webhook POST (buat terima event)
@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    print("EVENT:", data)
    return {"ok": True}

# optional (biar tetap aman jalan di local/railway)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
