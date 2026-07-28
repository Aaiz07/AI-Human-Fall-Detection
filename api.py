from fastapi import FastAPI

app = FastAPI()

latest_status = {
    "state": "NORMAL",
    "people": 0,
    "falls": 0
}

@app.get("/status")
def status():

    return latest_status