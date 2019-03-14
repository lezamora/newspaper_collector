import random
import time
import logging
from logging.config import fileConfig
from newspaper import Article

import config
from helpers import load_data, save_data

logger = logging.getLogger(__name__)
timeDelay = random.randrange(5, 20)


def download_info(row):
    if not(row['processed']):
        time.sleep(timeDelay)
        article = Article(row['url'])
        article.download()
        article.parse()
        row['title'] = article.title
        row['text'] = article.text
        row['publish_date'] = str(article.publish_date)
        row['processed'] = 1

        logging.info('El articulo {} ha sido descargado y guardado.'.format(row['url']))
        return row
    else:
        logger.info('El articulo ya ha sido descargado anteriormente.')
        return row


def main():
    df = load_data(config.data_path, 'csv')
    df = df.apply(lambda row: download_info(row), axis=1)
    save_data(df, config.data_path)


if __name__ == '__main__':
    logging.config.fileConfig(config.log_path)

    main()
