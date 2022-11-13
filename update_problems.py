"""Module UpdateProblems updating problems."""
import json
import logging
import pickle
import re

import pandas as pd
import progressbar

converters = {
    "problem": lambda str: re.sub(r'^【(.*)】$', r'\1', str),
    "level": lambda str: int(re.sub(r'\D', '', str)),
    "source": lambda str: re.sub(r'\D', '', str),
    "word_group": lambda str: tuple(re.split('\n|・', str)),
}

def fetch_problems(
        *, category: str, index_col: int, header: int, names: list
        ) -> pd.DataFrame:
    """Function fetching problems."""
    uri = F'http://teihitsu.html.xdomain.jp/{category}.xls'
    logging.info("Fetching problems from %s ...", uri)

    try:
        dataframe = pd.read_excel(
            uri,
            index_col=index_col,
            header=header,
            names=names,
            converters=converters,
        )

        logging.info("Succeeded in fetching %s problems.", category)
        return dataframe.fillna(0)

    except Exception as error:
        raise error


def dataframe_to_json(dataframe: pd.DataFrame) -> dict:
    """Function converting the DataFrame to JSON format."""
    return dataframe.to_json(orient='records', force_ascii=False, lines=True)

def store_dataframe(*, dataframe: pd.DataFrame, category: str) -> None:
    """Function storing the DataFrame in pickle format."""
    dataframe.to_pickle(F'problems/dataframe/{category}.pkl')

def store_dict(*, problem_data: pd.DataFrame, category: str) -> None:
    """Function storing the dict in pickle format."""
    with open(F'problems/vanilla/{category}.pkl', 'wb') as file:
        pickle.dump(problem_data.T.to_dict(), file)

def main(categories_: dict) -> None:
    """Function fetching problems for all categories."""
    logging.basicConfig(level=logging.INFO)
    for category, attr in progressbar.progressbar(categories_.items()):
        dataframe = fetch_problems(category=category, **attr)
        store_dataframe(dataframe=dataframe, category=category)
        store_dict(problem_data=dataframe, category=category)
        logging.debug(
            """Dataframe of %s in JSON format:

%s
            """,
            category,
            dataframe_to_json(dataframe)
        )


if __name__ == '__main__':
    with open('categories.json', encoding="utf-8") as f:
        categories = json.load(f)
        main(categories)
