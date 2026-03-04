from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"selamat datang di proyek Machine Learning dengan FastAPI!"}