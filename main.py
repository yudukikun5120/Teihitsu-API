"""Module Main serving problems as an API."""
import pickle

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{category}")
def read_items(category: str):
    """
    Function reading items.

    <category> ::=
    onyomi | kunyomi | kokuji | yoji-kaki | yoji-imi | jyuku_ate | onkun | tai-rui | kojikoto
    """
    with open(F'problems/vanilla/{category}.pkl', 'rb') as file:
        problems = pickle.load(file)
        return problems


@app.get("/items/{category}/{id_}")
def read_item(category: str, id_: int):
    "Function reading an item."
    with open(F'problems/vanilla/{category}.pkl', 'rb') as file:
        problems = pickle.load(file)
        return problems[id_]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
