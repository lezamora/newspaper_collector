class Config:
    LOG_CONFIG_PATH = '/home/lezamora/Repositorios/newspaper_collector/logging.ini'
    DATA_PATH = '/home/lezamora/Repositorios/newspaper_collector/data/rosario_news_2018_2019.csv'
    DRIVER_PATH = '/home/lezamora/Repositorios/.drivers/phantomjs-2.1.1-linux-x86_64/phantomjs'

    ROSARIO3_URL = 'https://www.rosario3.com/seccion/noticias/policiales/'
    ELCIUDADANO_URL = 'https://www.elciudadanoweb.com/seccion/policiales/page/{}/'


log_path = Config.LOG_CONFIG_PATH
driver_path = Config.DRIVER_PATH
data_path = Config.DATA_PATH

rosario3_url = Config.ROSARIO3_URL
elciudadano_url = Config.ELCIUDADANO_URL
