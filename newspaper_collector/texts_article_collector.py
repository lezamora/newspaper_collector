import random
import time
import logging
from logging.config import fileConfig

import click
from newspaper import Article

import config
from model import create_session
from model.news_article_model import NewsArticle

logger = logging.getLogger(__name__)
timeDelay = random.randrange(3, 10)
session = create_session()


def __parser_news(url):
    time.sleep(timeDelay)
    article = Article(url)
    article.download()
    article.parse()
    return article


def run_collector(nrows=100):
    news_articles = session.query(NewsArticle).filter(NewsArticle.processed == 0).limit(nrows).all()
    for new in news_articles:
        try:
            article = __parser_news(new.url)
            new.title = article.title
            new.news_text = article.text
            new.publish_date = str(article.publish_date)
            new.processed = 1
            session.add(new)
            session.commit()

            logging.info('El articulo con id {} ha sido descargado y guardado.'.format(new.id))

        except Exception as e:
            logging.exception("Exception occurred", exc_info=True)


@click.command()
@click.option('--nrows', help='Cantidad de registro a procesar.')
def main(nrows):
    """ El objetivo principal de este programa es descargar informacion de
     las urls descargadas anteriormente y guardarla.
    """
    run_collector(int(nrows))


if __name__ == '__main__':
    logging.config.fileConfig(config.log_path)

    main()
