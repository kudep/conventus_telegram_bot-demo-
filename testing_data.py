#!/bin/python3
# -*- coding: utf-8 -*-
import pandas as pd
__all__ = ["TestingData"]

class TestingData():
    def __init__(self, datapath = 'data.csv'):
        self.data = pd.read_csv(datapath)
        column_names = self.data.columns.values
        self.test_ids_col = column_names[0]
        self.test_name_col = column_names[1]
        self.question_ids_col = column_names[2]
        self.question_text_col = column_names[3]
        self.answer_ids_col = column_names[4]
        self.answer_text_col = column_names[5]
        self.psychotype_begin_col = column_names[6]
        self.psychotype_end_col = column_names[-1]

    def get_tests(self):
        return self.data[self.test_name_col].dropna().tolist()

    def get_questions(self, test_id = 0):
        return self.data[self.data[self.test_ids_col] == test_id][self.question_text_col].dropna().tolist()

    def get_answers(self, test_id = 0, question_id = 0):
        return self.data[self.data[self.test_ids_col] == test_id][self.data[self.question_ids_col] == question_id][self.answer_text_col].dropna().tolist()
