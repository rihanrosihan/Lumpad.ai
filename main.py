import os
from fastapi import FastAPI, Request, Response
import uvicorn


app = FastAPI()

VERIFY_TOKEN = "lumpad123"

@app.get("/webhook")
def verify(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    # debug print (opsional, bantu lihat di logs)
    print("MODE:", mode)
    print("TOKEN:", token)
    print("CHALLENGE:", challenge)

    if mode == "subscribe" and token == VERIFY_TOKEN and challenge:
        return Response(content=str(challenge), media_type="text/plain")

    return Response(content="forbidden", status_code=403)

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
