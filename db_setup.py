from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection string with charset
engine = create_engine('mysql+pymysql://news_user:Qwerty%4007@localhost/news_db?charset=utf8mb4')
Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True)
    link = Column(String(255), unique=True)  # Ensure link is unique to prevent duplicates
    published = Column(DateTime)
    summary = Column(Text)
    category = Column(String(50))

# Create the articles table
Base.metadata.create_all(engine)

# Set up session
Session = sessionmaker(bind=engine)
session = Session()
