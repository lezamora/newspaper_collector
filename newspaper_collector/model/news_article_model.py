import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NewsArticle(Base):
    """ NewsArticle Model for storing news related details """
    __tablename__ = 'news_articles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    website = db.Column(db.String(255))
    url = db.Column(db.String(255))
    processed = db.Column(db.Boolean, default=False)
    title = db.Column(db.String(255))
    news_text = db.Column(db.String(65000))
    publish_date = db.Column(db.String(100))

    def __repr__(self):
        return "<NewsArticle with url: '{}.'>".format(self.url)
