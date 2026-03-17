from fastapi import FastAPI, Response

app = FastAPI()

VERIFY_TOKEN = "lumpad123"

@app.get("/webhook")
def verify(
    hub_mode: str = None,
    hub_verify_token: str = None,
    hub_challenge: str = None
):
    try:
        print("MODE:", hub_mode)
        print("TOKEN:", hub_verify_token)
        print("CHALLENGE:", hub_challenge)

        if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
            if hub_challenge:
                return Response(content=str(hub_challenge), media_type="text/plain")
            else:
                return Response(content="no challenge", media_type="text/plain")

        return Response(content="ok", media_type="text/plain")

    except Exception as e:
        print("ERROR:", str(e))
        return Response(content="error", media_type="text/plain")
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
