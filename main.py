from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Lumpad running 🚀"}

@app.get("/webhook")
def verify():
    return {"status": "webhook ready"}

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    print("EVENT:", data)
    return {"ok": True}
