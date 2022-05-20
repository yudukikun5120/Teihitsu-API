"""Module UpdateProblems updating problems."""
import pandas as pd

categories = {
    "onyomi": {
        "header": 9,
        "names": [
            "id",
            "problem",
            "level",
            "correct_answer",
            "alt_correct_answers",
            "note",
            "",
        ],
        "index_col": 1,
    },
    "kunyomi": {
        "header": 8,
        "names": [
            "",
            "id",
            "problem",
            "level",
            "correct_answer",
            "note",
        ],
        "index_col": 0,
    },
    "kokuji": {
        "header": 7,
        "names": [
            "",
            "id",
            "problem",
            "pseudo-level",
            "correct_answer",
            "alt_correct_answer",
            "note",
        ],
        "index_col": 0,
    },
    "yoji-kaki": {
        "header": 8,
        "names": [
            "id",
            "problem",
            "reading",
            "level",
            "correct_answer",
            "alt_correct_answers",
            "source",
            "note",
            "",
        ],
        "index_col": 1,
    },
    "yoji-imi": {
        "header": 8,
        "names": [
            "",
            "id",
            "problem",
            "word_group",
            "level",
            "correct_answer",
            "alt_correct_answers",
            "source",
            "note",
        ],
        "index_col": 0,
    },
    "jyuku_ate": {
        "header": 6,
        "names": [
            "",
            "id",
            "problem",
            "level",
            "correct_answer",
            "alt_correct_answers",
            "note",
        ],
        "index_col": 0,
    },
    "onkun": {
        "header": 8,
        "names": [
            "",
            "id",
            "onyomi",
            "onyomi_answer",
            "kunyomi",
            "kunyomi_answer",
            "level",
            "note",
        ],
        "index_col": 0,
    },
    "tai-rui": {
        "header": 8,
        "names": [
            "",
            "id",
            "problem",
            "type",
            "word_group",
            "level",
            "correct_answer",
            "note_on_question",
            "note_on_answer",
        ],
        "index_col": 0,
    },
    "kojikoto": {
        "header": 10,
        "names": [
            "id",
            "problem",
            "level",
            "correct_answer",
            "alt_correct_answers",
            "note",
            "",
        ],
        "index_col": 1,
    },
}

converters = {
    "problem": lambda str: re.sub(r'^【(.*)】$', r'\1', str),
    "level": lambda str: int(re.sub(r'\D', '', str)),
    "source": lambda str: re.sub(r'\D', '', str),
    "word_group": lambda str: tuple(str.split()),
}


def fetch_problems(category, attr):
    "Function fetching problems."
    try:
        uri = F'http://teihitsu.html.xdomain.jp/{category}.xls'

        print(F"Fetching problems from {uri}...")

        dataframe = pd.read_excel(uri,
                                  index_col=attr["index_col"],
                                  header=attr["header"],
                                  names=attr["names"],
                                  converters=converters)

        print(dataframe.to_json(orient='records', force_ascii=False,
                                lines=True))

        dataframe.to_pickle(F'problems/{category}.pkl')
    except Exception as error:
        raise error


def main():
    "Function fetching problems for all categories."
    for category, attr in categories.items():
        fetch_problems(category, attr)


if __name__ == '__main__':
    import re
    main()
