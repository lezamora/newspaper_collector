import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NewsArticle(Base):
    """ NewsArticle Model for storing news related details """
    __tablename__ = 'news_articles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    website = db.Column(db.String)
    url = db.Column(db.String)
    processed = db.Column(db.Boolean, default=False)
    title = db.Column(db.String)
    news_text = db.Column(db.String)
    publish_date = db.Column(db.String)

    def __repr__(self):
        return "<NewsArticle with url: '{}.'>".format(self.url)
