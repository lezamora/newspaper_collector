class Config:
    LOG_CONFIG_PATH = '/home/lezamora/Repositorios/newspaper_collector/logging.ini'
    DRIVER_PATH = '/home/lezamora/Repositorios/.drivers/phantomjs-2.1.1-linux-x86_64/phantomjs'

    ROSARIO3_URL = 'https://www.rosario3.com/seccion/noticias/policiales/'
    ELCIUDADANO_URL = 'https://www.elciudadanoweb.com/seccion/policiales/page/{}/'
    ROSARIOPLUS_URL = 'https://www.rosarioplus.com/seccion/ensacoycorbata/seguridad/'

    ROSARIO3_DATA_PATH = ''
    ELCIUDADANO_DATA_PATH = ''
    ROSARIOPLUS_DATA_PATH = ''


log_path = Config.LOG_CONFIG_PATH
driver_path = Config.DRIVER_PATH

rosario3_url = Config.ROSARIO3_URL
elciudadano_url = Config.ELCIUDADANO_URL
rosarioplus_url = Config.ROSARIOPLUS_URL


rosario3_data_path = Config.ROSARIO3_DATA_PATH
elciudadano_data_path = Config.ELCIUDADANO_DATA_PATH
rosarioplus_data_path = Config.ROSARIOPLUS_DATA_PATH