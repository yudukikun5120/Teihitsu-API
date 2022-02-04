from fastapi import FastAPI
import pandas as pd
import re

app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/items/onyomi/{item_id}")
def read__onyomi_item(item_id: int):
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


@app.get("/items/kunyomi/{item_id}")
def read_kunyomi_item(item_id: int):
    uri = 'http://teihitsu.html.xdomain.jp/kunyomi.xls'
    df = pd.read_excel(uri, index_col=1)

    row_index = item_id + 7

    item = df.iloc[row_index].fillna("")

    return {
        "item_id": item_id,
        "q": item[1],
        "level": int(re.sub(r'\D', '', item[2])),
        "a": item[3],
        "comment": item[4]
    }


@app.get("/items/kokuji/{item_id}")
def read_kokuji_item(item_id: int):
    uri = 'http://teihitsu.html.xdomain.jp/kokuji.xls'
    df = pd.read_excel(uri, index_col=1)

    row_index = item_id + 6

    item = df.iloc[row_index].fillna("")

    return {
        "item_id": item_id,
        "q": item[1],
        "level": "",
        "a": item[3],
        "a_alt": item[4],
        "comment": item[5]
    }


@app.get("/items/yoji-kaki/{item_id}")
def read_yojikaki_item(item_id: int):
    uri = 'http://teihitsu.html.xdomain.jp/yoji-kaki.xls'
    df = pd.read_excel(uri, index_col=1)

    row_index = item_id + 7

    item = df.iloc[row_index].fillna("")

    return {
        "item_id": item_id,
        "q": item[1],
        "yomi": item[2],
        "level": int(re.sub(r'\D', '', item[3])),
        "a": item[4],
        "a_alt": item[5],
        "source": item[6],
        "comment": item[7]
    }


@app.get("/items/yoji-imi/{item_id}")
def read_yojiimi_item(item_id: int):
    uri = 'http://teihitsu.html.xdomain.jp/yoji-imi.xls'
    df = pd.read_excel(uri, index_col=1)

    row_index = item_id + 7

    item = df.iloc[row_index].fillna("")

    return {
        "item_id": item_id,
        "q": item[1],
        "word_group": item[2],
        "level": int(re.sub(r'\D', '', item[3])),
        "a": item[4],
        "a_alt": item[5],
        "source": item[6],
        "comment": item[7]
    }


@app.get("/items/jyuku-ate/{item_id}")
def read_jyukuate_item(item_id: int):
    uri = 'http://teihitsu.html.xdomain.jp/jyuku_ate.xls'
    df = pd.read_excel(uri, index_col=1)

    row_index = item_id + 6

    item = df.iloc[row_index].fillna("")

    return {
        "item_id": item_id,
        "q": item[1],
        "level": int(re.sub(r'\D', '', item[2])),
        "a": item[3],
        "a_alt": item[4],
        "comment": item[5]
    }


@app.get("/items/onkun/{item_id}")
def read_onkun_item(item_id: int):
    uri = 'http://teihitsu.html.xdomain.jp/onkun.xls'
    df = pd.read_excel(uri, index_col=1)

    row_index = item_id + 7

    item = df.iloc[row_index].fillna("")

    return {
        "item_id": item_id,
        "q": [
                {
                    "on": item[1],
                    "a": item[2],
                },
                {
                    "kun": item[3],
                    "a": item[4]
                }
            ],
        "level": int(re.sub(r'\D', '', item[5])),
        "comment": item[6]
    }


@app.get("/items/tai-rui/{item_id}")
def read_tairui_item(item_id: int):
    uri = 'http://teihitsu.html.xdomain.jp/tai-rui.xls'
    df = pd.read_excel(uri, index_col=1)

    row_index = item_id + 8

    item = df.iloc[row_index].fillna("")

    return {
        "item_id": item_id,
        "q": item[1],
        "type": item[2],
        "word_group": item[3],
        "level": int(re.sub(r'\D', '', item[4])),
        "a": item[5],
        "comment_on_question": item[6],
        "comment_on_answer": item[7]
    }


@app.get("/items/kojikoto/{item_id}")
def read_kojikoto_item(item_id: int):
    uri = 'http://teihitsu.html.xdomain.jp/kojikoto.xls'
    df = pd.read_excel(uri, index_col=1)

    row_index = item_id + 9

    item = df.iloc[row_index].fillna("")

    return {
        "item_id": item_id,
        "q": item[1],
        "level": int(re.sub(r'\D', '', item[2])),
        "a": item[3],
        "a_alt": item[4],
        "comment": item[5]
    }
