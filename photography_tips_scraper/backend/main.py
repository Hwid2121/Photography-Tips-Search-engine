from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW
# from pyterrier_api import pyterrier_query as pt
from pyterrier_api import pyterrier_indexing as py_q
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Hello, World!"

@app.get("/test")
def test():
    return "hello test!"


@app.get("/search")
def search_query(query: str):
    # py_q.init()
    # py_q.start_indexing()  # Corrected: Removed assignment to br
    results = py_q.search_query(query=query)
    return {"query": query, "results": results}
