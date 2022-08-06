"""Module Main serving problems as an API."""
from fastapi import FastAPI, Response
import pandas as pd

app = FastAPI()


@app.get("/items/{category}")
def read_items(category: str):
    """
    Function reading items.

    <category> ::=
    onyomi | kunyomi | kokuji | yoji-kaki | yoji-imi | jyuku_ate | onkun | tai-rui | kojikoto
    """
    problems = pd.read_pickle(F'problems/{category}.pkl')

    return Response(problems.to_json(orient='records', force_ascii=False,
                    lines=True), media_type="application/json")


@app.get("/items/{category}/{id_}")
def read_item(category: str, id_: int):
    "Function reading an item."
    problems = pd.read_pickle(F'problems/{category}.pkl')
    problem = problems.iloc[id_]

    return Response(problem.to_json(force_ascii=False),
                    media_type="application/json")
