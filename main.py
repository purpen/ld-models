from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def read_root():
    return {
        "message": "Hello World!"
    }


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {
        "item_id": item_id
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)