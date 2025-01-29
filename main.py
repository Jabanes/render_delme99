from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"CRITICAL! WARNING! CRITICAL WARNING! CRITICAL! WARNING! CRITICAL WARNING! CRITICAL! WARNING! CRITICAL WARNING!"}
