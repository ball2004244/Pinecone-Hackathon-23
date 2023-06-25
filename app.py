from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

HOST = 'localhost'
PORT = 8000
if __name__ == "__main__":
    uvicorn.run('app:app', host=HOST, port=PORT, reload=True)
