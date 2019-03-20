import types
import re
import csv
import time
import logging
from logging.config import fileConfig

import click
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import config
from helpers import get_date
from model import create_session
from model.news_article_model import NewsArticle

session = create_session()


class StrategyGetUrl:
    def __init__(self, func=None, limit_date=None):
        self.name = ''
        self.section_url = ''
        self.data_path = ''
        self.limit_date = limit_date
        self.urls = []

        if func is not None:
            self.execute = types.MethodType(func, self)

    def instance_driver(self):
        logging.info('Abriendo el navegador y redirigiendo hacia {}.'.format(self.section_url))

        driver = webdriver.PhantomJS(config.driver_path)
        driver.implicitly_wait(30)
        driver.get(self.section_url)
        return driver

    def run_collector(self):
        for url in self.urls:
            ed_user = NewsArticle(website=self.name, url=url)
            session.add(ed_user)
            session.commit()
        logging.info('Se ha guardado la info de forma correcta.')

def rosario_3(self):
    """ Esta funcion devuelve todas las urls de la seccion de policiales del portal de noticias
    rosario3. La limit_date define hasta que fecha se permitira obtener urls.
    """
    date_limit = get_date(self.limit_date)

    self.name = 'rosario 3'
    self.section_url = config.rosario3_url

    driver = self.instance_driver()

    # Obtenemos fecha de la ultima noticia en listing y verificamos que no sea mas antigua que la solicitada.
    logging.info('Cargando noticias hasta el dia {}.'.format(date_limit))

    for i in range(1,10000):
        try:
            date = driver.find_element_by_xpath('//div[2]//div[2]/article[{}]/div[2]/time'.format(i * 20)).text
        except NoSuchElementException as e:
            logging.exception("Exception occurred", exc_info=True)

        if re.match('.*-.*-.*', date):
            date = get_date(date)
            if date < date_limit:
                break

        # Si todavia estamos dentro del limite temporal solicitado seguimos cargando noticias.
        try:
            driver.find_element_by_xpath('(//a[@class="btn btn-medium"])[1]').click()
            time.sleep(5)
        except NoSuchElementException as e:
            logging.exception("Exception occurred", exc_info=True)

    # Obtenemos todas las urls de las noticias cargadas.
    elements = driver.find_elements_by_xpath("//div[2]/article//h1/a")

    if len(elements) > 0:
        self.urls = [e.get_attribute('href') for e in elements]
    else:
        logging.exception('Failed because elements list is empty.')

    logging.info('Se han recolectado {} urls.'.format(len(self.urls)))
    driver.quit()


def el_ciudadano(self):
    """ Esta funcion devuelve todas las urls de la seccion de policiales del portal de noticias
    el ciudadano. La limit_date en esta funcion no tiene sentido ya que este por portal
    no manipula fechas. Para fines practicos pasaremos como parametro un numero de pagina arbitrario.
    """
    self.name = 'el ciudadano'
    self.section_url = config.elciudadano_url

    driver = self.instance_driver()

    # Obtenemos para cada page todas las urls de las noticias que se muestran en pantalla.
    logging.info('Cargando noticias hasta la pagina {}.'.format(self.limit_date))

    for i in range(1, int(self.limit_date) + 1):
        driver.get(self.section_url.format(i))
        time.sleep(5)

        try:
            elements = driver.find_elements_by_xpath("//div[2]/h2/a")
        except NoSuchElementException as e:
            logging.exception("Exception occurred", exc_info=True)
        for e in elements:
            self.urls.append(e.get_attribute('href'))

    logging.info('Se han recolectado {} urls.'.format(len(self.urls)))
    driver.quit()


@click.command()
@click.option('--website', help='El sitio al que queremos ingresar.')
@click.option('--limit', help='Fecha o pagina limite a la que queremos llegar.')
def main(website, limit):
    """ El objetivo principal de este programa es obtener urls de algun portal solicitado y guardarlas
    fisicamente en el algun repositorio.
    """
    news_list = StrategyGetUrl(eval(website), limit)
    news_list.execute()
    news_list.run_collector()


if __name__ == '__main__':
    logging.config.fileConfig(config.log_path)

    main()
