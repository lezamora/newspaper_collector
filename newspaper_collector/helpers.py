import datetime
import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def get_date(s_date):
    date_patterns = ['%d-%m-%Y', '%Y%m%d']

    for pattern in date_patterns:
        try:
            return datetime.datetime.strptime(s_date, pattern).date()
        except:
            logger.info('Incorrect format.')


def load_data(data_path, ext_type):
    if os.path.exists(data_path):
        if ext_type == 'csv':
            return pd.read_csv(data_path)
        else:
            logger.info('Incorrect format.')


def save_data(df, data_path):
    if os.path.exists(data_path):
        pd.DataFrame.to_csv(df, data_path, index_label=False)
        logging.info('El dataframe se ha guardado de forma correcta.')
