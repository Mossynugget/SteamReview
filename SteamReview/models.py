from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

DeclarativeBase = declarative_base()


def db_connect():
    """ Performs database connections using database settings from settings.py
        Returns sqlalchemy engine instance
    """
    return create_engine(URL({
        'drivername': 'postgres',
        'host': 'localhost',
        'port': '5432',
        'username': 'admin',
        'password': 'admin',
        'database': 'SteamReviewScraper'
    }))


def create_reviews_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Reviews(DeclarativeBase):
    """SQLAlchemy RawSteamReviews Model"""
    __tablename__ = 'RawSteamReviews'

    RawSteamReviewId = Column(Integer, primary_key=True)
    RecommendedInd = Column('recommendedInd', String)
    HelpfulCount = Column('helpfulCount', Integer)
    FunnyCount = Column('funnyCount', Integer)
    HoursPlayed = Column('hoursPlayed', Integer)
    PostedDate = Column('postedDate', String)
    ResponseCount = Column('responseCount', Integer)
    Content = Column('content', String, nullable=True)
    AppId = Column('appId', Integer)