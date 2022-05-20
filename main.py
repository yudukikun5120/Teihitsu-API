"""Module Main serving problems as an API."""
from fastapi import FastAPI, Response
import pandas as pd

app = FastAPI()


@app.get("/items/{category}")
def read_items(category: str):
    "Function read items."
    problems = pd.read_pickle(F'problems/{category}.pkl')

    return Response(problems.to_json(orient='records', force_ascii=False,
                    lines=True), media_type="application/json")


@app.get("/items/{category}/{id_}")
def read_item(category: str, id_: int):
    "Function read an item."
    problems = pd.read_pickle(F'problems/{category}.pkl')
    problem = problems.iloc[id_]

    return Response(problem.to_json(force_ascii=False),
                    media_type="application/json")


if __name__ == '__main__':
    print(read_item("onyomi", 1))
