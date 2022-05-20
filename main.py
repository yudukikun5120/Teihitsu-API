from fastapi import FastAPI
import pandas as pd
import re

app = FastAPI()


@app.get("/items/{category}")
def read_items(category: str):
    problems = pd.read_pickle(F'problems/{category}.pkl')

    return problems.to_json(orient='records', force_ascii=False, lines=True)


@app.get("/items/{category}/{id}")
def read_item(category: str, id: int):
    problems = pd.read_pickle(F'problems/{category}.pkl')
    problem = problems.iloc[id]

    return problem.to_json(force_ascii=False)
