import datetime
import os
import pandas as pd


def get_date(s_date):
    date_patterns = ['%d-%m-%Y', '%Y%m%d']

    for pattern in date_patterns:
        try:
            return datetime.datetime.strptime(s_date, pattern).date()
        except:
            pass


def load_data(data_path, ext_type):
    if os.path.exists(data_path):
        if ext_type == 'csv':
            return pd.read_csv(data_path)
        else:
            pass # print('Incorrect format.')


def save_data(df, data_path):
    if not os.path.exists(data_path):
        pd.DataFrame.to_csv(df, data_path, index_label=False)