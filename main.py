from fastapi import FastAPI, Response, Request

app = FastAPI()

VERIFY_TOKEN = "lumpad123"

# ✅ GET → verifikasi webhook
@app.get("/webhook")
def verify(
    hub_mode: str = None,
    hub_verify_token: str = None,
    hub_challenge: str = None
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return Response(content=str(hub_challenge), media_type="text/plain")

    return Response(content="ok", media_type="text/plain")


# ✅ POST → terima event dari Strava
@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    print("EVENT:", data)
    return {"ok": True}
