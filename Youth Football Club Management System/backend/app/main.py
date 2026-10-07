from fastapi import FastAPI

app = FastAPI(title="Youth Football Manager")

@app.get("/")
def home():
    return {"message": "Youth Football API"}