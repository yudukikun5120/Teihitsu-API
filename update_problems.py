"""Module UpdateProblems updating problems."""
import re
import json
import pandas as pd

with open('categories.json') as f:
    categories = json.load(f)

converters = {
    "problem": lambda str: re.sub(r'^【(.*)】$', r'\1', str),
    "level": lambda str: int(re.sub(r'\D', '', str)),
    "source": lambda str: re.sub(r'\D', '', str),
    "word_group": lambda str: tuple(re.split('\n|・', str)),
}


def fetch_problems(*, category: str, attr: dict) -> pd.DataFrame:
    """Function fetching problems."""
    uri = F'http://teihitsu.html.xdomain.jp/{category}.xls'
    print(F"Fetching problems from {uri}...")

    try:
        dataframe = pd.read_excel(
            uri,
            index_col=attr["index_col"],
            header=attr["header"],
            names=attr["names"],
            converters=converters
        )
        return dataframe

    except Exception as error:
        raise error


def dataframe_to_json(dataframe: pd.DataFrame) -> dict:
    """Function converting the DataFrame to JSON format."""
    return dataframe.to_json(orient='records', force_ascii=False, lines=True)


def store_dataframe(*, dataframe: pd.DataFrame, category: str) -> None:
    """Function storing the DataFrame in pickle format."""
    dataframe.to_pickle(F'problems/{category}.pkl')


def main(categories_: dict) -> None:
    """Function fetching problems for all categories."""
    for category, attr in categories_.items():
        dataframe = fetch_problems(category=category, attr=attr)
        store_dataframe(dataframe=dataframe, category=category)
        print(dataframe_to_json(dataframe))


if __name__ == '__main__':
    main(categories)
