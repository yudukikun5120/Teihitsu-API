"""Module Main serving problems as an API."""
from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/items/{category}")
def read_items(category: str):
    "Function read items."
    problems = pd.read_pickle(F'problems/{category}.pkl')

    return problems.to_json(orient='records', force_ascii=False, lines=True)


@app.get("/items/{category}/{id_}")
def read_item(category: str, id_: int):
    "Function read an item."
    problems = pd.read_pickle(F'problems/{category}.pkl')
    problem = problems.iloc[id_]

    return problem.to_json(force_ascii=False)
