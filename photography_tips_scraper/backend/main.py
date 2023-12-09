from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from pyterrier_api import pyterrier_indexing as py_q
from typing import List

from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    history: str

@app.get("/")
def home():
    return "Hello, World!"

@app.get("/test")
def test():
    return "Hello, test!"

@app.get("/search")
def search_query(query: str):
    results = py_q.search_query(query=query)
    return {"query": query, "results": results}

@app.post("/rec")
async def advanced_search(item: Item):
    # print("resultAA: ", item)
    # query = item[1]
    results = py_q.recommender(history=item.history)
    return {"query": item.history, "results": results}
