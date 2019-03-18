import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

import pymysql
pymysql.install_as_MySQLdb()

import config

def create_session():
    engine = db.create_engine(config.mysql_path)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
