from fastapi import FastAPI
import pandas as pd
import re

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/onyomi/{item_id}")
def read_item(item_id: int):
    uri = 'http://teihitsu.html.xdomain.jp/onyomi.xls'
    df = pd.read_excel(uri, index_col=1)

    row_index = item_id + 8

    item = df.iloc[row_index].fillna("")

    return {
        "item_id": item_id,
        "q": item[1],
        "level": int(re.sub(r'\D', '', item[2])),
        "a": item[3],
        "a_alt": item[4],
        "comment": item[5]
    }
