"""Module _Unittest testing module update_problems"""
import json
import unittest
import numpy as np
from update_problems import fetch_problems


class TestProblemsDataFrame(unittest.TestCase):
    """Class TestProblemsDataFrame testing each problems data frames"""

    with open('categories.json', encoding="utf-8") as f:
        CATEGORIES = json.load(f)

    def test_onyomi(self, categories=CATEGORIES):
        """Function TestOnyomi testing the start row and data types"""
        attr = categories['onyomi']
        dataframe = fetch_problems(category='onyomi', attr=attr)
        self.assertEqual(dataframe.at[1, 'id'], 1)
        self.assertEqual(dataframe.at[1, 'problem'], "蹉跌")
        self.assertEqual(dataframe.at[1, 'level'], 1)
        self.assertEqual(dataframe.at[1, 'correct_answer'], 'さてつ')
        self.assertTrue(np.isnan(dataframe.at[1, 'alt_correct_answers']))
        self.assertEqual(dataframe.at[1, 'note'], "┌1.つまずくこと。\n"
            "└2.障害や失敗があって、行き詰まること。≒挫折〈漢字ペディア〉\n┌物事がうまく進まず、しくじること。挫折。失敗。〈大辞泉〉\n"
            "┌1.つまずいて足をすべらす。\n└2.ちぐはぐになって、失敗する。〈漢字源〉\n◇漢字ペディア大見出し\n●H4-1㈠"
        )

    # IDEA: write test_other_categories

if __name__ == '__main__':
    unittest.main()
